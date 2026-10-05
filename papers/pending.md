# Pending Papers and Artifacts

These items have not passed all relevant source or artifact checks as of **2026-10-05**. Pending papers are not included in the 134-record total.

## Papers needing method evidence

- **[Unified Audio Intelligence Without Regressing on Text Intelligence](https://arxiv.org/abs/2607.05196)** — Discovered in this refresh on 2026-10-05; first public date 2026-07-06. Section 4.4.3 names a multi-domain OPD stage and refers to the Nemotron-Cascade 2 recipe, but the inspected text does not identify Audex's actual teacher pool or spell out its direct distillation objective. Confirm these details before adding a strict-MOPD system record. The 2B model is SFT-only; do not transfer the 30B recipe to it.
- **[GCMRD: Global Consistency Multi-teacher Robustness Distillation](https://doi.org/10.1007/978-3-032-37356-4_26)** — Discovered 2026-10-05. Publisher metadata and abstract found, but the full method and earliest public version were not verified. Check whether student-dependent adversarial inputs satisfy the state criterion; do not decide the category from the abstract.
- **[UCM-Distill](https://doi.org/10.1016/j.inffus.2026.104817)** — Discovered 2026-10-05. Publisher abstract found; full method, exact bibliographic metadata, and teacher/state/objective details still need checking before acceptance.

## Artifact follow-up for an accepted paper

- **[Video-MOPD](https://arxiv.org/abs/2609.09300)** — Paper accepted after method verification. Its author-linked Hugging Face model `LandH/Video-MOPD-8B` returned HTTP 401 during this pass. The catalog's artifact list remains empty until availability can be verified. This does not make the paper itself pending.

## Candidate template

```markdown
- **Title:**
  - Discovered: YYYY-MM-DD
  - Paper / primary source:
  - Stable ID and first public date:
  - Proposed primary collection and record type:
  - State source and training regime:
  - Teacher topology and combination mechanism:
  - Supervision signals and domains:
  - Student-generated states evidence:
  - Multiple independent supervisors evidence:
  - Direct distillation objective evidence:
  - Verification still needed:
```
