# Search and Verification Strategy

**Cutoff:** 2026-08-31 (Asia/Shanghai). The catalog is a snapshot, not a claim of permanent completeness.

## Discovery queries

The seed search combined exact phrases and mechanism-level variants:

- `"multi-teacher on-policy distillation"`, `"multi teacher" "on-policy distillation"`
- `"multi-domain on-policy distillation"`, `"multi-expert" "on-policy distillation"`
- `MOPD distillation`, `multi-teacher OPD`, `specialize then unify distillation`
- `"multi-teacher knowledge distillation"`, `"multiple teacher distillation"`
- `ensemble distillation student`, `knowledge amalgamation heterogeneous teachers`
- `teacher selection routing multi-teacher distillation`
- citation and reference chaining from foundational, survey, and system papers

Searches covered arXiv, ACL Anthology, ACM/DOI landing pages, NeurIPS and PMLR proceedings, CVF Open Access, official project pages, author/organization GitHub repositories, and official model reports. General web search was used for discovery only.

## Evidence policy

Every accepted entry must have at least one primary source: the paper/preprint, official proceedings page, technical report, official project page, or author code repository. Titles and dates come from the primary paper record. Method labels come from reading the abstract and, when the boundary is unclear, the relevant method/training section.

The catalog does not infer peer-review status from an arXiv page. Code links are included only when their authorship or project connection is explicit. `—` means an official implementation was not verified by the cutoff date.

## Strict MOPD decision rule

All three must hold:

1. the student or a near-current copy/mixture of it generates the training trajectory or state;
2. at least two independent teachers, expert checkpoints, teacher views, or peer policies provide supervision; and
3. those signals directly update the student through divergence, sampled-token advantage, feature/field matching, or an equivalent objective.

System reports are kept separate from dedicated method papers. Static teacher data/logits/features/rationales are MTKD. Multi-rollout, EMA, privileged-view, and bidirectional co-distillation are adjacent unless they satisfy the independent-teacher criterion.

## Exclusions

- Pure parameter merging or weight averaging without distillation.
- Inference-only ensembles, self-consistency, and multi-agent debate without student training.
- Ordinary mixture-of-experts routing or multi-task learning.
- Reward-only RL where teachers do not provide a distillation target.
- A single teacher sampled many times, unless listed as a clearly labeled adjacent multi-view method.
- Blog posts or secondary list entries without a traceable primary source.

## Maintenance workflow

1. Put a newly discovered item in `papers/pending.md` with the discovery date and source.
2. Check title, first-public date, current version, teacher topology, rollout source, objective, and claimed official artifacts.
3. Assign exactly one primary category and write a neutral mechanism summary.
4. Add the entry to `data/papers.json` and its Markdown catalog.
5. Run `python3 scripts/validate.py`; review the diff manually.
6. Re-check renamed arXiv papers and dead project/code links during scheduled maintenance.

The initial discovery and organization were AI-assisted, followed by primary-source checks. A maintainer should independently review every item before publication and must do so before applying to the official Awesome index.
