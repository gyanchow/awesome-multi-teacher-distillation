# How other surveys help readers use a research field

This note compares **12 additional structural case studies**, checked on **2026-10-24**. They are writing and resource-design examples, **not additions to the distillation paper catalog**. The selection spans general LLMs, retrieval, agents, multimodality, evaluation, annotation, and an adjacent NLP methodology survey.

We inspected the stated versions' actual sections, selected figures and tables, and companion resources. This is a purposive structure study, not a citation ranking, exhaustive review, or reproduction of the papers' experiments. Publication metadata and the version used for structural analysis are distinguished below; an arXiv structure is not assumed to match every section of its later journal article.

## Twelve patterns to learn from

| Paper and version inspected | Organizing pattern | One reusable artifact or lesson |
| --- | --- | --- |
| [A Survey of Large Language Models](https://arxiv.org/html/2303.18223v19), v19, March 2026; [FCS 2026 publication](https://doi.org/10.1007/s11704-026-60308-3) | Lifecycle chapters, with resources and applications as additional entry points. | Maintain a versioned resource index; do not copy a 144-page survey's scope into a short paper. |
| [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/html/2312.10997v5), v5, March 2024; preprint | Contrasts system designs, then examines components, control flow, and evaluation. | A side-by-side process diagram can expose exactly when student states or supervision change. |
| [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/html/2309.07864v3), v3, September 2023; [SCIS 2025 publication](https://link.springer.com/article/10.1007/s11432-024-4222-0) | Moves from individual components to applications, interactions, and collective behavior. | Keep teacher identity, feedback providers, and the student's direct training target at separate analytical levels. |
| [A Survey on Hallucination in Large Language Models](https://arxiv.org/html/2311.05232v2), v2, November 2024; [TOIS 2025 publication](https://doi.org/10.1145/3703155) | Defines failures before examining causes, detection, mitigation, and a focused application. | Connect each failure to an observable diagnostic and a relevant intervention. |
| [A Survey on Multimodal Large Language Models](https://arxiv.org/html/2306.13549v4), v4, November 2024; [NSR 2024 publication](https://doi.org/10.1093/nsr/nwae403) | Establishes interfaces, then training data, evaluation, extensions, and reliability. | Show a training example with information visibility and loss coverage, rather than only naming objectives. |
| [A Survey on Evaluation of Large Language Models](https://arxiv.org/html/2307.03109v9), v9, December 2023; [TIST 2024 publication](https://doi.org/10.1145/3641289) | Separates evaluation objectives, datasets, procedures, and conditional findings. | Map inheritance, retention, and cost claims to distinct measurements and controls. |
| [PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://aclanthology.org/2025.acl-long.958/), ACL 2025 formal version | Organizes methods and evidence around six criteria for judging planning capabilities. | Turn taxonomy fields into questions readers can use to select comparison candidates. |
| [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/), ACL 2025 formal version | Uses a concrete example, component definitions, construction, and evaluation; detailed inventories sit in appendices. | Carry one example through the explanation and move extensive specifications to a searchable resource. |
| [Towards a Mechanistic Understanding of Large Reasoning Models](https://aclanthology.org/2026.acl-long.889/), ACL 2026 formal version | Links study objects and research questions to training, reasoning, and failure chapters. | End a mechanism section with what the evidence resolves and what remains indistinguishable. |
| [A Survey of Reasoning-Intensive Retrieval](https://aclanthology.org/2026.acl-long.1949/), ACL 2026 formal version | Establishes evaluation before grouping methods by where reasoning enters retrieval. | Navigate by the integration stage while retaining backbone, scale, and task conditions. |
| [Large Language Models for Data Annotation and Synthesis](https://aclanthology.org/2024.emnlp-main.54/), EMNLP 2024 formal version | Separates production, assessment, and use of generated annotations. | Record signal generation, filtering, and student optimization separately; filtered data do not establish successful transfer. |
| [Conformal Prediction for Natural Language Processing](https://aclanthology.org/2024.tacl-1.82/), TACL 2024 formal version; broader than LLMs | Introduces prediction objects and guarantees before extensions and applications. | Place assumptions next to a mathematical claim; separate identities, local approximations, and empirical evidence. |

## Five reader-oriented principles

1. **Start from a reader's decision.** Make access requirements, trajectory availability, and parameter compatibility visible before presenting method names. Use the [comparison guide](compare-methods.md) to identify relevant candidates, rather than imply a universal winner.
2. **Use a concrete example to explain the abstractions.** Track one prompt through teacher answer generation, student-state scoring, and feedback-mediated supervision. Mark what is fixed and what refreshes.
3. **Keep each claim attached to its evidence conditions.** State initialization, task, baseline, loss masking, refresh schedule, and cost denominator when relevant. A taxonomy alone does not establish a causal mechanism or performance advantage.
4. **Give the paper and repository complementary jobs.** A paper fixes an argument and evidence snapshot; a repository supports inspection, downloads, and corrections. The [mechanism comparison](../views/mechanism-comparison.md) and [structured audit](../data/mechanism-audit.json) should preserve the same field meanings and source locators.
5. **Make contribution and maintenance practical.** State inclusion rules, retain unknown values, date verification, and record corrections. These choices can make a resource easier to reuse; this comparison does not establish that they cause higher citations or stars.

## Verified companion resources

These links were connected to the papers through the paper itself, an author project page, or an explicit companion-repository statement, and were accessible when checked:

- General LLM resources: [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey).
- Retrieval and agents: [RAG-Survey](https://github.com/Tongji-KGLLM/RAG-Survey), [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List).
- Multimodality and evaluation: [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models), [LLM-eval-survey](https://github.com/MLGroupJLU/LLM-eval-survey).
- Planning and computer use: [Awesome-LLM-Planning-Capability](https://github.com/wll199566/Awesome-LLM-Planning-Capability), [OS-Agent-Survey](https://github.com/OS-Agent-Survey/OS-Agent-Survey).
- Mechanisms and generated data: [Awesome-LRM-Mechanisms](https://github.com/AheadOFpotato/Awesome-LRM-Mechanisms), [LLM4Annotation](https://github.com/Zhen-Tan-dmml/LLM4Annotation).

We did not identify a dedicated author companion repository for the hallucination, reasoning-intensive retrieval, or conformal-prediction survey during this check. That is a verification limit, not proof that none exists. Companion resources may evolve independently of the inspected paper versions; their existence does not establish that every entry is current.
