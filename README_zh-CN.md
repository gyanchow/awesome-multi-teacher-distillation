# Awesome Multi-Teacher Distillation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

多教师蒸馏将多个互补或专业化模型的知识迁移到单个学生中；在线策略蒸馏使用学生自身生成的状态进行训练。

[English](README.md)

## 目录

- [从这里开始](#从这里开始)
- [收录范围](#收录范围)
- [多教师在线策略蒸馏](#多教师在线策略蒸馏)
- [离线多教师蒸馏](#离线多教师蒸馏)
- [相邻与替代范式](#相邻与替代范式)
- [单教师基础工作](#单教师基础工作)
- [综述与教程](#综述与教程)

## 从这里开始

![在线策略、离线和相邻蒸馏方法的分类地图](assets/method-map.svg)

| 阅读目标 | 推荐入口 |
| --- | --- |
| 建立领域概念 | [方法导读](resources/guide_zh-CN.md)：三个证据问题、方法比较和八篇论文的阅读路线。 |
| 深入研究问题 | [专题阅读路线](resources/reading-order.md)：教师路由、能力整合、异构模型和离线蒸馏。 |
| 选择综述 | [综述阅读导读](resources/survey-guide_zh-CN.md)：适用范围、核实版本与推荐章节。 |
| 查找实现与模型 | [作者关联产物](views/with-artifacts.md)：代码、模型、数据集和项目页面；链接可访问不代表结果已复现。 |

下方是入门用的代表性论文；完整目录和交叉分类见[附注](#附注)。

## 收录范围

严格 MOPD 必须同时满足三个条件：训练状态由当前或近当前学生生成；监督来自多个可独立辨识的教师；这些教师信号通过蒸馏目标直接更新学生。使用静态教师数据的工作归入离线多教师蒸馏；同伴互蒸馏、自教师或 EMA 教师、特权视角、同源多 rollout 与 replay 替代方案，若不同时满足三个条件，则明确标为相邻范式。

每条记录只属于一个主集合。论文类型、训练范式、状态来源、教师拓扑、组合机制、监督信号与应用领域是彼此正交的标签，因此系统报告不再与方法类别并列。当前快照共 145 条收录记录：68 条多教师在线策略蒸馏、51 条离线多教师蒸馏、14 条相邻或替代范式、3 条单教师基础工作，以及 9 条综述或教程。最近一次增量检索与核验日期为 2026-10-23；本次新增条目均核对了原始来源与相关方法章节。

本仓库中的 MOPD 始终指多教师在线策略蒸馏；Multi-Rollout OPD 写作 MR-OPD。纯参数合并、仅推理时集成、普通混合专家路由、没有学生训练的多智能体辩论，以及仅使用奖励的强化学习，不属于严格 MOPD。

## 多教师在线策略蒸馏

- [Nash-MOPD: Optimizing Task Trade-offs in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.26124) - 利用按训练曝光量归一化的反向 KL 进展，通过局部极小极大调度分配各领域提示。
- [Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.13521) - 让非路由教师评估同一学生轨迹，调整 token 信号并约束冲突梯度。
- [Composing What Each Teacher Learned: Delta Distillation for Multi-Teacher On-Policy Learning](https://arxiv.org/abs/2610.10460) - 围绕学生的冻结初始模型组合教师相对各自基座的 logit 增量。
- [Rethinking Self-Distillation for Multi-Teacher Capability Merging](https://arxiv.org/abs/2610.04272) - 在统一设置下比较充分调参的离线、混合与在线策略蒸馏的能力恢复和训练成本。
- [From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.02179) - 分析蒸馏目标、优化器动量与数值设置如何将教师信号转化为能力提升。
- [Latent-MOPD: Latent Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.02381) - 在 token 级 OPD 中加入专家隐藏状态对齐与逐教师过渡调度。
- [MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.30837) - 以采样 token 的教学优势为信号，比较整个教师池中的 token 级路由。
- [Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.23697) - 用相对共享参照模型校准后的专业化程度，对教师蒸馏损失加权。
- [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098) - 提供诊断与平衡 MOPD 能力预算的开放训练方案。
- [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406) - 形式化从专家到通用学生的整合流程，在学生轨迹上接收教师监督。
- [Simplifying and Improving On-Policy Distillation for Few-Step Diffusion](https://arxiv.org/abs/2610.18472) - 将在线速度场回归用于少步生成，并整合针对不同奖励训练的专家教师。
- [Qwen-Image-2.0-RL Technical Report](https://arxiv.org/abs/2606.27608) - 在学生生成轨迹上匹配速度场，将图像生成与编辑专家整合到一个学生中。

## 离线多教师蒸馏

- [Scaling Multi-Teacher Distillation for Digital Pathology](https://arxiv.org/abs/2610.12574) - 用教师专属 token 与对比特征匹配扩展数字病理中的多教师蒸馏。
- [Med-RADIO: Reducing All Medical Domains Into One via Multi-Teacher Distillation](https://arxiv.org/abs/2609.37682) - 通过归一化特征匹配，对齐通用医学教师与不同模态的专业教师。
- [SoFT: Soft Targets for Generalizable LLM Fine-Tuning](https://arxiv.org/abs/2609.32493) - 使用软目标学习固定的多教师示范，同时保留基座模型行为。
- [Multi-Teacher Knowledge Distillation via Teacher-Informed Mixture Priors](https://arxiv.org/abs/2605.27967) - 结合教师引导的贝叶斯混合先验与逐样本熵权重。
- [Merge-of-Thought Distillation](https://arxiv.org/abs/2509.08814) - 交替进行各教师推理数据上的蒸馏与已训练学生分支的参数合并。
- [Find Your Optimal Teacher: Personalized Data Synthesis via Router-Guided Multi-Teacher Distillation](https://aclanthology.org/2026.acl-long.666/) - 同时依据教师回答质量与学生可学习性路由提示，用于个性化数据合成。
- [Exploring Knowledge Purification in Multi-Teacher Knowledge Distillation for LLMs](https://arxiv.org/abs/2602.01064) - 将多个教师相互冲突的推理净化为一条训练推理，并比较不同路由策略。
- [Beyond Answers: Transferring Reasoning Capabilities to Smaller LLMs Using Multi-Teacher Knowledge Distillation](https://arxiv.org/abs/2402.04616) - 把多个大语言模型教师的答案和推理过程迁移到小模型学生。
- [AM-RADIO: Agglomerative Vision Foundation Model — Reduce All Domains Into One](https://arxiv.org/abs/2312.06709) - 将互补视觉基础模型的表征聚合为一个高效通用视觉编码器。
- [Learning from Multiple Teacher Networks](https://dl.acm.org/doi/10.1145/3097983.3098135) - 早期代表性多教师方法，同时迁移平均暗知识与中间关系知识。

## 相邻与替代范式

- [A Fisher-Geometric View of Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.26525) - 分析蒸馏与 Fisher 合并的局部联系，再以残差门控重合并独立训练的 OPD 分支。
- [ROSS: Relearning from Self-Generated Rollouts through Selective Supervision](https://arxiv.org/abs/2609.35954) - 对保存的 RL 与 MOPD rollout 进行筛选和掩码监督，用离线训练重新学习历史经验。
- [MAS-OPD: On-Policy Distillation for Multi-agent Systems](https://arxiv.org/abs/2609.34234) - 用一个冻结教师的不同角色条件视角蒸馏多个交互智能体。
- [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/abs/2609.05295) - 从当前与滞后检查点外推出稠密自教师，而不是使用独立教师池。
- [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626) - 在特权教师视角和特权学生视角之间路由监督，并非独立多教师池。
- [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652) - 从同源成功与失败 rollout 构造教师信号；“multi”指多个 rollout，而非多个独立教师。

## 单教师基础工作

- [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898) - 提出 skew-KL 目标与高效的混合式在线蒸馏流程。
- [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649) - 形式化学生生成序列上的蒸馏，并统一多种散度目标。
- [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) - 发展基于反向 KL、由学生采样行为的生成式蒸馏与稳定化方法。

## 综述与教程

- [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) - 从学生状态与教师监督梳理 OPD，2026 年 10 月修订版包含多教师 OPD 专章。
- [Echoes of the Oracle: A Survey of On-Policy Distillation in the Era of Large Language Models](https://www.researchgate.net/publication/405427626_Echoes_of_the_Oracle_A_Survey_of_On-Policy_Distillation_in_the_Era_of_Large_Language_Models) - 作者上传的预印本，整理教师访问权限、OPD 优化方式、多教师方法与失败模式。
- [A Comprehensive Survey on Knowledge Distillation](https://arxiv.org/abs/2503.12067) - 梳理 KD 知识来源、训练方案和应用，并设多教师聚合专节。
- [A Statistical Perspective on Knowledge Distillation: Foundations, Classical Methods, and Large Language Model Extensions](https://arxiv.org/abs/2609.33727) - 从贝叶斯推断、教师不确定性与多教师聚合的角度解释蒸馏。

## 贡献

欢迎补充论文与纠正信息。提交 issue 或 pull request 前，请先阅读[贡献指南](CONTRIBUTING.md)。

## 附注

五个完整主目录分别为：[多教师在线策略蒸馏](papers/multi-teacher-on-policy.md)、[离线多教师蒸馏](papers/offline-multi-teacher.md)、[相邻与替代范式](papers/adjacent-alternatives.md)、[单教师基础工作](papers/single-teacher-foundations.md)和[综述与教程](papers/reviews-tutorials.md)。

交叉视图支持按[组合机制](views/by-mechanism.md)、[教师拓扑](views/by-teacher-topology.md)、[监督信号](views/by-supervision-signal.md)、[应用领域](views/by-domain.md)、[系统报告](views/system-reports.md)和[首次公开日期](views/chronological.md)浏览。

维护与复现资料包括[机器可读目录](data/papers.json)、[数据规范](data/schema.json)、[分类说明](resources/taxonomy.md)、[开放研究问题](resources/open-questions.md)以及[检索与核验流程](resources/search-strategy.md)。

本次更新的来源与分类边界见[10 月 23 日检索记录](resources/update-2026-10-23.md)；向 awesome 总榜投稿前请核对[收录准备检查](resources/awesome-submission.md)。
