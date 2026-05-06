---
type: dashboard
purpose: cross_check_flagged
tags:
- type/dashboard
- status/needs-review
---

# 需要人工复核的法规

> Stage 2 DeepSeek cross-check 标记为 `status/needs-review` 的 notes，共 425 条（29.4%）。93% 是 `unsure` (原文未明确提)，仅 7% 是实际 `mismatch`。

## 按 confidence 分组

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    region AS "Region",
    cross_check_overall_confidence AS "Conf",
    length(cross_check_flags) AS "Flags",
    file.mday AS "Modified"
FROM "01_Wiki/regulations"
WHERE contains(tags, "status/needs-review")
SORT cross_check_overall_confidence ASC, file.mday DESC
LIMIT 60
```

## 按区域分组（低置信度优先）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    title AS "Title",
    cross_check_overall_confidence AS "Conf"
FROM "01_Wiki/regulations"
WHERE contains(tags, "status/needs-review") AND cross_check_overall_confidence = "low"
SORT region ASC, reg_id ASC
LIMIT 80
```

## flagged 字段高频 TOP

由 `_stage2_stats.py` 离线分析结果：

| 字段 | flag 次数 | 常见原因 |
| --- | --: | --- |
| `implementation_date_in_use` | 1425 | 原文常不分新车/在用车实施时间 |
| `equivalent_to` | 1312 | 国内 GB 未写明 ≈ ECE 对应 |
| `supersedes` | 1206 | 被替代关系缺失 |
| `implementation_date_new_vehicle` | 842 | 仅给发布日期，无新车实施日 |
| `standard_body` | 701 | 合并机构表述差异 |
| `技术要求限值` | 558 | LLM 未结构化提取具体限值 |

**优先处理建议**：
1. `cross_check_overall_confidence: low` (330) → 先看 reg_id / title / 日期字段的 mismatch
2. `cross_check_overall_confidence: medium` (139) → 次级复核
3. 高频 mismatch 字段跨 note 聚类修复
