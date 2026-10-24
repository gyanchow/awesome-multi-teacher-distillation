#!/usr/bin/env python3
"""Validate and render the bounded mechanism audit; standard library only."""
from __future__ import annotations

import argparse
import csv
import io
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "paper_id", "study", "title", "source", "version", "locator",
    "learned_teacher_components", "state_origin", "refresh",
    "direct_student_target", "upstream_feedback", "integration_point", "caveat",
    "coding_checked_date", "analysis_group", "problem", "teacher_student_access",
    "method_details", "experiment_setup", "reported_findings", "evidence_limits",
    "survey_connection",
]

def md(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")

def outputs() -> dict[Path, str]:
    catalog = json.loads((ROOT / "data/papers.json").read_text())
    papers = {p["id"]: p for p in catalog["papers"]}
    audit = json.loads((ROOT / "data/mechanism-audit.json").read_text())
    rows = audit["studies"]
    seen: set[str] = set()
    if audit["schema_version"] != "1.0" or not rows:
        raise ValueError("Expected a non-empty schema 1.0 mechanism audit")
    date.fromisoformat(audit["last_verified"])
    for row in rows:
        for key in FIELDS:
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f"Missing text field {key}: {row.get('paper_id')}")
        if row["paper_id"] in seen or row["paper_id"] not in papers:
            raise ValueError(f"Duplicate or unknown catalog id: {row['paper_id']}")
        seen.add(row["paper_id"])
        if urlparse(row["source"]).scheme != "https":
            raise ValueError(f"Primary source must use HTTPS: {row['paper_id']}")
        if date.fromisoformat(row["coding_checked_date"]) > date.fromisoformat(audit["last_verified"]):
            raise ValueError("Study check date exceeds audit cutoff")
        if not row.get("source_locators"):
            raise ValueError(f"Missing primary-source locators: {row['paper_id']}")
        for loc in row["source_locators"]:
            if not all(isinstance(loc.get(k), str) and loc[k].strip() for k in ("section", "url", "supports")) or urlparse(loc["url"]).scheme != "https":
                raise ValueError(f"Invalid primary-source locator: {row['paper_id']}")
        if set(row["comparison"]) != {"state", "signal", "integration"}:
            raise ValueError(f"Missing comparison cells: {row['paper_id']}")

    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=FIELDS + ["catalog_collection"], lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({**{key: row[key] for key in FIELDS}, "catalog_collection": papers[row["paper_id"]]["collection"]})
    lines = [
        "# Mechanism Comparison", "",
        f"{len(rows)} purposively selected studies · Checked {audit['last_verified']}.", "",
        "Generated from [mechanism-audit.json](../data/mechanism-audit.json). "
        "Download [CSV](../data/mechanism-audit.csv) for filtering, or use the "
        "[decision guide](../resources/compare-methods.md) to choose a reading route.", "",
        audit["selection"], "", audit["verification"], "",
        "The collection column follows the current catalog. A row is a study or a specified "
        "training stage, not a performance rank or a claim of independent replication.", "",
        "| Study | Collection | Training state | Direct signal | Integration point |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        c = row["comparison"]
        cells = [f"[{row['study']}]({row['source']})", papers[row["paper_id"]]["collection"],
                 c["state"], c["signal"], c["integration"]]
        lines.append("| " + " | ".join(md(v) for v in cells) + " |")
    lines += ["", "Read the [30 detailed study cards](../resources/core-studies.md) for experimental conditions, reported findings, limitations and cross-paper connections.", "", "## Source notes and qualifications", ""]
    for row in rows:
        lines += [
            f"### {row['study']}", "",
            f"**Catalog ID:** {row['paper_id']}. **Source:** [{row['version']}]({row['source']}). "
            f"**Locator:** {row['locator']}", "",
            f"- **Learned components:** {row['learned_teacher_components']}",
            f"- **State origin:** {row['state_origin']}",
            f"- **Refresh:** {row['refresh']}",
            f"- **Direct student target:** {row['direct_student_target']}",
            f"- **Upstream feedback:** {row['upstream_feedback']}",
            f"- **Integration:** {row['integration_point']}",
            f"- **Qualification:** {row['caveat']}", "",
        ]
    lines += [
        "## Correct or reuse a record", "",
        "Cite the original study for its method and results. Cite this repository snapshot only "
        "when using its curation or coding. For corrections, give the paper version, section/equation, "
        "affected field, and replacement interpretation. See [CONTRIBUTING](../CONTRIBUTING.md).", "",
    ]
    cards = [
        "# Thirty Core Studies: Detailed Analysis", "",
        f"Primary-source checks: {audit['last_verified']}. Reported results have not been independently reproduced.", "",
        audit["selection"], "", audit["verification"], "",
        "Each card records the problem, required access, mechanism, experimental conditions, reported findings, evidence limits, and a cross-paper connection. The final connection is our synthesis. Numerical results retain their original setting and are not a common leaderboard.", "",
        "Use the [comparison table](../views/mechanism-comparison.md), [CSV](../data/mechanism-audit.csv), or [decision guide](compare-methods.md).", "",
        "## Contents", "",
    ]
    for i, row in enumerate(rows, 1):
        cards.append(f"{i}. [{row['study']}](#study-{i:02d}) — {row['analysis_group']}")
    for i, row in enumerate(rows, 1):
        cards += ["", f'<a id="study-{i:02d}"></a>', "", f"## {i}. {row['study']}", "",
                  f"{row['title']}", "",
                  f"**Source:** [{row['version']}]({row['source']}). **Catalog ID:** {row['paper_id']}. **Group:** {row['analysis_group']}.", ""]
        for label, key in [("Problem and inclusion", "problem"), ("Teachers, student and access", "teacher_student_access"),
                           ("Mechanism", "method_details"), ("Experimental setting", "experiment_setup"),
                           ("Reported findings", "reported_findings"), ("Evidence limits", "evidence_limits"),
                           ("Cross-paper synthesis", "survey_connection")]:
            cards += [f"**{label}.** {row[key]}", ""]
        cards += ["**Primary-source locators**", ""]
        for loc in row["source_locators"]:
            cards.append(f"- [{loc['section']}]({loc['url']}): {loc['supports']}")
    cards += ["", "## Corrections and reuse", "",
              "Please cite original papers for their results. Cite this repository snapshot when reusing its coding. Send corrections with the version, section or table, affected field, and proposed interpretation; see [CONTRIBUTING](../CONTRIBUTING.md).", ""]
    return {ROOT / "data/mechanism-audit.csv": buf.getvalue(),
            ROOT / "views/mechanism-comparison.md": "\n".join(lines),
            ROOT / "resources/core-studies.md": "\n".join(cards)}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate and fail if generated outputs differ")
    args = parser.parse_args()
    try:
        generated = outputs()
    except (KeyError, ValueError, OSError) as exc:
        parser.exit(1, f"Mechanism audit validation failed: {exc}\n")
    stale = []
    for path, content in generated.items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content)
    if stale:
        parser.exit(1, "Stale mechanism outputs: " + ", ".join(stale) + "\n")
    print(f"Mechanism audit valid; {len(generated)} outputs " + ("current." if args.check else "rendered."))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
