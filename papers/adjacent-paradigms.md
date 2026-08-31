# Adjacent Online Paradigms

These works are relevant to multi-teacher OPD but fail at least one strict criterion: independent frozen teachers, student-policy rollouts, or direct multi-teacher supervision. They are intentionally not counted as core MOPD.

## Online co-, self-, and multi-view distillation

| Paper | Date | Why adjacent rather than strict MOPD | Resources |
|---|:---:|---|---|
| [REGEN](https://arxiv.org/abs/2607.19450) | 2026-07 | Recycles specialist replay buffers through offline RL as an explicit lower-coupling alternative to MOPD. | [Code](https://github.com/yunjie-sysu/REGEN) |
| [DOPD](https://arxiv.org/abs/2606.30626) | 2026-06 | Routes supervision between one privileged teacher and a privileged student policy, rather than a pool of independent teachers. | — |
| [Be My Tutor / OPCoD](https://arxiv.org/abs/2606.14368) | 2026-06 | Two trainable peers tutor one another bidirectionally; there is no fixed teacher-to-one-student topology. | — |
| [Multi-Rollout OPD](https://arxiv.org/abs/2605.12652) | 2026-05 | Builds a teaching signal from sibling successes and failures; “multi” refers to rollouts, not independent teachers. | — |
| [CoDistill-GRPO](https://arxiv.org/abs/2605.08873) | 2026-05 | Two trainable policies co-distill inside GRPO rather than consolidating a fixed teacher pool. | — |
| [UniSD](https://arxiv.org/abs/2605.06597) | 2026-05 | Uses EMA/self teachers, multi-teacher agreement, and contrastive alignment within one self-distillation lineage. | [Code](https://github.com/Ahren09/UniSD) |

## Boundary cases to track separately

- [GATES](https://arxiv.org/abs/2602.20574): consensus across multiple samples from one privileged tutor, not multiple independent teachers.
- [AVSD](https://arxiv.org/abs/2605.20643): several privileged teacher views decomposed into shared consensus and view-specific residuals.
- [Skill-Conditioned Gated Self-Distillation](https://arxiv.org/abs/2605.28791): a verifier-gated, skill-conditioned self-teacher pool.
- [CoDA](https://arxiv.org/abs/2608.08764): student-rollout consensus/disagreement used as privileged context, not a conventional external teacher pool.

These boundary items are useful candidates for a future expanded metadata category. They are not yet part of `data/papers.json` unless individually promoted after full method-section review.

## Related routing/fusion, not multi-teacher

Single-teacher methods that route between objectives or executors can inspire MOPD but should not be mislabeled. Examples include SRPO, TRACE, StepOPSD, PADD, DRIFT, Relay-OPD, DASH-OPD, SAF-OPD, and WDL-OPD. Pure model merging, ordinary MoE routing, inference-only ensembles, and multi-agent debate without student training remain out of scope.
