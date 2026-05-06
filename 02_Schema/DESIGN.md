---
type: type/design-doc
title: CcVault 设计文档
version: 0.1
created: 2026-04-17
status: draft
---

# CcVault 设计文档

> **读完这份 = 理解整个项目**。约 15 分钟。
>
> 本文档的每条决策标注了 `[FIXED]`（已定，访谈阶段敲定）或 `[DEFAULT]`（默认值，可改）。你看完后可以直接告诉我哪条要改。

---

## 目录

0. [一句话摘要](#0-一句话摘要)
1. [项目定位](#1-项目定位)
2. [全部决策总表](#2-全部决策总表)
3. [架构总览](#3-架构总览)
4. [Schema 体系](#4-schema-体系)
5. [Pipeline 六阶段](#5-pipeline-六阶段)
6. [模型分工与成本](#6-模型分工与成本)
7. [时间线](#7-时间线)
8. [默认处理（A/B/C/D）](#8-默认处理abcd)
9. [验收标准](#9-验收标准)
10. [Phase 2/3 展望](#10-phase-23-展望)

---

## 0. 一句话摘要

**把 1537 份全球汽车法规源文件（1.81 GB）在 5 天内转化为一个可用 Obsidian 日常查询、可被 Smart Composer 深度问答、可被 GraphRAG 跨文档推理的结构化知识库，总预算 $94 Claude API + ¥400 DeepSeek + ¥60 OCR，约 ¥1000 人民币内。**

---

## 1. 项目定位

四个用途一体：

| 用途 | 具体表现 |
|---|---|
| **个人工具箱** | 工作时查"GB 11551-2014 HIC 限值"、"ECE R48 灯具颜色要求"秒得 |
| **论文脚手架** | 系统对比多区法规的版本演进、跨区差异、监管理念 |
| **职业竞争力** | 你是"一人移动法规局"，知识结构化到跨国车企工程师水平 |
| **持续学习** | 关系图随时间生长，Phase 2 接入损伤生物力学 / 交通伤 / IVISTA |

范围 `[FIXED]`：
- **第 1 阶段**：1537 份法规文档本身
- **第 2 阶段**：桥接损伤生物力学（THUMS/GHBMC）、交通伤数据、IVISTA 车型测评
- **第 3 阶段**：GraphRAG 图构建 + 跨文档推理

---

## 2. 全部决策总表

| # | 主题 | 决定 | 状态 |
|---|---|---|---|
| 1 | 使用场景 | 4 种通吃（工具箱 / 论文 / 职业 / 学习） | `[FIXED]` |
| 2 | 范围桥接 | Phase 2 接入损伤生物力学 / 交通伤 / IVISTA | `[FIXED]` |
| 3 | Wiki schema | 主条目 + 扁平版本页 + 修改单独立页 | `[FIXED]` |
| 4 | Graph 节点类型 | 8 类：regulation / version / amendment / test-method / dummy / injury-metric / vehicle-class / topic | `[FIXED]` |
| 5 | 源文件策略 | 只读不动；批量处理时复制 markdown 中间产物到 `.staging/` | `[FIXED]` |
| 6 | 部署 | 全云 API（本地无独显） | `[FIXED]` |
| 7 | 模型分工 | DeepSeek V3 批量 + Sonnet 4.6 审校/综述 + Opus 4.7 跨区/图谱/问答 | `[FIXED]` |
| 8 | 查询界面 | Obsidian + Smart Composer + Dataview + Templater + Omnisearch + PDF++ + Graph Analysis | `[FIXED]` |
| 9 | GraphRAG 节奏 | 三阶段渐进（骨架 → 批量 → 图谱） | `[FIXED]` |
| 10 | OCR 策略 | pdfplumber / 百度云 OCR / MinerU CPU 三层 | `[FIXED]` |
| 11 | 人工复核 | AI self-check 三道防线，不前置人工 | `[FIXED]` |
| 12 | Tag 体系 | 四维度并行（type / region / topic / vehicle-class） | `[FIXED]` |
| 13 | Phase 1 样板 | GB 4785 外部照明 + GB 11551 正面碰撞 + ECE R94 验证跨区 | `[FIXED]` |
| 14 | 机器配置 | 本地无独显，全云 API，OCR 分层兜底 | `[FIXED]` |
| 15 | 每周投入时间 | > 10 小时 | `[FIXED]` |
| 16 | 敏感文件 | 全部当正常处理 | `[FIXED]` |
| 17 | Opus 使用策略 | 仅高价值环节（跨区、GraphRAG、日常问答） | `[FIXED]` |
| 18 | Vault 位置 | `D:\CcVault`（独立 vault，和 obsidian_brain 完全隔离） | `[FIXED]` |
| 19 | 源文件处理 | 移动 `00_Raw/标准库` 到新 vault | `[FIXED]` |
| 20 | 预算 | $94 Claude + ¥400 DeepSeek + ¥60 OCR，约 ¥1000 RMB | `[FIXED]` |
| A | equivalent_to 子类型 | 5 种：identical / modified / partial / topic-equivalent / non-equivalent | `[DEFAULT]` |
| B | 文件命名 | 主条目 `GB 4785 外部照明安装规定.md`；版本 `GB 4785-2019.md`；修改单 `GB 4785-2007 修改单-1.md` | `[DEFAULT]` |
| C | 多语言 | ECE 中英配对为"同一 note 双语块"；FMVSS/JIS 不主动翻译 | `[DEFAULT]` |
| D | 批次顺序 | 国标 → ECE → 欧盟 → 各国综述 | `[DEFAULT]` |

---

## 3. 架构总览

```
┌──────────────────────────────────────────────────────────────┐
│  00_Raw/ 标准库 1537 份源文件                                 │
└────────────────────────┬─────────────────────────────────────┘
                         │
         ┌───────────────▼───────────────┐
         │    Pipeline (99_SystemScripts)│
         │                               │
         │  ┌─────────────────────────┐  │
         │  │ OCR 分层                │  │  免费 / ¥60
         │  │ pdfplumber > 百度云     │  │
         │  │ > MinerU CPU            │  │
         │  └──────────┬──────────────┘  │
         │             ▼                 │
         │  ┌─────────────────────────┐  │
         │  │ DeepSeek V3 结构化抽取  │  │  ¥300-350
         │  │ frontmatter+章节+条款   │  │
         │  └──────────┬──────────────┘  │
         │             ▼                 │
         │  ┌─────────────────────────┐  │
         │  │ Sonnet 4.6 Cross-check  │  │  $25
         │  │ (batch API)             │  │
         │  └──────────┬──────────────┘  │
         │             ▼                 │
         │  ┌─────────────────────────┐  │
         │  │ Opus 4.7 跨区+Topic+    │  │  $54
         │  │ GraphRAG (batch API)    │  │
         │  └──────────┬──────────────┘  │
         └─────────────┼─────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 01_Wiki/  结构化 notes                                        │
│                                                              │
│  regulations/    test-methods/    dummies/    injury-metrics/│
│  vehicle-classes/    topics/    _index.md    _review_queue.md│
└─────────────────────────┬────────────────────────────────────┘
                          │
         ┌────────────────▼────────────────┐
         │  Obsidian + 插件                │
         │  Dataview (聚合查询)             │
         │  Smart Composer (Opus/Sonnet 问答)│
         │  Templater (新条目模板)          │
         │  Omnisearch (全文检索)           │
         │  PDF++ (原文溯源)                │
         │  Graph Analysis (关系图谱)       │
         └─────────────────────────────────┘
```

---

## 4. Schema 体系

### 4.1 节点类型（8 类）

| 类型 | frontmatter `type` | 作用 | 示例文件 |
|---|---|---|---|
| 主条目 | `type/regulation` | 一份法规的"名片"，不含版本细节 | `GB 4785 外部照明安装规定.md` |
| 版本页 | `type/version` | 具体某版本的完整技术内容 | `GB 4785-2019.md` |
| 修改单 | `type/amendment` | 单独的修改单文件 | `GB 4785-2007 修改单-1.md` |
| 试验方法 | `type/test-method` | 可被多个法规引用的试验方法 | `MDB 可变形壁障试验.md` |
| 假人 | `type/dummy` | Phase 2 桥接损伤生物力学的关键节点 | `Hybrid III 50th.md` |
| 损伤指标 | `type/injury-metric` | 同上 | `HIC15.md` |
| 车型分类 | `type/vehicle-class` | M1/M2/M3/N1/N2/N3/L/O | `M1.md` |
| 主题聚合 | `type/topic` | 跨法规、跨区的主题综述页 | `正面碰撞.md` |

### 4.2 四维度 Tag

见 `02_Schema/02_taxonomy.md`。简要：

- `type/*`（节点类型）
- `reg/*`（地区，前 2 级固定：`reg/cn` `reg/ece` `reg/eu` …）
- `topic/*`（主题，允许 4 级：`topic/passive-safety/frontal-impact/occupant-protection/dummy-response`）
- `veh/*`（车型，固定到 `veh/M1` `veh/N2` 等）

每份法规 note 同时打 4 维度 tag，Dataview 可以按任一维度聚合。

### 4.3 Frontmatter

详见 `02_Schema/03_frontmatter_schema.md`。核心字段：

```yaml
type: type/version
reg_id: GB 4785-2019
title: 机动车及挂车外部照明和光信号装置的安装规定
parent_regulation: "[[GB 4785 外部照明安装规定]]"
region: cn
standard_body: SAC/TC 114
publication_date: 2019-05-10
implementation_date_new_vehicle: 2020-01-01
implementation_date_in_use: 2022-01-01
withdrawn_date: null
status: active
equivalent_to:
  - ref: ECE R48
    version: "06 Suppl.8"
    relation: modified    # identical/modified/partial/topic-equivalent
supersedes: "[[GB 4785-2007]]"
amendments: []
vehicle_classes: [M1, M2, M3, N1, N2, N3, O]
topics:
  - topic/lighting/headlamp
  - topic/lighting/position-lamp
confidence: high
source_pdf: "D:/CcVault/00_Raw/标准库/国内法规/.../GB 4785-2019.pdf"
source_lang: [zh]
extracted_by: deepseek-v3
verified_by: sonnet-4.6
tags:
  - type/version
  - reg/cn
  - topic/lighting
  - veh/M1
```

---

## 5. Pipeline 六阶段

### 阶段 0 · OCR 预处理

- **pdfplumber**（约 1200 份电子 PDF）：免费，一次性几十分钟
- **百度云 OCR**（约 300 份扫描件）：¥60，异步提交
- **MinerU CPU**（约 37 份复杂表格）：免费，挂机一夜

**产出**：`.staging/{reg_id}/raw.md` 每份一份 markdown

### 阶段 1 · 结构化抽取（DeepSeek V3）

- 读 `.staging/{reg_id}/raw.md` → 调 DeepSeek V3
- Prompt 见 `99_SystemScripts/auto_reg_index/prompts/extract.md`
- 输出 YAML frontmatter + 章节化正文 + 条款列表
- 并发 10 线程
- 成本：¥300-350

**产出**：`.staging/{reg_id}/extracted.md`（含 `confidence` 自评）

### 阶段 2 · Cross-check（Sonnet 4.6 via batch API）

- 读 `extracted.md` + `raw.md` 的关键段 → 调 Sonnet 审校
- 关键法规 700 份（国标 + 核心 ECE）
- 不一致字段打 `status/needs-review` tag，进 `_review_queue.md`
- 成本：$25

**产出**：`.staging/{reg_id}/verified.md`

### 阶段 3 · 跨区等效关系（Opus 4.7 via batch API）

- 500 对候选关系（GB↔ECE / GB↔FMVSS / ECE↔其他）
- Opus 判定 5 种关系子类型
- 成本：$42

**产出**：`01_Wiki/regulations/*/...md` 的 `equivalent_to` 字段填充

### 阶段 4 · Topic 综述（Sonnet 4.6 via batch API）

- 30 个主题
- Sonnet 综合同 topic 下多区法规，自动写综述
- 成本：$4

**产出**：`01_Wiki/topics/*.md`

### 阶段 5 · GraphRAG 社区摘要（Opus 4.7 via batch API）

- Phase 3 才启动。50 个实体社区。
- Opus 写深度综述。
- 成本：$8

**产出**：`01_Wiki/topics/*.md` 的 community summary 块

### 阶段 6 · 日常问答（Smart Composer + Opus/Sonnet 自动路由）

- Obsidian 里你直接提问，插件路由到 Opus（复杂）或 Sonnet（简单）
- 预留预算：$15-20 / 3 个月

---

## 6. 模型分工与成本

| 阶段 | 模型 | Token 量 | 成本 | 备注 |
|---|---|---|---|---|
| OCR | 非 LLM | — | **¥60** | 80% pdfplumber 免费 |
| 结构化抽取 | DeepSeek V3 | 80-120M | **¥300-350** | 你另买 DeepSeek API |
| Cross-check | Sonnet 4.6 batch | 15M | **$25** | 走 Claude 额度 |
| 跨区关系 | Opus 4.7 batch | 15M in + 1.5M out | **$42** | 走 Claude 额度 |
| Topic 综述 | Sonnet 4.6 batch | 3M | **$4** | 走 Claude 额度 |
| GraphRAG | Opus 4.7 batch | 2.5M | **$8** | 走 Claude 额度 |
| 日常问答 | Opus/Sonnet | — | **$15-20/3mo** | 走 Claude 额度 |
| **Claude 合计** | | | **$94** | 压你 $95 代充额度 |
| **DeepSeek 合计** | | | **¥300-350** | 另账户 |
| **OCR 合计** | | | **¥60** | 百度云 |
| **总计 RMB** | | | **≈ ¥1000** | |

---

## 7. 时间线（5 天）

| 天 | 任务 | Claude 消耗 | DeepSeek 消耗 |
|---|---|---|---|
| Day 1 | 建骨架 + 写 `ingest.py` + OCR/LLM 客户端 | $0 | $0 |
| Day 2 | 移动源文件 + OCR 全量 + GB 4785 样板跑通 | $1 | ¥20 |
| Day 3 上午 | DeepSeek 批量抽取 1537 份 | $0 | ¥300-350 |
| Day 3 下午 | Sonnet cross-check 提交 batch（12h 返回） | $25 | — |
| Day 4 上午 | cross-check 结果入库 + 抽检 20 份 | $0 | — |
| Day 4 下午 | Opus 跨区关系 + Sonnet topic 综述提交 batch | $46 | — |
| Day 5 上午 | batch 返回 + 入库 | $0 | — |
| Day 5 下午 | Phase 3 GraphRAG + Obsidian Smart Composer 集成调通 | $8 | — |
| **合计** | | **$80** | **¥320-370** |

> 剩 $15 Claude 额度留给日常问答 3 个月。

---

## 8. 默认处理（A/B/C/D）

这四类都是 `[DEFAULT]`，读到不顺眼的直接告诉我改。

### A. Schema 字段语义

- `equivalent_to` 的 5 种关系：
  - `identical`：等同采用（逐字）
  - `modified`：修改采用（有偏差但整体对齐）
  - `partial`：部分等效（只采用部分章节）
  - `topic-equivalent`：主题等效（目标相同但技术路径不同）
  - `non-equivalent`：非等效（仅作参照，不可互认）
- `supersedes` 的 3 种语义：
  - `full-withdrawal`：新版完全废止旧版
  - `transitional-coexistence`：过渡期并存
  - `partial-replacement`：只替代部分章节
- 实施日期拆 4 字段：
  - `publication_date`：发布日
  - `implementation_date_new_vehicle`：新车生效
  - `implementation_date_in_use`：在用车生效
  - `withdrawn_date`：废止日
- `status` 状态机：`draft / active / superseded / withdrawn / under_revision`

### B. 文件命名

- 主条目：`GB 4785 外部照明安装规定.md`（含标准号 + 简称，方便 wikilink 识别）
- 版本页：`GB 4785-2019.md`（扁平，不用子目录）
- 修改单：`GB 4785-2007 修改单-1.md`
- 国外法规：`ECE R48-06 Suppl.8.md`、`FMVSS 108-2016.md`
- Wikilink 稳定性：通过 `reg_id` frontmatter 字段保证即使重命名仍可追溯

### C. 跨区多语言

- ECE 中英对照：同一版本 note 里分 `## 中文` `## English` 两段，`source_lang: [zh, en]`
- FMVSS / JIS / KMVSS：frontmatter 有中文摘要 + 关键字段翻译；正文保留英文不翻译
- 等效关系双向：A 写 `equivalent_to: [B]`，B 的主条目通过 dataview 自动反向显示

### D. Phase 2 批次顺序

1. **批 1**（Day 3）：国标 ≈ 400 份（核心 + 高复用）
2. **批 2**（Day 3）：ECE 中文 ≈ 150 份
3. **批 3**（Day 3）：欧盟指令/法规 ≈ 50 份
4. **批 4**（Day 3）：美国 FMVSS + 日韩 + 东盟 + 其他区综述 ≈ 100 份
5. **批 5**（Day 3）：剩余辅助文件（Word/Excel/PPT 综述、流程）≈ 50 份

**全部在 Day 3 单日内完成**（DeepSeek 并发 10 线程）。

---

## 9. 验收标准

### Phase 1（Day 2 结束）
- GB 4785 的 3 个版本 + 2 个修改单 全部入库
- 每份 frontmatter 字段齐全，`confidence: high`
- `equivalent_to: ECE R48` 正确填入
- Dataview 查询 `GB 4785` 的版本链正常展开

### Phase 2（Day 5 结束）
- 1537 份全量入库
- 跨区 500 对 `equivalent_to` 填入，关系分类合理
- 30 个 topic 聚合页生成，每页含综述 + dataview 关联法规表
- `_review_queue` 中待审 < 10%（< 155 份）

### Phase 3（Day 5 下午）
- GraphRAG 社区摘要生成
- Obsidian Smart Composer 能调用 Opus 回答"M1 车型正面碰撞有哪些法规、版本、实施日期、等效国际法规"这种跨文档查询
- 查询响应时间 < 10 秒

---

## 10. Phase 2/3 展望

### 后续接入（Phase 2 桥接）
- **损伤生物力学**：THUMS / GHBMC 模型、假人生物保真度、BMI/BSI 指标
- **交通伤数据**：道路交通事故数据库、中国 CIDAS
- **IVISTA**：车型测评结果，和法规要求做"合规度 vs 实际表现"对比
- **学术论文**：你读的论文提取关键结论，关联到对应法规条款

### Phase 3（GraphRAG 深化）
- Neo4j 或 LanceDB 存储图结构
- 支持"从一个假人模型 → 查所有引用它的试验方法 → 查所有依赖这些方法的法规 → 查这些法规的跨区等效 → 查每区的最新实施日期"这种深度跨文档推理
- 自建 Obsidian plugin 做图谱可视化 + MCP 服务器给其他工具（Claude Desktop、Cursor）共享

---

## 文档结束

其他详细 schema 见：
- `01_compile_instructions.md` — LLM 编译指令（prompt 模板）
- `02_taxonomy.md` — 四维度 tag 字典完整列表
- `03_frontmatter_schema.md` — 每类节点的完整 YAML schema
- `04_self_check_rules.md` — Cross-check 规则与 prompts
