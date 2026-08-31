# Contributing

Thank you for helping keep this list accurate. The repository favors a small number of well-classified, primary-source-backed entries over a large unverified dump.

## Before submitting a paper

Please check that the work has a public paper, technical report, or official proceedings page and that knowledge transfer from more than one source is a material part of training.

Classify it using exactly one primary category:

- `core_mopd`: the current or near-current student policy generates the training states, and at least two teachers, expert checkpoints, teacher views, or peer policies directly supervise the student.
- `mopd_systems`: a model/system report in which MOPD is a material training stage.
- `adjacent`: an online co-distillation, multi-view/self-teacher method, or a carefully motivated alternative/boundary case.
- `multi_teacher_kd`: offline or static-data transfer from multiple teacher logits, features, relations, responses, or rationales.
- `foundations_surveys`: a foundational policy/KD/OPD paper, survey, or tutorial needed to understand the field.

Pure parameter merging, inference-only ensembles, ordinary MoE routing, multi-agent debate without student training, and reward-only RL do not qualify as MOPD.

## Submission checklist

1. Search the title, arXiv ID, DOI, and paper URL in `data/papers.json` and the Markdown catalogs.
2. Read the paper itself; do not classify from a search snippet or another awesome list.
3. Use the paper's current title and first public date in `YYYY-MM-DD` form.
4. Link the primary paper/proceedings page. Link code only when it is an author or organization repository clearly tied to the work.
5. Write a neutral one-sentence summary of the mechanism—not a leaderboard or marketing claim.
6. Add one JSON entry and one Markdown catalog entry. Do not duplicate the same paper across multiple primary sections.
7. Run `python3 scripts/validate.py` from the repository root.

## Metadata style

- IDs use a stable namespace, such as `arxiv:2608.19098`, `doi:10.x/...`, `acl:2026.acl-long.666`, or `cvf:cvpr2024-short-name`.
- `—` means no official code/project link was verified; it does not claim that no implementation exists.
- Preprints must not be described as peer-reviewed unless an official proceedings page confirms publication.
- In tables, write the direction as `Teachers → student`.
- `MOPD` means Multi-Teacher On-Policy Distillation here; write Multi-Rollout OPD as `MR-OPD`.

## Human review and disclosure

Automated search, metadata extraction, and language tools may help discover candidates, but a maintainer must verify every accepted entry against a primary source and take responsibility for the final wording. This is also required before seeking inclusion in the official Awesome index.

## Pull requests

Keep each pull request focused. Explain the classification decision, quote or point to the section of the paper establishing the rollout source and teacher topology, and note any ambiguous boundary. The maintainers may move an entry to `papers/pending.md` while evidence is incomplete.
