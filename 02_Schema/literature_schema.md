---
type: schema_definition
schema_version: 1.0
namespace: literature
created: 2026-04-22
tags:
- type/schema
- schema/literature
---

# Literature Zettelkasten · FM Schema 权威定义

> 跟 `@D:\CcVault\02_Schema\03_frontmatter_schema.md` (法规 schema) 并列。
> 本文件定义 `01_Wiki/literature/` 下 3 类 note 的 FM 字段规范。

---

## 1. Literature Note (LN) · `papers/<paper_id>.md`

**目的**：一篇学术文献的**资料层笔记**。记录元数据 + 全文可检索 + 图表保留。
**不做**：深度提炼、批判、关联网络（那是 PN 的工作）。

### FM Schema

```yaml
---
# === 主键 / 必填 ===
type: literature                      # 固定值
paper_id: Yang2023_HBM_thorax         # 主键：<FirstAuthorLastName><Year>_<TopicKeyword>，唯一
authors:                              # 所有作者，按顺序
  - Yang, J.
  - Zhang, X.
  - Li, M.
year: 2023                            # 出版年
title: >-
  Thorax injury prediction using subject-specific THUMS
  under oblique 25-degree frontal impact

# === 出版信息 ===
journal: Journal of Biomechanics      # 或 conference name
volume: 145
issue: 3
pages: 110234
doi: 10.1016/j.jbiomech.2023.110234   # 稳定定位，最好有
pmid: null                            # 医学文献才有
arxiv: null                           # 预印本才有
publisher: Elsevier
language: en                          # en / zh / de / ...

# === 研究性质 ===
paper_type: research_article          # research_article / review / case_study / proceedings / thesis / textbook
methodology:                          # 多选
  - FE_simulation                     # 有限元仿真
  - physical_test                     # 物理实验
  - literature_review                 # 文献综述
  - cohort_study                      # 队列研究
  - ML_model                          # 机器学习
  - theoretical                       # 理论推导
subjects:                             # 研究对象，多选
  - HBM                               # human body model
  - thorax
  - rib_fracture
  - adult_male_50th

# === 摘要 / 关键词 ===
abstract: >-
  We developed a subject-specific thorax FE model based on THUMS AM50...
  (DeepSeek 从 MinerU full.md 抽取)
keywords:                             # 作者给的关键词
  - THUMS
  - thorax biomechanics
  - FE simulation
  - rib fracture prediction

# === Taxonomy（我们自己分的）===
topic: hbm_thorax_injury              # 粗分类（见下）
tags:
  - literature/hbm
  - literature/injury_criterion
  - reviewed/2026-04-22

# === 跨链接 ===
related_regs:                         # 文献引用/评价了哪些法规（自动扫 body 填）
  - "[[ECE R94]]"
  - "[[FMVSS 208]]"
  - "[[GB 20071-2006]]"

cites: []                             # 本文引用的其他文献（paper_id），手工或工具填
cited_by: []                          # 哪些别的文献引了本文（自动反向填）

permanent_notes: []                   # 本文派生出的 PN 列表（手工 append）

# === 来源与存档 ===
pdf_path: D:\Literature_Inbox\Yang2023.pdf
_mineru_content_hash: abc123...
_mineru_outputs_dir: outputs/abc123
_mineru_merged_at: '2026-04-22'

# === 状态追踪 ===
reading_status: to_read               # to_read / reading / read / skimmed
my_rating: null                       # null / 1-5 (我自己评分)
importance: high                      # high / medium / low (对我的研究)
notes_progress: 0                     # 已从本文派生的 PN 数量
---
```

### Body 结构（自动生成 + 人工补充）

```markdown
## 元信息
- DOI: [10.1016/j.jbiomech.2023.110234](https://doi.org/...)
- 作者: Yang, J.; Zhang, X.; Li, M.
- 出版: Journal of Biomechanics, 2023
- PDF: `@D:\Literature_Inbox\Yang2023.pdf`

## 摘要
（LLM 抽取）

## 我的阅读笔记
（人工写，初读时的 fleeting thoughts）
- 一句话贡献：...
- 方法新颖性：...
- 数据可信度：...
- 与我研究的关系：...

## 从本文派生的原子笔记
- [[HIC_threshold_1000]]
- [[THUMS_subject_specific_calibration]]

## 原文参考（MinerU 云解析）
（同 regulations 的 "## 原文参考" 节，表格/公式/图像）
```

### paper_id 生成规则

`<FirstAuthorLastName><Year>_<TopicKeyword>`

例子：
- `Yang2023_HBM_thorax`
- `Kleiven2007_brain_injury`
- `Li2020_pedestrian_lower_limb`

同年同一作者多篇：加后缀 `a/b/c`（如 `Yang2023a_HBM`, `Yang2023b_pelvis`）。

---

## 2. Permanent Note (PN) · `concepts/<concept_id>.md`

**目的**：一条可独立引用的**原子性主张/方法/数据**。
Zettelkasten 的**最小知识单元**。
**人在其中不可或缺**——LLM 只能辅助写初稿。

### FM Schema

```yaml
---
# === 主键 / 必填 ===
type: concept                         # 固定值
concept_id: HIC_threshold_1000        # 主键：snake_case，概括性
category: injury_criterion            # 分类（见下）

# === 核心内容（最重要的字段）===
claim: >-
  HIC 值 ≥ 1000 对应 AIS≥3 头部损伤概率约 16%，
  这是当前多数主动安全法规的设计阈值。
# 一句话主张。不能太长，不能含"我认为"，必须是可证伪的陈述。

# === 来源 ===
sources:                              # 本概念从哪些文献提炼而来
  - "[[Yang2023_HBM_thorax]]"
  - "[[Kleiven2007_brain_injury]]"
  - "[[Prasad1985_HIC_derivation]]"
# 至少 1 个。没有 sources 的 PN 就是 fleeting thought，不能进 concepts/

# === 关联 ===
related_concepts:                     # 概念间网络
  - "[[HIC_criterion]]"
  - "[[head_acceleration]]"
  - "[[skull_fracture_threshold]]"
related_regs:                         # 该概念被哪些法规采纳/验证
  - "[[ECE R94]]"
  - "[[FMVSS 208]]"
opposing_concepts: []                 # 挑战本主张的概念（争议追踪）
supports_concepts: []                 # 支持本主张的其他概念

# === 状态 ===
status: established                   # established / debated / emerging / deprecated
# - established: 学界共识
# - debated: 有争议
# - emerging: 新兴但证据尚少
# - deprecated: 已被更新的证据驳斥

evidence_strength: high               # high / medium / low
# 当 sources 有多篇独立研究相互印证 → high
# 单篇结论或推测 → low

tags:
  - concept/injury_criterion
  - domain/biomechanics

# === 维护 ===
created: 2026-04-25
last_reviewed: 2026-04-25
author: me                            # 通常是自己，LLM 辅助时标 "llm_assisted"
---
```

### category 候选（按需扩展）

```
injury_criterion          损伤准则（HIC, chest deflection, ...）
test_methodology          试验方法
fe_model                  有限元模型
experimental_protocol     实验方案
regulatory_interpretation 法规解读
theoretical_framework     理论框架
data_point                关键数据点（阈值、系数）
controversy               学术争议
historical_fact           历史事实
```

### Body 结构

```markdown
# <concept_id>

## 主张
（= FM 的 claim 字段，展开阐述）

## 证据
- [[Yang2023_HBM_thorax]]：在 25° 斜撞工况下复现 HIC = 987，与预测 16% 风险一致
- [[Kleiven2007_brain_injury]]：提出 BrIC 作为 HIC 替代品，但承认 HIC 在头部碰撞场景下仍有效

## 反对证据 / 局限
（如果 status = debated/controversial）
- HIC 对非线性加速度不敏感
- [[Takhounts2013]] 证明旋转加速度主导弥漫性轴突损伤

## 我的思考
（此条对我的研究意味着什么？）
- ...
- ...

## 引用到的法规
- [[ECE R94]] Annex 4 使用 HIC ≥ 1000 作为刚性墙全宽碰撞 Pass/Fail 判据
- [[FMVSS 208]] §571.208 S6.3 同样阈值
```

---

## 3. MOC (Map of Content) · `mocs/MOC_<topic>.md`

**目的**：在 concepts/ 累积到一定密度后，绘制**主题地图**。
**触发条件**：某主题 ≥ 10 条相关 PN。

### FM Schema

```yaml
---
type: moc
moc_id: MOC_HBM_evolution
title: 人体模型 (HBM) 在车辆碰撞仿真中的演化
topic: hbm                            # 粗粒度主题
covered_papers: 12                    # 本 MOC 串联的文献数
covered_concepts: 23                  # 本 MOC 串联的 PN 数
last_updated: 2026-06-01
created: 2026-05-15
tags:
  - moc
  - topic/hbm
  - topic/biomechanics
---
```

### Body 结构（自由度最高）

你想怎么写怎么写，常见模式：
- 时间线（按年份列举 PN）
- 概念分类树
- 争议对比表
- 方法学谱系
- 你自己的 synthesis

---

## 命名冲突避免

- LN paper_id：`Author + Year + Topic`（唯一，永不重名）
- PN concept_id：snake_case（如 `rib_fracture_threshold_50pct`）
- MOC moc_id：`MOC_<snake_case>`（前缀区分）

不同层之间的文件名不会冲突（papers/Yang2023 vs concepts/HIC）。

---

## 与 regulations/ schema 的关系

| 字段 | regulations | literature |
|---|---|---|
| 主键 | `reg_id` | `paper_id`（LN） / `concept_id`（PN） |
| 跨链接 | `supersedes/equivalent_to` | `sources/cites/related_regs` |
| 状态 | `active/superseded/...` | `established/debated/emerging/...` |
| 置信度 | `cross_check_overall_confidence` | `evidence_strength` |

两者共享的是**主题 taxonomy**：`topic` 字段使用相同的 37 个主题分类（或新增文献专属）。

---

## 版本记录

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-22 | 初版 |

## 相关文档

- `@D:\CcVault\01_Wiki\literature\README.md` — namespace 概览
- `@D:\CcVault\02_Schema\templates\literature_note.md` — LN 模板（Alt+N 可插）
- `@D:\CcVault\02_Schema\templates\concept_note.md` — PN 模板
- `@D:\CcVault\02_Schema\templates\moc_note.md` — MOC 模板
