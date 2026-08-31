# Taxonomy

This taxonomy separates **where training states come from** from **how multiple knowledge sources are combined**. Those two questions are often conflated.

## Regime

| Regime | Training-state source | Supervision | Repository label |
|---|---|---|---|
| Strict multi-teacher OPD | Current or near-current student / mixture policy | Two or more independent teachers, expert checkpoints, teacher views, or peers | `MOPD` |
| MOPD system | Same as above, reported as one stage of a larger system | Material capability-consolidation stage | `System` |
| Offline multi-teacher KD | Static corpus, teacher generations, or cached activations | Multiple teacher logits, features, relations, responses, or rationales | `MTKD` |
| Ensemble distillation | Static data | A teacher ensemble distribution or prediction | `E→1` boundary of MTKD |
| Co-/self-distillation | One or more changing peers or copies of the student | Bidirectional, EMA, multi-view, or sibling-rollout signals | `Adjacent` |

## Teacher topology

- **Parallel specialists:** independently trained domain, reward, platform, modality, or budget experts.
- **Checkpoint teachers:** different stages, seeds, reasoning budgets, or retained specialist checkpoints.
- **Heterogeneous teachers:** different architectures, tokenizers, modalities, latent spaces, or action spaces.
- **Collective/debate:** several teachers exchange critiques before producing supervision.
- **Peer policies:** trainable models tutor or distill one another; not a fixed external teacher pool.
- **Multi-view/self teachers:** several privileged views or EMA/sibling policies derived from one lineage.

## Selection granularity

| Granularity | Typical question |
|---|---|
| Domain / task | Which specialist owns this dataset or environment? |
| Prompt / example | Which teacher is most reliable and teachable for this sample? |
| Trajectory | Which teacher evaluates the complete student rollout? |
| Step / span | Which teacher should supervise this reasoning or action segment? |
| Token | Which distribution or teacher is trustworthy at this position? |
| Vocabulary coordinate | Which teacher-support coordinates must be retained? |
| Latent field / pixel | Which visual capability field matches the student-induced state? |

## Aggregation and routing

- **Hard routing:** choose one teacher using metadata, a router, confidence, or outcome.
- **Soft weighting:** combine teacher losses or distributions with fixed or adaptive weights.
- **Consensus:** retain signals on which teachers agree; optionally model disagreement separately.
- **Union / residual:** represent a shared consensus plus teacher-specific residual capabilities.
- **Debate / review:** aggregate after inter-teacher critique or verification.
- **Dynamic scheduling:** adapt how often each domain or teacher receives rollout and update budget.
- **Sequential / progressive (`SEQ`):** teachers act in stages; this borders on teacher-assistant chains.

## Signal type and objective

- Full-vocabulary or top-$K$ logits; forward, reverse, symmetric, skewed, or generalized KL.
- Sampled-token log-probability gaps or advantages.
- Hidden-state, relation, attention, or feature matching.
- Natural-language feedback, answers, rationales, demonstrations, or synthetic data.
- Flow/velocity fields, representations, action distributions, and other domain-specific targets.

## Common failure modes

- **Teacher conflict:** useful gradients cancel or one expert overwrites another.
- **Capability imbalance:** long outputs, high initial KL, or slow domains consume disproportionate token budget.
- **Stale supervision:** asynchronous rollouts, rewards, or teacher checkpoints no longer match the current student.
- **Support truncation:** top-$K$ mass looks adequate but drops decision-critical coordinates.
- **Router collapse:** one teacher dominates, or out-of-domain prompts are sent to the wrong specialist.
- **Negative transfer / seesaw:** gains in one domain reduce general or neighboring capabilities.
- **Heterogeneous mismatch:** tokenizer, architecture, modality, latent, or action-space differences invalidate direct matching.
- **Teacher ceiling:** aggregation cannot create a reliable solution outside the union of teacher-supported behavior without exploration or external feedback.

## Boundary tests

A work is not strict MOPD merely because it contains multiple experts. Ask:

1. Who generated the state or trajectory being trained on?
2. Are there at least two independently identifiable supervision sources?
3. Do those sources directly affect the student's training objective?
4. Is the mechanism training-time distillation rather than inference-time ensembling or parameter merging alone?

If the first answer is “a static teacher dataset,” classify it as MTKD. If the second is “one teacher with several samples,” classify it as multi-view or multi-rollout adjacent work. If the third or fourth is “no,” keep it outside the catalog or in an explicitly related section.
