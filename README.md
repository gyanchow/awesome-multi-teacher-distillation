# Awesome Multi-Teacher Distillation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of research on consolidating complementary, conflicting, or specialized teachers into one student, with an emphasis on multi-teacher on-policy distillation (MOPD).

[中文](README_zh-CN.md)

## Contents

- [Scope](#scope)
- [Multi-Teacher On-Policy Distillation](#multi-teacher-on-policy-distillation)
- [Offline Multi-Teacher Distillation](#offline-multi-teacher-distillation)
- [Adjacent and Alternative Paradigms](#adjacent-and-alternative-paradigms)
- [Single-Teacher Foundations](#single-teacher-foundations)
- [Reviews and Tutorials](#reviews-and-tutorials)

## Scope

A work belongs to the strict MOPD collection when the current or near-current student generates the training states, multiple independently identifiable teachers provide supervision, and those signals directly update the student through a distillation objective. Static teacher data belongs to offline multi-teacher distillation; peers, self/EMA teachers, privileged views, sibling rollouts, and replay-based alternatives are labeled as adjacent unless they satisfy all three tests.

Every record has exactly one primary collection. Record type, training regime, state source, teacher topology, combination mechanism, supervision signal, and domain are independent facets, so a system report is no longer treated as a competing method category. The snapshot contains 95 verified records: 41 multi-teacher on-policy works, 41 offline multi-teacher works, 6 adjacent or alternative works, 3 single-teacher foundations, and 4 reviews or tutorials. Metadata was checked through 2026-08-31.

MOPD means multi-teacher on-policy distillation in this repository. Multi-rollout OPD is written as MR-OPD. Parameter merging, inference-only ensembles, ordinary mixture-of-experts routing, multi-agent debate without student training, and reward-only reinforcement learning are outside strict MOPD.

## Multi-Teacher On-Policy Distillation

- [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409) - Compares parameter merging, mixed-domain reinforcement learning, and MOPD under controlled experts and data.
- [D$^3$-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](https://arxiv.org/abs/2608.24987) - Adapts domain sampling from reverse-KL trajectories to reduce wasted updates across differently converging teachers.
- [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098) - Provides an open recipe with token-share balancing, gap-aware allocation, and refreshed student rewards.
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) - System report that consolidates nine domain-by-reasoning-effort policies with clipped sampled-token rewards.
- [When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2607.07050) - Shows how truncated teacher support can omit decision-critical tokens and cause tool-call drift.
- [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](https://arxiv.org/abs/2607.02592) - Arbitrates token-level supervision between vision-language and text-only teachers using confidence.
- [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406) - Gives a general specialize-then-unify formulation with routed dense supervision on student trajectories.
- [CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2605.25378) - Consolidates many visual-effect LoRAs through dual-stream routing and coarse-to-fine distillation.
- [ProteinOPD: Towards Effective and Efficient Preference Alignment for Protein Design](https://arxiv.org/abs/2605.10189) - Combines preference-specific protein teachers through an adaptively weighted geometric consensus.
- [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/abs/2605.01347) - Turns multiple debating teachers into confidence-weighted supervision for language models and agents.
- [Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220) - System report that interleaves cascade reinforcement learning with multi-domain OPD from strong checkpoints.
- [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780) - Early frontier-model report that explicitly names MOPD as a post-training capability-consolidation stage.

## Offline Multi-Teacher Distillation

- [Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation](https://aclanthology.org/2026.acl-long.666/) - Routes prompts by both teacher response quality and student learnability for personalized data synthesis.
- [Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs](https://arxiv.org/abs/2602.01064) - Purifies conflicting teacher rationales into one training rationale and studies alternative routing strategies.
- [Beyond Answers: Transferring Reasoning Capabilities to Smaller LLMs Using Multi-Teacher Knowledge Distillation](https://arxiv.org/abs/2402.04616) - Transfers answers and rationales from several language-model teachers into a smaller student.
- [Knowledge Fusion of Large Language Models](https://arxiv.org/abs/2401.10491) - Aligns and fuses token distributions from heterogeneous source language models through continual training.
- [AM-RADIO: Agglomerative Vision Foundation Model — Reduce All Domains Into One](https://arxiv.org/abs/2312.06709) - Agglomerates complementary vision-foundation-model representations into one efficient visual encoder.
- [One Teacher is Enough? Pre-trained Language Model Distillation from Multiple Teachers](https://arxiv.org/abs/2106.01023) - Co-finetunes several pretrained-language-model teachers and transfers hidden states and soft labels.
- [Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space](https://proceedings.neurips.cc/paper/2020/hash/91c77393975889bd08f301c9e13a44b7-Abstract.html) - Treats teachers as separate gradient objectives and searches for a Pareto-compatible student update.
- [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) - Seminal multi-teacher method that transfers averaged dark knowledge and intermediate relations.
- [Policy Distillation](https://arxiv.org/abs/1511.06295) - Establishes policy compression and transfer from multiple expert policies into one student.
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) - Introduces temperature-scaled knowledge distillation and ensemble-to-student compression.

## Adjacent and Alternative Paradigms

- [REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning](https://arxiv.org/abs/2607.19450) - Recycles specialist replay buffers as an offline alternative to coupled MOPD rollout training.
- [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626) - Routes supervision between privileged teacher and privileged student views rather than an independent teacher pool.
- [Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback](https://arxiv.org/abs/2606.14368) - Lets two trainable domain peers tutor one another through feedback-conditioned self-distillation.
- [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652) - Builds teacher signals from sibling rollouts; “multi” refers to rollouts rather than independent teachers.
- [CoDistill-GRPO: A Co-Distillation Recipe for Efficient Group Relative Policy Optimization](https://arxiv.org/abs/2605.08873) - Bidirectionally distills two co-trained policies inside group-relative policy optimization.
- [UniSD: Towards a Unified Self-Distillation Framework for Large Language Models](https://arxiv.org/abs/2605.06597) - Combines EMA teachers, agreement, contrastive alignment, and clipping within one self-teacher lineage.

## Single-Teacher Foundations

- [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898) - Introduces skew-KL objectives and an efficient hybrid online distillation pipeline.
- [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649) - Formalizes distillation on student-generated sequences and unifies several divergence objectives.
- [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) - Develops reverse-KL generative distillation with student-sampled behavior and stabilization methods.

## Reviews and Tutorials

- [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) - Reviews OPD objectives, signal sources, stabilization, systems, and applications.
- [Knowledge Distillation for Language Models](https://aclanthology.org/2025.naacl-tutorial.4/) - Tutorial covering prediction and representation matching, reinforcement-learning-based KD, and multi-teacher methods.
- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) - Surveys knowledge elicitation and white-box and black-box distillation for language models.
- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) - Organizes response-, feature-, and relation-based knowledge across training schemes and applications.

## Contributing

Suggestions and corrections are welcome. Please read the [contribution guide](CONTRIBUTING.md) before opening an issue or pull request.

## Footnotes

The complete canonical catalogs cover [multi-teacher on-policy distillation](papers/multi-teacher-on-policy.md), [offline multi-teacher distillation](papers/offline-multi-teacher.md), [adjacent and alternative paradigms](papers/adjacent-alternatives.md), [single-teacher foundations](papers/single-teacher-foundations.md), and [reviews and tutorials](papers/reviews-tutorials.md).

Cross-cutting views are available by [mechanism](views/by-mechanism.md), [teacher topology](views/by-teacher-topology.md), [supervision signal](views/by-supervision-signal.md), [domain](views/by-domain.md), [system report](views/system-reports.md), [verified artifact](views/with-artifacts.md), and [first public date](views/chronological.md).

For maintenance and reproducibility, see the [machine-readable catalog](data/papers.json), [schema](data/schema.json), [taxonomy](resources/taxonomy.md), [reading paths](resources/reading-order.md), [open research questions](resources/open-questions.md), and [search and verification protocol](resources/search-strategy.md).
