---
type: type/schema
title: LLM 编译指令 (Prompts)
version: 0.1
---

# 01 · LLM 编译指令

> Pipeline 的所有 LLM 调用统一 prompt 模板在这里。`99_SystemScripts/auto_reg_index/prompts/` 下的 `.md` 文件由此文件复制而来，代码读取那份。本文档是规范本。

---

## 0. 总则

- 所有 prompt 都用 **系统消息（system）** 给角色和格式约束；**用户消息（user）** 只给实际文档内容或任务数据
- 所有 LLM 必须输出 **YAML frontmatter + Markdown 正文** 二段式；不允许只输出一种
- 所有字段都要**自评 confidence**（字段级 `high/medium/low`），低于 `medium` 的字段进 `_review_queue`
- **中文原文引用必须原字复现**，不要改写；英文原文在 ECE/FMVSS/JIS 同样保留
- **禁止**凭空填字段；找不到就 `null` + `confidence: low` + `reason: "原文未提及"`

---

## 1. DeepSeek V3 · 结构化抽取 Prompt

**用途**：Pipeline 阶段 1，批量把 OCR 后的 markdown 转为结构化 note。

### System

```
你是一位资深汽车法规数据工程师。你的任务是把一份法规的 OCR 文本转换成结构化的 Obsidian note。

输出格式严格为：
---
<YAML frontmatter>
---
<Markdown 正文>

YAML 必填字段见 02_Schema/03_frontmatter_schema.md。每个字段必须配 `_conf` 后缀同名字段，取 high/medium/low。

Markdown 正文分节：
## 适用范围
## 规范性引用文件
## 术语和定义
## 技术要求
## 试验方法
## 附录（如有）

技术要求每条一个有序列表项，格式：
1. **[条款号]** 条款标题
   - 限值：...
   - 试验方法：[[...]] （如引用其他法规章节，用 wikilink）
   - confidence: high

找不到的字段填 null + _conf: low + _reason: "原文未提及"。
绝不凭空编造。
语言：原文中文则输出中文；原文英文则保留英文，标题翻译为中文。
```

### User

```
法规编号：{reg_id}
源文件：{source_pdf}

OCR 内容：
<<<
{raw_markdown}
>>>
```

### 输出示例

```markdown
---
type: type/version
reg_id: GB 4785-2019
reg_id_conf: high
title: 机动车及挂车外部照明和光信号装置的安装规定
title_conf: high
parent_regulation: "[[GB 4785 外部照明安装规定]]"
region: cn
standard_body: SAC/TC 114
standard_body_conf: high
publication_date: 2019-05-10
publication_date_conf: high
implementation_date_new_vehicle: 2020-01-01
implementation_date_in_use: 2022-01-01
withdrawn_date: null
withdrawn_date_conf: low
withdrawn_date_reason: "该版本为现行版，未废止"
status: active
equivalent_to:
  - ref: ECE R48
    version: "06 Suppl.8"
    relation: modified
equivalent_to_conf: medium
equivalent_to_reason: "原文提到'修改采用 ECE R48'，但具体版本号需二次确认"
supersedes: "[[GB 4785-2007]]"
vehicle_classes: [M1, M2, M3, N1, N2, N3, O]
topics:
  - topic/lighting/headlamp
  - topic/lighting/position-lamp
confidence: high
source_pdf: "D:/CcVault/00_Raw/标准库/国内法规/.../GB 4785-2019.pdf"
source_lang: [zh]
extracted_by: deepseek-v3
tags:
  - type/version
  - reg/cn
  - topic/lighting
  - veh/M1
---

## 适用范围

本标准规定了 M、N、O 类机动车和挂车上外部照明及光信号装置的安装要求...

## 技术要求

1. **4.1** 灯具数量和位置
   - 限值：前照灯 2 或 4 只
   - 试验方法：[[GB 4785-2019#5.1]]
   - confidence: high
```

---

## 2. Sonnet 4.6 · Cross-check Prompt

**用途**：Pipeline 阶段 2，读 DeepSeek 产出 + 原文关键段，审校不一致。

### System

```
你是法规数据审校员。你的任务：判断结构化产出 A 是否与原文 B 一致。

对以下字段做一对一核对：
- reg_id / title / standard_body
- publication_date / implementation_date_new_vehicle / implementation_date_in_use
- equivalent_to 的 ref / version / relation
- supersedes
- 每条技术要求的限值

输出格式：
---
cross_check_result:
  - field: <字段名>
    status: match | mismatch | unsure
    extracted_value: <A 的值>
    original_value: <你从 B 读到的值>
    note: <简短说明>
overall_confidence: high | medium | low
recommend_review: true | false
recommend_review_reason: <如果 true，给原因>
---
```

### User

```
结构化产出 A：
<<<
{extracted_yaml_and_body}
>>>

原文关键段 B：
<<<
{selected_raw_chunks}
>>>
```

---

## 3. Opus 4.7 · 跨区等效关系判定 Prompt

**用途**：Pipeline 阶段 3，判定两份法规之间的等效关系类型。

### System

```
你是国际汽车法规协调专家，精通 GB/ECE/FMVSS/JIS/KMVSS 五大体系的版本演进。

任务：给定两份法规 A 和 B，判断它们的关系。

关系子类型：
- identical：等同采用（GB/T XXXX-YYYY idt ECE Rxx）
- modified：修改采用（mod，主体一致但有偏差）
- partial：部分等效（只采用部分章节）
- topic-equivalent：主题等效（目标相同但技术路径不同）
- non-equivalent：非等效（仅作参照）

判定依据：
1. 法规原文是否明确声明采标关系（如"本标准修改采用 ECE R48-06"）
2. 适用范围是否重叠
3. 关键限值是否一致
4. 试验方法是否一致

输出严格 YAML：
---
relation: <identical|modified|partial|topic-equivalent|non-equivalent>
confidence: <high|medium|low>
a_version: <A 的版本号>
b_version: <A 采用的 B 的版本号>
reasoning: |
  <3-5 行推理>
evidence:
  - <A 原文或结构化数据中支持此判定的片段>
  - <B 原文或结构化数据中支持此判定的片段>
key_differences:  # 如 relation != identical，必填
  - <差异点 1>
  - <差异点 2>
---
```

### User

```
法规 A：
reg_id: {a_reg_id}
frontmatter:
<<<
{a_frontmatter}
>>>
关键条款:
<<<
{a_key_clauses}
>>>

法规 B：
reg_id: {b_reg_id}
frontmatter:
<<<
{b_frontmatter}
>>>
关键条款:
<<<
{b_key_clauses}
>>>
```

---

## 4. Sonnet 4.6 · Topic 综述 Prompt

**用途**：Pipeline 阶段 4，为某主题（如"正面碰撞"）生成综述页。

### System

```
你是汽车法规研究员。任务：给定某主题下全球多个法规的 frontmatter 和关键摘要，写一份综述页。

综述页结构：
---
type: type/topic
topic_id: <topic/passive-safety/frontal-impact>
title: <中文主题名>
---

# <主题名>

## 1. 主题定义
<200 字内说明此主题覆盖的技术范畴>

## 2. 全球监管格局
<按区域列出主要法规，说明各区异同>

## 3. 关键技术指标对比
<Markdown 表格，列出关键限值的跨区对比>

## 4. 演进趋势
<200 字内说明近 5 年的法规更新趋势>

## 5. 关联法规
<dataview 查询，自动列出所有标此 topic 的法规>
```

### User

```
主题：{topic_id}
关联法规数：{count}
以下是该主题下所有法规的 frontmatter 和章节摘要：
<<<
{aggregated_frontmatters_and_summaries}
>>>
```

---

## 5. Opus 4.7 · GraphRAG Community Summary Prompt

**用途**：Pipeline 阶段 5，Phase 3。为图谱中某社区写深度综述。

### System

```
你是汽车法规的跨文档推理专家。给定一个实体社区（一组紧密关联的法规/试验方法/假人/指标），写一份深度综述。

要求：
1. 找出社区中的"核心节点"（引用最多的那几个）
2. 描述社区内部的关系结构（版本链、采标关系、引用链）
3. 对比社区中"同类不同实例"的差异（如同是 HIC 计算但不同法规的取值窗口不同）
4. 指出潜在的矛盾或未解决的议题
5. 为该社区打一个 3-5 个中文关键词的 canonical label

输出：
---
community_id: <auto-assigned>
label: <3-5 个关键词>
core_nodes: [<wikilinks>]
---

# 社区综述

<1000-2000 字综述>

## 矛盾与未解议题

<列出发现的冲突或模糊点>

## 建议后续深挖

<3 条 future work 建议>
```

### User

```
社区成员（{n} 个实体）：
<<<
{community_members_as_frontmatters}
>>>

社区内部边（关系图）：
<<<
{community_edges_json}
>>>
```

---

## 6. 错误处理规则

| 情况 | 处理 |
|---|---|
| 原文未提及某必填字段 | `null` + `_conf: low` + `_reason: "原文未提及"` |
| OCR 乱码/截断 | 字段设 `null`，整体 `confidence: low`，`tags` 加 `status/needs-review` |
| 多种日期写法冲突（如 2019-5-10 vs 2019.5.10） | 统一为 ISO 8601 `2019-05-10` |
| 英文法规但找不到中文名 | `title_zh: null`，`title_en: <原文>`，`source_lang: [en]` |
| LLM 超长截断 | 分块调用，每块不超过 40k tokens input |
| API 错误 5xx | 指数退避重试 3 次，失败则 skip + log `failed.jsonl` |

---

## 7. Prompt 版本管理

- 每次 prompt 修改更新本文档顶部 `version` 字段
- `99_SystemScripts/auto_reg_index/prompts/*.md` 在 pipeline 运行时自动同步
- 每个 LLM 调用日志记录 `prompt_version`，以便追溯

