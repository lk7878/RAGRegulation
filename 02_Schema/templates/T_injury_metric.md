<%*
const metric_id = await tp.system.prompt("Metric ID（如 metric/hic15）");
const title = await tp.system.prompt("中文全称");
const title_en = await tp.system.prompt("English full name");
const abbreviation = await tp.system.prompt("缩写（如 HIC15）");
const body_region = await tp.system.suggester(
  ["head", "neck", "chest", "abdomen", "pelvis", "femur", "tibia", "lower-leg", "upper-leg", "全身"],
  ["head", "neck", "chest", "abdomen", "pelvis", "femur", "tibia", "lower-leg", "upper-leg", "whole-body"]
);
-%>
---
type: type/injury-metric
metric_id: <% metric_id %>
title: <% title %>
title_en: <% title_en %>
abbreviation: <% abbreviation %>
body_region: <% body_region %>
formula: ""
used_by_regulations: []
biomechanics_refs: []
confidence: high
extracted_by: manual
tags:
  - type/injury-metric
  - status/manually-edited
---

# <% abbreviation %> — <% title %>

## 定义

## 公式

$$
<!-- 在这里写 LaTeX 公式 -->
$$

## 计算细节

- 采样率：
- 滤波：
- 时间窗：
- 单位：

## 各法规限值

| 法规 | 车型 | 限值 | 注 |
|---|---|---|---|
|  |  |  |  |

## 引用此指标的法规

```dataview
LIST
FROM "01_Wiki/regulations"
WHERE contains(string(file.file.content), "<% abbreviation %>")
```

## 生物力学依据（Phase 2 桥接）

<!-- 待 Phase 2 引入相关论文后补充 -->
