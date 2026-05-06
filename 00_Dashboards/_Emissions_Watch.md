---
type: dashboard
purpose: emissions_tracking
tags:
- type/dashboard
- topic/emissions
---

# 排放法规监控

> 跟踪 国六 / Euro VI / WLTP / CAFC / OBD 相关法规的最新动向。对标 [[emissions_exhaust - 排放与燃料]] 主题页。

## 国内燃料消耗量（CAFC）最新

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    implementation_date_new_vehicle AS "新车实施"
FROM "01_Wiki/regulations/cn"
WHERE contains(reg_id, "19578") OR contains(reg_id, "20997") OR contains(reg_id, "30510") OR contains(reg_id, "22757")
SORT publication_date DESC
```

## 国内排放限值（轻型 / 重型）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    title AS "标题"
FROM "01_Wiki/regulations/cn"
WHERE contains(reg_id, "18352") OR contains(reg_id, "17691") OR contains(reg_id, "18285") OR contains(reg_id, "11340")
SORT publication_date DESC
```

## ECE R101 WLTP 油耗 / CO2 修正案

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R101")
SORT publication_date DESC
LIMIT 15
```

## ECE R49 重型污染物最新修正

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R49") AND contains(type, "amendment")
SORT publication_date DESC
LIMIT 10
```

## ECE R83 轻型车型式认证

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R83")
SORT publication_date DESC
LIMIT 10
```

## 跨主题关联

- [[emissions_exhaust - 排放与燃料]] — 完整主题索引（98 条）
- [[fuel_lpg_cng - 燃料装置（液体 · 气体）]] — R115 改装后排放
- [[energy_labeling - 能耗 · 油耗标识]] — CAFC 数据下游
- [[engine_power_performance - 发动机功率 · 性能测试]] — 台架测试基础
