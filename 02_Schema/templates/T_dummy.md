<%*
const dummy_id = await tp.system.prompt("Dummy ID（如 dummy/hybrid-iii-50th）");
const family = await tp.system.suggester(
  ["Hybrid III", "Hybrid II", "Q", "WorldSID", "THOR", "ES-2", "EuroSID", "BioRID", "Other"],
  ["Hybrid III", "Hybrid II", "Q", "WorldSID", "THOR", "ES-2", "EuroSID", "BioRID", "Other"]
);
const percentile = await tp.system.suggester(
  ["5th", "50th", "95th", "child"],
  ["5th", "50th", "95th", "child"]
);
const child_age = (percentile === "child")
  ? (await tp.system.prompt("儿童假人年龄（月）") || "")
  : "";
-%>
---
type: type/dummy
dummy_id: <% dummy_id %>
family: <% family %>
percentile: <% percentile %>
<% child_age ? `child_age_months: ${child_age}` : "" %>
used_in_methods: []
injury_metrics_supported: []
biofidelity_refs: []
confidence: high
extracted_by: manual
tags:
  - type/dummy
  - status/manually-edited
---

# <% family %> <% percentile %>

## 几何与质量

## 传感器配置

## 支持的损伤指标

```dataview
LIST
FROM "01_Wiki/injury-metrics"
WHERE contains(file.inlinks, this.file.link)
```

## 引用此假人的试验方法

```dataview
LIST
FROM "01_Wiki/test-methods"
WHERE contains(dummies_used, this.file.link)
```

## 生物保真度（Phase 2 桥接）

<!-- 待 Phase 2 引入 THUMS/GHBMC 和文献后补充 -->
