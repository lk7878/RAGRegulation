---
type: dashboard
purpose: trusted_index
tags:
- type/dashboard
- status/verified
---

# 高可信度索引

> **1016 条 notes (71.9%)** 经 Stage 2 cross-check 标记为 `cross_check_overall_confidence: high`。可作为 **可信参考源** 使用。
>
> *最后更新：2026-04-25 · 含 Opus 复审 + MinerU 全量补补后的数字*

## 高置信度中国 GB

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    status AS "状态",
    title AS "标题"
FROM "01_Wiki/regulations/cn"
WHERE cross_check_overall_confidence = "high"
SORT publication_date DESC
LIMIT 40
```

## 高置信度 ECE（按 reg_id）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    publication_date AS "Published"
FROM "01_Wiki/regulations/ece"
WHERE cross_check_overall_confidence = "high"
SORT reg_id ASC
LIMIT 50
```

## 置信度 ≠ high 且状态 active（次级可信）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    cross_check_overall_confidence AS "Conf",
    status AS "Status",
    publication_date AS "Published"
FROM "01_Wiki/regulations"
WHERE status = "active" AND cross_check_overall_confidence != "high" AND cross_check_overall_confidence != null
SORT cross_check_overall_confidence ASC
LIMIT 50
```

## 置信度分布（概览）

| confidence | count | 占比 |
| --- | --: | --: |
| high    | **1016** | **71.9%** |
| medium  |     353  |     25.0% |
| low     |      35  |      2.5% |
| unknown |      10  |      0.7% |

> 详细分析参见 [[_Topics MOC#Stage 2 Cross-check 最终状态（1414/1414，100%）|Topics MOC Stage 2 段]]。
>
> **进化历史**：high 从 70.8% → 71.8% → **71.9%**（Opus 复审 + MinerU 全量 OCR 补补后的进一步提升）。

## 判断依据

- **high**: 核心字段（reg_id / title / 发布机构 / 日期）与原文 OCR 一致
- **medium**: 某非关键字段存在少量不匹配或缺失
- **low**: 关键字段 mismatch，或原文 OCR 质量差不可核实
- **unknown**: LLM 无法给出确定性判断

## 使用建议

- 给他人引用或对标时，**优先选 `high` 标签的 note**
- `medium` / `low` 注意检查 `cross_check_flags` 字段找出具体疑点
- 低置信度可以用 DeepSeek 或 Claude 再跑 Stage 2 单独复核
