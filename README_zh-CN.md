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

每条记录只属于一个主集合。论文类型、训练范式、状态来源、教师拓扑、组合机制、监督信号与应用领域是彼此正交的标签，因此系统报告不再与方法类别并列。当前快照共 95 条已核验记录：41 条多教师在线策略蒸馏、41 条离线多教师蒸馏、6 条相邻或替代范式、3 条单教师基础工作，以及 4 条综述或教程。元数据核验截止日期为 2026-08-31。

本仓库中的 MOPD 始终指多教师在线策略蒸馏；Multi-Rollout OPD 写作 MR-OPD。纯参数合并、仅推理时集成、普通混合专家路由、没有学生训练的多智能体辩论，以及仅使用奖励的强化学习，不属于严格 MOPD。

## 多教师在线策略蒸馏

- [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409) - 在相同专家和数据条件下，对参数合并、混合域强化学习与 MOPD 进行受控比较。
- [D$^3$-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](https://arxiv.org/abs/2608.24987) - 根据反向 KL 轨迹动态调整领域采样，减少不同教师收敛速度不一致造成的无效更新。
- [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098) - 给出开放训练方案，并用 token 份额平衡、差距感知分配和学生奖励刷新缓解能力失衡。
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) - 系统报告；使用裁剪后的采样 token 奖励整合九个“领域 × 推理强度”专家策略。
- [When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2607.07050) - 说明截断后的教师支持集如何遗漏决策关键 token，并导致工具调用漂移。
- [H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation](https://arxiv.org/abs/2607.02592) - 按 token 置信度在视觉语言教师与纯文本教师之间仲裁监督。
- [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406) - 给出“先专业化、再统一”的一般形式，在学生轨迹上进行路由后的稠密监督。
- [CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2605.25378) - 通过双流路由与由粗到细蒸馏，将大量视觉效果 LoRA 整合到一个 LoRA 中。
- [ProteinOPD: Towards Effective and Efficient Preference Alignment for Protein Design](https://arxiv.org/abs/2605.10189) - 以自适应加权的几何共识组合多个蛋白质偏好教师。
- [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/abs/2605.01347) - 把多个辩论教师转化为置信度加权的语言模型与智能体监督。
- [Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220) - 系统报告；在级联强化学习阶段之间，从各领域最强检查点执行多领域 OPD。
- [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780) - 较早明确把 MOPD 命名为后训练能力整合阶段的前沿模型报告。

## 离线多教师蒸馏

- [Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation](https://aclanthology.org/2026.acl-long.666/) - 同时依据教师回答质量与学生可学习性路由提示，用于个性化数据合成。
- [Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs](https://arxiv.org/abs/2602.01064) - 将多个教师相互冲突的推理净化为一条训练推理，并比较不同路由策略。
- [Beyond Answers: Transferring Reasoning Capabilities to Smaller LLMs Using Multi-Teacher Knowledge Distillation](https://arxiv.org/abs/2402.04616) - 把多个大语言模型教师的答案和推理过程迁移到小模型学生。
- [Knowledge Fusion of Large Language Models](https://arxiv.org/abs/2401.10491) - 对齐并融合异构源语言模型的 token 分布，再通过持续训练迁移到目标模型。
- [AM-RADIO: Agglomerative Vision Foundation Model — Reduce All Domains Into One](https://arxiv.org/abs/2312.06709) - 将互补视觉基础模型的表征聚合为一个高效通用视觉编码器。
- [One Teacher is Enough? Pre-trained Language Model Distillation from Multiple Teachers](https://arxiv.org/abs/2106.01023) - 联合微调多个预训练语言模型教师，并迁移对齐后的隐藏状态和软标签。
- [Agree to Disagree: Adaptive Ensemble Knowledge Distillation in Gradient Space](https://proceedings.neurips.cc/paper/2020/hash/91c77393975889bd08f301c9e13a44b7-Abstract.html) - 将各教师视为独立梯度目标，寻找兼容帕累托方向的学生更新。
- [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) - 早期代表性多教师方法，同时迁移平均暗知识与中间关系知识。
- [Policy Distillation](https://arxiv.org/abs/1511.06295) - 奠定策略压缩以及从多个专家策略向单一学生迁移的基础。
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) - 提出温度缩放知识蒸馏及从集成模型压缩到学生模型的基本思路。

## 相邻与替代范式

- [REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning](https://arxiv.org/abs/2607.19450) - 回收专家 replay buffer，作为需要耦合 rollout 训练的 MOPD 的离线替代方案。
- [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626) - 在特权教师视角和特权学生视角之间路由监督，并非独立多教师池。
- [Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback](https://arxiv.org/abs/2606.14368) - 两个可训练领域同伴通过反馈条件化自蒸馏相互辅导。
- [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652) - 从同源成功与失败 rollout 构造教师信号；“multi”指多个 rollout，而非多个独立教师。
- [CoDistill-GRPO: A Co-Distillation Recipe for Efficient Group Relative Policy Optimization](https://arxiv.org/abs/2605.08873) - 在组相对策略优化中，让两个共同训练的策略进行双向蒸馏。
- [UniSD: Towards a Unified Self-Distillation Framework for Large Language Models](https://arxiv.org/abs/2605.06597) - 在同一自教师谱系中组合 EMA 教师、一致性、对比对齐和裁剪。

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
