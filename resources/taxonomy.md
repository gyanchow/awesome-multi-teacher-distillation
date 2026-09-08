# Taxonomy

The catalog uses one **mutually exclusive primary collection** plus several **orthogonal facets**. This avoids forcing papers into a single tree in which system reports, training regimes, teacher structures, and algorithms compete at the same level.

## Primary collections

| Collection | Inclusion rule | Current count |
|---|---|---:|
| `multi_teacher_on_policy` | Current or near-current student states receive direct distillation supervision from multiple independently identifiable teachers. | 47 |
| `offline_multi_teacher` | Multiple teachers or an ensemble supervise the student through static data, teacher generations, cached targets, or replay. | 45 |
| `adjacent_alternative` | Closely related online, peer, self/EMA, privileged-view, sibling-rollout, or replay method that fails at least one strict-MOPD test. | 11 |
| `single_teacher_foundation` | A foundational generative or on-policy distillation method with one teacher. | 3 |
| `review_tutorial` | A field-level survey or tutorial rather than a method record. | 4 |

The primary collection answers **where a reader should find the paper**. It does not encode every property of the work.

## Strict-MOPD evidence tests

Each record stores three separate evidence fields:

1. `student_generated_states`: whether the trained-on state or trajectory comes from the current or near-current student;
2. `multiple_independent_supervisors`: whether at least two independently identifiable teachers, expert checkpoints, or teacher policies supervise the student; and
3. `direct_distillation_objective`: whether those signals directly update the student through a divergence, sampled-token advantage, feature or field target, or an equivalent objective.

The allowed answers are `yes`, `no`, `partial`, `unclear`, and `not_applicable`. These values describe the three facts independently; they are not a single confidence score. A free-text `classification_note` records the paper-level rationale.

Strict MOPD requires `yes` or a clearly explained `partial` for all three tests. Static teacher data is offline multi-teacher distillation. A single teacher with several samples, views, or rollouts does not satisfy the independent-supervisor test. Pure parameter merging, inference-time ensembling, reward-only reinforcement learning, and debate without student training do not satisfy the direct-distillation test.

## Record type

`record_type` is independent of the primary collection:

- `method`: proposes or materially extends a training method;
- `analysis`: primarily diagnoses, compares, or explains a phenomenon;
- `system_report`: reports a larger model or system in which distillation is a material stage;
- `survey`: reviews a body of literature; and
- `tutorial`: teaches or synthesizes a field for practitioners.

This is why a frontier-model technical report remains in `multi_teacher_on_policy` while carrying `system_report` as a facet.

## Training regime and state source

`training_regime` records the overall recipe: `on_policy`, `offline`, `hybrid`, `online_peer`, `self_distillation`, or `not_applicable`.

`state_source` records the provenance of the states that receive supervision: `current_student`, `near_current_student`, `static_corpus`, `teacher_generated`, `replay_buffer`, `mixed`, or `not_applicable`.

Keeping these fields separate matters. A hybrid recipe can still contain a qualifying MOPD stage, while a current-student state source can belong to a single-teacher or peer method rather than multi-teacher MOPD.

## Teacher topology

A record can carry more than one topology facet:

| Facet | Meaning |
|---|---|
| `ensemble_to_one` | Predictions from an ensemble are compressed into one student. |
| `independent_multi_teacher` | At least two separately identifiable supervision sources are present. |
| `specialist_pool` | Teachers specialize by domain, task, reward, platform, or capability. |
| `checkpoint_pool` | Teachers are retained checkpoints, stages, seeds, or reasoning budgets. |
| `heterogeneous_pool` | Teachers differ in architecture, tokenizer, modality, latent space, or action space. |
| `debate_collective` | Teachers deliberate, critique, or review before supervision is formed. |
| `peer_mutual` | Trainable peers supervise one another bidirectionally. |
| `self_ema` | Teachers are copies, EMA variants, or descendants of the student lineage. |
| `privileged_views` | Supervision comes from different information views rather than independent experts. |
| `sequential_chain` | Teachers or assistants transfer knowledge in stages. |
| `single_teacher` | One teacher provides the distillation target. |

## Combination mechanism

Every method has one `primary_mechanism`; optional `mechanism_tags` capture secondary mechanisms without repeating the primary label.

- `direct_matching`: directly matches distributions, representations, actions, or fields;
- `routing_selection`: selects a teacher by domain, prompt, trajectory, step, token, or coordinate;
- `adaptive_weighting`: combines teacher targets or losses with learned or dynamic weights;
- `conflict_resolution`: detects, filters, decomposes, or reconciles incompatible supervision;
- `dynamic_scheduling`: reallocates domains, teachers, or optimization budgets over time;
- `heterogeneous_alignment`: bridges incompatible tokenizers, architectures, modalities, or latent spaces;
- `progressive_sequential`: transfers knowledge through ordered teachers or training stages;
- `collective_deliberation`: forms supervision through debate, critique, or peer review; and
- `not_applicable`: reserved for surveys and tutorials.

The primary mechanism is the paper's central combination contribution, not every operation in its training loss.

## Supervision signal

Signals are multi-valued: `logits_distribution`, `sampled_token_advantage`, `features`, `relations`, `responses_rationales`, `feedback_reward`, `action_distribution`, `latent_velocity`, `gradients`, and `teacher_generated_data`.

This axis separates methods that look similar at the topology level but expose very different information and cost profiles. For example, full-distribution reverse KL, sampled-token advantages, natural-language rationales, and latent flow matching all provide direct supervision in different spaces.

## Domain

The controlled domain labels are `llm_general`, `llm_reasoning`, `llm_agents`, `llm_alignment`, `nlp`, `speech`, `vision`, `multimodal`, `generative_models`, `recommendation_search`, `knowledge_graphs`, `robotics_embodied`, `scientific_healthcare`, and `general_machine_learning`.

Domains are intentionally multi-valued. A multimodal agent paper, for example, need not be forced into only one application bucket.

## How to browse

The five files in `papers/` are canonical, mutually exclusive catalogs. Files in `views/` are generated cross-sections of the same JSON source by mechanism, topology, signal, domain, record type, artifact availability, or time. A paper may appear in several derived views without becoming a duplicate catalog record.

When a classification is uncertain, keep the candidate in `papers/pending.md`, mark the unresolved evidence as `unclear`, and cite the exact method or training section needed to resolve it before acceptance.
