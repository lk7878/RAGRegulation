---
type: type/schema
title: Self-Check 三道防线规则
version: 0.1
---

# 04 · AI Self-Check 三道防线

> 因为不做前置人工审校（决策 11），所有质量保障必须由 AI 自身完成。这份文档定义三道防线的**规则** + **prompt 模板**。

---

## 0. 三道防线总览

```
┌──────────────────────────────────────────────────────┐
│  防线 1：DeepSeek V3 字段级自评 (self-confidence)    │
│  每个 frontmatter 字段都有 _conf: high/medium/low    │
└──────────────────┬───────────────────────────────────┘
                   │ 低 conf 字段 → 标记
                   ▼
┌──────────────────────────────────────────────────────┐
│  防线 2：Sonnet 4.6 二次审校 (cross-check)           │
│  读 DeepSeek 产出 + 原文关键段，判断不一致           │
└──────────────────┬───────────────────────────────────┘
                   │ 不一致字段 → _review_queue
                   ▼
┌──────────────────────────────────────────────────────┐
│  防线 3：查询时按需复核 (lazy re-extraction)         │
│  Smart Composer 回答问题前，若命中 low-conf 条目，   │
│  现场触发 Opus 重抽取 + 原 PDF 溯源                  │
└──────────────────────────────────────────────────────┘
```

---

## 1. 防线 1：字段级自评 (DeepSeek V3)

### 规则

- **每个 frontmatter 字段**都必须配一个 `_conf` 后缀的同名字段，取 `high/medium/low`
- **每条技术要求条款**末尾必须有 `confidence: high/medium/low` 行
- 标准：
  - `high`：原文明确写明，无歧义
  - `medium`：原文提到但需推断（如 `publication_date` 只看到"2019 年 5 月"，补全为 `2019-05-01` 时 conf 降为 medium）
  - `low`：完全未提及 / OCR 乱码 / 推理链条 > 2 步

### 实现

见 `01_compile_instructions.md` 第 1 节 DeepSeek V3 Prompt 的 System 部分。

### 低置信度触发

- 一份 note 的 frontmatter 中若有任一 `_conf: low`，该 note 自动标 `status/needs-review` tag
- 若 > 3 个字段 `_conf: low` 或 `_conf: medium`，note 整体 `confidence: low`

---

## 2. 防线 2：Cross-check (Sonnet 4.6)

### 规则

- 只对**关键法规**做 cross-check（节约成本）
  - 国标 GB（约 400 份）全部做
  - ECE 中文版（约 150 份）全部做
  - 其他地区主要法规（FMVSS 108 / 208 / 301 等）约 150 份做
  - 总计约 **700 份**，不做的 837 份依赖防线 1
- cross-check 的字段（必须核对）：
  - `reg_id` / `title`
  - `publication_date` / `implementation_date_*`
  - `equivalent_to` 的 `ref` + `version`
  - `supersedes`
  - 技术要求中的**限值**字段（HIC 数值、照明角度范围等）
- cross-check 不核对的字段（省 token）：
  - `source_pdf`、`extracted_by` 这类元数据
  - 章节标题（DeepSeek 抽章节一般不出错）

### Cross-check Prompt

见 `01_compile_instructions.md` 第 2 节。

### 不一致处理

Sonnet 返回每个字段的 `match / mismatch / unsure`。处理规则：

| 结果 | 处理 |
|---|---|
| 所有字段 `match`，`overall: high` | 标 `status/verified`，不动 |
| 任一字段 `mismatch` | 该字段的 `_conf` 降为 `low`，整体 `confidence: low`，加 `status/needs-review` |
| 任一字段 `unsure` | 该字段 `_conf` 降一档（high→medium），`recommend_review` 若为 true 则加 `status/needs-review` |
| `overall: low` 且无 `mismatch` | 加 `status/needs-review`，`note` 写 "cross-check 对原文不确定" |

---

## 3. 防线 3：查询时按需复核 (Lazy Re-extraction)

### 规则

- Smart Composer 或其他 LLM 问答插件在回答用户问题前，检查所命中 notes 的 `confidence` 字段
- 若有任一命中 note `confidence: low` 或包含 `status/needs-review` tag：
  1. 自动在回答前插入**原 PDF 对应段的引用**
  2. 触发一次 **Opus 4.7 现场重抽取**（对该 PDF 的该段重跑抽取，对比结果）
  3. 如果 Opus 结果与原 note 不一致，把分歧展示给用户，并更新 note（标 `status/manually-edited` 由用户最终确认）

### 实现

- 这部分代码在 Obsidian plugin 或 MCP server 里（Phase 3 做）
- Phase 1-2 先实现前两道防线即可

### 成本预算

- 每天估算 10% 查询命中低置信度条目，每次 Opus 重抽取约 2k input + 500 output
- 单次成本 ≈ $0.025
- 每天 10 次 = $0.25 / 日 = **$7.5 / 月**
- 3 个月总计 ≈ $22.5，包含在 DESIGN.md 的 "日常问答预留 $15-20" 里

---

## 4. Review Queue 进出规则

### 入队（自动）

满足以下任一条件：
1. `confidence: low` 或 > 3 个字段 `_conf: low`
2. 含 `status/needs-review` tag（防线 2 添加）
3. 用户在 Smart Composer 手动点"flag for review"

### 出队（手动 or 半自动）

- **手动**：你打开 note 精修，移除 `status/needs-review` tag，把 `_conf: low` 改为 `high` 或 `medium`
- **半自动**（Phase 3）：你在 Smart Composer 里对某 note 做 3 次以上成功查询（无纠错），系统自动 "graduate" 它出队

---

## 5. 规模预估

| 阶段 | 预估入队数 | 出队目标 |
|---|---|---|
| Phase 1（Day 2 结束） | ~5 份（仅 GB 4785 样板） | 全部手动精修出队 |
| Phase 2（Day 5 结束） | 150-200 份（1537 × 10%-13%） | < 155 份（验收门槛）|
| Phase 3（长期） | 新增缓慢 | 每月手动精修 20-30 份 |

> 如果 Phase 2 结束 review queue > 200，说明 Sonnet cross-check 阈值过严，应放松 `unsure` 处理规则。

---

## 6. 监控指标

Pipeline 跑完后在 `99_SystemScripts/auto_reg_index/logs/self_check_report.md` 产出报告：

- 总 note 数
- `status/verified` 占比
- `status/needs-review` 占比
- 字段级平均 confidence 分布
- Cross-check mismatch 字段 top 10（哪些字段最易出错）
- 建议的 prompt 改进方向
