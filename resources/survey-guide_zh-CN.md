# 综述阅读导读

[English](survey-guide.md) · 核验日期：2026-10-23。

已经有多篇相关综述。与本仓库最贴近的两篇以 OPD 为主题，设有多教师章节；传统多教师蒸馏则可以从通用 KD 综述入手。本轮尚未核实到一篇完全以严格 MOPD 为唯一主题的独立综述。

## 按阅读目标选择

| 阅读目标 | 综述与核实版本 | 建议重点 |
| --- | --- | --- |
| 直接了解当前 MOPD | [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)，v5 更新于 2026-10-21，首发 2026-04-01 | 优先读第 6 节：教师资格、路由、目标组合、能力平衡与专家演化；不熟悉目标函数时先读第 2–3 节。 |
| 比较 OPD 的不同形式 | [Echoes of the Oracle](https://www.researchgate.net/publication/405427626_Echoes_of_the_Oracle_A_Survey_of_On-Policy_Distillation_in_the_Era_of_Large_Language_Models)，作者上传的预印本，2026-05-29 | 第 3.2 节讲多教师 OPD；全文按教师访问权限、监督粒度、优化方式和失败模式梳理方法。 |
| 梳理传统多教师方法 | [A Comprehensive Survey on Knowledge Distillation](https://arxiv.org/abs/2503.12067)，v2 为 2025-10-11，首发 2025-03-15 | 第 4.3 节覆盖聚合、自适应加权与知识融合；第 6.1 节连接到 LLM 应用。 |
| 理解权重与不确定性 | [A Statistical Perspective on Knowledge Distillation](https://arxiv.org/abs/2609.33727)，2026-09 | 第 3 节给出统计与贝叶斯视角，第 4.1 节讨论多教师聚合及可靠性。 |
| 建立 LLM 蒸馏全景 | [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116)，首发 2024-02-20 | 理解知识提取、蒸馏算法、能力与应用领域，适合作为近期 MOPD 的背景。 |
| 比较白盒、黑盒与评估 | [Survey on Knowledge Distillation for Large Language Models: Methods, Evaluation, and Application](https://arxiv.org/abs/2407.01885)，2024-07-02 | 第 3.1–3.6 节比较不同教师访问条件及鲁棒性评估。 |
| 研究蒸馏数据如何构造 | [Knowledge Distillation and Dataset Distillation of Large Language Models](https://arxiv.org/abs/2504.14772)，v2 为 2026-01-03，首发 2025-04-20 | Multi-Teacher KD 小节与第 4–5 节，适合连接多教师信号、数据集压缩和合成数据。 |
| 补齐经典概念 | [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525)，首发 2020-06-09 | 响应、特征、关系知识，以及不同蒸馏训练方案。 |

另有 [NAACL 2025 的语言模型蒸馏教程](https://aclanthology.org/2025.naacl-tutorial.4/)，包含多教师与自蒸馏，适合教学入门；目录中将其标为 tutorial。

## 推荐阅读顺序与使用边界

建议先读 OPD Survey 的第 6 节，再读通用 KD 综述的第 4.3 节，最后读统计综述的第 4.1 节：先了解当前能力整合问题，再追溯聚合方法，最后检查理论假设。Echoes of the Oracle 可以作为另一种 OPD 分类视角对照阅读。

使用综述整理仓库时，仍需逐篇检查训练状态由谁产生、教师是否独立、教师信号如何更新学生。综述中的“多教师”可能包含静态视觉数据方法、合成教师变体或更宽泛的整合流程，不能仅凭章节归属就认定为严格 MOPD。

OPD Survey v5 标注为 *Work in Progress*；Echoes of the Oracle 目前核实到作者的 ResearchGate 上传版本，未核实到正式发表信息。上表区分了版本更新日期和首次公开日期，引用时应记录实际阅读版本。

更多信息见[完整综述目录](../papers/reviews-tutorials.md)、[方法论文阅读路线](reading-order.md)和[10 月 23 日更新记录](update-2026-10-23.md)。
