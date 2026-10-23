# Survey Reading Guide

[中文](survey-guide_zh-CN.md) · Checked 2026-10-23.

Several surveys are useful for this repository. The closest verified sources cover MOPD within a broader OPD survey; general KD reviews supply the earlier multi-teacher literature. This search did not establish a standalone survey devoted exclusively to strict MOPD.

## Where to start

| Reading goal | Source and verified version | Recommended focus |
| --- | --- | --- |
| Understand current MOPD | [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626), v5, 2026-10-21; first posted 2026-04-01 | Section 6: teacher eligibility, routing, target composition, capability balance, and evolving specialists. Read Sections 2–3 first if the objectives are unfamiliar. |
| Compare OPD formulations | [Echoes of the Oracle](https://www.researchgate.net/publication/405427626_Echoes_of_the_Oracle_A_Survey_of_On-Policy_Distillation_in_the_Era_of_Large_Language_Models), author-uploaded preprint, 2026-05-29 | Section 3.2 covers multi-teacher OPD; the wider survey contrasts teacher access, supervision granularity, optimization styles, and failure modes. |
| Trace traditional multi-teacher methods | [A Comprehensive Survey on Knowledge Distillation](https://arxiv.org/abs/2503.12067), v2, 2025-10-11; first posted 2025-03-15 | Section 4.3: aggregation, adaptive weighting, and knowledge amalgamation. Section 6.1 connects the taxonomy to LLMs. |
| Study aggregation and uncertainty | [A Statistical Perspective on Knowledge Distillation](https://arxiv.org/abs/2609.33727), 2026-09 | Section 3 develops a statistical/Bayesian perspective; Section 4.1 discusses multiple teachers and reliability-dependent aggregation. |
| Build a broad LLM-KD map | [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116), first posted 2024-02-20 | Knowledge elicitation, algorithms, skills, and application domains; useful background before the recent MOPD literature. |
| Compare access and evaluation settings | [Survey on Knowledge Distillation for Large Language Models: Methods, Evaluation, and Application](https://arxiv.org/abs/2407.01885), 2024-07-02 | Sections 3.1–3.6: white-box/black-box KD and robustness evaluation. |
| Connect teacher signals and training data | [Knowledge Distillation and Dataset Distillation of Large Language Models](https://arxiv.org/abs/2504.14772), v2, 2026-01-03; first posted 2025-04-20 | The Multi-Teacher KD subsection and Sections 4–5 connect knowledge transfer, compact datasets, and synthetic data. |
| Learn the classical vocabulary | [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525), first posted 2020-06-09 | Response, feature, and relation knowledge; distillation schemes and applications. |

For a teaching-oriented introduction, the [NAACL 2025 tutorial](https://aclanthology.org/2025.naacl-tutorial.4/) covers language-model KD, including multi-teacher and self-distillation. It is cataloged as a tutorial rather than a survey.

## A short reading route

Start with the OPD survey's Section 6, then the comprehensive KD survey's Section 4.3, and finally the statistical review's Section 4.1. This connects current capability integration to earlier aggregation methods and their assumptions. Use Echoes of the Oracle to compare alternative ways of organizing OPD.

Apply the repository's three evidence tests to each cited method: who generated the training states, whether teachers are independently identifiable, and how their signals update the student. A survey's “multi-teacher” heading can include static vision methods, synthetic teacher variants, or broader integration pipelines. It does not by itself establish strict MOPD eligibility.

The OPD survey v5 is marked *Work in Progress*. For Echoes of the Oracle, the verified source is the author's ResearchGate upload; venue publication was not established. Revision dates above are distinct from first-public dates. Survey coverage and terminology should be checked against the original methods before being used as classification evidence.

See the [complete review catalog](../papers/reviews-tutorials.md), [method reading paths](reading-order.md), and [October 23 update record](update-2026-10-23.md).
