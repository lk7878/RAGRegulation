---
type: type/review-queue
title: 待人工复核队列
created: 2026-04-17
---

# _review_queue —— 待人工复核队列

> Pipeline 的 AI self-check 三道防线的最后出口。所有 `confidence < 0.80` 或双模型 cross-check 不一致的条目会自动进入本队列。
>
> 日常你不需要主动来这里；只有在你**查询某条法规时 Smart Composer 提示"该条目未经复核"**时，可来此做一次精修。

## 队列统计

```dataview
TABLE WITHOUT ID
  link(file.link, reg_id) AS "法规",
  review_reason AS "原因",
  confidence AS "置信度",
  file.mtime AS "入队时间"
FROM "01_Wiki/regulations"
WHERE contains(tags, "status/needs-review")
SORT confidence ASC
```

## 进入此队列的触发条件

1. **任意 frontmatter 字段 `confidence: low`**（DeepSeek V3 抽取时自评）
2. **Sonnet cross-check 与 DeepSeek 产出不一致**（关键字段差异）
3. **用户在 Smart Composer 查询时提示"字段缺失"或"语义不明"**
4. **Opus 跨区等效判定的结果与现有 `equivalent_to` 字段冲突**

## 处理流程

1. 打开某条目，查看右栏的 `review_reason` 字段
2. 点击 frontmatter 里的 `source_pdf` 跳回原文（PDF++）
3. 对照原文校正字段
4. 校正后将 `status/needs-review` tag 移除，`confidence` 改为 `high`

## 统计

```dataview
TABLE WITHOUT ID
  review_reason AS "原因",
  length(rows) AS "数量"
FROM "01_Wiki/regulations"
WHERE contains(tags, "status/needs-review")
GROUP BY review_reason
SORT length(rows) DESC
```

---

**设计决策引用**：参见 `02_Schema/04_self_check_rules.md`。
