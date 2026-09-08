# Reading Paths

These paths are intentionally separate from the primary taxonomy. A paper has one canonical collection, but readers can approach the literature by prerequisite, mechanism, or application.

## From knowledge distillation to MOPD

1. [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) introduces temperature-scaled soft targets and ensemble compression.
2. [Policy Distillation](https://arxiv.org/abs/1511.06295) transfers expert policies into compact or multi-task students.
3. [MiniLLM](https://arxiv.org/abs/2306.08543) develops reverse-KL generative distillation.
4. [On-Policy Distillation of Language Models](https://arxiv.org/abs/2306.13649) formalizes training on student-generated sequences.
5. [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) provides a broader map of modern OPD.

## LLM capability consolidation

1. [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780) presents an early named MOPD stage in a frontier-model pipeline.
2. [MOPD](https://arxiv.org/abs/2606.30406) gives a general specialize-then-unify formulation.
3. [One Student, Many Teachers](https://arxiv.org/abs/2607.18293) implements lightweight task teachers as independently trained soft prompts on one frozen backbone.
4. [When Top-K Misses the Decision](https://arxiv.org/abs/2607.07050) studies decision-critical support lost by distribution approximation.
5. [Open-MOPD](https://arxiv.org/abs/2608.19098) provides an open recipe and analyzes capability-budget imbalance.
6. [D$^3$-MOPD](https://arxiv.org/abs/2608.24987) adapts the domain schedule during training.
7. [Consolidating RLVR Capabilities Across Domains](https://arxiv.org/abs/2608.27409) compares merging, mixed reinforcement learning, and MOPD under controlled conditions.
8. [Verify Before You Distill](https://arxiv.org/abs/2609.02998) verifies prompt-level teacher reliability before admitting dense supervision.
9. [Learn from Whoever Is Right](https://arxiv.org/abs/2609.02548) replaces domain-only routing with answer-verified teacher eligibility.
10. [Rethinking OPD II](https://arxiv.org/abs/2609.04172) analyzes prompt diversity and state coverage in three-teacher MOPD.

## Teacher routing and conflict

1. [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) is a direct multi-teacher response-and-relation baseline.
2. [Agree to Disagree](https://proceedings.neurips.cc/paper/2020/hash/91c77393975889bd08f301c9e13a44b7-Abstract.html) resolves teacher disagreement in gradient space.
3. [Uni-OPD](https://arxiv.org/abs/2605.03677) calibrates teacher reliability against student outcomes.
4. [Beyond the Best Teacher](https://arxiv.org/abs/2607.27770) decomposes teacher consensus and residual capabilities.
5. [Uncertainty-Calibrated MOPD](https://arxiv.org/abs/2608.26735) filters trajectories and token updates under uncertain supervision.
6. [Student-Centric Answer Selection](https://arxiv.org/abs/2605.26872) ranks verified teacher responses by estimated learning cost for the current student.
7. [Verify Before You Distill](https://arxiv.org/abs/2609.02998) rejects dense teacher updates when verifier probes expose unreliability.
8. [Learn from Whoever Is Right](https://arxiv.org/abs/2609.02548) admits all teachers that are verified correct for a sample and consolidates their feedback.

## Heterogeneous and non-LLM settings

1. [H-OPD](https://arxiv.org/abs/2607.02592) arbitrates between text-only and vision-language teachers at token level.
2. [CollectionLoRA](https://arxiv.org/abs/2605.25378) consolidates many image-effect adapters.
3. [Poly-OPD](https://arxiv.org/abs/2608.04349) bridges incompatible flow-model latent spaces.
4. [ProteinOPD](https://arxiv.org/abs/2605.10189) handles conflicting protein-design preferences.
5. [The Physics of Multi-Turn Long-Horizon Planning](https://arxiv.org/abs/2607.24720) studies teacher integration in long-horizon agents.
6. [CA-OPD](https://arxiv.org/abs/2609.02401) couples confidence-aware intervention with direct CE and KL in GUI grounding and OCR.
7. [LoFi RADIO](https://arxiv.org/abs/2609.02676) aligns three heterogeneous vision teachers into a low-field MRI backbone.

## Offline multi-teacher LLM distillation

1. [One Teacher is Enough?](https://arxiv.org/abs/2106.01023) distills hidden states and predictions from multiple pretrained language models.
2. [Knowledge Fusion of Large Language Models](https://arxiv.org/abs/2401.10491) aligns distributions across heterogeneous source models.
3. [Beyond Answers](https://arxiv.org/abs/2402.04616) transfers answers and rationales from several teachers.
4. [Exploring Knowledge Purification](https://arxiv.org/abs/2602.01064) consolidates conflicting multi-teacher rationales.
5. [Find Your Optimal Teacher](https://aclanthology.org/2026.acl-long.666/) routes prompts by both teacher quality and student learnability.
6. [Student-Centric Answer Selection](https://arxiv.org/abs/2605.26872) searches a large verified answer pool for examples the current student can learn efficiently.
7. [MERGED](https://arxiv.org/abs/2609.01913) turns VLM-teacher agreement into SFT data and meta-judged disagreement into DPO pairs.

## Distinguishing teacher pools from self, peers, and rollouts

1. [Multi-Rollout OPD](https://arxiv.org/abs/2605.12652) uses sibling student rollouts rather than independent teacher models.
2. [Best-of-N Teacher Rollout Selection](https://arxiv.org/abs/2605.09725) samples several trajectories from one teacher rather than several teachers.
3. [Skill-Conditioned Gated Self-Distillation](https://arxiv.org/abs/2605.28791) creates several privileged views of one synchronized policy.
4. [WDL-OPD](https://arxiv.org/abs/2608.09447) co-trains two learner branches against one frozen external teacher.
5. [RISE](https://arxiv.org/abs/2609.05295) extrapolates a synthetic teacher from checkpoints in one policy lineage.

For exhaustive browsing, use the generated views by [mechanism](../views/by-mechanism.md), [teacher topology](../views/by-teacher-topology.md), [supervision signal](../views/by-supervision-signal.md), [domain](../views/by-domain.md), or [date](../views/chronological.md).
