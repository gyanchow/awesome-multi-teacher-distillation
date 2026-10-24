# Thirty Core Studies: Detailed Analysis

Primary-source checks: 2026-10-24. Reported results have not been independently reproduced.

30 purposively selected studies: 12 offline or NLP antecedents, 14 direct MOPD methods/comparative analyses, and 4 adjacent integration or state-boundary studies. Reviews and single-teacher foundations are contextual references and are not counted among these 30. Selection favors mechanism contrasts and relevant empirical controls; it is not a field census or 30 independent algorithms.

AI-assisted primary-source method and experiment checks with paper versions and section/table locators. Findings are author-reported, not independently reproduced; cross-paper connections are our synthesis. No independent human double coding or exhaustive coverage is claimed. Source hashes identify inspected snapshots where available.

Each card records the problem, required access, mechanism, experimental conditions, reported findings, evidence limits, and a cross-paper connection. The final connection is our synthesis. Numerical results retain their original setting and are not a common leaderboard.

Use the [comparison table](../views/mechanism-comparison.md), [CSV](../data/mechanism-audit.csv), or [decision guide](compare-methods.md).

## Contents

1. [MT-BERT](#study-01) — Offline and NLP antecedents
2. [FuseLLM](#study-02) — Offline and NLP antecedents
3. [FuseChat](#study-03) — Offline and NLP antecedents
4. [TinyLLM](#study-04) — Offline and NLP antecedents
5. [PILE](#study-05) — Offline and NLP antecedents
6. [GOVERN](#study-06) — Offline and NLP antecedents
7. [PerSyn](#study-07) — Offline and NLP antecedents
8. [FAIR / Committee](#study-08) — Offline and NLP antecedents
9. [Knowledge Purification](#study-09) — Offline and NLP antecedents
10. [SCAS](#study-10) — Offline and NLP antecedents
11. [MergeDistill](#study-11) — Offline and NLP antecedents
12. [SoFT](#study-12) — Offline and NLP antecedents
13. [MOPD](#study-13) — Direct MOPD methods and comparative analyses
14. [Open-MOPD](#study-14) — Direct MOPD methods and comparative analyses
15. [TrustMOPD](#study-15) — Direct MOPD methods and comparative analyses
16. [Delta-MOPD](#study-16) — Direct MOPD methods and comparative analyses
17. [Cross-teacher guarding](#study-17) — Direct MOPD methods and comparative analyses
18. [Nash-MOPD](#study-18) — Direct MOPD methods and comparative analyses
19. [Rethinking capability merging](#study-19) — Direct MOPD methods and comparative analyses
20. [PromptSD](#study-20) — Direct MOPD methods and comparative analyses
21. [D3-MOPD](#study-21) — Direct MOPD methods and comparative analyses
22. [DN-MOPD](#study-22) — Direct MOPD methods and comparative analyses
23. [MOPD-Router / ExpertAlign](#study-23) — Direct MOPD methods and comparative analyses
24. [Latent-MOPD](#study-24) — Direct MOPD methods and comparative analyses
25. [SF-MOPD](#study-25) — Direct MOPD methods and comparative analyses
26. [UCMOPD](#study-26) — Direct MOPD methods and comparative analyses
27. [RGBM / Fisher view](#study-27) — Adjacent integration and state boundaries
28. [MT-SDPO](#study-28) — Adjacent integration and state boundaries
29. [MAS-OPD](#study-29) — Adjacent integration and state boundaries
30. [ROSS](#study-30) — Adjacent integration and state boundaries

<a id="study-01"></a>

## 1. MT-BERT

One Teacher is Enough? Pre-trained Language Model Distillation from Multiple Teachers

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2106.01023). **Catalog ID:** arxiv:2106.01023. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can several pretrained encoders jointly supervise a compressed task model, and should unreliable teachers contribute equally on each labeled example?

**Teachers, student and access.** Twelve-layer BERT, RoBERTa and UniLMv2 teachers; four-/six-layer UniLM-initialized students. Requires teacher hidden states, predictions, task labels and co-finetuning access.

**Mechanism.** Fixed labeled task examples, not autoregressive student trajectories. No student-rollout refresh in the coded training stage. Aligned teacher hidden states, error-weighted soft labels and gold-label loss. Several teacher losses update one compressed task model.

**Experimental setting.** SST-2 sentiment classification, RTE inference and MIND news-topic classification; accuracy, plus macro-F1 on imbalanced MIND. Five repetitions are averaged. Compares four-/six-layer single-teacher distillers, teacher combinations, and removal of co-finetuning or loss weighting.

**Reported findings.** Table 2 gives six-layer MT-BERT SST-2 accuracy 94.6 versus TinyBERT6 93.1; RTE 75.7 versus 70.0. The strongest UniLM teacher remains higher on those tasks (95.1 and 81.3). Table 3 and Figures 4-5 support benefits from the tested teacher combinations and component choices.

**Evidence limits.** SST-2/RTE baseline numbers are taken from original reports, while MIND baselines are rerun. Results concern supervised encoder compression, not autoregressive skill integration. Task labels and teacher-layer correspondence are important assumptions.

**Cross-paper synthesis.** An early example of reliability weighting and representation alignment. Contrast with TrustMOPD's unlabeled reference-relative reliability proxy and with MergeDistill's task-agnostic masked-LM transfer.

**Primary-source locators**

- [§§2.1–2.2, Eqs.1–3, footnote4; §3.1; PDF pp.2–3](https://arxiv.org/pdf/2106.01023): Method, state provenance and integration mechanism
- [§§3.1–3.4; Tables 1–3; Figures 3–5; PDF pp.3–5.](https://arxiv.org/pdf/2106.01023): Experimental setting, author-reported results and limitations

<a id="study-02"></a>

## 2. FuseLLM

Knowledge Fusion of Large Language Models

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2401.10491). **Catalog ID:** arxiv:2401.10491. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can models with different vocabularies and architectures contribute to one language model without interpolating incompatible weights?

**Teachers, student and access.** Llama-2, OpenLLaMA and MPT, all 7B; another Llama-2 7B is the trainable target. Requires teacher predictive distributions and token alignment on the same raw corpus.

**Mechanism.** Fixed MiniPile corpus prefixes scored by the source models. Corpus histories remain fixed; teacher distribution alignment/fusion is applied to those histories. Aligned and selected/weighted source distributions plus causal-language-model loss. Prediction-space fusion directly trains one target model.

**Experimental setting.** One epoch over MiniPile (approximately 1.8B tokens). BBH evaluates 27 reasoning tasks, five commonsense tasks use zero-shot likelihood, and MultiPL-E evaluates ten programming languages. Baselines include source models and Llama-2 continual training on the same corpus without fused targets.

**Reported findings.** §4.2 reports 5.16% average relative BBH improvement over Llama-2, compared with 1.86% for corpus-only continual training. Gains also appear in the commonsense and code aggregates. Geometric Shapes and Word Sorting regress, so gains are not uniform across tasks.

**Evidence limits.** Tokenizer alignment may fall back to one-hot targets; corpus coverage and weak sources can affect transfer. The reported relative improvements are not percentage-point changes or controlled evidence for arbitrary teacher pools.

**Cross-paper synthesis.** Distribution alignment and fusion into one student contrast with MergeDistill's union vocabulary and FuseChat's pairwise students followed by parameter merging.

**Primary-source locators**

- [§§3.1–3.3, Eqs.1–5, Algorithm1; §4; PDF pp.3–6](https://arxiv.org/pdf/2401.10491): Method, state provenance and integration mechanism
- [§§4.1–4.4; Tables 1–3; Algorithm 1; Eq.5.](https://arxiv.org/pdf/2401.10491): Experimental setting, author-reported results and limitations

<a id="study-03"></a>

## 3. FuseChat

FuseChat: Knowledge Fusion of Chat Models

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2408.07990). **Catalog ID:** arxiv:2408.07990. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** How can heterogeneous chat models be consolidated without making simultaneous many-teacher fusion too difficult?

**Teachers, student and access.** OpenChat-3.5-7B is the main pivot; five other sources range from 7B through Mixtral-8x7B to Qwen1.5-72B. Requires source distributions for pairwise alignment and compatible pivot-shaped target parameters for final SCE merging.

**Mechanism.** Fixed instruction-response dataset prefixes. No continual student-rollout refresh in the pairwise transfer stage. Pairwise aligned teacher distributions and supervised response targets. Pairwise transfer first; SCE parameter merging consolidates the resulting targets.

**Experimental setting.** About 95,000 fixed dialogues, including pivot-training data and new community data; pairwise targets train three epochs. Evaluates AlpacaEval 2.0 with GPT-4-1106-Preview and MT-Bench with GPT-4-0125-Preview; includes pivot SFT, simultaneous multi-source fusion, individual pairwise targets, and inference ensembles.

**Reported findings.** Table 1: the final 7B model's AlpacaEval length-controlled win rate is 17.16 versus 14.50 for pivot SFT; MT-Bench average is 7.38 versus 6.88. Pairwise targets usually improve over simultaneous fusion, and merging further improves these aggregate scores.

**Evidence limits.** These are LLM-judge benchmarks; the 7B target does not outperform all source models or all inference ensembles. Dataset engineering, pivot choice and the staged training budget affect conclusions; hallucination mitigation is not directly established.

**Cross-paper synthesis.** Use as a counterexample to treating every multi-teacher method as concurrent supervision of one shared student. Compare its distill-then-merge pipeline with RGBM's merge–branch-OPD–remerge sequence.

**Primary-source locators**

- [§§3.1–3.4, Eqs.1–4, Fig.2; §6; PDF pp.4–6,10](https://arxiv.org/pdf/2408.07990): Method, state provenance and integration mechanism
- [§§4.1–4.4; Table 1; Figures 3–4; §6 limitations.](https://arxiv.org/pdf/2408.07990): Experimental setting, author-reported results and limitations

<a id="study-04"></a>

## 4. TinyLLM

Beyond Answers: Transferring Reasoning Capabilities to Smaller LLMs Using Multi-Teacher Knowledge Distillation

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2402.04616). **Catalog ID:** arxiv:2402.04616. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can several teachers' rationales transfer reasoning to compact sequence-to-sequence students more effectively than answer-only or single-rationale supervision?

**Teachers, student and access.** FLAN-T5-xlarge 3B and LLaMA-2-chat 7B generate rationales; FLAN-T5 students are 80M, 250M and 780M. Teacher text access suffices, but gold answers are supplied during rationale construction.

**Mechanism.** Teacher-generated rationales and gold answers under teacher-forced training prefixes. Preconstructed rationale supervision; no student-prefix collection in the coded update. Token cross-entropy on teacher rationales and gold answers, with teacher-specific task prefixes. Multiple rationale sources train one student through separate task-conditioned losses.

**Experimental setting.** Accuracy on OBQA, ARC, PIQA, RiddleSense, PubMedQA and BioASQ; compares fine-tuning, standard KD and Distill-step-by-step. Table 2 removes in-context examples, individual/diverse teachers, and gold-answer conditioning; Figure 2 varies training-set size.

**Reported findings.** Table 1: the 250M student's six-dataset mean is 65.02, versus 58.29 for full fine-tuning and 58.94 for Distill-step-by-step. Component ablations are lower in the reported 780M setup. Student scores exceeding teacher inference scores do not establish universally superior general reasoning.

**Evidence limits.** Reasoning quality is mainly inferred from answer accuracy; giving teachers the correct answer does not certify rationale faithfulness. Teachers and task-trained students do not have identical adaptation histories; only two teachers and selected QA tasks are tested.

**Cross-paper synthesis.** Provides the rationale-pooling baseline for Knowledge Purification. Contrast its fixed teacher-forced targets with FAIR's cached student-error-informed data and live OPD states.

**Primary-source locators**

- [§§3.2–3.3, Eqs.1–4; §4.1; PDF pp.3–4](https://arxiv.org/pdf/2402.04616): Method, state provenance and integration mechanism
- [§§4.1–4.4; Tables 1–2; Figure 2; method Eqs.1–4.](https://arxiv.org/pdf/2402.04616): Experimental setting, author-reported results and limitations

<a id="study-05"></a>

## 5. PILE

PILE: Pairwise Iterative Logits Ensemble for Multi-Teacher Labeled Distillation

**Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2022.emnlp-industry.60.pdf). **Catalog ID:** acl:2022.emnlp-industry.60. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can relevance labels correct biased ensemble ranking logits before they teach a smaller ranker?

**Teachers, student and access.** Three twelve-layer teachers share pretraining but are finetuned on different samples; a six-layer student receives corrected logits. Requires teacher scores and human relevance labels on query–document pairs.

**Mechanism.** Logged/labeled query-document examples. Iterative ensemble correction changes weights, not the provenance of fixed inputs. Corrected ensemble ranking logits. Corrected logit ensemble supervises one compact ranker.

**Experimental setting.** Commercial Baidu search data; teacher comparisons, base student, single-teacher KD, averaged ensemble KD and PILE-KD. Offline positive-negative ratio (PNR), deployed interleaving, DCG and annotator Good/Same/Bad comparisons; teacher-count and update-rate ablations.

**Reported findings.** Table 2: student PNR is 3.18 with PILE, 3.16 with averaged teachers, 3.15 with one teacher and 3.11 without distillation. Table 3 reports positive deployment changes for random/tail queries. These are ranking-specific metrics; PNR 3.18 is not an accuracy percentage.

**Evidence limits.** Proprietary data and deployment protocols limit independent reproduction. Label-driven correction is not applicable unchanged when labels are absent. Online experiments refer to deployed evaluation, not on-policy training.

**Cross-paper synthesis.** Shows label-based reliability before generative LLMs. GOVERN removes label dependence from its first stage, while TrustMOPD uses a reference-relative proxy; their evidence and tasks differ.

**Primary-source locators**

- [§§3.1–3.3, Fig.1; §§4.1–4.2; printed pp.589–591](https://aclanthology.org/2022.emnlp-industry.60.pdf): Method, state provenance and integration mechanism
- [§§4.1–4.6; Tables 2–3; Figures 2–3; §3.3.](https://aclanthology.org/2022.emnlp-industry.60.pdf): Experimental setting, author-reported results and limitations

<a id="study-06"></a>

## 6. GOVERN

GOVERN: Gradient Orientation Vote Ensemble for Multi-Teacher Reinforced Distillation

**Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2024.emnlp-industry.120.pdf). **Catalog ID:** acl:2024.emnlp-industry.120. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** How can unlabeled examples support sample-wise teacher selection before a supervised answer-selection stage?

**Teachers, student and access.** Four ERNIE-2.0 teachers range from 125M to 10B; the deployed student is 125M/12 layers. Access to scalar relevance logits is required; the base vote rule uses student predictions, while GOVERN-CA also uses labels.

**Mechanism.** Fixed question-paragraph inputs, unlabeled then labeled. Teacher selection depends on current student scalar logits; no generated-history refresh. MSE to selected ensemble logits; supervised GOVERN-CA adds label-guided weighting. Per-example selected targets directly train one student.

**Experimental setting.** 100M unlabeled and about 2.47M labeled question–paragraph pairs from commercial search. Evaluates question- and pair-level recall at 90% precision; distilled results average five seeds. Deployment compares answer quality and user behaviors; a smaller-student ablation varies teacher number.

**Reported findings.** Table 2: unlabeled GOVERN gives question-level recall 83.65 versus 82.04 for mean-ensemble distillation; GOVERN-CA gives 83.69. Table 3 reports positive answer-quality changes. The authors also note that large teachers may be underfitted, qualifying student-versus-teacher comparisons.

**Evidence limits.** Private data and limited deployment statistics constrain replication. The majority rule does not by itself establish each selected teacher's competence. Its scalar-logit directions are not full parameter-gradient vectors.

**Cross-paper synthesis.** Compare teacher-logit disagreement handling with ROAD's same-trajectory parameter-gradient intervention. Dynamic student-dependent selection here still uses fixed examples.

**Primary-source locators**

- [§3.1.1, Eqs.3–7; §3.2, Eqs.8–11; §4.2; Limitations](https://aclanthology.org/2024.emnlp-industry.120.pdf): Method, state provenance and integration mechanism
- [§§4.1–4.6; Tables 1–4; Figure 3; §3.1.1 Eqs.3–7; §3.2 Eqs.8–11.](https://aclanthology.org/2024.emnlp-industry.120.pdf): Experimental setting, author-reported results and limitations

<a id="study-07"></a>

## 7. PerSyn

Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation

**Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2026.acl-long.666.pdf). **Catalog ID:** acl:2026.acl-long.666. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can a prompt router balance teacher quality against what a particular student can learn, before paying to generate every teacher response?

**Teachers, student and access.** Five main students span Qwen2.5 0.5B/1.5B/3B, Gemma-2-2B and Llama-3.2-3B. Pools contain 19 instruction and 15 math teachers. Needs teacher text, student likelihood and quality rewards; a student-specific router is calibrated with parallel teacher generations.

**Mechanism.** Teacher-generated responses selected by a learned prompt router. Router learned for the student/setting before dataset synthesis; response-only SFT uses fixed synthetic histories. Token likelihood of routed teacher responses. Routing consolidates sources into a synthetic dataset before training one student.

**Experimental setting.** 50K Magpie-Zoo instruction prompts and 10K OpenR1-derived math queries; 2.5K parallel-response prompts calibrate routers. Tests IFEval, TruthfulQA, LiveBench, GSM8K, MATH and SVAMP against strongest-teacher, mixed, same-family and CAR strategies.

**Reported findings.** Table 2 reports the highest six-benchmark average for PerSyn on all five main students; Qwen2.5-3B averages 58.09 versus CAR's 57.17. Individual exceptions remain: its MATH score 57.80 is below CAR's 58.10. Routing therefore supports a conditional aggregate benefit, not universal superiority.

**Evidence limits.** Router calibration still pays for all teachers on a subset; a router is trained separately per student/setting. No demonstrated elimination of all generation costs or applicability to arbitrary new tasks.

**Cross-paper synthesis.** Distinguish prompt-level route-before-generation from SCAS's iterative answer selection, and distinguish adaptation to student learnability from on-policy state collection.

**Primary-source locators**

- [§§2.1–2.3, Eqs.1–4; §3.1; Limitations](https://aclanthology.org/2026.acl-long.666.pdf): Method, state provenance and integration mechanism
- [§§2.1–2.3 Eqs.1–4; §§3.1–3.3; Table 2; Limitations.](https://aclanthology.org/2026.acl-long.666.pdf): Experimental setting, author-reported results and limitations

<a id="study-08"></a>

## 8. FAIR / Committee

Learning from Committee: Reasoning Distillation from a Mixture of Teachers with Peer-Review

**Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2025.findings-acl.217.pdf). **Catalog ID:** acl:2025.findings-acl.217. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can teachers explain a student's mistakes and cross-review rationales before those texts become training targets?

**Teachers, student and access.** GPT-3.5-Turbo, Gemini-1.0-Pro and Mixtral-8x7B-Instruct teachers; Llama2-7B-chat, Qwen2.5-1.5B-Instruct and Llama3.1-8B-Instruct students. Uses teacher text APIs and a precollected student-error set.

**Mechanism.** Precollected student errors inform corrected-rationale and feedback examples used in fixed fine-tuning. Fine-tuning data are not continually refreshed with new student errors; that extension is left for future work. Accepted rationale and mistake-feedback token targets. Committee output is consolidated into training data for one student.

**Experimental setting.** GSM8K, SVAMP, StrategyQA and LogiQA accuracy; compares individual teachers, pooled teachers with/without peer review, and feedback-loss weights. A 100-example LogiQA sample checks automated review against human judgments.

**Reported findings.** Table 1: Qwen2.5-1.5B GSM8K accuracy is 72.48 with reviewed multiple teachers versus 67.48 without review and 68.01 for GPT-only distillation. The same-table multi-teacher gains recur across tested students; comparisons to separate published systems mix training settings.

**Evidence limits.** Peer review is a filter, not a correctness guarantee. The authors' limitation notes that errors are collected once and not refreshed each epoch. Teacher/API cost and varying feedback weights matter; unrelated-system score comparisons are not controlled causal evidence.

**Cross-paper synthesis.** Connects teacher feedback to student-aware offline data. Contrast with MT-SDPO's online feedback-conditioned EMA target and ROSS's historical-rollout span selection.

**Primary-source locators**

- [§§3.1–3.4, Eqs.1–7, Fig.2; Limitations; printed pp.4192–4194,4198](https://aclanthology.org/2025.findings-acl.217.pdf): Method, state provenance and integration mechanism
- [§§4.1–4.4; Tables 1–2; §§5.1–5.5; Table 3; Limitations; method §§3.1–3.4.](https://aclanthology.org/2025.findings-acl.217.pdf): Experimental setting, author-reported results and limitations

<a id="study-09"></a>

## 9. Knowledge Purification

Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2602.01064). **Catalog ID:** arxiv:2602.01064. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** When several rationale teachers conflict, should the student learn every rationale, an aggregated rationale, or a selected teacher?

**Teachers, student and access.** FLAN-T5-xlarge, Llama-2-chat, BioMistral-7B and Llama-3.1-8B-Instruct; FLAN-T5 students 77M/248M/783M. Text targets suffice; routers/selector additionally require encoders, supervised preferences or student losses depending on variant.

**Mechanism.** Teacher rationale prefixes and gold answers. RL-based selection can alternate with distillation; teacher-rationale provenance remains offline. Selected/consolidated rationale tokens plus a gold-answer objective. One rationale target per question updates a common student.

**Experimental setting.** OBQA, ARC, RiddleSense and PubMedQA; 80% training data distills students and 20% forms router public data. Compares full fine-tuning, Distill-step-by-step and TinyLLM against aggregation, three routing variants and RL teacher selection; analyzes OOD transfer, teacher count and compute.

**Reported findings.** Table 1 and §5.1 favor the similarity router or RL selector on average, depending on student size; there is no single dominant variant. The 783M RL-selector mean is 67.55, versus 63.18 for fine-tuning. Aggregation by a stronger model yields little overall improvement in this setup.

**Evidence limits.** Four-teacher main experiments and a small six-teacher extension do not establish large-pool scalability. Selection and generation overheads differ; aggregate, router and RL results must not be collapsed into one algorithm or universal improvement.

**Cross-paper synthesis.** Tests an explicit response to TinyLLM's many-rationale supervision. It shows that an adaptive/RL teacher selector can remain offline because student updates use teacher-generated rationale prefixes.

**Primary-source locators**

- [§3.3, Eqs.4–6; §4, Eqs.12–14; Table1; §6 Limitations](https://arxiv.org/pdf/2602.01064): Method, state provenance and integration mechanism
- [§§5.1–5.3; Tables 1–5; §6; Appendix D; method §3.3 and §4 Eqs.4–14.](https://arxiv.org/pdf/2602.01064): Experimental setting, author-reported results and limitations

<a id="study-10"></a>

## 10. SCAS

When the Strongest Teacher Is Not the Best Teacher: Student-Centric Answer Selection

**Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2605.26872). **Catalog ID:** arxiv:2605.26872. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Which correct teacher answer should a changing student train on, given that quality alone does not measure learning difficulty?

**Teachers, student and access.** Six Qwen/Llama students span 0.5B–8B. Math candidates come from 30 teachers and are answer-verified; instruction candidates are ten samples from one Llama-3.3-70B teacher. Needs student representations/likelihood and teacher text, without backward passes for the selection proxy.

**Mechanism.** Fixed teacher-generated candidate answers; student scores candidates without generating the supervised histories. Selection/SFT rounds re-rank candidates as the student changes. Token likelihood of selected low-cost candidate answers. Changing selected supervision trains one student.

**Experimental setting.** MATH, GSM8K, DeepScaleR and OpenR1-Math; Magpie instruction training with IFEval/LiveBench evaluation. Baselines include random/RSR variants, GRACE, likelihood/IFD, routers and influence scoring under matched student/data/fine-tuning budgets.

**Reported findings.** Table 1 reports the highest average for all three Qwen2.5 scales: 24.19/52.43/60.26 versus the strongest comparator means 21.00/49.12/56.78. Iterative-selection and proxy analyses support the tested mechanism; averages mix task metrics and are not a universal effect size.

**Evidence limits.** Only the mathematical setting establishes a multi-teacher pool. Low estimated learning cost is not a proof of correct intermediate reasoning or broad educational value. Candidate verification, student access and finite pool/scale coverage condition the results.

**Cross-paper synthesis.** A clean counterexample to equating student-aware adaptation with OPD: selection changes, while the supervised prefixes remain teacher-generated. Contrast with PerSyn's prompt routing and live MOPD.

**Primary-source locators**

- [§§2.1–2.3, Eqs.5–11, Algorithm1; §3 Models/Datasets; §9](https://arxiv.org/pdf/2605.26872): Method, state provenance and integration mechanism
- [§3 setup; §§4.1–4.5; Table 1; Figures 3–6; Appendix A/B; §9 limitations; method §§2.1–2.3.](https://arxiv.org/pdf/2605.26872): Experimental setting, author-reported results and limitations

<a id="study-11"></a>

## 11. MergeDistill

MergeDistill: Merging Language Models using Pre-trained Distillation

**Source:** [Official Findings ACL-IJCNLP 2021 PDF; first public arXiv v1 on 2021-06-05](https://aclanthology.org/2021.findings-acl.254.pdf). **Catalog ID:** arxiv:2106.02834. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can existing language specialists form a multilingual student while retaining their vocabularies and strengths, without retraining all teachers together?

**Teachers, student and access.** Requires teacher tokenizers and cached top-k masked-token logits. BERT-base students use a union vocabulary; embedding dimensions are adjusted to control capacity in the multilingual setting.

**Mechanism.** Masked Wikipedia transfer-corpus examples tokenized separately by the corresponding teachers. Teacher top-k masked-token logits are computed and stored offline; no student-rollout collection. Teacher soft-label cross-entropy plus ordinary masked-token prediction, with teacher tokens mapped into a union vocabulary. Mapped teacher predictions train one multilingual task-agnostic student; no teacher-weight interpolation.

**Experimental setting.** Wikipedia transfer data; similar/dissimilar language-group students evaluated on NER, POS and QA. A second experiment combines mBERT/MuRIL and evaluates XTREME, with vocabulary-only versus vocabulary-plus-teacher-prediction ablations.

**Reported findings.** Tables 2–4 support competitive transfer, but the MuRIL-preferred recipe outperforms using both teachers on overlapping languages. Table 5 gives vocabulary-only SM2 75.4 versus distillation SM3 75.3 at full training, while at 100k steps distillation reaches 74.5 versus 71.6: vocabulary and training budget explain part of the gain.

**Evidence limits.** Language families, tokenization and data volume co-vary. Reported relative deviations are not percentage-point improvements. This is masked-LM transfer, not autoregressive OPD or parameter-space merging.

**Cross-paper synthesis.** Historical control for heterogeneous-interface claims: compare union-vocabulary transfer with FuseLLM's sequence alignment and FuseChat's distill-then-merge. Also motivates vocabulary-matched and limited-budget baselines.

**Primary-source locators**

- [§3.1 Steps 1–4 and Eqs.1–2; §§4.1–4.4; Tables 2–5](https://aclanthology.org/2021.findings-acl.254.pdf): Method, state provenance and integration mechanism
- [§§4.1–4.4; Tables 2–5; Appendix A.3; vocabulary and limited-step ablations in Table 5.](https://aclanthology.org/2021.findings-acl.254.pdf): Experimental setting, author-reported results and limitations

<a id="study-12"></a>

## 12. SoFT

SoFT: Soft Targets for Generalizable LLM Fine-Tuning

**Source:** [arXiv v2, 2026-10-13](https://arxiv.org/html/2609.32493v2). **Catalog ID:** arxiv:2609.32493. **Group:** Offline and NLP antecedents.

**Problem and inclusion.** Can offline multi-domain teacher demonstrations improve new capabilities without the broad regressions that one-hot SFT can cause?

**Teachers, student and access.** Qwen2.5-1.5B-Instruct/7B reasoning students and Qwen3-8B agent student. Needs demonstration text and frozen Base probabilities, but no external teacher logits or student rollout training. Practical target storage uses Base top-32 plus demonstrated token and a tail bucket.

**Mechanism.** Fixed teacher-forced prefixes of multi-teacher reasoning and agentic demonstration corpora. Targets depend only on frozen Base probabilities and validation-selected domain budgets; they remain fixed and can be cached. No online rollout refresh. Cross-entropy to the minimum-KL projection of Base that puts a floor on the demonstrated token; equivalently coupled demonstration CE and forward-KL preservation. Mixed teacher data and Base-derived target construction train one student.

**Experimental setting.** 36,000 reasoning and 8,252 agent trajectories, matched initializations/data/training budgets, held-out domain-budget selection. Eight ID/OOD tests per setting; fixed four temperature–seed attempts and geometric-mean aggregation. Appendix B reports one training epoch and seed 42.

**Reported findings.** Tables 2–3 give the best geometric mean among tested methods in all three settings: 54.17/65.88/36.93. It improves 22 of 24 scores over Base, ties one and regresses on Qwen3-8B LiveCodeBench (39.05 to 38.04). Other methods lead some individual tasks.

**Evidence limits.** Four evaluation attempts are not four independent training seeds. Validation-prefix KL is distinct from behavioral retention; domain budget tuning and a single reported training seed limit broader claims. This does not compare all modern OPD systems.

**Cross-paper synthesis.** Provides a current retention-aware offline comparator for MOPD. Distinguish its frozen-Base target construction from Delta's teacher-precursor shifts and its initial-logit budget from Nash exposure allocation or ROAD gradient projection.

**Primary-source locators**

- [§§3.1–3.4 Eqs.3–8; §§4–6 Tables 1–3; Appendices B.2.1/C/D/F](https://arxiv.org/html/2609.32493v2): Method, state provenance and integration mechanism
- [§§4.1–4.2; Tables 1–3; §§5.1–5.3/6.1; Appendix B.2.1 (approximation and training seed), C/D/F.](https://arxiv.org/html/2609.32493v2): Experimental setting, author-reported results and limitations

<a id="study-13"></a>

## 13. MOPD

MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training

**Source:** [arXiv v1](https://arxiv.org/html/2606.30406v1). **Catalog ID:** arxiv:2606.30406. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Integrate separately reinforced domain specialists into one deployable language model while avoiding the interference and uneven transfer observed in the tested joint, sequential, offline and merging baselines.

**Teachers, student and access.** The controlled study starts the student and frozen RL specialists from one mixed-domain SFT checkpoint. Teacher token log-probabilities, or the specified teacher top-k interface, are required on student-generated prefixes.

**Mechanism.** A domain label routes each collected student trajectory to one specialist. Reverse-KL transfer is implemented either through clipped sampled-token policy-gradient advantages or a separately specified mass-corrected teacher-top-k loss. Both update one shared student.

**Experimental setting.** Qwen3-30B-A3B is tested on mathematics, instruction following and software engineering; baselines share its SFT initialization. MiMo-V2-Flash 309B adds code and tool use in a separate scale experiment. The Qwen normalized score averages per-domain gain recovery relative to the SFT student and corresponding specialist.

**Reported findings.** Table 2 reports normalized recovery 0.9373 for MOPD, 0.8818 for Mix-RL and 0.8241 for offline finetuning. These are recovery scores, not raw accuracies. Table 3 reports that the MiMo student exceeds its corresponding teacher on five of seven benchmarks but remains lower on IFBench and SWE-bench Verified. Section 4.4.2 reports worse transfer when the math teacher is replaced with a stronger, differently initialized Qwen3-235B-A22B teacher in the controlled replacement.

**Evidence limits.** The reported same-origin stability and sampled-token/top-k comparison do not establish universal compatibility or estimator equivalence. The paper's offline baseline is not equivalent to every independently tuned offline transfer recipe. Observed deployment overhead and sample efficiency must retain the model, task and hardware conditions.

**Cross-paper synthesis.** Provides the domain-routed student-state reference for Open-MOPD, TrustMOPD and ROAD. Its same-origin result should be compared with Delta-MOPD's precursor-aware targets and Rethinking's stronger offline controls, without pooling unlike recovery definitions.

**Primary-source locators**

- [§§3.1–3.3, Eqs.1–5](https://arxiv.org/html/2606.30406v1#S3): Teacher construction, student states, routing and objectives
- [§§4.1–4.3, Tables 2–3](https://arxiv.org/html/2606.30406v1#S4.SS1): Experimental scope and reported recovery/scale results
- [§4.4.1–4.4.2](https://arxiv.org/html/2606.30406v1#S4.SS4): Estimator and cross-origin replacement analyses

<a id="study-14"></a>

## 14. Open-MOPD

Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

**Source:** [arXiv v1](https://arxiv.org/html/2608.19098v1). **Catalog ID:** arxiv:2608.19098. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Diagnose why a unified multi-domain OPD student remains below separately routed single-domain students, with emphasis on unequal response-token contribution and stale student-dependent rewards.

**Teachers, student and access.** Three frozen math/code/instruction RL specialists and one student share a mixed-SFT SmolLM3-3B initialization. The implementation scores teacher probabilities on student top-16 support.

**Mechanism.** Token-share balancing controls weighted token contribution; gap-following weights favor larger teacher-student reward gaps. Inner-update reward refresh recomputes the student term while caching teacher scores on rollout-time prefixes. It does not recollect trajectories.

**Experimental setting.** The end-to-end recipe targets one 8×A100-80GB node. Six benchmarks form three equally weighted domain averages: AIME24/25, LiveCodeBench v5/v6, IFEval/IFBench. Table 4 separates K=1 and K=4 inner-update ladders.

**Reported findings.** Table 4 reports 31.24 overall for the full K=4 recipe versus 29.28 for its same-K naive control, a 1.96-point difference; 3.19 points uses the different K=1 naive row. Within the K=4 ladder, reward refresh adds 0.81 points over token-share plus gap-following controls. Section 5.3 reports 1298 versus 1313 seconds per outer step with/without refresh; the authors treat this as variation-compatible, not a measured speedup.

**Evidence limits.** Reward refresh leaves rollout histories stale during batch reuse. Equal weighted token shares do not imply equal gradient norms or equal task accuracy. Negative conflict-mask findings concern the tested diagnostics and interventions, not a universal absence of teacher conflict.

**Cross-paper synthesis.** Separates token contribution, remaining loss gap and state freshness. Contrast its loss weighting with Nash-MOPD's prompt-share controller and its conflict diagnosis with ROAD's different task and gradient setting.

**Primary-source locators**

- [§§2.1–2.4, Tables 1–2](https://arxiv.org/html/2608.19098v1#S2): Models, interface, recipe and evaluation
- [§§3.2–3.3](https://arxiv.org/html/2608.19098v1#S3): Conflict and imbalance diagnosis
- [§§4.1–4.4; §5/Table 4](https://arxiv.org/html/2608.19098v1#S4): Allocation mechanisms and controlled ablation ladder
- [§5.3/Figure 8](https://arxiv.org/html/2608.19098v1#S5.SS3): Reward freshness and runtime accounting

<a id="study-15"></a>

## 15. TrustMOPD

Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation

**Source:** [arXiv v3](https://arxiv.org/html/2609.23697v3). **Catalog ID:** arxiv:2609.23697. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Allocate supervision when a prompt can combine capabilities and a unique domain label cannot select the appropriate specialist.

**Teachers, student and access.** Three separately RL-specialized teachers require a shared pre-RL reference and token-distribution access on student prefixes. The default backbone is SmolLM3-3B; a DeepSeek-R1-Distill-Qwen-7B pool is also tested.

**Mechanism.** For each prefix, compute centered log-policy displacement from the shared reference, divide by a teacher-specific calibration mean fixed from initial-student rollouts, power-normalize, and detach weights over teacher reverse-KL losses.

**Experimental setting.** SingleCap and mixed-capability MultiCap each contain 7,458 training prompts. Six benchmarks cover math, code and instruction following. Final checkpoints are evaluated over five seeds; the uniquely domain-routed baseline is included only on SingleCap.

**Reported findings.** Table 1 reports 30.04±0.47 overall on SingleCap versus 27.95±0.59 for uniform weighting and 30.18±0.25 for label-based MOPD. On MultiCap, Trust reaches 30.41±0.60 versus 27.96±0.49 for the strongest reported label-free control, random weighting. Section 4.4 reports benefits over uniform weighting under both a changed backbone and independently sourced training prompts.

**Evidence limits.** Calibration constants are frozen, not continuously re-estimated. Displacement is a reference-relative reliability proxy, not answer correctness or calibrated truth probability. Shared-reference and calibration-distribution assumptions restrict extrapolation to arbitrary heterogeneous pools; no unique-domain-route baseline is reported for MultiCap.

**Cross-paper synthesis.** Contrast reference-relative loss weighting with Delta-MOPD's reference-relative target construction. Use its mixed-capability setting to show when a static domain label is inadequate without claiming that reference displacement universally identifies expertise.

**Primary-source locators**

- [§§3.1–3.3, Eqs.2–5](https://arxiv.org/html/2609.23697v3#S3): Displacement, fixed calibration and detached weighting
- [§4.1; Table 1](https://arxiv.org/html/2609.23697v3#S4.SS1): Models, data, seeds, baselines and results
- [§4.4; Appendix A.5](https://arxiv.org/html/2609.23697v3#S4.SS4): Sensitivity, transfer and interpretation limits

<a id="study-16"></a>

## 16. Delta-MOPD

Composing What Each Teacher Learned: Delta Distillation for Multi-Teacher On-Policy Learning

**Source:** [arXiv v2](https://arxiv.org/html/2610.10460v2). **Catalog ID:** arxiv:2610.10460. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Reduce inherited base-model differences when composing or routing specialists, by distinguishing a teacher endpoint from its post-training change relative to its exact precursor.

**Teachers, student and access.** The student/anchor is DeepSeek-R1-Distill-Qwen-1.5B. Main teachers include Nemotron, Polaris-7B and JustRL; each exact precursor is required. Token-distribution alignment is necessary, with a projected cross-tokenizer extension reported separately.

**Mechanism.** Subtract each teacher's precursor logits, combine selected shifts on a frozen student anchor, normalize once, and match the target on student prefixes. Same-origin single-teacher construction reduces to endpoint OPD.

**Experimental setting.** Paired arms share initialization, prompts, optimizer and budget. BigMath composition compares two and three teachers; routed Math/Science/IF uses interleaved and two phased orders. Main scaling results report step-100 greedy pass@1 macros.

**Reported findings.** Table 2: three-teacher shift composition exceeds endpoint composition by 4.11 Math and 1.95 five-suite percentage points, but trails Science/IF by 1.29 points. The two-teacher mechanism run has similar aggregate average-sampling accuracy: 44.91% versus 45.14%. Table 3: five-suite margins over endpoint targets are 0.62 points for interleaving and 5.68/1.60 points for the two phased orders.

**Evidence limits.** Teacher-minus-precursor changes also include style and calibration; they are not experimentally isolated skill variables. Cross-origin in the principal comparison means a different-size base in the same lineage; this is narrower than arbitrary independent architectures. Precursor access and compatible token mappings are substantive requirements; composition gains are domain- and schedule-dependent.

**Cross-paper synthesis.** Shows that integration can change target content before updating the student. Contrast with Trust's weighting, FuseLLM's token alignment and endpoint aggregation, and MOPD's teacher-student distribution-gap observation.

**Primary-source locators**

- [§§3.1–3.2, Eqs.3–6](https://arxiv.org/html/2610.10460v2#S3): Anchored shift construction and reference interpretation
- [§4/Table 1; §5.3/Table 2](https://arxiv.org/html/2610.10460v2#S4): Checkpoint provenance and composition setting
- [§5.4/Table 3](https://arxiv.org/html/2610.10460v2#S5.SS4): Routed schedule findings
- [§9; Appendix F](https://arxiv.org/html/2610.10460v2#S9): Scope and token compatibility limits

<a id="study-17"></a>

## 17. Cross-teacher guarding

Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation

**Source:** [arXiv v2](https://arxiv.org/html/2610.13521v2). **Catalog ID:** arxiv:2610.13521. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Limit damage to other specialist capabilities when domain-routed updates improve the active domain but interfere with auxiliary objectives.

**Teachers, student and access.** Qwen3-4B/1.7B students use Qwen3-4B math/code specialists and a Qwen3-8B-derived II-Medical-8B teacher. Routed and auxiliary teachers score the same student trajectory relative to a frozen reference.

**Mechanism.** Reference-relative teacher agreement modulates detached token advantages. Tensorwise partial gradient projection then constrains the target update using auxiliary gradients on those same target-domain trajectories, subject to a norm-retention floor.

**Experimental setting.** Eleven math, code and medical benchmarks; paired-domain settings use 10,000 prompts per domain. Comparators include Vanilla MOPD, ExOPD, CaMOPD and Open-MOPD. Math/code use multi-sample average correctness; reported domain means are equally weighted.

**Reported findings.** Table 3: the Qwen3-4B three-domain mean is 52.89 versus 51.71 for CaMOPD, with medical 48.45. Across the four medical-containing pair/student settings, the reported two-domain mean exceeds the strongest compared multi-domain method by 0.72–2.89 points. For 1.7B students, medical improvements coexist with math/code scores below ExOPD; the aggregate advantage depends on equal domain weighting.

**Evidence limits.** An auxiliary teacher is a compatibility signal, not necessarily an expert on the target-domain task. The norm floor can leave residual negative alignment; full conflict elimination is not guaranteed. First-order same-trajectory loss statements do not guarantee retention on an auxiliary benchmark after an optimizer update.

**Cross-paper synthesis.** Separates modifying supervision strength from constraining the parameter update. Contrast with GOVERN's logit-direction voting and Open-MOPD's allocation diagnosis without treating different conflict measurements as direct contradictions.

**Primary-source locators**

- [§3.2, Eqs.4–5; §3.3, Eqs.6–9](https://arxiv.org/html/2610.13521v2#S3.SS2): Agreement modulation and tensorwise guarded update
- [§§4.1–4.2, Tables 1–3](https://arxiv.org/html/2610.13521v2#S4.SS1): Models, evaluation and domain trade-offs
- [Appendix A.2; Appendix D](https://arxiv.org/html/2610.13521v2#A1.SS2): Projection floor and limits

<a id="study-18"></a>

## 18. Nash-MOPD

Nash-MOPD: Optimizing Task Trade-offs in Multi-Teacher On-Policy Distillation

**Source:** [arXiv v1](https://arxiv.org/html/2610.26124v1). **Catalog ID:** arxiv:2610.26124. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Allocate finite training exposure when domains progress at unequal rates, without altering the routed teacher or the underlying distillation objective.

**Teachers, student and access.** A DeepSeek-R1-Distill-Qwen-1.5B student uses math, code and instruction specialists; Qwen3-8B-Base uses two same-base math/code specialists. Teacher scoring and existing loss statistics supply the controller.

**Mechanism.** Estimate proportional reverse-KL-gap reduction per prompt exposure, then use a bounded and smoothed inverse-rate minimax allocation. The adversarial component is an analytic bottleneck construction, not a learned critic.

**Experimental setting.** Fixed, D3-MOPD and Nash share 200 optimizer updates, with checkpoints every 20 updates. Endpoint avg@k and candidate pass@k are distinguished; convergence curves use pass@1 and instruction-following scores.

**Reported findings.** For 1.5B, endpoint MATH-500 avg@4 is 85.95%, LCB avg@4 23.29%, and Multi-IF 43.01%, respectively 2.90, 1.72 and 2.76 points above Fixed. The reported checkpoint curves cross baseline endpoint math/code scores by step 100 in the tested settings. Full 200-step runs take 6.81 versus 6.63 hours at 1.5B and 13.21 versus 12.97 hours at 8B for Nash versus Fixed; wall-clock time to early crossings was not measured.

**Evidence limits.** The local minimax result assumes frozen positive rates and separable progress, not nonlinear training convergence or guaranteed worst-domain accuracy. A zero KL gap denotes target matching rather than task correctness; zero-rate domains need fallback treatment. Earlier optimizer-update crossings are not measured wall-clock speedups, and avg@k is not pass@k.

**Cross-paper synthesis.** Makes exposure a distinct design choice. Compare its prompt-share allocation with Open-MOPD's token-loss contribution and Trust's within-state teacher weighting; retain metric and compute denominators in any cross-paper table.

**Primary-source locators**

- [§§4.1–4.3, Eqs.5–12](https://arxiv.org/html/2610.26124v1#S4): Progress normalization and constrained controller
- [§§5.1–5.3, Tables 1–2, Figures 3–5](https://arxiv.org/html/2610.26124v1#S5): Settings, endpoint accuracy and update/time comparison
- [Appendix A.1–A.5](https://arxiv.org/html/2610.26124v1#A1): Local assumptions and inactive-domain treatment

<a id="study-19"></a>

## 19. Rethinking capability merging

Rethinking Self-Distillation for Multi-Teacher Capability Merging

**Source:** [arXiv v1](https://arxiv.org/html/2610.04272v1). **Catalog ID:** arxiv:2610.04272. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Test whether live on-policy distillation consistently improves capability recovery after independently tuning credible offline baselines.

**Teachers, student and access.** Domain RL experts and students share an initialization within each controlled setup. SFT needs recorded successful responses; Soft-KD needs teacher distributions; hybrid/live arms score student-generated responses with differing interaction histories.

**Mechanism.** Compare SFT, teacher-context forward-KL Soft-KD, Offline-MOPD and live MOPD. Offline-MOPD generates current responses after recorded teacher histories; live MOPD executes student actions to obtain subsequent observations. This is a comparison study, not one new algorithm.

**Experimental setting.** Four models (Qwen3-1.7B/8B, Qwen3.5-4B-Base, Ministral-3-3B-Instruct) and MIA/Agent×3 expert compositions. Methods are tuned separately, use a common successful-teacher corpus for prompts and report three-seed results. Recovery is an aggregate teacher-gain ratio.

**Reported findings.** Table 1: Qwen3-8B's four distillation recipes recover 96.9–98.2% of aggregate in-domain gain on MIA and 97.6–99.3% on Agent×3. Across tested models, the study finds no consistent in-domain advantage for live MOPD; out-of-domain retention trade-offs remain. For Qwen3-8B full configured runs, MOPD/SFT training GPU-hour ratios are 14.8× and 23.1×; these exclude teacher-corpus generation, evaluation and other tuning runs.

**Evidence limits.** Results concern the tested shared-initialization compositions and do not prove universal offline/on-policy equivalence. In single-turn tasks Offline-MOPD can share MOPD's sampling/objective; the distinction matters for interactive histories. Full-budget training cost is neither time-to-equal-performance nor end-to-end pipeline cost; online scoring is included, reusable teacher-corpus generation is excluded.

**Cross-paper synthesis.** Supplies a necessary counterpoint to broad OPD superiority claims. Separate state freshness from recipe quality, and require learning-rate tuning, response masks, rejection sampling and transparent cost denominators before attributing gains to on-policy sampling.

**Primary-source locators**

- [§3.1, Eqs.1–4; §3.3, Eq.6](https://arxiv.org/html/2610.04272v1#S3): Comparison arms and recovery definition
- [§§4.1–4.3; §5.1, Tables 1–2](https://arxiv.org/html/2610.04272v1#S4): Controlled protocol and reported recovery
- [§5.2; Appendix G.2–G.3, Table 19](https://arxiv.org/html/2610.04272v1#A7.SS3): Configured compute ratios and excluded costs
- [§6.3–6.4](https://arxiv.org/html/2610.04272v1#S6.SS3): Strong offline-baseline analysis

<a id="study-20"></a>

## 20. PromptSD

One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context

**Source:** [arXiv v1](https://arxiv.org/html/2607.18293v1). **Catalog ID:** arxiv:2607.18293. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Build task-specific teachers with separately learned soft prompts on a common backbone, then absorb their specialization into one prompt-free student.

**Teachers, student and access.** Four independently trained soft-prompt parameter sets share frozen Qwen3-1.7B-Base backbone weights. Teacher and student token probabilities are required; distinct learned prompts are not four independently trained full backbones.

**Mechanism.** First optimize each task prompt while freezing the backbone, then freeze the teacher prompts. Route each example to its task prompt and optimize student-to-teacher token reverse KL. The rollout buffer is recollected every 64 updates.

**Experimental setting.** Science, tool use, biology and mathematics use separate train/validation/test splits; validation controls early stopping. Main results compare sequential/multi-task SFT and prompt/LoRA OPD. Held-out utility averages MMLU-Pro, HellaSwag and TruthfulQA.

**Reported findings.** Table 2 reports target-task average 56.2 for multi-task PromptSD versus 43.7 for multi-task SFT and 47.5 for multi-task LoRA OPD. Held-out utility is 51.7 for PromptSD and LoRA OPD, versus 50.4 for the initial student. The reported four-task benefit does not demonstrate interference-free scaling; tool-use performance does not lead every baseline.

**Evidence limits.** A 64-step replay buffer is not strict current-policy sampling at every optimization update. Shared backbone weights do not erase separately learned teacher-policy components, but ordinary untrained role prompts would not satisfy the same criterion. Four tasks and a small backbone do not establish arbitrary task-count scaling or formal guarantees of capability preservation.

**Cross-paper synthesis.** Operationalizes teacher identity through learned components rather than checkpoint count. Contrast with MAS-OPD's role views of one frozen teacher and MT-SDPO's feedback-conditioned EMA target.

**Primary-source locators**

- [§§4.1–4.3, Eqs.5–10](https://arxiv.org/html/2607.18293v1#S4): Learned prompts, reverse KL and task routing
- [§§5.1–5.3, Tables 1–2](https://arxiv.org/html/2607.18293v1#S5.SS1): Backbone, refresh interval, task and utility results
- [§7; Appendices B and F](https://arxiv.org/html/2607.18293v1#S7): Scope, implementation and multi-task exposure control

<a id="study-21"></a>

## 21. D3-MOPD

D$^3$-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation

**Source:** [arXiv v2](https://arxiv.org/html/2608.24987v2). **Catalog ID:** arxiv:2608.24987. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Fixed domain mixtures spend equal allocation on teachers whose remaining learning headroom and convergence speeds differ. Included as a direct MOPD example where the intervention is data exposure rather than teacher-signal weighting.

**Teachers, student and access.** Four frozen, independently GRPO-specialized Qwen3.6-35B-A3B teachers for math, code, instruction following and tool use; student initialized from their common base. Teacher token probabilities/log-probabilities on student states are required. The existing domain-routed reverse-KL/OPD teacher target is retained. The scheduler multiplies normalized remaining KL gap by clipped nonnegative KL-descent velocity, then applies softmax, a 0.10 domain floor and sampling jitter.

**Mechanism.** Student-generated response prefixes in the asynchronous slime rollout/update system; operationally near-current rather than guaranteed synchronized with every optimizer step. New rollout batches supply states and logged reverse-KL. A separate watcher recomputes domain ratios every 10 rollout steps after warm-up (20 steps); W=10, R=3, with the full three-window statistic available from step 40. The 300-second file polling interval is not the policy/ratio update cadence. The existing domain-routed reverse-KL/OPD teacher target is retained. The scheduler multiplies normalized remaining KL gap by clipped nonnegative KL-descent velocity, then applies softmax, a 0.10 domain floor and sampling jitter. Domain prompt/rollout allocation before teacher supervision; not a new token mixture or parameter merge.

**Experimental setting.** Main run: Qwen3.6-35B-A3B, four domain-specialist teachers, four roughly 4k prompt pools, 256 rollout steps, 128 prompts × 4 responses, 8192 response-token cap, no-thinking mode. Seven benchmarks are evaluated at 16 checkpoints. Appendix E adds a 4B setting; main numerical comparisons below refer to the 35B experiment.

**Reported findings.** Best mean benchmark score rises from 61.36 (vanilla, step 143) to 62.34 (D3, step 95). D3 crosses the approximately 61.4 vanilla peak at step 47; the roughly 3× figure is rollout steps to that threshold. (Table 1; §4.3). Separate per-benchmark peak normalization gives 0.97 versus 0.63; at each method’s single best-average checkpoint the corresponding normalization is 0.73 versus 0.48, with IFBench lower for D3. (Table 2 versus Appendix D, Table 6). Reported throughput is 520 versus 531 tokens/GPU/s; authors attribute the difference to changed response lengths. No additional teacher forward pass does not imply literally zero total systems cost. (Appendix B).

**Evidence limits.** The exponential KL-decay model motivates a marginal-progress heuristic, not a theorem about downstream benchmark gains (Appendix F). A KL rebound yields zero clipped descent velocity even if a domain still has a large gap; near-zero initial KL can destabilize gap normalization (Appendix I). Checkpoint-envelope results must be separated from final or selected single-checkpoint scores and from compute-matched comparisons.

**Cross-paper synthesis.** Contrast with DN-MOPD: D3 changes how often domains are sampled; DN changes the scale of feedback after sampling. Connect to Open-MOPD/Nash-MOPD through exposure scheduling, and to Rethinking-MOPD through the need to distinguish steps, tokens, GPU hours and checkpoint selection.

**Primary-source locators**

- [§3, Eqs. (2)–(6), Algorithm 1; §§4.1–4.4, Tables 1–2; Appendix B (infrastructure), D/Table 6 (one-checkpoint result), F (assumptions), I (failure modes).](https://arxiv.org/html/2608.24987v2): Method, state provenance and integration mechanism
- [§3, Eqs. (2)–(6), Algorithm 1; §§4.1–4.4, Tables 1–2; Appendix B (infrastructure), D/Table 6 (one-checkpoint result), F (assumptions), I (failure modes).](https://arxiv.org/html/2608.24987v2): Experimental setting, author-reported results and limitations

<a id="study-22"></a>

## 22. DN-MOPD

Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation

**Source:** [arXiv v1](https://arxiv.org/html/2609.35347v1). **Catalog ID:** arxiv:2609.35347. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Domain labels can assign the correct specialist while its advantage variance still makes that domain dominate optimization. Included to separate teacher assignment from effective learning-signal strength.

**Teachers, student and access.** Three frozen independently RL-trained math/code/instruction-following specialists at each Qwen3.5 size (9B, 4B, 2B); each student shares the specialists’ base initialization. Assigned-teacher sampled-token log-probabilities and domain labels suffice for the core normalization. Domain-routed teacher/student token log-ratio advantage, multiplied by clip(sigma_pool/sigma_domain, 0.25, 4) inside the clipped policy objective. No mean subtraction; signs preserved; fallback weight 1 for zero dispersion or fewer than two observations.

**Mechanism.** Fresh student-generated responses in each rollout iteration; rollout-policy cached scores and current pre-update actor scores are distinguished. Domain and pooled population standard deviations are recomputed from cached valid response-token log ratios in each rollout batch. Weights are stop-gradient; actor advantages are recomputed for the policy update. No independent teacher-refresh interval is specified because teachers remain frozen. Domain-routed teacher/student token log-ratio advantage, multiplied by clip(sigma_pool/sigma_domain, 0.25, 4) inside the clipped policy objective. No mean subtraction; signs preserved; fallback weight 1 for zero dispersion or fewer than two observations. Scalar domain feedback normalization after fixed prompt allocation and teacher routing; not teacher selection.

**Experimental setting.** Three model scales, three specialists per scale, 80 student updates; principal seed 42 with 43/44 controls. Six benchmarks: AIME25/26, LiveCodeBench v5/v6, IFEval and IFBench; reported 8k and 16k evaluation limits. Training response cap is 8192. Offline SeqKD uses 84 updates and 16k teacher-answer caps, so its compute is not identical. Teacher pools are fixed across student seeds.

**Reported findings.** At the 16k evaluation limit, six-task Total improves from Label-MOPD 58.4 to 59.6 at 9B, 50.3 to 52.5 at 4B, and 26.6 to 29.0 at 2B. SeqKD-SFT reports 62.6, 55.9 and 32.9 respectively. (Tables 1–2). Downweighting instruction-following alone recovers much of the improvement. Fixed approximate domain weights or first-batch weights are comparable to online normalization at 9B/4B; online adaptation is more useful in the reported 2B comparison. (Table 3; Appendix C). Additional student seeds and 160-update controls support the local Label-MOPD comparison, but do not sample new independently trained teacher pools or establish full convergence. (Table 5; Appendix C).

**Evidence limits.** The 16k evaluation setting was selected after inspection; avoid presenting all displayed choices as preregistered. The paper reports an earlier Qwen3-4B recipe without a clear gain; hyperparameter bounds and transfer across recipes remain limitations (§5). Offline and online baselines differ in generation length, targets and update budgets; their rankings are evidence under these recipes, not a universal regime ranking.

**Cross-paper synthesis.** A counterexample to treating all adaptive weights as teacher reliability: here weights correct dispersion rather than correctness. Pair with D3 to distinguish exposure from feedback scale, with Trust-MOPD for reliability versus variance, and with Rethinking-MOPD for strong offline controls.

**Primary-source locators**

- [§2 and Algorithm 1 (normalization/objective); §§3.1–3.4, Tables 1–5; Appendix C (fixed-weight, budget and seed controls); §5 (limitations).](https://arxiv.org/html/2609.35347v1): Method, state provenance and integration mechanism
- [§2 and Algorithm 1 (normalization/objective); §§3.1–3.4, Tables 1–5; Appendix C (fixed-weight, budget and seed controls); §5 (limitations).](https://arxiv.org/html/2609.35347v1): Experimental setting, author-reported results and limitations

<a id="study-23"></a>

## 23. MOPD-Router / ExpertAlign

MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation

**Source:** [arXiv v2](https://arxiv.org/html/2609.30837v2). **Catalog ID:** arxiv:2609.30837. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Prompt domain labels are coarse and can suppress useful cross-domain teachers; low entropy alone does not identify task-relevant expertise. Included as dynamic teacher selection on a shared student state.

**Teachers, student and access.** Three frozen Qwen3-4B math/code/IF specialists, a shared frozen pre-specialization base reference, and Qwen3-1.7B or 4B students. ExpertAlign needs teacher/base/student log probabilities on the student top-16 support; the teacher pool is queried token-wise. The router itself is not learned. Weighted teacher-minus-rollout-student sampled-token log-ratio advantages. ExpertAlign compares teacher specialization (teacher–base log-probability displacement) with teaching direction (teacher–student displacement), retains positive alignment, and uses uniform or cosine-weighted retained teachers; all-negative tokens are skipped.

**Mechanism.** Prefixes generated by the rollout student; routed advantages are held for clipped actor updates, so distinguish rollout policy from updated actor. New rollout batch per outer iteration; all teachers and reference score its prefixes. Algorithm 1 constructs routing weights before inner minibatch updates. Reported main configuration uses three epochs, train and minibatch size 1024, and one response per prompt; do not infer that Algorithm 1’s general K always exceeds one. Weighted teacher-minus-rollout-student sampled-token log-ratio advantages. ExpertAlign compares teacher specialization (teacher–base log-probability displacement) with teaching direction (teacher–student displacement), retains positive alignment, and uses uniform or cosine-weighted retained teachers; all-negative tokens are skipped. Token-level teacher filtering/weighting across the full pool, inside the clipped OPD policy objective.

**Experimental setting.** Teachers are three Qwen3-4B non-thinking specialists; students 1.7B/4B. Unlabeled pool: 60k prompts from chat plus math/code; labeled pool: 66k math/code/IF prompts. Nine benchmarks cover four math, three code and two instruction-following tests. All four scale/data combinations are evaluated; seed replication is narrower than this full grid.

**Reported findings.** For the 4B student, benchmark mean increases from Standard MOPD 48.76 to ExpertAlign 53.76 on the unlabeled pool, and 50.63 to 54.58 on the labeled pool. These are within-recipe comparisons, not pooled evidence for all students. (Tables 1–2). Gate/weight, token/response and full-pool/domain-restricted controls support the contribution of the routing design within the tested pools. Bootstrap intervals cover all four settings, while three training seeds are reported for the same-size labeled setting. (Tables 3–4; Appendix D). Same-size labeled training reports 716.9 versus 692.9 GPU hours (+3.5%), but time per token is 1.18×; changed generation lengths partly offset total cost. Timings exclude initialization/download and validation I/O outside steps. (Table 5 and its timing protocol).

**Evidence limits.** Experiments use three same-family specialists; extensions to unrelated teacher bases remain future work (Appendix A). Domain labels for the unlabeled-pool label-routing baselines are generated by DeepSeek-V4-Flash, which is an additional baseline resource, not label-free ground truth. Aggregate mean comparisons conceal benchmark-level tradeoffs; confidence intervals from evaluation resampling are distinct from independent training-seed variability.

**Cross-paper synthesis.** Compare to Trust-MOPD’s use of a base reference and to Delta-MOPD’s relative teacher signal: ExpertAlign uses displacement geometry to select/weight teachers rather than directly construct a shifted target distribution. Cross-reference D3/DN as allocation, routing and feedback scaling at distinct stages.

**Primary-source locators**

- [§§3.1–3.3, Eqs. (1)–(11), Algorithm 1; §4, Tables 1–5; Appendix A (scope), B/Table 6 (training), D (uncertainty), E (routing controls).](https://arxiv.org/html/2609.30837v2): Method, state provenance and integration mechanism
- [§§3.1–3.3, Eqs. (1)–(11), Algorithm 1; §4, Tables 1–5; Appendix A (scope), B/Table 6 (training), D (uncertainty), E (routing controls).](https://arxiv.org/html/2609.30837v2): Experimental setting, author-reported results and limitations

<a id="study-24"></a>

## 24. Latent-MOPD

Latent-MOPD: Latent Multi-Teacher On-Policy Distillation

**Source:** [arXiv v1](https://arxiv.org/html/2610.02381v1). **Catalog ID:** arxiv:2610.02381. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Output probabilities can omit intermediate specialist structure; abrupt or poorly organized representation imitation may destabilize learning. Included as a direct multi-teacher method combining internal and output supervision rather than merely changing routing.

**Teachers, student and access.** Three frozen math/code/logic specialists. Student: DeepSeek-R1-Distill-Qwen-1.5B. Same-family teachers share its backbone; the cross-family panel uses 7B Qwen-backbone specialists with the same tokenizer and 28 blocks but width 3584 versus student width 1536. Requires teacher hidden states and token distributions; a shared trainable projector is used across unequal widths. Joint normalized hidden-state alignment and a fixed-advantage token objective on student top-16 support, using full-vocabulary log-probability normalization. Representation weight fades down while token weight rises; same-family default aligns last three layers, unequal-width default the last layer’s final 2000 response positions via a linear projector.

**Mechanism.** Fresh student-generated responses, with a domain-pure batch selecting one specialist for both representation and token supervision. One policy optimization epoch and one actor update per rollout batch; 62 global updates rotate math/code/logic. Teacher-local counter advances only when that teacher is active. Crossfade windows are 10 teacher-local updates (30 global) same-family and 7 (21 global) cross-family; representation loss is zero from global steps 31/22 respectively. Joint normalized hidden-state alignment and a fixed-advantage token objective on student top-16 support, using full-vocabulary log-probability normalization. Representation weight fades down while token weight rises; same-family default aligns last three layers, unequal-width default the last layer’s final 2000 response positions via a linear projector. Two direct supervision channels—representation alignment and output-token OPD—within the same routed student update; final inference discards the projector.

**Experimental setting.** Three domains and 62 optimizer updates; 32 prompts × 4 responses per update, hence 1984 prompt presentations and 7936 responses from a 17856-prompt pool. Same-family panel has nine benchmarks; cross-family panel six. All main numbers use the final checkpoint, not the best intermediate checkpoint. Representation-layer, projector, sustained-joint-loss and batch-organization controls are reported.

**Reported findings.** Same-family default improves all nine benchmarks over the matched token-only baseline and exceeds the best-teacher envelope on five. Headroom-weighted Norm is 1.05 versus 0.90. (Table 1; Appendix A, Eq. (5)). Cross-family linear-projector Norm is 0.26 versus token-only 0.16; an MLP variant gives 0.27, with different per-benchmark winners. The projector comparison changes both architecture and initialization. (Table 2; Appendix A). Domain-pure versus interleaved all-layer representation-only controls show a large stability difference (MATH-500 final 91.7 versus 43.2); this control is not a result for every joint-supervision method. General-task scores stay near the base but do not show zero forgetting. (§5; Appendix F; general evaluation in §4/Appendix D).

**Evidence limits.** Norm is the ratio of summed score improvements to summed teacher headroom, not an unweighted average of per-benchmark recovery fractions. It is not numerically interchangeable with D3/MOPD normalization. Selecting three of 28 feature layers gives an analytic 89.3% reduction in those stored feature tensors only; weights, optimizer, attention/autograd buffers and transient allocations are excluded. CKA motivates layer choice descriptively; it does not establish a causal explanation for transfer. Same vocabulary and limited teacher/student architectures constrain generalization.

**Cross-paper synthesis.** Connect internal-state distillation to MT-BERT while distinguishing student-generated online states from offline feature matching. Link to FuseLLM-style heterogeneity as an access/interface issue and to DN-MOPD because token advantages are also domain-scaled, without treating the two full training protocols as identical.

**Primary-source locators**

- [§3, Eqs. (1)–(3); §4, Tables 1–3; §5 (batch control); Appendix A (implementation and Norm Eq. (5)), F (batch organization), J (scope).](https://arxiv.org/html/2610.02381v1): Method, state provenance and integration mechanism
- [§3, Eqs. (1)–(3); §4, Tables 1–3; §5 (batch control); Appendix A (implementation and Norm Eq. (5)), F (batch organization), J (scope).](https://arxiv.org/html/2610.02381v1): Experimental setting, author-reported results and limitations

<a id="study-25"></a>

## 25. SF-MOPD

Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation

**Source:** [arXiv v1](https://arxiv.org/html/2610.02324v1). **Catalog ID:** arxiv:2610.02324. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** Specialist fusion can improve visual domain tasks while eroding general visual-language capability. Included as a multimodal extension of direct MOPD that introduces an evolving retention reference.

**Teachers, student and access.** Four frozen Qwen3-VL-8B visual specialists (Data Chart, Real-World Item, Schematic Diagram and perception); students Qwen3-VL-2B/4B/8B-Instruct. An EMA copy of the evolving student is a moving reference, not a fifth independently trained specialist. Full token distributions and student parameter access are needed. Projected specialist log-probability pseudo-targets under JSD plus an original unprojected multi-teacher JSD term. Centered teacher displacement components opposing the EMA-student direction are attenuated using a ridge denominator (1e-3); target distributions are stop-gradient.

**Mechanism.** Current-student generated response prefixes, scored by all four specialists and the EMA student reference. The EMA parameters track student updates with decay 0.999, initialized from the student. The main description uses student-generated samples for distillation; a separate numerical rollout-buffer refresh interval is not explicitly reported. Projected specialist log-probability pseudo-targets under JSD plus an original unprojected multi-teacher JSD term. Centered teacher displacement components opposing the EMA-student direction are attenuated using a ridge denominator (1e-3); target distributions are stop-gradient. Teacher output-space target modification and joint distillation loss; equal teacher weights, not hard domain routing. The base MOPD objective in this paper is summed JSD.

**Experimental setting.** Four 8B specialist teachers; student scales 2B/4B/8B. Training: one epoch, batch 64, AdamW learning rate 1e-5. Eleven evaluations split five general and six specialist benchmarks. Answer extraction uses deterministic rules with Qwen3-VL-8B judge fallback. Projection and original-JSD-loss ablations are reported.

**Reported findings.** At 8B, general-task mean is 77.2 for the base, 73.3 for MOPD and 76.4 for SF-MOPD; specialist-task mean is 57.2, 59.0 and 60.4. Overall MOPD/SF means are 65.5/67.7. (Table 1). At 4B/2B the SF general means (74.2/66.4) also remain below the respective base means (75.1/67.2), despite improving the paper’s MOPD baseline. (Table 1). Removing the slow-fast projection gives 64.0 overall versus 67.7, but this variant becomes an EMA-constraint formulation and therefore changes the objective structure; it is not a pure removal of an otherwise identical arithmetic operation. (Table 2 and §3.3).

**Evidence limits.** Evidence is in a short same-family multimodal study, not language-only MOPD or arbitrary teacher architectures. The inspected method/experiment sections do not report a broad independent-training-seed analysis; small benchmark differences should not be promoted to universal guarantees. The EMA target and unprojected auxiliary term require objective-level distinctions when comparing methods labeled MOPD.

**Cross-paper synthesis.** Place next to ROAD-MOPD’s conflict treatment while distinguishing output-space displacement projection from parameter-gradient projection. Compare Delta-MOPD’s frozen relative anchor with SF’s evolving EMA anchor, and UCMOPD’s filtering with SF’s target modification for retention.

**Primary-source locators**

- [§§2.1–2.4, Eqs. (4)–(10); §§3.1–3.3, Tables 1–2. Short multimodal paper; no appendix-derived refresh interval assumed.](https://arxiv.org/html/2610.02324v1): Method, state provenance and integration mechanism
- [§§2.1–2.4, Eqs. (4)–(10); §§3.1–3.3, Tables 1–2. Short multimodal paper; no appendix-derived refresh interval assumed.](https://arxiv.org/html/2610.02324v1): Experimental setting, author-reported results and limitations

<a id="study-26"></a>

## 26. UCMOPD

Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation

**Source:** [arXiv v2](https://arxiv.org/html/2608.26735v2). **Catalog ID:** arxiv:2608.26735. **Group:** Direct MOPD methods and comparative analyses.

**Problem and inclusion.** A domain-specialized student may have lost general ability, while indiscriminate OPD can transmit uncertain guidance or suppress useful specialized behavior. Included as two independently learned supervision components with explicit trajectory and token acceptance rules.

**Teachers, student and access.** Two frozen teachers per specialization setting: general base and SFT domain specialist; student starts from the specialist. Role-playing uses Qwen3-4B-Instruct-2507 lineage. Medical uses II-Medical-7B-Preview, which the paper’s configuration table identifies as an 8B Qwen3 architecture, with Qwen3-8B general teacher. Core implementation needs sampled-token log-probabilities and teacher top-50 probabilities, not teacher hidden states. Teacher-minus-student token advantages filtered twice. GGE retains exploration responses whose mean positive advantage among positive-advantage tokens is at least the anchor’s. TEF uses entropy-centered teacher log likelihood to form a token endorsement probability; positive-advantage tokens use that keep probability and negative-advantage tokens its complement. A Bernoulli mask gates the OPD loss.

**Mechanism.** New current-student anchor and exploration trajectories for each prompt; domain label chooses its teacher rather than averaging both teachers. Each outer update collects new rollouts; one actor update per batch. One anchor (temperature 1.0, top-p 1.0) plus seven role-playing or three medical explorations (temperature 1.5, top-p 0.9). Three epochs: 468/231 outer updates in the reported settings. Teachers are fixed. Teacher-minus-student token advantages filtered twice. GGE retains exploration responses whose mean positive advantage among positive-advantage tokens is at least the anchor’s. TEF uses entropy-centered teacher log likelihood to form a token endorsement probability; positive-advantage tokens use that keep probability and negative-advantage tokens its complement. A Bernoulli mask gates the OPD loss. Trajectory acceptance followed by token-level supervision masking, under fixed domain teacher routing.

**Experimental setting.** Role-playing: 20k prompts split CoSER/general; medical: 19926 prompts split medical/general. Per-update candidate response count 1024, 32768 response cap, learning rate 2e-6. Role-playing is evaluated in no-thinking mode, medical in thinking mode, so the two settings are not a controlled scale comparison. General evaluation includes 13 benchmarks plus role-playing or medical task suites.

**Reported findings.** Role-playing general mean is 54.43 versus MOPD 52.09, while vertical mean is 45.00 versus 41.22. Medical general mean is 55.88 versus 51.81 (+4.07 percentage points), with vertical mean 60.95 versus 60.78, close to SFT 60.96. (Table 2). The general means remain below the base models (56.93 role-playing and 59.48 medical). Abstract relative-percentage improvements should not be relabeled as percentage-point gains. (Table 2 and abstract). Ablation additions are cumulative, not a fully factorial test. Appendix B adds a matched-rollout-count comparison, which is useful but does not make generated tokens or GPU compute identical. (Table 3; Appendix B).

**Evidence limits.** Teacher probability/entropy can be confidently wrong; the formal filtering properties concern the selected statistics, not downstream correctness or universal retention. Top-50 entropy is approximate; multi-sample exploration and rejection change cost as well as data quality. Two applied specializations and mode differences constrain generalization.

**Cross-paper synthesis.** Compare Trust-MOPD’s relative teacher confidence with entropy-centered token endorsement. Pair with ROSS to show that token masks can act on fresh OPD advantages or historical cross-entropy targets, which are different training regimes. Compare SF-MOPD’s transformed targets with UCMOPD’s selective acceptance.

**Primary-source locators**

- [§3 (GGE and TEF), §4, Tables 2–3; Appendix A (teacher/student IDs, sampling and entropy approximation); Appendix B (matched-rollout and weighting controls); Appendix C (properties).](https://arxiv.org/html/2608.26735v2): Method, state provenance and integration mechanism
- [§3 (GGE and TEF), §4, Tables 2–3; Appendix A (teacher/student IDs, sampling and entropy approximation); Appendix B (matched-rollout and weighting controls); Appendix C (properties).](https://arxiv.org/html/2608.26735v2): Experimental setting, author-reported results and limitations

<a id="study-27"></a>

## 27. RGBM / Fisher view

A Fisher-Geometric View of Multi-Teacher On-Policy Distillation

**Source:** [arXiv v1](https://arxiv.org/html/2610.26525v1). **Catalog ID:** arxiv:2610.26525. **Group:** Adjacent integration and state boundaries.

**Problem and inclusion.** Determine which specialist changes can be consolidated through parameter merging and which residual discrepancies require additional isolated distillation.

**Teachers, student and access.** The main suite uses homologous SmolLM3-3B specialists; a Qwen3-4B math/code suite is secondary. Both compatible weights and probability scoring are required. Specialist-generated calibration completions precede branch-local student rollouts.

**Mechanism.** Phase 1 solves a minimax subspace merge using unnormalized reward-second-moment residuals. Normalized residuals subsequently gate isolated per-domain OPD branches; selected updates are shrunk and remerged. The consolidated model receives no joint multi-teacher gradient.

**Experimental setting.** Open-MOPD evaluates three domain means; G-OPD evaluates seven math/code tasks. Phase 2 alternatives start from the same Phase 1 merge and reuse branch updates when comparing write-back rules.

**Reported findings.** Open-MOPD Table 1: Phase 1 macro is 32.52 versus 30.93 for the released 600-step OPD student; gated Phase 2 reaches 33.03. G-OPD Table 3: Phase 1/2 averages are 53.34/54.14 versus 53.79 for ExOPD. Section 4.1 reports less than two GPU-hours for unlabeled Phase 1 scoring; that is not the entire pipeline's cost.

**Evidence limits.** The Fisher relation is local and second-order, not global equivalence between arbitrary merging and distillation. The practical minimax residual solution differs from a weighted Fisher stationary point. Only Phase 1 avoids gradient training; Phase 2 trains branches. Low residual is a coupled write-back diagnostic, not proof that a domain cannot improve by itself.

**Cross-paper synthesis.** A useful boundary case for the integration-position axis: merge, train branches, then remerge. Contrast with FuseChat's distill-then-merge ordering and shared-student MOPD; preserve parameter compatibility and two-stage cost accounting.

**Primary-source locators**

- [§§2.2–2.4; §§3.1–3.3, Eqs.8–11](https://arxiv.org/html/2610.26525v1#S3): Local theory versus operational two-phase procedure
- [§§4.1–4.2, Table 1](https://arxiv.org/html/2610.26525v1#S4.SS1): Suites, scoring cost and main results
- [§4.5/Table 3; Appendix C.7](https://arxiv.org/html/2610.26525v1#A3.SS7): Branch admission and final write-back specification

<a id="study-28"></a>

## 28. MT-SDPO

Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs

**Source:** [arXiv v1](https://arxiv.org/html/2609.02548v1). **Catalog ID:** arxiv:2609.02548. **Group:** Adjacent integration and state boundaries.

**Problem and inclusion.** Choose external feedback by sample-level answer eligibility rather than the nominal domain, while transferring privileged information through a single self-teacher.

**Teachers, student and access.** Five student configurations span Qwen3-1.7B/4B/8B, Llama-3.1-8B-Instruct and OLMo-3-7B-Instruct. Three frozen domain teachers provide text feedback; one privileged EMA self-teacher, not those external experts, supplies token-distribution targets.

**Mechanism.** Verify one private teacher answer per prompt before training, then cache eligibility. Online failed student rollouts receive lexically sanitized eligible feedback; successful peer rollouts provide anchors. A masked, importance-weighted JSD objective matches the context-conditioned EMA self-teacher, refreshed once per rollout batch.

**Experimental setting.** Chemistry/materials/physics SciKnowEval multiple-choice questions; approximately 9:1 train/test split. Online methods share a multi-domain initialization, 100 steps and eight rollouts per prompt. Each domain has 79 held-out questions evaluated with avg@16.

**Reported findings.** For Qwen3-8B, MT-SDPO improves Macro by 4.64 and Worst by 14.79 points over the shared initialization, reducing Gap from 20.96 to 5.30. Qwen3-1.7B/4B also reduce Gap, but stronger-domain declines make Macro worse; OLMo shows aggregate improvement. Table 2: removing teacher eligibility verification lowers Macro by 6.56 points relative to the full Qwen3-8B method.

**Evidence limits.** Answer eligibility is not semantic verification of subsequent feedback; lexical sanitization does not establish critique correctness. The domain-routing control keeps the privileged self-teacher pipeline; it is not an unrestricted reproduction of all standard MOPD details. Smaller domain disparity is not equivalent to higher aggregate capability; the held-out sample size and multiple-choice verifier constrain generalization.

**Cross-paper synthesis.** Distinguishes multiple upstream supervisors from multiple direct distribution teachers. Pair with PromptSD and Trust to show that feedback conditioning, learned teacher prompts and weighted external KL targets are different supervision topologies.

**Primary-source locators**

- [§§4.1–4.4, Eqs.4–7](https://arxiv.org/html/2609.02548v1#S4): Eligibility, sanitized feedback and privileged EMA target
- [§§5.1–5.3, Table 1](https://arxiv.org/html/2609.02548v1#S5.SS1): Student configurations, metrics and conditional gains
- [§5.5/Table 2; Appendix A and B.1–B.3](https://arxiv.org/html/2609.02548v1#S5.SS5): Ablations, initialization and implemented divergence

<a id="study-29"></a>

## 29. MAS-OPD

MAS-OPD: On-Policy Distillation for Multi-agent Systems

**Source:** [arXiv v1](https://arxiv.org/html/2609.34234v1). **Catalog ID:** arxiv:2609.34234. **Group:** Adjacent integration and state boundaries.

**Problem and inclusion.** Multi-agent training can collapse role specialization and misassign coordination credit. Retained as an explicit boundary example because multiple roles and teacher contexts are easily mistaken for multiple learned teachers.

**Teachers, student and access.** One frozen Qwen3-14B teacher scored under contrasting role conditions. Student role policies are independently optimized Qwen3-1.7B or 4B instances. Multiple student agents and role-conditioned teacher views do not constitute multiple independently trained teachers. Detached token advantage combining ordinary teacher–student OPD with a target-role versus contrasting-role teacher log-probability difference (role weight 0.1). Eq. (13) averages tokens, turns and roles, with each role gradient updating only its own policy.

**Mechanism.** Joint trajectories generated by the current student-agent system, including environment interactions; code uses Coder/Tester and math uses Reasoner/Tool-User. A batch of joint rollouts precedes synchronized updates of the separate role policies. Each response is teacher-scored twice with only the role condition changed. Privileged attribution is available only for completed preceding turns; it is empty at the first turn. Detached token advantage combining ordinary teacher–student OPD with a target-role versus contrasting-role teacher log-probability difference (role weight 0.1). Eq. (13) averages tokens, turns and roles, with each role gradient updating only its own policy. One teacher’s context-dependent signals supervise several interacting student policies; no many-teacher-to-one-student integration.

**Experimental setting.** CodeContests and Polaris-53K training; three code and three math evaluations. Qwen3 teacher 14B, role students 1.7B/4B, no-thinking mode, up to four interaction turns, 150 optimization steps, batch 128. Every trained method has five independent training runs; prompt-only baselines have five decoding evaluations. All use a common eight-H20 infrastructure.

**Reported findings.** The full system has the highest reported means across the six tested benchmarks at both student scales; the 4B multi-agent system exceeds the single-agent 14B reference, with inference topology differing. (Table 1; Appendix D.5–D.6.1). Removing role-advantage specialization or privileged attribution lowers the reported six benchmark means; role exchange and single-role diagnostics probe specialization. (Table 2; §§4.3–4.4). The extra role contrast requires a second teacher force-decode per response; joint-rollout time dominates update time in the reported cost table, so teacher-free deployment does not mean single-agent inference cost. (Appendix D.6.3–D.6.4, Table 4).

**Evidence limits.** The main study uses one model family and a single teacher scale; cross-family and teacher-size effects are left open (Appendix A). Verifier-assisted attribution relies on task checkability and fixed collaboration workflows. Independent role policies are students, while contrasted teacher contexts share one set of frozen teacher weights; teacher count must follow learned components, not the number of scoring passes.

**Cross-paper synthesis.** Use beside PromptSD and privileged-context distillation to distinguish contextual views from independently learned teachers. Connect feedback mediators to MTSDPO, while retaining the direct role-conditioned token target here. Exclude MAS-OPD from strict multi-teacher counts even when analyzed among the 30 studies.

**Primary-source locators**

- [§§2.1–2.2, 3.1–3.4, Eqs. (7)–(13), Algorithm 1; §4, Tables 1–2; Appendix A, D.5–D.6, F.3–F.6.](https://arxiv.org/html/2609.34234v1): Method, state provenance and integration mechanism
- [§§2.1–2.2, 3.1–3.4, Eqs. (7)–(13), Algorithm 1; §4, Tables 1–2; Appendix A, D.5–D.6, F.3–F.6.](https://arxiv.org/html/2609.34234v1): Experimental setting, author-reported results and limitations

<a id="study-30"></a>

## 30. ROSS

ROSS: Relearning from Self-Generated Rollouts through Selective Supervision

**Source:** [arXiv v2](https://arxiv.org/html/2609.35954v2). **Catalog ID:** arxiv:2609.35954. **Group:** Adjacent integration and state boundaries.

**Problem and inclusion.** Verifier-positive trajectories can still contain locally incorrect, redundant or brittle tokens; imitating them all may undo upstream gains. Retained as the state-refresh boundary and as a contrast to selective online supervision.

**Teachers, student and access.** Historical student policies generated the stored trajectories. One GLM-5.2 high-thinking reviewer selects/excludes spans rather than supplying replacement token targets. In one setting multiple teachers belong to the preceding MOPD run, not to the ROSS relearning objective. Masked cross-entropy on accepted original student-generated assistant tokens, keeping masked errors, tool outputs and other context in the sequence. The reviewer does not rewrite targets or supply missing reasoning.

**Mechanism.** Saved historical self-rollouts from earlier RL/MOPD checkpoints, with original full context retained. No fresh current-policy rollout collection during relearning. Stored examples are filtered and annotated, then reused for configured SFT epochs (three for the main single-turn cases; a separate eight-epoch agentic configuration). Reviewer calls refresh masks, not student states. Masked cross-entropy on accepted original student-generated assistant tokens, keeping masked errors, tool outputs and other context in the sequence. The reviewer does not rewrite targets or supply missing reasoning. Offline example/token selection followed by supervised replay into one student, initialized from the final upstream checkpoint.

**Experimental setting.** Main model Qwen3.6-35B-A3B; saved Math-RL, Code-RL and three-domain MOPD histories. MOPD uses the first 200 steps; ROSS retains 31228 examples versus 42558 verifier-positive examples. ROSS and its no-mask control share retained examples and full context. Single-turn results use epoch-three endpoints; agentic SWE experiments use a separate thinking/context/scaffold protocol. Appendix H adds a 4B case.

**Reported findings.** On the six-benchmark MOPD panel, mean score is 58.40 upstream, 59.16 after continued MOPD, 57.70 after positive-rollout SFT and 62.20 after ROSS. These are author-reported results for that history and recipe. (Table 1). Holding retained examples and full context fixed, ROSS without the selective loss mask scores 58.49 versus 62.20 with it, isolating a mask contrast more cleanly than comparing differently filtered datasets. (Table 3; Appendix C.1). SWE-bench Verified improves from upstream 64.20 to 68.40 in the stated agentic setup (positive-rollout SFT 65.20). This uses a different generation/context protocol from single-turn experiments. (Table 2; Appendix C.4).

**Evidence limits.** The main evidence is one MoE lineage with an additional 4B case; replay quality depends on available upstream histories and the strong annotation reviewer. Filtering comparisons alter dataset composition/size and supervised-token count; matched examples isolate masking but do not make every other baseline compute identical. Semantic categories assigned to 1185 sampled trajectories are model annotations, not verified universal error frequencies. Historical successes may be informative without proving generalization beyond the inspected evaluation sets.

**Cross-paper synthesis.** Pair with UCMOPD: both mask tokens, but ROSS masks historical CE targets while UCMOPD masks fresh teacher-derived advantages. Connect to FAIR-style offline error/data selection and use ROSS to explain why state origin and refresh must be coded separately from the upstream training label.

**Primary-source locators**

- [§3, Eqs. (1)–(4); §4, Tables 1–4; Appendix C.1–C.4, Tables 6–7; Appendix E.1–E.4; Appendix H (4B case).](https://arxiv.org/html/2609.35954v2): Method, state provenance and integration mechanism
- [§3, Eqs. (1)–(4); §4, Tables 1–4; Appendix C.1–C.4, Tables 6–7; Appendix E.1–E.4; Appendix H (4B case).](https://arxiv.org/html/2609.35954v2): Experimental setting, author-reported results and limitations

## Corrections and reuse

Please cite original papers for their results. Cite this repository snapshot when reusing its coding. Send corrections with the version, section or table, affected field, and proposed interpretation; see [CONTRIBUTING](../CONTRIBUTING.md).
