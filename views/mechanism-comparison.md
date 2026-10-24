# Mechanism Comparison

30 purposively selected studies · Checked 2026-10-24.

Generated from [mechanism-audit.json](../data/mechanism-audit.json). Download [CSV](../data/mechanism-audit.csv) for filtering, or use the [decision guide](../resources/compare-methods.md) to choose a reading route.

30 purposively selected studies: 12 offline or NLP antecedents, 14 direct MOPD methods/comparative analyses, and 4 adjacent integration or state-boundary studies. Reviews and single-teacher foundations are contextual references and are not counted among these 30. Selection favors mechanism contrasts and relevant empirical controls; it is not a field census or 30 independent algorithms.

AI-assisted primary-source method and experiment checks with paper versions and section/table locators. Findings are author-reported, not independently reproduced; cross-paper connections are our synthesis. No independent human double coding or exhaustive coverage is claimed. Source hashes identify inspected snapshots where available.

The collection column follows the current catalog. A row is a study or a specified training stage, not a performance rank or a claim of independent replication.

| Study | Collection | Training state | Direct signal | Integration point |
| --- | --- | --- | --- | --- |
| [MT-BERT](https://arxiv.org/pdf/2106.01023) | offline_multi_teacher | Fixed labeled inputs | Hidden states + soft labels | Shared student |
| [FuseLLM](https://arxiv.org/pdf/2401.10491) | offline_multi_teacher | Fixed corpus prefixes | Aligned token distributions | Shared student |
| [FuseChat](https://arxiv.org/pdf/2408.07990) | offline_multi_teacher | Fixed response prefixes | Pairwise aligned distributions | Branches, then merge |
| [TinyLLM](https://arxiv.org/pdf/2402.04616) | offline_multi_teacher | Teacher rationale prefixes | Rationale + answer tokens | Shared student |
| [PILE](https://aclanthology.org/2022.emnlp-industry.60.pdf) | offline_multi_teacher | Fixed ranking inputs | Corrected ensemble logits | Shared ranker |
| [GOVERN](https://aclanthology.org/2024.emnlp-industry.120.pdf) | offline_multi_teacher | Fixed task inputs | Selected scalar logits | Shared student |
| [PerSyn](https://aclanthology.org/2026.acl-long.666.pdf) | offline_multi_teacher | Routed teacher responses | Response token targets | Dataset, then student |
| [FAIR / Committee](https://aclanthology.org/2025.findings-acl.217.pdf) | offline_multi_teacher | Historical student errors | Correction + feedback tokens | Dataset, then student |
| [Knowledge Purification](https://arxiv.org/pdf/2602.01064) | offline_multi_teacher | Teacher rationale prefixes | Purified rationale + answer | Shared student |
| [SCAS](https://arxiv.org/pdf/2605.26872) | offline_multi_teacher | Fixed answer pool | Selected answer tokens | Shared student |
| [MergeDistill](https://aclanthology.org/2021.findings-acl.254.pdf) | offline_multi_teacher | Masked corpus examples | Mapped soft labels + MLM | One multilingual student |
| [SoFT](https://arxiv.org/html/2609.32493v2) | offline_multi_teacher | Fixed demonstration prefixes | Base-anchored soft target | Data + target, then student |
| [MOPD](https://arxiv.org/html/2606.30406v1) | multi_teacher_on_policy | Student rollout prefixes | Routed log-probability signal | Shared student |
| [Open-MOPD](https://arxiv.org/html/2608.19098v1) | multi_teacher_on_policy | Student batches; reuse | Log-ratio advantage on student top-k | Shared student |
| [TrustMOPD](https://arxiv.org/html/2609.23697v3) | multi_teacher_on_policy | Student rollout prefixes | Weighted teacher KL losses | Shared student |
| [Delta-MOPD](https://arxiv.org/html/2610.10460v2) | multi_teacher_on_policy | Student rollout prefixes | Anchored teacher logit shifts | Target, then student |
| [Cross-teacher guarding](https://arxiv.org/html/2610.13521v2) | multi_teacher_on_policy | Same student trajectories | Modulated token advantage | Shared update constraint |
| [Nash-MOPD](https://arxiv.org/html/2610.26124v1) | multi_teacher_on_policy | Student rollout prefixes | Routed reverse-KL signal | Shared student; allocation |
| [Rethinking capability merging](https://arxiv.org/html/2610.04272v1) | multi_teacher_on_policy | Fixed / hybrid / current | Recipe-dependent targets | Comparative study |
| [PromptSD](https://arxiv.org/html/2607.18293v1) | multi_teacher_on_policy | Student buffer; 64-step refresh | Prompt-teacher reverse KL | Shared student |
| [D3-MOPD](https://arxiv.org/html/2608.24987v2) | multi_teacher_on_policy | Near-current student rollouts | Unchanged routed reverse-KL target | Adaptive domain sampling |
| [DN-MOPD](https://arxiv.org/html/2609.35347v1) | multi_teacher_on_policy | Current student rollout batches | Dispersion-scaled routed advantages | Domain-level loss scaling |
| [MOPD-Router / ExpertAlign](https://arxiv.org/html/2609.30837v2) | multi_teacher_on_policy | Rollout-student prefixes | ExpertAlign-weighted token advantages | Full-pool token routing |
| [Latent-MOPD](https://arxiv.org/html/2610.02381v1) | multi_teacher_on_policy | Current student, domain-pure batches | Routed hidden states + token targets | Representation/output crossfade |
| [SF-MOPD](https://arxiv.org/html/2610.02324v1) | multi_teacher_on_policy | Current student multimodal rollouts | Projected + original teacher JSD | EMA-guided target modification |
| [UCMOPD](https://arxiv.org/html/2608.26735v2) | multi_teacher_on_policy | Current anchor/exploration rollouts | Filtered teacher token advantages | Trajectory + token filtering |
| [RGBM / Fisher view](https://arxiv.org/html/2610.26525v1) | adjacent_alternative | Teacher completions + branch rollouts | Branch OPD; parameter updates | Merge, branches, remerge |
| [MT-SDPO](https://arxiv.org/html/2609.02548v1) | adjacent_alternative | Student groups; cached eligibility | EMA self-teacher distribution | Context, then self-teacher |
| [MAS-OPD](https://arxiv.org/html/2609.34234v1) | adjacent_alternative | Joint student-agent rollouts | Role-conditioned teacher advantages | One teacher, role students |
| [ROSS](https://arxiv.org/html/2609.35954v2) | adjacent_alternative | Historical student rollouts | Selected original token CE targets | Offline replay into one student |

Read the [30 detailed study cards](../resources/core-studies.md) for experimental conditions, reported findings, limitations and cross-paper connections.

## Source notes and qualifications

### MT-BERT

**Catalog ID:** arxiv:2106.01023. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2106.01023). **Locator:** §§2.1–2.2, Eqs.1–3, footnote4; §3.1; PDF pp.2–3

- **Learned components:** BERT, RoBERTa and UniLMv2; co-finetuned with shared prediction/pooling components before student transfer.
- **State origin:** Fixed labeled task examples, not autoregressive student trajectories.
- **Refresh:** No student-rollout refresh in the coded training stage.
- **Direct student target:** Aligned teacher hidden states, error-weighted soft labels and gold-label loss.
- **Upstream feedback:** Gold labels determine teacher-error weights.
- **Integration:** Several teacher losses update one compressed task model.
- **Qualification:** Co-finetuning couples teachers; distinct sources are not statistically independent. Hidden alignment assumes equal teacher layer counts.

### FuseLLM

**Catalog ID:** arxiv:2401.10491. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2401.10491). **Locator:** §§3.1–3.3, Eqs.1–5, Algorithm1; §4; PDF pp.3–6

- **Learned components:** Llama-2, OpenLLaMA and MPT source models; target initialized from one source.
- **State origin:** Fixed MiniPile corpus prefixes scored by the source models.
- **Refresh:** Corpus histories remain fixed; teacher distribution alignment/fusion is applied to those histories.
- **Direct student target:** Aligned and selected/weighted source distributions plus causal-language-model loss.
- **Upstream feedback:** Corpus-token cross-entropy scores guide fusion; no separate critique mediator.
- **Integration:** Prediction-space fusion directly trains one target model.
- **Qualification:** Unmatched token alignment may use one-hot fallback; heterogeneous source weights are not directly merged.

### FuseChat

**Catalog ID:** arxiv:2408.07990. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2408.07990). **Locator:** §§3.1–3.4, Eqs.1–4, Fig.2; §6; PDF pp.4–6,10

- **Learned components:** A pivot chat model and other heterogeneous source models; pairwise target models share the pivot architecture.
- **State origin:** Fixed instruction-response dataset prefixes.
- **Refresh:** No continual student-rollout refresh in the pairwise transfer stage.
- **Direct student target:** Pairwise aligned teacher distributions and supervised response targets.
- **Upstream feedback:** No separate feedback-mediated direct teacher in the coded stage.
- **Integration:** Pairwise transfer first; SCE parameter merging consolidates the resulting targets.
- **Qualification:** All K source teachers do not jointly optimize one continually shared student. Substantial dataset engineering is part of the recipe.

### TinyLLM

**Catalog ID:** arxiv:2402.04616. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2402.04616). **Locator:** §§3.2–3.3, Eqs.1–4; §4.1; PDF pp.3–4

- **Learned components:** FLAN-T5-xlarge and LLaMA-2-chat teachers in the reported reasoning setup.
- **State origin:** Teacher-generated rationales and gold answers under teacher-forced training prefixes.
- **Refresh:** Preconstructed rationale supervision; no student-prefix collection in the coded update.
- **Direct student target:** Token cross-entropy on teacher rationales and gold answers, with teacher-specific task prefixes.
- **Upstream feedback:** Gold answers and in-context demonstrations condition rationale generation.
- **Integration:** Multiple rationale sources train one student through separate task-conditioned losses.
- **Qualification:** Gold-answer-conditioned reasoning need not be faithful. This teacher-forcing terminology does not mean scoring student rollouts.

### PILE

**Catalog ID:** acl:2022.emnlp-industry.60. **Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2022.emnlp-industry.60.pdf). **Locator:** §§3.1–3.3, Fig.1; §§4.1–4.2; printed pp.589–591

- **Learned components:** Three separately fine-tuned ranking teachers from a common pretrained initialization.
- **State origin:** Logged/labeled query-document examples.
- **Refresh:** Iterative ensemble correction changes weights, not the provenance of fixed inputs.
- **Direct student target:** Corrected ensemble ranking logits.
- **Upstream feedback:** Labeled relevance identifies pairwise ranking errors for correction.
- **Integration:** Corrected logit ensemble supervises one compact ranker.
- **Qualification:** Requires relevance labels and proprietary search data; online deployment experiments are not on-policy distillation.

### GOVERN

**Catalog ID:** acl:2024.emnlp-industry.120. **Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2024.emnlp-industry.120.pdf). **Locator:** §3.1.1, Eqs.3–7; §3.2, Eqs.8–11; §4.2; Limitations

- **Learned components:** ERNIE-2.0 teachers of different depths/scales, separately fine-tuned on sampled labeled data.
- **State origin:** Fixed question-paragraph inputs, unlabeled then labeled.
- **Refresh:** Teacher selection depends on current student scalar logits; no generated-history refresh.
- **Direct student target:** MSE to selected ensemble logits; supervised GOVERN-CA adds label-guided weighting.
- **Upstream feedback:** Majority scalar-logit directions; gold labels in the supervised phase.
- **Integration:** Per-example selected targets directly train one student.
- **Qualification:** Logit-direction voting is not full parameter-gradient surgery. Base unsupervised voting does not distinguish selected teachers' competence.

### PerSyn

**Catalog ID:** acl:2026.acl-long.666. **Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2026.acl-long.666.pdf). **Locator:** §§2.1–2.3, Eqs.1–4; §3.1; Limitations

- **Learned components:** Distinct teacher model pool; mathematics calibration uses parallel answers from 15 teachers.
- **State origin:** Teacher-generated responses selected by a learned prompt router.
- **Refresh:** Router learned for the student/setting before dataset synthesis; response-only SFT uses fixed synthetic histories.
- **Direct student target:** Token likelihood of routed teacher responses.
- **Upstream feedback:** Student likelihood and response-quality reward supply router preferences.
- **Integration:** Routing consolidates sources into a synthetic dataset before training one student.
- **Qualification:** All-teacher calibration generations remain a cost; routing does not remove every parallel-generation expense.

### FAIR / Committee

**Catalog ID:** acl:2025.findings-acl.217. **Source:** [ACL Anthology proceedings PDF](https://aclanthology.org/2025.findings-acl.217.pdf). **Locator:** §§3.1–3.4, Eqs.1–7, Fig.2; Limitations; printed pp.4192–4194,4198

- **Learned components:** GPT-3.5-Turbo, Gemini-1.0-Pro and Mixtral-8x7B-Instruct teacher sources.
- **State origin:** Precollected student errors inform corrected-rationale and feedback examples used in fixed fine-tuning.
- **Refresh:** Fine-tuning data are not continually refreshed with new student errors; that extension is left for future work.
- **Direct student target:** Accepted rationale and mistake-feedback token targets.
- **Upstream feedback:** Teachers correct errors and peer-review candidate rationales.
- **Integration:** Committee output is consolidated into training data for one student.
- **Qualification:** Student errors are used, but this is not continual on-policy querying. Peer-review confidence does not certify correctness.

### Knowledge Purification

**Catalog ID:** arxiv:2602.01064. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2602.01064). **Locator:** §3.3, Eqs.4–6; §4, Eqs.12–14; Table1; §6 Limitations

- **Learned components:** Main pool: FLAN-T5-xlarge, LLaMA-2-chat, BioMistral-7B and Llama-3.1-8B-Instruct.
- **State origin:** Teacher rationale prefixes and gold answers.
- **Refresh:** RL-based selection can alternate with distillation; teacher-rationale provenance remains offline.
- **Direct student target:** Selected/consolidated rationale tokens plus a gold-answer objective.
- **Upstream feedback:** Aggregation/routing variants; student losses supply selector rewards in the RL variant.
- **Integration:** One rationale target per question updates a common student.
- **Qualification:** Variants differ; do not treat all selectors as fixed or claim every variant wins. Main evidence is commonsense/biomedical QA.

### SCAS

**Catalog ID:** arxiv:2605.26872. **Source:** [Unversioned arXiv PDF snapshot inspected 2026-10-24; no exact revision asserted](https://arxiv.org/pdf/2605.26872). **Locator:** §§2.1–2.3, Eqs.5–11, Algorithm1; §3 Models/Datasets; §9

- **Learned components:** 30 teacher models in mathematics; instruction experiments use 10 samples from one Llama-3.3-70B-Instruct teacher.
- **State origin:** Fixed teacher-generated candidate answers; student scores candidates without generating the supervised histories.
- **Refresh:** Selection/SFT rounds re-rank candidates as the student changes.
- **Direct student target:** Token likelihood of selected low-cost candidate answers.
- **Upstream feedback:** Verification and a student learning-cost proxy determine candidate eligibility/ranking.
- **Integration:** Changing selected supervision trains one student.
- **Qualification:** Multi-teacher status applies to the mathematical setting. The learning-cost proxy does not prove correctness or universal teaching quality.

### MergeDistill

**Catalog ID:** arxiv:2106.02834. **Source:** [Official Findings ACL-IJCNLP 2021 PDF; first public arXiv v1 on 2021-06-05](https://aclanthology.org/2021.findings-acl.254.pdf). **Locator:** §3.1 Steps 1–4 and Eqs.1–2; §§4.1–4.4; Tables 2–5

- **Learned components:** Separate pretrained monolingual BERT-family models; multilingual mBERT and MuRIL in another setting.
- **State origin:** Masked Wikipedia transfer-corpus examples tokenized separately by the corresponding teachers.
- **Refresh:** Teacher top-k masked-token logits are computed and stored offline; no student-rollout collection.
- **Direct student target:** Teacher soft-label cross-entropy plus ordinary masked-token prediction, with teacher tokens mapped into a union vocabulary.
- **Upstream feedback:** Observed corpus tokens provide masked-language-model labels; overlapping teachers are both used or selected by teacher LM loss.
- **Integration:** Mapped teacher predictions train one multilingual task-agnostic student; no teacher-weight interpolation.
- **Qualification:** Vocabulary construction and teacher predictions have separable effects; additional teachers are not uniformly beneficial.

### SoFT

**Catalog ID:** arxiv:2609.32493. **Source:** [arXiv v2, 2026-10-13](https://arxiv.org/html/2609.32493v2). **Locator:** §§3.1–3.4 Eqs.3–8; §§4–6 Tables 1–3; Appendices B.2.1/C/D/F

- **Learned components:** Fixed demonstrations from DeepSeek-R1, GLM-5.1, Kimi-K2.5, QwQ-32B/STILL-2, Qwen3-235B-A22B, GPT-OSS-20B, DeepSeek V4 Flash and Qwen3.6-27B; the student's frozen Base distribution provides the preservation reference.
- **State origin:** Fixed teacher-forced prefixes of multi-teacher reasoning and agentic demonstration corpora.
- **Refresh:** Targets depend only on frozen Base probabilities and validation-selected domain budgets; they remain fixed and can be cached. No online rollout refresh.
- **Direct student target:** Cross-entropy to the minimum-KL projection of Base that puts a floor on the demonstrated token; equivalently coupled demonstration CE and forward-KL preservation.
- **Upstream feedback:** Verified demonstrations and held-out domain validation determine data and the budget setting; external teacher logits are not required.
- **Integration:** Mixed teacher data and Base-derived target construction train one student.
- **Qualification:** The budget controls initial gold-logit gradient mass, not general parameter-gradient norms. Low KL on validation prefixes does not guarantee task retention.

### MOPD

**Catalog ID:** arxiv:2606.30406. **Source:** [arXiv v1](https://arxiv.org/html/2606.30406v1). **Locator:** §§3.1–3.3, Eqs.1–5; §4.4.2; AppendixA

- **Learned components:** Frozen domain RL experts independently specialized from a common SFT checkpoint.
- **State origin:** Student-generated responses/trajectories dispatched by prompt domain.
- **Refresh:** §3.1 collects a student trajectory per batch; asynchronous teacher prefill overlaps collection.
- **Direct student target:** Routed per-token reverse-KL formulation; clipped sampled-token advantage or mass-corrected top-k implementations.
- **Upstream feedback:** Domain label selects the teacher; no separate feedback-to-self-teacher mediator.
- **Integration:** Teacher signals update one shared student across domain batches.
- **Qualification:** Same-origin stability is a tested condition, not universal compatibility. Top-k corrections do not recover unobserved full-vocabulary support.

### Open-MOPD

**Catalog ID:** arxiv:2608.19098. **Source:** [arXiv v1](https://arxiv.org/html/2608.19098v1). **Locator:** §§2.1,2.3; §§3.2–3.3; §§4.1–4.4,Algorithm1

- **Learned components:** Three math/code/instruction-following RL teachers from one mixed-SFT SmolLM3 checkpoint.
- **State origin:** Current-student rollouts reused for inner updates.
- **Refresh:** New rollout batches; student probabilities/rewards refreshed during inner updates while teacher scores can be cached.
- **Direct student target:** Detached teacher-student log differences over student top-16 support, aggregated into PPO token advantages.
- **Upstream feedback:** Fixed domain routing; token shares and teacher-student gaps control exposure.
- **Integration:** Balanced domain supervision updates one shared student.
- **Qualification:** Refreshing rewards does not refresh histories. Negative conflict-mask results apply to the tested metric, interventions and setting.

### TrustMOPD

**Catalog ID:** arxiv:2609.23697. **Source:** [arXiv v3](https://arxiv.org/html/2609.23697v3). **Locator:** §§3.1–3.3,Eqs.2–5; §4.1; AppendixB.1

- **Learned components:** Separately RL-specialized math/code/instruction teachers with a shared pre-RL reference.
- **State origin:** Student-generated prefixes scored by the specialist pool.
- **Refresh:** Weights recomputed at each prefix; offline calibration constants remain fixed. Exact batch refresh interval not extracted.
- **Direct student target:** Calibrated displacement-derived detached weights on teacher-specific reverse-KL losses.
- **Upstream feedback:** No external correctness verifier in the main weighting mechanism.
- **Integration:** Weighted specialist losses update one student.
- **Qualification:** Displacement is a reliability proxy, not correctness. Student initialization need not equal the shared reference.

### Delta-MOPD

**Catalog ID:** arxiv:2610.10460. **Source:** [arXiv v2](https://arxiv.org/html/2610.10460v2). **Locator:** §§2–3,Eqs.2–5; composition/routing experiments; AppendixB

- **Learned components:** Specialist endpoints with their exact precursor checkpoints; student initialization is a frozen anchor.
- **State origin:** Student-generated prefixes.
- **Refresh:** Target shifts evaluated on collected student prefixes; exact batch refresh interval not extracted.
- **Direct student target:** Anchor logits plus selected teacher-minus-precursor logit shifts; reverse-KL-derived matching signal.
- **Upstream feedback:** Routing/composition chooses participating teachers, without a feedback-mediated self-teacher.
- **Integration:** Composed or routed shift targets update one student.
- **Qualification:** Shifts include style and calibration. Compatible tokens/projection and precursor access are needed; interleaved routing need not improve over endpoint transfer.

### Cross-teacher guarding

**Catalog ID:** arxiv:2610.13521. **Source:** [arXiv v2](https://arxiv.org/html/2610.13521v2). **Locator:** §§3.1–3.4,Eqs.4–11; AppendixA

- **Learned components:** Routed and auxiliary specialists evaluated relative to a shared frozen reference.
- **State origin:** The same current-student target-domain trajectories are scored by routed and auxiliary teachers.
- **Refresh:** Teacher agreement and auxiliary gradients use stored current-batch trajectories; exact collection interval not extracted.
- **Direct student target:** Detached agreement-modulated token advantage in a PPO-style loss; auxiliary-gradient projection modifies the update.
- **Upstream feedback:** Auxiliary teacher preferences supply compatibility evidence, not proof of target-task correctness.
- **Integration:** Modulated/protected updates train one shared student.
- **Qualification:** The norm-retention floor may leave conflict. Same-trajectory local constraints do not guarantee auxiliary-domain preservation.

### Nash-MOPD

**Catalog ID:** arxiv:2610.26124. **Source:** [arXiv v1](https://arxiv.org/html/2610.26124v1). **Locator:** §3.1,Eqs.1–2; §§4.1–4.3; AppendixA

- **Learned components:** Frozen domain-specialist teachers; the domain routing rule is held fixed.
- **State origin:** Student-generated responses sampled under changing domain prompt shares.
- **Refresh:** Fresh training collections follow the controller; exposure-normalized recent progress changes allocation.
- **Direct student target:** Routed reverse-KL objective; controller reallocates prompt exposure without changing teacher targets.
- **Upstream feedback:** Existing loss/progress statistics supply scheduling signals.
- **Integration:** Domain allocation controls learning by one shared student.
- **Qualification:** Maximin justification assumes a local separable progress model; it does not guarantee downstream worst-domain accuracy.

### Rethinking capability merging

**Catalog ID:** arxiv:2610.04272. **Source:** [arXiv v1](https://arxiv.org/html/2610.04272v1). **Locator:** §§3.1,4–6; AppendixG.2–G.3,Table19

- **Learned components:** Domain experts and students share an initialization in the controlled consolidation study.
- **State origin:** Compared arms: recorded teacher histories; student responses after recorded histories; or live/current-student trajectories.
- **Refresh:** SFT/Soft-KD reuse fixed corpora; hybrid samples after recorded histories; MOPD collects current trajectories.
- **Direct student target:** Respectively hard tokens, teacher distributions, or on-policy teacher-matching objectives; merging is a separate comparator.
- **Upstream feedback:** Rejection sampling constructs successful teacher corpora; independently tuned comparison arms.
- **Integration:** Alternative recipes each produce a consolidated student; this is a comparative study, not one new algorithm.
- **Qualification:** Training GPU-hour ratios exclude teacher-corpus generation, evaluation and other tuning runs. Results do not cover all heterogeneous teachers.

### PromptSD

**Catalog ID:** arxiv:2607.18293. **Source:** [arXiv v1](https://arxiv.org/html/2607.18293v1). **Locator:** §§4.1–4.3,Eqs.5–10; §5.1 implementation

- **Learned components:** Four task-specific soft prompts learned independently on a common frozen backbone; routed teachers are fixed.
- **State origin:** Student-generated prefixes on the merged task corpus.
- **Refresh:** Rollout buffer refreshed every 64 steps; policies can lag between refreshes.
- **Direct student target:** Token-level reverse KL to the task-tag-routed soft-prompt teacher.
- **Upstream feedback:** Task labels route teachers; gold task data train prompts beforehand.
- **Integration:** Distinct learned prompt policies transfer into one prompt-free student.
- **Qualification:** Four learned prompt components are not four independently trained backbones. Periodic collection is not strict current-policy sampling at every update.

### D3-MOPD

**Catalog ID:** arxiv:2608.24987. **Source:** [arXiv v2](https://arxiv.org/html/2608.24987v2). **Locator:** §3, Eqs. (2)–(6), Algorithm 1; §§4.1–4.4, Tables 1–2; Appendix B (infrastructure), D/Table 6 (one-checkpoint result), F (assumptions), I (failure modes).

- **Learned components:** Four frozen, independently GRPO-specialized Qwen3.6-35B-A3B teachers for math, code, instruction following and tool use; student initialized from their common base. Teacher token probabilities/log-probabilities on student states are required.
- **State origin:** Student-generated response prefixes in the asynchronous slime rollout/update system; operationally near-current rather than guaranteed synchronized with every optimizer step.
- **Refresh:** New rollout batches supply states and logged reverse-KL. A separate watcher recomputes domain ratios every 10 rollout steps after warm-up (20 steps); W=10, R=3, with the full three-window statistic available from step 40. The 300-second file polling interval is not the policy/ratio update cadence.
- **Direct student target:** The existing domain-routed reverse-KL/OPD teacher target is retained. The scheduler multiplies normalized remaining KL gap by clipped nonnegative KL-descent velocity, then applies softmax, a 0.10 domain floor and sampling jitter.
- **Upstream feedback:** Smoothed reverse-KL trajectories from already executed training; no new external judge or extra synchronous teacher query for scheduling.
- **Integration:** Domain prompt/rollout allocation before teacher supervision; not a new token mixture or parameter merge.
- **Qualification:** The 0.97 normalized transfer figure pools separate per-benchmark maxima across 16 checkpoints; it is not the score of one student checkpoint. KL proxies, asynchronous rollouts and rollout-step accounting limit any stronger causal or wall-clock claim.

### DN-MOPD

**Catalog ID:** arxiv:2609.35347. **Source:** [arXiv v1](https://arxiv.org/html/2609.35347v1). **Locator:** §2 and Algorithm 1 (normalization/objective); §§3.1–3.4, Tables 1–5; Appendix C (fixed-weight, budget and seed controls); §5 (limitations).

- **Learned components:** Three frozen independently RL-trained math/code/instruction-following specialists at each Qwen3.5 size (9B, 4B, 2B); each student shares the specialists’ base initialization. Assigned-teacher sampled-token log-probabilities and domain labels suffice for the core normalization.
- **State origin:** Fresh student-generated responses in each rollout iteration; rollout-policy cached scores and current pre-update actor scores are distinguished.
- **Refresh:** Domain and pooled population standard deviations are recomputed from cached valid response-token log ratios in each rollout batch. Weights are stop-gradient; actor advantages are recomputed for the policy update. No independent teacher-refresh interval is specified because teachers remain frozen.
- **Direct student target:** Domain-routed teacher/student token log-ratio advantage, multiplied by clip(sigma_pool/sigma_domain, 0.25, 4) inside the clipped policy objective. No mean subtraction; signs preserved; fallback weight 1 for zero dispersion or fewer than two observations.
- **Upstream feedback:** Empirical dispersion of teacher-minus-rollout log probabilities; no verifier or reliability labels. Token-pooled statistics differ from the loss reduction, which averages valid tokens per response then responses.
- **Integration:** Scalar domain feedback normalization after fixed prompt allocation and teacher routing; not teacher selection.
- **Qualification:** Equalizing advantage dispersion does not equalize gradient norms or establish teacher correctness. Strong SeqKD-SFT remains better under the paper’s own recipe, and fixed approximate weights match online estimates in several settings.

### MOPD-Router / ExpertAlign

**Catalog ID:** arxiv:2609.30837. **Source:** [arXiv v2](https://arxiv.org/html/2609.30837v2). **Locator:** §§3.1–3.3, Eqs. (1)–(11), Algorithm 1; §4, Tables 1–5; Appendix A (scope), B/Table 6 (training), D (uncertainty), E (routing controls).

- **Learned components:** Three frozen Qwen3-4B math/code/IF specialists, a shared frozen pre-specialization base reference, and Qwen3-1.7B or 4B students. ExpertAlign needs teacher/base/student log probabilities on the student top-16 support; the teacher pool is queried token-wise. The router itself is not learned.
- **State origin:** Prefixes generated by the rollout student; routed advantages are held for clipped actor updates, so distinguish rollout policy from updated actor.
- **Refresh:** New rollout batch per outer iteration; all teachers and reference score its prefixes. Algorithm 1 constructs routing weights before inner minibatch updates. Reported main configuration uses three epochs, train and minibatch size 1024, and one response per prompt; do not infer that Algorithm 1’s general K always exceeds one.
- **Direct student target:** Weighted teacher-minus-rollout-student sampled-token log-ratio advantages. ExpertAlign compares teacher specialization (teacher–base log-probability displacement) with teaching direction (teacher–student displacement), retains positive alignment, and uses uniform or cosine-weighted retained teachers; all-negative tokens are skipped.
- **Upstream feedback:** Entropy, overlap/accessibility and specialization/teaching-direction geometry; no external verifier in the routing rule. Benchmark teacher specialization is a model-derived proxy, not ground-truth expertise.
- **Integration:** Token-level teacher filtering/weighting across the full pool, inside the clipped OPD policy objective.
- **Qualification:** The main ExpertAlign setup assumes a shared teacher base and compatible token support. Querying all teachers and a base reference adds cost; log-probability direction alignment is not an identified causal measure of skill.

### Latent-MOPD

**Catalog ID:** arxiv:2610.02381. **Source:** [arXiv v1](https://arxiv.org/html/2610.02381v1). **Locator:** §3, Eqs. (1)–(3); §4, Tables 1–3; §5 (batch control); Appendix A (implementation and Norm Eq. (5)), F (batch organization), J (scope).

- **Learned components:** Three frozen math/code/logic specialists. Student: DeepSeek-R1-Distill-Qwen-1.5B. Same-family teachers share its backbone; the cross-family panel uses 7B Qwen-backbone specialists with the same tokenizer and 28 blocks but width 3584 versus student width 1536. Requires teacher hidden states and token distributions; a shared trainable projector is used across unequal widths.
- **State origin:** Fresh student-generated responses, with a domain-pure batch selecting one specialist for both representation and token supervision.
- **Refresh:** One policy optimization epoch and one actor update per rollout batch; 62 global updates rotate math/code/logic. Teacher-local counter advances only when that teacher is active. Crossfade windows are 10 teacher-local updates (30 global) same-family and 7 (21 global) cross-family; representation loss is zero from global steps 31/22 respectively.
- **Direct student target:** Joint normalized hidden-state alignment and a fixed-advantage token objective on student top-16 support, using full-vocabulary log-probability normalization. Representation weight fades down while token weight rises; same-family default aligns last three layers, unequal-width default the last layer’s final 2000 response positions via a linear projector.
- **Upstream feedback:** No verifier reward in training. Domain labels route teacher selection; feature/logit values come directly from frozen specialists. Cross-family projector ridge initialization uses a separate small rollout sample.
- **Integration:** Two direct supervision channels—representation alignment and output-token OPD—within the same routed student update; final inference discards the projector.
- **Qualification:** The cross-family label does not demonstrate arbitrary architecture or vocabulary compatibility. The paper’s MOPD-style baseline and Norm definition differ from the original MOPD system; its selected-feature storage ratio is not measured peak GPU-memory reduction.

### SF-MOPD

**Catalog ID:** arxiv:2610.02324. **Source:** [arXiv v1](https://arxiv.org/html/2610.02324v1). **Locator:** §§2.1–2.4, Eqs. (4)–(10); §§3.1–3.3, Tables 1–2. Short multimodal paper; no appendix-derived refresh interval assumed.

- **Learned components:** Four frozen Qwen3-VL-8B visual specialists (Data Chart, Real-World Item, Schematic Diagram and perception); students Qwen3-VL-2B/4B/8B-Instruct. An EMA copy of the evolving student is a moving reference, not a fifth independently trained specialist. Full token distributions and student parameter access are needed.
- **State origin:** Current-student generated response prefixes, scored by all four specialists and the EMA student reference.
- **Refresh:** The EMA parameters track student updates with decay 0.999, initialized from the student. The main description uses student-generated samples for distillation; a separate numerical rollout-buffer refresh interval is not explicitly reported.
- **Direct student target:** Projected specialist log-probability pseudo-targets under JSD plus an original unprojected multi-teacher JSD term. Centered teacher displacement components opposing the EMA-student direction are attenuated using a ridge denominator (1e-3); target distributions are stop-gradient.
- **Upstream feedback:** EMA-student displacement provides an evolving retention direction. No separate correctness judge supplies the training signal. The evaluation judge fallback is distinct from this training mechanism.
- **Integration:** Teacher output-space target modification and joint distillation loss; equal teacher weights, not hard domain routing. The base MOPD objective in this paper is summed JSD.
- **Qualification:** Ridge-stabilized projection does not create exact orthogonality, and the added unprojected JSD term can reintroduce an opposing component. Output log-probability displacements are not actual parameter gradients. Capability loss is reduced, not eliminated.

### UCMOPD

**Catalog ID:** arxiv:2608.26735. **Source:** [arXiv v2](https://arxiv.org/html/2608.26735v2). **Locator:** §3 (GGE and TEF), §4, Tables 2–3; Appendix A (teacher/student IDs, sampling and entropy approximation); Appendix B (matched-rollout and weighting controls); Appendix C (properties).

- **Learned components:** Two frozen teachers per specialization setting: general base and SFT domain specialist; student starts from the specialist. Role-playing uses Qwen3-4B-Instruct-2507 lineage. Medical uses II-Medical-7B-Preview, which the paper’s configuration table identifies as an 8B Qwen3 architecture, with Qwen3-8B general teacher. Core implementation needs sampled-token log-probabilities and teacher top-50 probabilities, not teacher hidden states.
- **State origin:** New current-student anchor and exploration trajectories for each prompt; domain label chooses its teacher rather than averaging both teachers.
- **Refresh:** Each outer update collects new rollouts; one actor update per batch. One anchor (temperature 1.0, top-p 1.0) plus seven role-playing or three medical explorations (temperature 1.5, top-p 0.9). Three epochs: 468/231 outer updates in the reported settings. Teachers are fixed.
- **Direct student target:** Teacher-minus-student token advantages filtered twice. GGE retains exploration responses whose mean positive advantage among positive-advantage tokens is at least the anchor’s. TEF uses entropy-centered teacher log likelihood to form a token endorsement probability; positive-advantage tokens use that keep probability and negative-advantage tokens its complement. A Bernoulli mask gates the OPD loss.
- **Upstream feedback:** Teacher uncertainty/entropy and student–teacher advantage, not verified correctness. Implementation approximates entropy with the unrenormalized top-50 contribution; theoretical full-distribution expressions should not be conflated with that approximation.
- **Integration:** Trajectory acceptance followed by token-level supervision masking, under fixed domain teacher routing.
- **Qualification:** v2 calls the method UCMOPD; UP-MOPD is only a historical repository alias. Extra exploration, scoring and entropy computation have cost. General recovery remains incomplete relative to the original base, and teacher endorsement is not a factual-correctness certificate.

### RGBM / Fisher view

**Catalog ID:** arxiv:2610.26525. **Source:** [arXiv v1](https://arxiv.org/html/2610.26525v1). **Locator:** §§2.2–2.4,3.1–3.3,4.3; AppendixC.7

- **Learned components:** Homologous domain specialists from a common base; retained specialists supervise isolated domain branches.
- **State origin:** Specialist-generated calibration completions for merging; branch-generated trajectories for residual OPD.
- **Refresh:** Branch-local rollout collection; the consolidated merge receives no joint multi-teacher rollout-training step.
- **Direct student target:** Residual parameter-combination objective, then single-domain branch OPD targets; final branch updates are gated/shrunk.
- **Upstream feedback:** Label-free residual and linearity diagnostics control branch admission/write-back.
- **Integration:** Parameter-space merge, isolated branch transfer, and selected parameter remerge.
- **Qualification:** Fisher equivalence is local/second order. Practical minimax residual optimization is not the exact full Fisher solution.

### MT-SDPO

**Catalog ID:** arxiv:2609.02548. **Source:** [arXiv v1](https://arxiv.org/html/2609.02548v1). **Locator:** §§4.1–4.4; §§5.3–5.5; AppendixB.1–B.3

- **Learned components:** Several frozen external feedback teachers; one EMA self-teacher directly provides the distribution target.
- **State origin:** Current student rollout groups; offline teacher answers establish prompt-level eligibility.
- **Refresh:** Eligibility is verified once before training; feedback and self-anchors are constructed for individual online rollouts.
- **Direct student target:** Masked, importance-weighted token divergence to a privileged EMA self-teacher.
- **Upstream feedback:** Answer-verified eligibility admits sanitized external feedback; correct peer rollouts supply self-anchors.
- **Integration:** Multiple feedback sources enter privileged context, then one self-teacher distribution trains the student.
- **Qualification:** The verifier checks teacher answers, not the correctness of every feedback statement. Better balance can coexist with aggregate regression.

### MAS-OPD

**Catalog ID:** arxiv:2609.34234. **Source:** [arXiv v1](https://arxiv.org/html/2609.34234v1). **Locator:** §§2.1–2.2, 3.1–3.4, Eqs. (7)–(13), Algorithm 1; §4, Tables 1–2; Appendix A, D.5–D.6, F.3–F.6.

- **Learned components:** One frozen Qwen3-14B teacher scored under contrasting role conditions. Student role policies are independently optimized Qwen3-1.7B or 4B instances. Multiple student agents and role-conditioned teacher views do not constitute multiple independently trained teachers.
- **State origin:** Joint trajectories generated by the current student-agent system, including environment interactions; code uses Coder/Tester and math uses Reasoner/Tool-User.
- **Refresh:** A batch of joint rollouts precedes synchronized updates of the separate role policies. Each response is teacher-scored twice with only the role condition changed. Privileged attribution is available only for completed preceding turns; it is empty at the first turn.
- **Direct student target:** Detached token advantage combining ordinary teacher–student OPD with a target-role versus contrasting-role teacher log-probability difference (role weight 0.1). Eq. (13) averages tokens, turns and roles, with each role gradient updating only its own policy.
- **Upstream feedback:** Rule-based task verifiers assign responsibility for previous completed turns; these attributions enter teacher-only privileged context, not student context or a generated replacement answer.
- **Integration:** One teacher’s context-dependent signals supervise several interacting student policies; no many-teacher-to-one-student integration.
- **Qualification:** A multi-agent system outperforming a single 14B teacher is not by itself evidence of single-model compression or a compute-matched teacher comparison. The teacher and verifier are training-only, but inference retains multiple interacting students.

### ROSS

**Catalog ID:** arxiv:2609.35954. **Source:** [arXiv v2](https://arxiv.org/html/2609.35954v2). **Locator:** §3, Eqs. (1)–(4); §4, Tables 1–4; Appendix C.1–C.4, Tables 6–7; Appendix E.1–E.4; Appendix H (4B case).

- **Learned components:** Historical student policies generated the stored trajectories. One GLM-5.2 high-thinking reviewer selects/excludes spans rather than supplying replacement token targets. In one setting multiple teachers belong to the preceding MOPD run, not to the ROSS relearning objective.
- **State origin:** Saved historical self-rollouts from earlier RL/MOPD checkpoints, with original full context retained.
- **Refresh:** No fresh current-policy rollout collection during relearning. Stored examples are filtered and annotated, then reused for configured SFT epochs (three for the main single-turn cases; a separate eight-epoch agentic configuration). Reviewer calls refresh masks, not student states.
- **Direct student target:** Masked cross-entropy on accepted original student-generated assistant tokens, keeping masked errors, tool outputs and other context in the sequence. The reviewer does not rewrite targets or supply missing reasoning.
- **Upstream feedback:** Outcome verifier first filters positives; LLM proposal/audit identifies valid single-turn spans or agentic defects. Deterministic alignment compiles masks against original stored tokens; unresolved decisions/boundaries are withheld.
- **Integration:** Offline example/token selection followed by supervised replay into one student, initialized from the final upstream checkpoint.
- **Qualification:** Following MOPD does not make ROSS on-policy or multi-teacher. No new rollouts does not mean no extra model calls: reviewing, auditing and SFT cost remain. The annotation reviewer is not an independent human adjudication panel.

## Correct or reuse a record

Cite the original study for its method and results. Cite this repository snapshot only when using its curation or coding. For corrections, give the paper version, section/equation, affected field, and replacement interpretation. See [CONTRIBUTING](../CONTRIBUTING.md).
