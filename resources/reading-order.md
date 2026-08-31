# Reading Order

Choose the path that matches your goal. Dates and links were last checked on 2026-08-31.

## A. New to on-policy distillation

1. [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) — soft targets, temperature, and ensemble compression.
2. [Policy Distillation](https://arxiv.org/abs/1511.06295) — policy compression and multiple expert policies.
3. [MiniLLM](https://arxiv.org/abs/2306.08543) — reverse-KL generative distillation.
4. [GKD](https://arxiv.org/abs/2306.13649) — student-generated sequences and generalized divergences.
5. [A Survey of On-Policy Distillation for LLMs](https://arxiv.org/abs/2604.00626) — modern map of objectives, signal sources, systems, and applications.

## B. LLM post-training and capability consolidation

1. [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780) — the first frontier report to name the MOPD stage explicitly.
2. [MOPD](https://arxiv.org/abs/2606.30406) — the canonical specialize-then-unify formulation.
3. [When Top-K Misses the Decision](https://arxiv.org/abs/2607.07050) — why distribution approximation can miss behavior-critical tokens.
4. [Open-MOPD](https://arxiv.org/abs/2608.19098) — reproducible pipeline and capability-budget diagnosis.
5. [D$^3$-MOPD](https://arxiv.org/abs/2608.24987) — dynamic domain scheduling.
6. [Consolidating RLVR Capabilities Across Domains](https://arxiv.org/abs/2608.27409) — controlled choice among merging, mixed RL, and MOPD.

## C. Agents, multimodal systems, and non-LLM domains

1. [UI-MOPD](https://arxiv.org/abs/2607.04425) — platform-conditioned GUI-agent routing.
2. [The Physics of Multi-Turn Long-Horizon Planning](https://arxiv.org/abs/2607.24720) — controlled single-/multi-teacher planning study.
3. [H-OPD](https://arxiv.org/abs/2607.02592) — token-level arbitration between text and vision-language teachers.
4. [CollectionLoRA](https://arxiv.org/abs/2605.25378) and [Poly-OPD](https://arxiv.org/abs/2608.04349) — image-editing and heterogeneous flow-model consolidation.
5. [ProteinOPD](https://arxiv.org/abs/2605.10189) — preference conflict beyond natural-language models.

## D. Classical and offline multi-teacher distillation

1. [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) — explicit multi-teacher response and relation transfer.
2. [Agree to Disagree](https://proceedings.neurips.cc/paper/2020/hash/91c77393975889bd08f301c9e13a44b7-Abstract.html) — conflict-aware gradient aggregation.
3. [One Teacher is Enough?](https://aclanthology.org/2021.findings-acl.387/) — multiple pretrained-language-model teachers.
4. [FuseLLM](https://arxiv.org/abs/2401.10491) — heterogeneous generative-distribution fusion.
5. [Beyond Answers / TinyLLM](https://arxiv.org/abs/2402.04616) — answer and rationale transfer from several LLMs.
6. [Knowledge Purification](https://arxiv.org/abs/2602.01064) — conflicts in multi-teacher LLM rationales.

## E. Designing a new MOPD method

Read [Counteraction-Aware MOPD](https://arxiv.org/abs/2605.27115) for interference, [Uni-OPD](https://arxiv.org/abs/2605.03677) for teacher calibration, [TU-OPD](https://arxiv.org/abs/2607.27770) for union/residual decomposition, [Uncertainty-Calibrated MOPD](https://arxiv.org/abs/2608.26735) for filtered updates, and the repository's [taxonomy](taxonomy.md) before choosing a routing unit and evaluation protocol.
