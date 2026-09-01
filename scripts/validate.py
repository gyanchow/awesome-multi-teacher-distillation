#!/usr/bin/env python3
"""Validate the v2 catalog without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
README_PATHS = [ROOT / "README.md", ROOT / "README_zh-CN.md"]

TOP_LEVEL_FIELDS = {"schema_version", "last_verified", "papers"}
PAPER_FIELDS = {
    "id",
    "title",
    "date",
    "collection",
    "record_type",
    "training_regime",
    "state_source",
    "teacher_topology",
    "primary_mechanism",
    "mechanism_tags",
    "signals",
    "domains",
    "paper",
    "artifacts",
    "summary",
    "evidence",
}
EVIDENCE_FIELDS = {
    "student_generated_states",
    "multiple_independent_supervisors",
    "direct_distillation_objective",
    "classification_note",
}

COLLECTIONS = {
    "multi_teacher_on_policy",
    "offline_multi_teacher",
    "adjacent_alternative",
    "single_teacher_foundation",
    "review_tutorial",
}
RECORD_TYPES = {"method", "analysis", "system_report", "survey", "tutorial"}
TRAINING_REGIMES = {
    "on_policy",
    "offline",
    "hybrid",
    "online_peer",
    "self_distillation",
    "not_applicable",
}
STATE_SOURCES = {
    "current_student",
    "near_current_student",
    "static_corpus",
    "teacher_generated",
    "replay_buffer",
    "mixed",
    "not_applicable",
}
TEACHER_TOPOLOGIES = {
    "ensemble_to_one",
    "independent_multi_teacher",
    "specialist_pool",
    "checkpoint_pool",
    "heterogeneous_pool",
    "debate_collective",
    "peer_mutual",
    "self_ema",
    "privileged_views",
    "sequential_chain",
    "single_teacher",
}
MECHANISMS = {
    "direct_matching",
    "routing_selection",
    "adaptive_weighting",
    "conflict_resolution",
    "dynamic_scheduling",
    "heterogeneous_alignment",
    "progressive_sequential",
    "collective_deliberation",
    "not_applicable",
}
MECHANISM_TAGS = MECHANISMS - {"not_applicable"}
SIGNALS = {
    "logits_distribution",
    "sampled_token_advantage",
    "features",
    "relations",
    "responses_rationales",
    "feedback_reward",
    "action_distribution",
    "latent_velocity",
    "gradients",
    "teacher_generated_data",
}
DOMAINS = {
    "llm_general",
    "llm_reasoning",
    "llm_agents",
    "llm_alignment",
    "nlp",
    "speech",
    "vision",
    "multimodal",
    "generative_models",
    "recommendation_search",
    "knowledge_graphs",
    "robotics_embodied",
    "scientific_healthcare",
    "general_machine_learning",
}
EVIDENCE_VALUES = {"yes", "no", "partial", "unclear", "not_applicable"}
ARTIFACT_TYPES = {"code", "project", "model", "data"}
COLLECTION_PATHS = {
    "multi_teacher_on_policy": ROOT / "papers" / "multi-teacher-on-policy.md",
    "offline_multi_teacher": ROOT / "papers" / "offline-multi-teacher.md",
    "adjacent_alternative": ROOT / "papers" / "adjacent-alternatives.md",
    "single_teacher_foundation": ROOT / "papers" / "single-teacher-foundations.md",
    "review_tutorial": ROOT / "papers" / "reviews-tutorials.md",
}
EXPECTED_CURATED_COUNTS = {
    "multi_teacher_on_policy": 12,
    "offline_multi_teacher": 10,
    "adjacent_alternative": 6,
    "single_teacher_foundation": 3,
    "review_tutorial": 4,
}


class DuplicateKeyError(ValueError):
    pass


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def load_catalog(errors: list[str]) -> dict[str, object] | None:
    try:
        return json.loads(
            DATA_PATH.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except (OSError, json.JSONDecodeError, DuplicateKeyError) as exc:
        errors.append(f"{DATA_PATH.relative_to(ROOT)}: {exc}")
        return None


def parse_iso_date(value: object, label: str, errors: list[str]) -> date | None:
    if not isinstance(value, str):
        errors.append(f"{label}: expected a YYYY-MM-DD string")
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid date {value!r}")
        return None
    if parsed.isoformat() != value:
        errors.append(f"{label}: date must be zero-padded YYYY-MM-DD")
    return parsed


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def exact_fields(
    value: dict[str, object], expected: set[str], label: str, errors: list[str]
) -> None:
    keys = set(value)
    missing = expected - keys
    extra = keys - expected
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")
    if extra:
        errors.append(f"{label}: unexpected fields {sorted(extra)}")


def enum_value(value: object, allowed: set[str], label: str, errors: list[str]) -> None:
    if value not in allowed:
        errors.append(f"{label}: invalid value {value!r}")


def enum_list(
    value: object,
    allowed: set[str],
    label: str,
    errors: list[str],
    *,
    allow_empty: bool = True,
) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{label}: expected a list")
        return []
    if not allow_empty and not value:
        errors.append(f"{label}: expected at least one value")
    if len(value) != len(set(item for item in value if isinstance(item, str))):
        errors.append(f"{label}: duplicate values are not allowed")
    for item in value:
        if not isinstance(item, str) or item not in allowed:
            errors.append(f"{label}: invalid value {item!r}")
    return [item for item in value if isinstance(item, str)]


def validate_evidence(value: object, label: str, errors: list[str]) -> dict[str, object]:
    if not isinstance(value, dict):
        errors.append(f"{label}: expected an object")
        return {}
    exact_fields(value, EVIDENCE_FIELDS, label, errors)
    for field in EVIDENCE_FIELDS - {"classification_note"}:
        enum_value(value.get(field), EVIDENCE_VALUES, f"{label}.{field}", errors)
    note = value.get("classification_note")
    if not isinstance(note, str) or len(note.strip()) < 12:
        errors.append(f"{label}.classification_note: expected at least 12 characters")
    return value


def validate_artifacts(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"{label}: expected a list")
        return
    seen: set[tuple[str, str]] = set()
    for index, artifact in enumerate(value, start=1):
        item_label = f"{label}[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{item_label}: expected an object")
            continue
        exact_fields(artifact, {"type", "url"}, item_label, errors)
        enum_value(artifact.get("type"), ARTIFACT_TYPES, f"{item_label}.type", errors)
        if not is_https_url(artifact.get("url")):
            errors.append(f"{item_label}.url: expected a valid https URL")
        pair = (str(artifact.get("type")), str(artifact.get("url")))
        if pair in seen:
            errors.append(f"{item_label}: duplicate artifact")
        seen.add(pair)


def validate_collection_rules(
    paper: dict[str, object], label: str, evidence: dict[str, object], errors: list[str]
) -> None:
    collection = paper.get("collection")
    record_type = paper.get("record_type")
    regime = paper.get("training_regime")
    state = paper.get("state_source")
    topology = paper.get("teacher_topology")
    mechanism = paper.get("primary_mechanism")
    tags = paper.get("mechanism_tags")
    signals = paper.get("signals")

    if collection == "multi_teacher_on_policy":
        if record_type not in {"method", "analysis", "system_report"}:
            errors.append(f"{label}: on-policy collection has incompatible record_type")
        if regime not in {"on_policy", "hybrid"}:
            errors.append(f"{label}: on-policy collection requires on_policy or hybrid regime")
        if state not in {"current_student", "near_current_student", "mixed"}:
            errors.append(f"{label}: on-policy collection has incompatible state_source")
        for field in (
            "student_generated_states",
            "multiple_independent_supervisors",
            "direct_distillation_objective",
        ):
            if evidence.get(field) not in {"yes", "partial"}:
                errors.append(f"{label}.evidence.{field}: strict collection requires yes or partial")

    if collection == "offline_multi_teacher":
        if regime != "offline":
            errors.append(f"{label}: offline collection requires offline regime")
        if state not in {"static_corpus", "teacher_generated", "replay_buffer", "mixed"}:
            errors.append(f"{label}: offline collection has incompatible state_source")
        if evidence.get("multiple_independent_supervisors") not in {"yes", "partial"}:
            errors.append(f"{label}: offline multi-teacher work requires multiple supervisors")

    if collection == "single_teacher_foundation":
        if record_type not in {"method", "analysis"}:
            errors.append(f"{label}: single-teacher foundation has incompatible record_type")
        if not isinstance(topology, list) or "single_teacher" not in topology:
            errors.append(f"{label}: single-teacher foundation requires single_teacher topology")
        if evidence.get("multiple_independent_supervisors") != "no":
            errors.append(f"{label}: single-teacher foundation requires multiple-supervisor evidence=no")

    if collection == "review_tutorial":
        if record_type not in {"survey", "tutorial"}:
            errors.append(f"{label}: review/tutorial collection has incompatible record_type")
        if regime != "not_applicable" or state != "not_applicable":
            errors.append(f"{label}: review/tutorial regime and state must be not_applicable")
        if topology != [] or tags != [] or signals != []:
            errors.append(f"{label}: review/tutorial topology, mechanism_tags, and signals must be empty")
        if mechanism != "not_applicable":
            errors.append(f"{label}: review/tutorial mechanism must be not_applicable")
        for field in EVIDENCE_FIELDS - {"classification_note"}:
            if evidence.get(field) != "not_applicable":
                errors.append(f"{label}.evidence.{field}: review/tutorial value must be not_applicable")


def stable_anchor(paper_id: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", paper_id.casefold()).strip("-")


def validate_markdown_catalogs(papers: list[dict[str, object]], errors: list[str]) -> None:
    texts: dict[str, str] = {}
    for collection, path in COLLECTION_PATHS.items():
        if not path.exists():
            errors.append(f"{path.relative_to(ROOT)}: canonical catalog is missing")
            texts[collection] = ""
        else:
            texts[collection] = path.read_text(encoding="utf-8")

    corpus = "\n".join(texts.values())
    for paper in papers:
        paper_id = str(paper.get("id", ""))
        paper_url = str(paper.get("paper", ""))
        collection = str(paper.get("collection", ""))
        expected_text = texts.get(collection, "")
        if corpus.count(paper_url) != 1:
            errors.append(f"{paper_id}: primary URL must appear exactly once across canonical catalogs")
        expected_anchor = f'<a id="{stable_anchor(paper_id)}"></a>'
        if expected_text.count(expected_anchor) != 1:
            errors.append(f"{paper_id}: canonical anchor is missing or duplicated")


def validate_curated_readmes(papers: list[dict[str, object]], errors: list[str]) -> None:
    selections: list[set[str]] = []
    papers_by_url = {str(paper["paper"]): paper for paper in papers}
    for path in README_PATHS:
        if not path.exists():
            errors.append(f"{path.relative_to(ROOT)}: file is missing")
            selections.append(set())
            continue
        text = path.read_text(encoding="utf-8")
        selected: set[str] = set()
        counts: Counter[str] = Counter()
        for url, paper in papers_by_url.items():
            count = text.count(f"]({url})")
            if count:
                selected.add(url)
                counts[str(paper["collection"])] += 1
            if count > 1:
                errors.append(f"{path.name}: paper URL appears {count} times: {url}")
        if counts != Counter(EXPECTED_CURATED_COUNTS):
            errors.append(
                f"{path.name}: curated collection counts are {dict(counts)}, "
                f"expected {EXPECTED_CURATED_COUNTS}"
            )
        selections.append(selected)
    if len(selections) == 2 and selections[0] != selections[1]:
        only_english = sorted(selections[0] - selections[1])
        only_chinese = sorted(selections[1] - selections[0])
        errors.append(
            "README selections differ: "
            f"English-only={only_english}, Chinese-only={only_chinese}"
        )


def validate() -> tuple[list[str], Counter[str], Counter[str], int]:
    errors: list[str] = []
    catalog = load_catalog(errors)
    if catalog is None:
        return errors, Counter(), Counter(), 0

    exact_fields(catalog, TOP_LEVEL_FIELDS, "catalog", errors)
    if catalog.get("schema_version") != "2.0":
        errors.append("schema_version: expected '2.0'")
    cutoff = parse_iso_date(catalog.get("last_verified"), "last_verified", errors)

    papers = catalog.get("papers")
    if not isinstance(papers, list):
        errors.append("papers: expected a list")
        return errors, Counter(), Counter(), 0

    seen_ids: dict[str, int] = {}
    seen_titles: dict[str, int] = {}
    seen_urls: dict[str, int] = {}
    collection_counts: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()

    for index, paper in enumerate(papers, start=1):
        label = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{label}: expected an object")
            continue
        exact_fields(paper, PAPER_FIELDS, label, errors)

        paper_id = paper.get("id")
        if not isinstance(paper_id, str) or len(paper_id.strip()) < 5:
            errors.append(f"{label}.id: expected at least 5 characters")
        elif paper_id in seen_ids:
            errors.append(f"{label}.id: duplicate of papers[{seen_ids[paper_id]}]")
        else:
            seen_ids[paper_id] = index

        title = paper.get("title")
        normalized_title = title.casefold().strip() if isinstance(title, str) else ""
        if len(normalized_title) < 5:
            errors.append(f"{label}.title: expected at least 5 characters")
        elif normalized_title in seen_titles:
            errors.append(f"{label}.title: duplicate of papers[{seen_titles[normalized_title]}]")
        else:
            seen_titles[normalized_title] = index

        published = parse_iso_date(paper.get("date"), f"{label}.date", errors)
        if published and cutoff and published > cutoff:
            errors.append(f"{label}.date: {published} is later than cutoff {cutoff}")

        paper_url = paper.get("paper")
        if not is_https_url(paper_url):
            errors.append(f"{label}.paper: expected a valid https URL")
        elif paper_url in seen_urls:
            errors.append(f"{label}.paper: duplicate of papers[{seen_urls[paper_url]}]")
        else:
            seen_urls[str(paper_url)] = index

        collection = paper.get("collection")
        record_type = paper.get("record_type")
        enum_value(collection, COLLECTIONS, f"{label}.collection", errors)
        enum_value(record_type, RECORD_TYPES, f"{label}.record_type", errors)
        enum_value(paper.get("training_regime"), TRAINING_REGIMES, f"{label}.training_regime", errors)
        enum_value(paper.get("state_source"), STATE_SOURCES, f"{label}.state_source", errors)
        topology = enum_list(
            paper.get("teacher_topology"),
            TEACHER_TOPOLOGIES,
            f"{label}.teacher_topology",
            errors,
            allow_empty=collection == "review_tutorial",
        )
        mechanism = paper.get("primary_mechanism")
        enum_value(mechanism, MECHANISMS, f"{label}.primary_mechanism", errors)
        tags = enum_list(
            paper.get("mechanism_tags"), MECHANISM_TAGS, f"{label}.mechanism_tags", errors
        )
        if mechanism in tags:
            errors.append(f"{label}.mechanism_tags: must not repeat primary_mechanism")
        enum_list(
            paper.get("signals"),
            SIGNALS,
            f"{label}.signals",
            errors,
            allow_empty=collection == "review_tutorial",
        )
        enum_list(paper.get("domains"), DOMAINS, f"{label}.domains", errors, allow_empty=False)
        validate_artifacts(paper.get("artifacts"), f"{label}.artifacts", errors)

        summary = paper.get("summary")
        if not isinstance(summary, str) or len(summary.strip()) < 20:
            errors.append(f"{label}.summary: expected at least 20 characters")
        evidence = validate_evidence(paper.get("evidence"), f"{label}.evidence", errors)
        validate_collection_rules(paper, label, evidence, errors)

        if isinstance(collection, str):
            collection_counts[collection] += 1
        if isinstance(record_type, str):
            type_counts[record_type] += 1

    missing_collections = COLLECTIONS - set(collection_counts)
    if missing_collections:
        errors.append(f"catalog: empty collections {sorted(missing_collections)}")

    validate_markdown_catalogs(papers, errors)
    validate_curated_readmes(papers, errors)

    return errors, collection_counts, type_counts, len(papers)


def main() -> int:
    errors, collections, record_types, total = validate()
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    collection_text = ", ".join(f"{key}={collections[key]}" for key in sorted(collections))
    type_text = ", ".join(f"{key}={record_types[key]}" for key in sorted(record_types))
    print(f"Validated {total} papers ({collection_text}; {type_text}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
