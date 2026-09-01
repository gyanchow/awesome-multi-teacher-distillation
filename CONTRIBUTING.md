# Contributing

Thank you for helping keep this list accurate and useful. The repository favors well-classified, primary-source-backed entries over an unverified paper dump.

## Eligibility

An accepted research entry must have a public paper, technical report, or official proceedings page. Knowledge transfer from one or more teachers must be a material part of training; pure merging, inference-only ensembles, ordinary mixture-of-experts routing, debate without student training, and reward-only reinforcement learning are out of scope.

Choose exactly one primary collection:

- `multi_teacher_on_policy`: current or near-current student states, multiple independent supervisors, and a direct distillation objective;
- `offline_multi_teacher`: multiple teachers or an ensemble distilled through static data, teacher generations, cached targets, or replay;
- `adjacent_alternative`: a close peer, self/EMA, privileged-view, multi-rollout, or replay boundary case that fails a strict-MOPD test;
- `single_teacher_foundation`: a foundational generative or on-policy method with one teacher; or
- `review_tutorial`: a field-level survey or tutorial.

Record type and mechanism are separate from the collection. In particular, `system_report` is a record type, not a sixth category. Read the complete [taxonomy](resources/taxonomy.md) before proposing a boundary case.

## Submission checklist

1. Search the title, stable ID, and primary URL in `data/papers.json`.
2. Read the paper itself; do not classify from a search result, abstract snippet, or secondary list.
3. Use the current paper title and first public date in `YYYY-MM-DD` format.
4. Link the primary paper or proceedings page. Include artifacts only when the author or organization connection is explicit.
5. Answer the three evidence tests separately: student-generated states, multiple independent supervisors, and direct distillation objective.
6. Select the record type, training regime, state source, teacher topology, one primary mechanism, optional secondary mechanisms, supervision signals, and domains.
7. Write a neutral one-sentence mechanism summary, not a marketing claim or isolated leaderboard result.
8. Add or edit only the canonical entry in `data/papers.json`; generated catalogs and views must not be edited by hand.
9. Run `python3 scripts/render.py`, `python3 scripts/validate.py`, and `python3 scripts/render.py --check` from the repository root.

## Metadata rules

- Stable IDs use a namespace such as `arxiv:2608.19098`, `doi:10.x/...`, `acl:2026.acl-long.666`, or `cvf:cvpr2024-short-name`.
- Every list-valued facet contains unique controlled labels.
- `primary_mechanism` must not be repeated in `mechanism_tags`.
- Use `partial` only when part of a recipe satisfies an evidence test and explain the boundary in `classification_note`.
- Use `unclear` only while the exact method evidence remains unresolved; accepted entries should minimize this value.
- Use `not_applicable` for method evidence only on survey and tutorial records.
- `MOPD` means multi-teacher on-policy distillation here; write multi-rollout OPD as `MR-OPD`.
- Do not describe an arXiv preprint as peer reviewed unless an official proceedings page confirms publication.

## Pull requests

Keep each pull request focused. Point to the exact paper section that establishes the state source, teacher topology, and student-training objective. Explain every boundary decision and every official artifact link. A maintainer may move an entry to `papers/pending.md` when evidence is incomplete.

Automated discovery and metadata tools can help find candidates, but an accepting maintainer must verify the primary source and take responsibility for the final classification and wording.
