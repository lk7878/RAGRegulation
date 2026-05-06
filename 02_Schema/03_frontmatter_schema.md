---
type: type/schema
title: Frontmatter Schema (8 种节点类型)
version: 0.1
---

# 03 · Frontmatter Schema

> 每种 note 类型的 YAML frontmatter 完整定义。字段列表 + 类型 + 必填/可选 + 示例。

---

## 0. 通用约定

### 所有节点共有字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | string (enum) | ✅ | `type/regulation` / `type/version` 等，参见 02_taxonomy |
| `title` | string | ✅ | 中文标题，不含标准号前缀 |
| `confidence` | enum `high/medium/low` | ✅ | 整体置信度 |
| `extracted_by` | string | ✅ | 抽取模型如 `deepseek-v3` |
| `verified_by` | string | 可选 | 审校模型如 `sonnet-4.6` |
| `tags` | list\<string\> | ✅ | 四维度 tag 组合 |

### 字段级置信度

所有**可能有风险**的字段都有同名 `_conf` 后缀：

```yaml
publication_date: 2019-05-10
publication_date_conf: high
```

如果 `_conf: low`，必须配 `_reason: <说明>`。

### 日期格式

统一 ISO 8601 `YYYY-MM-DD`。缺日补 `01`，缺月补 `-01-01`：
- 原文 "2019 年" → `2019-01-01`，`_conf: medium`，`_reason: "原文仅精确到年"`
- 原文 "2019 年 5 月" → `2019-05-01`，`_conf: medium`

### 引用关系

wikilink 写法 `"[[GB 4785-2019]]"`（带引号，避免 YAML 解析冲突）。

---

## 1. `type/regulation` · 主条目

**用途**：一份法规的"名片"，不含版本技术细节。是 Obsidian 默认 wikilink 目标。

### 字段

| 字段 | 类型 | 必填 | 说明 | 示例 |
|---|---|---|---|---|
| `type` | enum | ✅ | `type/regulation` | `type/regulation` |
| `reg_id` | string | ✅ | 标准号（无版本后缀） | `GB 4785` |
| `title` | string | ✅ | 完整中文标题 | `机动车及挂车外部照明和光信号装置的安装规定` |
| `title_short` | string | 可选 | 简称用于 wikilink | `外部照明安装规定` |
| `region` | enum | ✅ | 地区 | `cn` |
| `standard_body` | string | ✅ | 归口单位 | `SAC/TC 114` |
| `category` | enum | ✅ | `mandatory`/`recommended`/`draft` | `mandatory` |
| `latest_version` | wikilink | ✅ | 指向最新 active 版本 | `"[[GB 4785-2019]]"` |
| `all_versions` | list\<wikilink\> | ✅ | 所有版本（含已废止） | `["[[GB 4785-1998]]", "[[GB 4785-2007]]", "[[GB 4785-2019]]"]` |
| `all_amendments` | list\<wikilink\> | 可选 | 所有修改单 | `["[[GB 4785-2007 修改单-1]]"]` |
| `equivalent_to` | list\<object\> | 可选 | 跨区等效关系 | 见下方 |
| `vehicle_classes` | list\<enum\> | ✅ | 适用车型 | `[M1, M2, M3, N1]` |
| `topics` | list\<tag\> | ✅ | 主题 | `[topic/lighting]` |
| `source_pdf` | null | — | 主条目无 PDF | `null` |

### `equivalent_to` 对象 schema

```yaml
equivalent_to:
  - ref: ECE R48
    version: "06 Suppl.8"
    relation: modified       # identical/modified/partial/topic-equivalent/non-equivalent
    confidence: high
    evidence: "原文 '修改采用 ECE R48-06 增补系列 08'"
```

### 完整示例

```yaml
---
type: type/regulation
reg_id: GB 4785
title: 机动车及挂车外部照明和光信号装置的安装规定
title_short: 外部照明安装规定
region: cn
standard_body: SAC/TC 114
standard_body_conf: high
category: mandatory
latest_version: "[[GB 4785-2019]]"
all_versions:
  - "[[GB 4785-1998]]"
  - "[[GB 4785-2007]]"
  - "[[GB 4785-2019]]"
all_amendments:
  - "[[GB 4785-2007 修改单-1]]"
  - "[[GB 4785-2007 修改单-2]]"
equivalent_to:
  - ref: ECE R48
    version: "06 Suppl.8"
    relation: modified
    confidence: high
vehicle_classes: [M1, M2, M3, N1, N2, N3, O]
topics:
  - topic/lighting
confidence: high
extracted_by: deepseek-v3
verified_by: sonnet-4.6
tags:
  - type/regulation
  - status/verified
  - reg/cn
  - topic/lighting
  - veh/M1
  - veh/M2
  - veh/M3
  - veh/N1
  - veh/N2
  - veh/N3
  - veh/O
---
```

---

## 2. `type/version` · 版本页

**用途**：某版本的完整技术内容。和具体 PDF 一对一。

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/version` |
| `reg_id` | string | ✅ | 含版本号 `GB 4785-2019` |
| `parent_regulation` | wikilink | ✅ | 指向主条目 |
| `title` | string | ✅ | 本版本标题（可能含修订说明） |
| `region` | enum | ✅ | |
| `publication_date` | date | ✅ | 发布日 |
| `implementation_date_new_vehicle` | date | ✅ | 新车生效 |
| `implementation_date_in_use` | date | 可选 | 在用车生效 |
| `withdrawn_date` | date \| null | ✅ | 废止日（null = 现行） |
| `status` | enum | ✅ | `draft/active/superseded/withdrawn/under_revision` |
| `supersedes` | wikilink \| null | 可选 | 替代的旧版本 |
| `superseded_by` | wikilink \| null | 可选 | 被哪个新版本替代 |
| `equivalent_to` | list\<object\> | 可选 | 跨区等效关系（精确到版本） |
| `amendments_applied` | list\<wikilink\> | 可选 | 累加的修改单 |
| `vehicle_classes` | list\<enum\> | ✅ | |
| `topics` | list\<tag\> | ✅ | |
| `source_pdf` | path | ✅ | PDF 绝对路径 |
| `source_lang` | list\<enum\> | ✅ | `[zh]` / `[en]` / `[zh, en]` |
| `page_count` | int | 可选 | PDF 页数 |

### 正文结构（Markdown body）

```markdown
## 适用范围
## 规范性引用文件
## 术语和定义
## 技术要求
  (逐条列出，每条附 confidence)
## 试验方法
## 附录（如有）
```

### 完整示例

```yaml
---
type: type/version
reg_id: GB 4785-2019
parent_regulation: "[[GB 4785 外部照明安装规定]]"
title: 机动车及挂车外部照明和光信号装置的安装规定
region: cn
publication_date: 2019-05-10
publication_date_conf: high
implementation_date_new_vehicle: 2020-01-01
implementation_date_new_vehicle_conf: high
implementation_date_in_use: 2022-01-01
implementation_date_in_use_conf: high
withdrawn_date: null
status: active
supersedes: "[[GB 4785-2007]]"
superseded_by: null
equivalent_to:
  - ref: ECE R48
    version: "06 Suppl.8"
    relation: modified
    confidence: high
amendments_applied: []
vehicle_classes: [M1, M2, M3, N1, N2, N3, O]
topics:
  - topic/lighting/headlamp
  - topic/lighting/position-lamp
  - topic/lighting/signal-lamp
confidence: high
source_pdf: "D:/CcVault/00_Raw/标准库/国内法规/国内标准/GB 4785-2019.pdf"
source_lang: [zh]
page_count: 45
extracted_by: deepseek-v3
verified_by: sonnet-4.6
tags:
  - type/version
  - status/verified
  - reg/cn
  - topic/lighting
  - veh/M1
---
```

---

## 3. `type/amendment` · 修改单

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/amendment` |
| `amendment_id` | string | ✅ | 如 `GB 4785-2007 修改单-1` |
| `parent_version` | wikilink | ✅ | 修改的版本 |
| `amendment_number` | int | ✅ | 第几号 |
| `publication_date` | date | ✅ | |
| `implementation_date` | date | ✅ | |
| `scope` | enum | ✅ | `full-withdrawal/transitional-coexistence/partial-replacement` |
| `modified_clauses` | list\<string\> | ✅ | 被改的条款号列表 |
| `source_pdf` | path | ✅ | |

### 示例

```yaml
---
type: type/amendment
amendment_id: GB 4785-2007 修改单-1
parent_version: "[[GB 4785-2007]]"
amendment_number: 1
publication_date: 2012-03-15
implementation_date: 2013-01-01
scope: partial-replacement
modified_clauses: ["4.3.1", "5.2", "附录 A.2"]
confidence: high
source_pdf: "D:/.../GB 4785-2007 第1号修改单.pdf"
source_lang: [zh]
extracted_by: deepseek-v3
tags:
  - type/amendment
  - status/verified
  - reg/cn
  - topic/lighting
---
```

---

## 4. `type/test-method` · 试验方法

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/test-method` |
| `method_id` | string | ✅ | 规范化 ID 如 `test/mdb-side-impact` |
| `title` | string | ✅ | 中文名 |
| `title_en` | string | 可选 | 英文名 |
| `category` | enum | ✅ | `dynamic-impact/static/mechanical/environmental/emc/electrical` |
| `equipment` | list\<string\> | 可选 | 所需设备 |
| `dummies_used` | list\<wikilink\> | 可选 | 所用假人 |
| `injury_metrics_measured` | list\<wikilink\> | 可选 | 测量的损伤指标 |
| `used_by_regulations` | list\<wikilink\> | ✅ | 引用此方法的法规 |
| `parameters` | dict | 可选 | 关键参数（速度、角度等） |

### 示例

```yaml
---
type: type/test-method
method_id: test/mdb-side-impact
title: 移动可变形壁障侧面碰撞试验
title_en: MDB Side Impact Test
category: dynamic-impact
equipment:
  - AE-MDB 壁障
  - 试验台车
dummies_used:
  - "[[WorldSID 50th]]"
injury_metrics_measured:
  - "[[HIC36]]"
  - "[[胸部侧向压缩量]]"
used_by_regulations:
  - "[[GB 20071-2006]]"
  - "[[ECE R95]]"
parameters:
  impact_speed_kmh: 50
  impact_angle_deg: 90
confidence: high
extracted_by: opus-4.7
tags:
  - type/test-method
  - topic/passive-safety/side-impact
---
```

---

## 5. `type/dummy` · 假人

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/dummy` |
| `dummy_id` | string | ✅ | 规范化 ID `dummy/hybrid-iii-50th` |
| `family` | enum | ✅ | `Hybrid III/Hybrid II/Q/WorldSID/THOR/ES-2/EuroSID/BioRID` |
| `percentile` | enum | ✅ | `5th/50th/95th/child` |
| `child_age_months` | int | 可选 | 如是儿童假人 |
| `used_in_methods` | list\<wikilink\> | ✅ | |
| `injury_metrics_supported` | list\<wikilink\> | ✅ | |
| `biofidelity_refs` | list\<string\> | 可选 | 生物保真度论文 DOI（Phase 2 接入） |

### 示例

```yaml
---
type: type/dummy
dummy_id: dummy/hybrid-iii-50th
family: Hybrid III
percentile: 50th
used_in_methods:
  - "[[test/frontal-impact-rigid-barrier]]"
injury_metrics_supported:
  - "[[HIC15]]"
  - "[[胸部压缩量]]"
  - "[[股骨载荷]]"
biofidelity_refs: []
confidence: high
tags:
  - type/dummy
  - topic/passive-safety/frontal-impact
---
```

---

## 6. `type/injury-metric` · 损伤指标

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/injury-metric` |
| `metric_id` | string | ✅ | 如 `metric/hic15` |
| `title` | string | ✅ | 中文全称 |
| `title_en` | string | ✅ | 英文全称 |
| `abbreviation` | string | ✅ | 缩写 |
| `body_region` | enum | ✅ | `head/neck/chest/abdomen/pelvis/femur/tibia/lower-leg/upper-leg/全身` |
| `formula` | string | 可选 | LaTeX 公式 |
| `used_by_regulations` | list\<wikilink\> | ✅ | |
| `biomechanics_refs` | list\<string\> | 可选 | Phase 2 接入 |

### 示例

```yaml
---
type: type/injury-metric
metric_id: metric/hic15
title: 15 毫秒头部伤害指数
title_en: Head Injury Criterion (15 ms window)
abbreviation: HIC15
body_region: head
formula: "HIC = max{ (t2-t1) * [ 1/(t2-t1) ∫ a(t) dt ]^2.5 }, t2-t1 ≤ 15 ms"
used_by_regulations:
  - "[[GB 11551-2014]]"
  - "[[ECE R94]]"
  - "[[FMVSS 208]]"
biomechanics_refs: []
confidence: high
tags:
  - type/injury-metric
  - topic/passive-safety
---
```

---

## 7. `type/vehicle-class` · 车型分类

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/vehicle-class` |
| `class_id` | string | ✅ | `M1`/`N2`/... |
| `description_zh` | string | ✅ | 中文定义 |
| `description_en` | string | 可选 | 英文定义 |
| `max_mass_kg` | int \| null | 可选 | 上限质量 |
| `max_seats` | int \| null | 可选 | 上限座位数 |
| `equivalent_classes` | dict | 可选 | 跨体系对应 |

### 示例

```yaml
---
type: type/vehicle-class
class_id: M1
description_zh: 除驾驶员外座位数不多于 8 座的载客汽车
description_en: Vehicles used for the carriage of passengers and comprising no more than eight seats in addition to the driver's seat
max_seats: 9
equivalent_classes:
  us_fmvss: PC (Passenger Car)
  cn_gb: 乘用车
confidence: high
tags:
  - type/vehicle-class
---
```

---

## 8. `type/topic` · 主题聚合

### 字段

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | ✅ | `type/topic` |
| `topic_id` | tag | ✅ | 如 `topic/passive-safety/frontal-impact` |
| `title` | string | ✅ | 中文主题名 |
| `title_en` | string | 可选 | 英文 |
| `summary_length_words` | int | ✅ | 综述字数（由 Sonnet 填） |
| `related_regulations_count` | int | ✅ | dataview 自动计算 |
| `generated_at` | datetime | ✅ | 综述生成时间 |
| `generated_by` | string | ✅ | `sonnet-4.6` 或 `opus-4.7` |

### 正文结构

```markdown
# 主题名

## 1. 主题定义
## 2. 全球监管格局
## 3. 关键技术指标对比
## 4. 演进趋势
## 5. 关联法规（dataview）
## 6. （Phase 3）社区摘要（Opus）
```

### 示例

```yaml
---
type: type/topic
topic_id: topic/passive-safety/frontal-impact
title: 正面碰撞
title_en: Frontal Impact
summary_length_words: 1200
related_regulations_count: 15
generated_at: 2026-04-17T14:30:00+08:00
generated_by: sonnet-4.6
confidence: high
tags:
  - type/topic
  - topic/passive-safety/frontal-impact
---
```

---

## 9. 字段优先级 vs 成本

### 必须完美的字段（防线 2 重点核对）
- `reg_id` / `title` / `region`
- 所有日期字段
- `equivalent_to`
- `vehicle_classes`

### 可以容忍 medium 的字段
- `standard_body`
- `topics` 的第 3-4 级
- `source_lang`

### 允许 low（不阻塞）的字段
- `page_count`
- `title_short`（没有就用全名）
- `biofidelity_refs` / `biomechanics_refs`（Phase 2 再补）
