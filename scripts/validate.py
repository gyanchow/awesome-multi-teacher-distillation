#!/usr/bin/env python3
"""Validate the curated paper catalog without third-party dependencies."""

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
README_PATH = ROOT / "README.md"

REQUIRED_TOP_LEVEL = {"last_verified", "categories", "scope_labels", "papers"}
REQUIRED_PAPER_FIELDS = {
    "id",
    "title",
    "date",
    "category",
    "scope",
    "domain",
    "paper",
    "code",
    "project",
    "summary",
}
CATEGORY_SCOPE = {
    "core_mopd": "strict",
    "mopd_systems": "system",
    "adjacent": "adjacent",
    "multi_teacher_kd": "background",
    "foundations_surveys": "foundation",
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


def parse_iso_date(value: object, label: str, errors: list[str]) -> date | None:
    if not isinstance(value, str):
        errors.append(f"{label}: expected YYYY-MM-DD string")
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid date {value!r}")
        return None
    if parsed.isoformat() != value:
        errors.append(f"{label}: date must use zero-padded YYYY-MM-DD")
    return parsed


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def load_catalog(errors: list[str]) -> dict[str, object] | None:
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)
    except (OSError, json.JSONDecodeError, DuplicateKeyError) as exc:
        errors.append(f"{DATA_PATH.relative_to(ROOT)}: {exc}")
        return None


def markdown_corpus() -> str:
    paths = [README_PATH, *sorted((ROOT / "papers").glob("*.md"))]
    return "\n".join(path.read_text(encoding="utf-8") for path in paths if path.exists())


def validate() -> tuple[list[str], Counter[str], int]:
    errors: list[str] = []
    catalog = load_catalog(errors)
    if catalog is None:
        return errors, Counter(), 0

    top_keys = set(catalog)
    missing_top = REQUIRED_TOP_LEVEL - top_keys
    extra_top = top_keys - REQUIRED_TOP_LEVEL
    if missing_top:
        errors.append(f"catalog: missing top-level fields: {sorted(missing_top)}")
    if extra_top:
        errors.append(f"catalog: unexpected top-level fields: {sorted(extra_top)}")

    cutoff = parse_iso_date(catalog.get("last_verified"), "last_verified", errors)
    categories = catalog.get("categories")
    if not isinstance(categories, list) or set(categories) != set(CATEGORY_SCOPE):
        errors.append(f"categories must contain exactly {sorted(CATEGORY_SCOPE)}")

    scope_labels = catalog.get("scope_labels")
    if not isinstance(scope_labels, dict) or set(scope_labels) != set(CATEGORY_SCOPE.values()):
        errors.append(f"scope_labels must contain exactly {sorted(set(CATEGORY_SCOPE.values()))}")

    papers = catalog.get("papers")
    if not isinstance(papers, list):
        errors.append("papers: expected a list")
        return errors, Counter(), 0

    seen_ids: dict[str, int] = {}
    seen_urls: dict[str, int] = {}
    seen_titles: dict[str, int] = {}
    counts: Counter[str] = Counter()
    corpus = markdown_corpus()

    for index, paper in enumerate(papers, start=1):
        label = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{label}: expected an object")
            continue

        fields = set(paper)
        missing = REQUIRED_PAPER_FIELDS - fields
        extra = fields - REQUIRED_PAPER_FIELDS
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
        if extra:
            errors.append(f"{label}: unexpected fields {sorted(extra)}")

        paper_id = paper.get("id")
        title = paper.get("title")
        category = paper.get("category")
        scope = paper.get("scope")
        paper_url = paper.get("paper")
        published = parse_iso_date(paper.get("date"), f"{label}.date", errors)

        if not isinstance(paper_id, str) or not paper_id.strip():
            errors.append(f"{label}.id: expected a non-empty string")
        elif paper_id in seen_ids:
            errors.append(f"{label}.id: duplicate of papers[{seen_ids[paper_id]}]: {paper_id}")
        else:
            seen_ids[paper_id] = index

        normalized_title = title.casefold().strip() if isinstance(title, str) else ""
        if len(normalized_title) < 5:
            errors.append(f"{label}.title: expected at least 5 characters")
        elif normalized_title in seen_titles:
            errors.append(f"{label}.title: duplicate of papers[{seen_titles[normalized_title]}]")
        else:
            seen_titles[normalized_title] = index

        if category not in CATEGORY_SCOPE:
            errors.append(f"{label}.category: invalid value {category!r}")
        else:
            counts[str(category)] += 1
            expected_scope = CATEGORY_SCOPE[str(category)]
            if scope != expected_scope:
                errors.append(
                    f"{label}: category {category!r} requires scope {expected_scope!r}, got {scope!r}"
                )

        if published and cutoff and published > cutoff:
            errors.append(f"{label}.date: {published} is later than cutoff {cutoff}")

        if not is_https_url(paper_url):
            errors.append(f"{label}.paper: expected a valid https URL")
        elif paper_url in seen_urls:
            errors.append(f"{label}.paper: duplicate of papers[{seen_urls[paper_url]}]: {paper_url}")
        else:
            seen_urls[str(paper_url)] = index
            if str(paper_url) not in corpus:
                errors.append(f"{label}: primary URL is absent from README.md and papers/*.md")

        for field in ("code", "project"):
            value = paper.get(field)
            if value is not None and not is_https_url(value):
                errors.append(f"{label}.{field}: expected null or a valid https URL")

        for field, minimum in (("domain", 2), ("summary", 20)):
            value = paper.get(field)
            if not isinstance(value, str) or len(value.strip()) < minimum:
                errors.append(f"{label}.{field}: expected at least {minimum} characters")

    if README_PATH.exists():
        readme = README_PATH.read_text(encoding="utf-8")
        badge_match = re.search(r"papers-(\d+)-blue", readme)
        if not badge_match:
            errors.append("README.md: paper-count badge not found")
        elif int(badge_match.group(1)) != len(papers):
            errors.append(
                f"README.md: badge says {badge_match.group(1)} papers, catalog contains {len(papers)}"
            )

        prose_match = re.search(r"machine-readable catalog with (\d+) verified entries", readme)
        if not prose_match:
            errors.append("README.md: machine-readable entry count not found")
        elif int(prose_match.group(1)) != len(papers):
            errors.append(
                f"README.md: prose says {prose_match.group(1)} entries, catalog contains {len(papers)}"
            )

    return errors, counts, len(papers)


def main() -> int:
    errors, counts, total = validate()
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    breakdown = ", ".join(f"{key}={counts[key]}" for key in CATEGORY_SCOPE)
    print(f"Validated {total} papers ({breakdown}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
