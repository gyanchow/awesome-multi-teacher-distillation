# Search and Verification Strategy

**Latest search:** 2026-10-05 (Asia/Shanghai). This is an incremental refresh of the 2026-09-08 snapshot, not a claim of exhaustive coverage or a fresh review of every existing record. New accepted submissions reach 2026-10-01, and earlier omissions retain their first-public dates. See the [dated update record](update-2026-10-05.md) for method evidence and deferred candidates.

## Discovery queries

The seed search combined exact phrases and mechanism-level variants:

- `"multi-teacher on-policy distillation"`, `"multi teacher" "on-policy distillation"`
- `"multi-domain on-policy distillation"`, `"multi-expert" "on-policy distillation"`
- `MOPD distillation`, `multi-teacher OPD`, `specialize then unify distillation`
- `"multi-teacher knowledge distillation"`, `"multiple teacher distillation"`
- `ensemble distillation student`, `knowledge amalgamation heterogeneous teachers`
- `teacher selection routing multi-teacher distillation`
- `answer-verified teacher`, `teacher gating verifier`, `student-centric teacher selection`
- `soft-prompt teacher on-policy`, `self-extrapolating policy distillation`, `best-of-N teacher rollout`
- citation and reference chaining from foundational, survey, and system papers

Searches covered arXiv, ACL Anthology, ACM/DOI landing pages, NeurIPS and PMLR proceedings, CVF Open Access, official project pages, author/organization GitHub repositories, and official model reports. General web search was used for discovery only.

## Evidence policy

Every accepted entry must have at least one primary source: the paper/preprint, official proceedings page, technical report, official project page, or author code repository. Titles and dates come from the primary paper record. Method labels come from reading the abstract and, when the boundary is unclear, the relevant method/training section.

The catalog does not infer peer-review status from an arXiv page. Code links are included only when their authorship or project connection is explicit. `—` means an official implementation was not verified by the cutoff date.

## Classification protocol

Strict MOPD requires all three evidence tests to hold:

1. the student or a near-current copy/mixture of it generates the training trajectory or state;
2. at least two independently identifiable teacher models, expert checkpoints, or separately trained adapters provide supervision; different prompts or roles of a single unchanged teacher do not by themselves meet this test; and
3. those signals directly update the student through divergence, sampled-token advantage, feature/field matching, or an equivalent objective.

System reports are represented through `record_type`, not a separate primary collection. Static teacher data, logits, features, and rationales belong to `offline_multi_teacher`. Multi-rollout, EMA, privileged-view, peer, and bidirectional co-distillation belong to `adjacent_alternative` unless they satisfy every strict-MOPD test. Single-teacher generative OPD methods are kept in `single_teacher_foundation`; surveys and tutorials have their own collection.

After assigning one primary collection, the maintainer independently records training regime, state source, record type, teacher topology, primary and secondary mechanisms, supervision signals, domains, and the three evidence values. The controlled vocabulary is defined in `resources/taxonomy.md` and enforced by `data/schema.json` and `scripts/validate.py`.

## Exclusions

- Pure parameter merging or weight averaging without distillation.
- Inference-only ensembles, self-consistency, and multi-agent debate without student training.
- Ordinary mixture-of-experts routing or multi-task learning.
- Reward-only RL where teachers do not provide a distillation target.
- A single teacher sampled many times, unless listed as a clearly labeled adjacent multi-view method.
- Blog posts or secondary list entries without a traceable primary source.

## Maintenance workflow

1. Put a newly discovered item in `papers/pending.md` with the discovery date and source.
2. Check title, first-public date, current version, teacher topology, state source, objective, and claimed official artifacts.
3. Record all three strict-MOPD evidence tests and explain any `partial` or `unclear` value.
4. Assign exactly one primary collection, choose one primary mechanism, and write a neutral mechanism summary.
5. Add the entry to `data/papers.json`; run `python3 scripts/render.py` to rebuild canonical catalogs and views.
6. Run `python3 scripts/validate.py` and `python3 scripts/render.py --check`, then review the complete diff manually.
7. Re-check renamed arXiv papers and dead project/code links during scheduled maintenance.

Discovery and organization were AI-assisted, followed by primary-source checks. A maintainer should independently review the entries. Such review does not by itself resolve the official Awesome index’s separate non-AI-generated-list requirement; see the [submission audit](awesome-submission.md).
