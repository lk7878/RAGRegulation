<%*
const topic_id = await tp.system.prompt("Topic ID（如 topic/passive-safety/frontal-impact）");
const title = await tp.system.prompt("中文主题名");
const title_en = await tp.system.prompt("English name (optional)") || "";
-%>
---
type: type/topic
topic_id: <% topic_id %>
title: <% title %>
title_en: <% title_en %>
summary_length_words: 0
related_regulations_count: 0
generated_at: <% tp.date.now("YYYY-MM-DDTHH:mm:ssZ") %>
generated_by: manual
confidence: high
tags:
  - type/topic
  - status/manually-edited
  - <% topic_id %>
---

# <% title %>

<% title_en ? `*(${title_en})*` : "" %>

## 1. 主题定义

<!-- 200 字以内说明此主题覆盖的技术范畴 -->

## 2. 全球监管格局

### 中国 GB

### 欧洲 ECE

### 美国 FMVSS

### 日本 / 韩国 / 其他

## 3. 关键技术指标对比

| 指标 | GB | ECE | FMVSS | JIS |
|---|---|---|---|---|
|  |  |  |  |  |

## 4. 演进趋势

<!-- 近 5 年更新方向 + 预计下一轮 -->

## 5. 关联法规

```dataview
TABLE WITHOUT ID
  link(file.link, reg_id) AS "法规",
  region AS "地区",
  status AS "状态",
  latest_version AS "最新版",
  implementation_date_new_vehicle AS "新车实施"
FROM "01_Wiki/regulations"
WHERE contains(topics, "<% topic_id %>")
SORT region ASC
```

## 6. 关联试验方法

```dataview
LIST
FROM "01_Wiki/test-methods"
WHERE contains(tags, "<% topic_id %>")
```

## 7. 关联假人和指标

```dataview
LIST
FROM "01_Wiki/dummies" OR "01_Wiki/injury-metrics"
WHERE contains(tags, "<% topic_id %>")
```

## 8. 社区综述（Phase 3 自动填）

<!-- Opus GraphRAG 产出会覆盖此段 -->
