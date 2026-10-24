# Choosing a Multi-Teacher Distillation Comparison

[中文](compare-methods_zh-CN.md) · Checked 2026-10-24.

Start from the information you can access and the claim you want to test. The following routes identify comparable method families; they do not predict a universally best method.

## Choose the question before the method

| Your setting or question | Start with | What to hold fixed or report |
| --- | --- | --- |
| Only teacher answers or API text are available | TinyLLM, PerSyn, FAIR, Knowledge Purification, SCAS | Candidate generation, answer filtering, student-dependent selection, and total API cost. Changing selection does not by itself refresh training states. |
| Teacher distributions use different tokenizers | FuseLLM; multilingual antecedents in the full catalog | Alignment rules, unmatched tokens, corpus, and available distributions. Token averages require a common interface. |
| Student errors change later states or tool observations | MOPD and controlled offline/live comparisons | Who generated earlier actions and observations; rollout age; teacher scoring and collection cost. |
| Sources are called “multiple teachers,” but their roles differ | PromptSD, MAS-OPD, MT-SDPO | Separately learned components, context views, external feedback providers, and the direct distribution teacher. |
| Some capabilities improve while others deteriorate | Open-MOPD, Nash-MOPD, ROAD | Prompt and token exposure, objective, optimizer, per-domain scores, and held-out retention. Reduced local conflict is not a retention guarantee. |
| Compatible specialist weights are available | FuseChat and RGBM, alongside shared-student baselines | Initialization, model compatibility, pairwise/branch training, merge cost, and final retained capabilities. |
| You want to claim better efficiency | Rethinking capability merging and the cost notes in the audit | Matched compute versus matched supervision; preparation, training, tuning, and inference as separate denominators. |

Each named study has a primary-source link and locator in the [30-study comparison](../views/mechanism-comparison.md). Filter the [CSV](../data/mechanism-audit.csv) or read the [JSON and coding rules](../data/mechanism-audit.json). These cases are a purposive subset of the 146-record catalog, not a complete search or a leaderboard.

## A worked classification example

Consider a student answering a math question using two separately trained specialists. This is an illustrative example, not an experiment.

- If the specialists first generate a fixed answer dataset, later reranking those answers with the evolving student remains offline sequence transfer.
- If a saved student attempt is rescored repeatedly, the score may be current while the preceding tokens still come from an older student.
- If new student attempts are collected at a stated interval and specialists score those states, annotate both the direct teachers and the refresh interval.
- If specialists only critique an attempt and an EMA self-teacher converts that critique into a probability target, count the experts as upstream feedback sources and the EMA policy as the direct target source.

The three strict-MOPD tests must apply to the same transfer stage. A pipeline cannot satisfy them by combining separate facts about different stages.

## Reuse the evidence

1. Preserve the stable catalog ID, inspected source version or snapshot information, and exact section/equation.
2. Copy the [evaluation record template](evaluation-record-template.json) before comparing results. Null means not recorded; it never means zero cost or zero error.
3. Keep teacher competence, student inheritance, retained capabilities, and total cost separate.
4. Cite original papers for their methods and results; cite the repository snapshot for reused curation or coding.
5. Submit a source-backed correction when a field is wrong. AI-assisted extraction is not independent human review.

For how other LLM surveys make their comparisons useful, see the [survey-structure study](llm-survey-structures.md). For a beginner's route, use the [field guide](guide.md).
