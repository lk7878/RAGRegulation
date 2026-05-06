<%*
const method_id = await tp.system.prompt("Method ID（如 test/mdb-side-impact）");
const title = await tp.system.prompt("中文名");
const title_en = await tp.system.prompt("English name（可选）") || "";
const category = await tp.system.suggester(
  ["dynamic-impact", "static", "mechanical", "environmental", "emc", "electrical"],
  ["dynamic-impact", "static", "mechanical", "environmental", "emc", "electrical"]
);
-%>
---
type: type/test-method
method_id: <% method_id %>
title: <% title %>
title_en: <% title_en %>
category: <% category %>
equipment: []
dummies_used: []
injury_metrics_measured: []
used_by_regulations: []
parameters: {}
confidence: high
extracted_by: manual
tags:
  - type/test-method
  - status/manually-edited
---

# <% title %>

## 试验目的

## 试验设备

## 试验参数

| 参数 | 值 | 单位 |
|---|---|---|
|  |  |  |

## 试验步骤

## 损伤指标采集

## 相关法规

```dataview
LIST
FROM "01_Wiki/regulations"
WHERE contains(string(file.file.content), "<% method_id %>")
   OR contains(topics, "<% method_id %>")
```

## 相关假人

```dataview
LIST
FROM "01_Wiki/dummies"
WHERE contains(used_in_methods, "[[<% method_id %>]]")
```
