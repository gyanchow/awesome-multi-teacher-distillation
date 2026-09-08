# Awesome Multi-Teacher Distillation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选整理将互补、冲突或专业化的多个教师整合到单个学生中的研究，重点关注多教师在线策略蒸馏（Multi-Teacher On-Policy Distillation，MOPD）。

[English](README.md)

## 目录

- [收录范围](#收录范围)
- [多教师在线策略蒸馏](#多教师在线策略蒸馏)
- [离线多教师蒸馏](#离线多教师蒸馏)
- [相邻与替代范式](#相邻与替代范式)
- [单教师基础工作](#单教师基础工作)
- [综述与教程](#综述与教程)

## 收录范围

严格 MOPD 必须同时满足三个条件：训练状态由当前或近当前学生生成；监督来自多个可独立辨识的教师；这些教师信号通过蒸馏目标直接更新学生。使用静态教师数据的工作归入离线多教师蒸馏；同伴互蒸馏、自教师或 EMA 教师、特权视角、同源多 rollout 与 replay 替代方案，若不同时满足三个条件，则明确标为相邻范式。

每条记录只属于一个主集合。论文类型、训练范式、状态来源、教师拓扑、组合机制、监督信号与应用领域是彼此正交的标签，因此系统报告不再与方法类别并列。当前快照共 110 条已核验记录：47 条多教师在线策略蒸馏、45 条离线多教师蒸馏、11 条相邻或替代范式、3 条单教师基础工作，以及 4 条综述或教程。元数据核验截止日期为 2026-09-08。

本仓库中的 MOPD 始终指多教师在线策略蒸馏；Multi-Rollout OPD 写作 MR-OPD。纯参数合并、仅推理时集成、普通混合专家路由、没有学生训练的多智能体辩论，以及仅使用奖励的强化学习，不属于严格 MOPD。

## 多教师在线策略蒸馏

- [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172) - 发现状态覆盖率比原始数据量更能解释 OPD 的数据效率；每个领域 16 个查询即可匹配全数据三教师 MOPD。
- [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](https://arxiv.org/abs/2609.02548) - 用已验证的正确性而非领域标签，决定每条学生 rollout 应由哪些冻结教师监督。
- [Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](https://arxiv.org/abs/2609.02998) - 先用 verifier probe 检查教师可靠性；不可靠时从稠密蒸馏切换到 GRPO。
- [CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction](https://arxiv.org/abs/2609.02401) - 在 GUI grounding 与 OCR 中，将学生提议和基于置信度的教师纠错交错成 rollout。
- [Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791) - 开放系统报告；在 MOPD 阶段把学生 rollout 路由给指令遵循专家或 DPO 锚点。
- [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409) - 在相同专家和数据条件下，对参数合并、混合域强化学习与 MOPD 进行受控比较。
- [D$^3$-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](https://arxiv.org/abs/2608.24987) - 根据反向 KL 轨迹动态调整领域采样，减少不同教师收敛速度不一致造成的无效更新。
- [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098) - 给出开放训练方案，并用 token 份额平衡、差距感知分配和学生奖励刷新缓解能力失衡。
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) - 系统报告；使用裁剪后的采样 token 奖励整合九个“领域 × 推理强度”专家策略。
- [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](https://arxiv.org/abs/2607.02592) - 按 token 置信度在视觉语言教师与纯文本教师之间仲裁监督。
- [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406) - 给出“先专业化、再统一”的一般形式，在学生轨迹上进行路由后的稠密监督。
- [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/abs/2605.01347) - 把多个辩论教师转化为置信度加权的语言模型与智能体监督。

## 离线多教师蒸馏

- [LoFi RADIO: A Distilled In-Domain Backbone Applied for Artifact-Severity Grading of Ultra-Low-Field Neonatal Brain MR](https://arxiv.org/abs/2609.02676) - 把三个异构视觉基础模型对齐并压缩为一个低场 MRI 领域骨干。
- [MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation](https://arxiv.org/abs/2609.01913) - 对教师一致样本做 SFT，并把经 meta-judge 处理的分歧转成多语言商品匹配 DPO 数据。
- [When the Strongest Teacher Is Not the Best Teacher: Student-Centric Answer Selection](https://arxiv.org/abs/2605.26872) - 按预计的学生学习成本而非教师强弱，选择已验证的教师答案。
- [Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation](https://aclanthology.org/2026.acl-long.666/) - 同时依据教师回答质量与学生可学习性路由提示，用于个性化数据合成。
- [Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs](https://arxiv.org/abs/2602.01064) - 将多个教师相互冲突的推理净化为一条训练推理，并比较不同路由策略。
- [Beyond Answers: Transferring Reasoning Capabilities to Smaller LLMs Using Multi-Teacher Knowledge Distillation](https://arxiv.org/abs/2402.04616) - 把多个大语言模型教师的答案和推理过程迁移到小模型学生。
- [Knowledge Fusion of Large Language Models](https://arxiv.org/abs/2401.10491) - 对齐并融合异构源语言模型的 token 分布，再通过持续训练迁移到目标模型。
- [AM-RADIO: Agglomerative Vision Foundation Model — Reduce All Domains Into One](https://arxiv.org/abs/2312.06709) - 将互补视觉基础模型的表征聚合为一个高效通用视觉编码器。
- [Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space](https://proceedings.neurips.cc/paper/2020/hash/91c77393975889bd08f301c9e13a44b7-Abstract.html) - 将各教师视为独立梯度目标，寻找兼容帕累托方向的学生更新。
- [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) - 早期代表性多教师方法，同时迁移平均暗知识与中间关系知识。

## 相邻与替代范式

- [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/abs/2609.05295) - 从当前与滞后检查点外推出稠密自教师，而不是使用独立教师池。
- [WDL-OPD: Weak-Driven On-Policy Distillation via Mixture-Constrained Co-Training](https://arxiv.org/abs/2608.09447) - 让两个学生分支在锚点生成的状态上共同匹配一个冻结教师。
- [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626) - 在特权教师视角和特权学生视角之间路由监督，并非独立多教师池。
- [Skill-Conditioned Gated Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.28791) - 把同一在线策略的多个技能条件视角组织成门控自教师池。
- [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652) - 从同源成功与失败 rollout 构造教师信号；“multi”指多个 rollout，而非多个独立教师。
- [On-Policy Distillation with Best-of-N Teacher Rollout Selection](https://arxiv.org/abs/2605.09725) - 从一个教师的多条轨迹中选择监督，因此属于 rollout 选择而非多教师路由。

## 单教师基础工作

- [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898) - 提出 skew-KL 目标与高效的混合式在线蒸馏流程。
- [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649) - 形式化学生生成序列上的蒸馏，并统一多种散度目标。
- [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) - 发展基于反向 KL、由学生采样行为的生成式蒸馏与稳定化方法。

## 综述与教程

- [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) - 综述 OPD 目标、信号来源、稳定化方法、系统和应用。
- [Knowledge Distillation for Language Models](https://aclanthology.org/2025.naacl-tutorial.4/) - 涵盖预测与表征匹配、基于强化学习的知识蒸馏和多教师方法的教程。
- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) - 系统整理大语言模型的知识提取以及白盒、黑盒蒸馏方法。
- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) - 按响应、特征和关系知识组织蒸馏训练方案与应用。

## 贡献

欢迎补充论文与纠正信息。提交 issue 或 pull request 前，请先阅读[贡献指南](CONTRIBUTING.md)。

## 附注

五个完整主目录分别为：[多教师在线策略蒸馏](papers/multi-teacher-on-policy.md)、[离线多教师蒸馏](papers/offline-multi-teacher.md)、[相邻与替代范式](papers/adjacent-alternatives.md)、[单教师基础工作](papers/single-teacher-foundations.md)和[综述与教程](papers/reviews-tutorials.md)。

交叉视图支持按[组合机制](views/by-mechanism.md)、[教师拓扑](views/by-teacher-topology.md)、[监督信号](views/by-supervision-signal.md)、[应用领域](views/by-domain.md)、[系统报告](views/system-reports.md)、[已核验产物](views/with-artifacts.md)和[首次公开日期](views/chronological.md)浏览。

维护与复现资料包括[机器可读目录](data/papers.json)、[数据规范](data/schema.json)、[分类说明](resources/taxonomy.md)、[阅读路径](resources/reading-order.md)、[开放研究问题](resources/open-questions.md)以及[检索与核验流程](resources/search-strategy.md)。
