<%*
const class_id = await tp.system.prompt("车型类 ID（M1/M2/M3/N1/N2/N3/L/O/G/all）");
const desc_zh = await tp.system.prompt("中文定义（1-2 句）");
const desc_en = await tp.system.prompt("English definition (optional)") || "";
const max_seats = await tp.system.prompt("最大座位数（可选）") || "";
const max_mass = await tp.system.prompt("最大总质量 kg（可选）") || "";
-%>
---
type: type/vehicle-class
class_id: <% class_id %>
description_zh: <% desc_zh %>
description_en: <% desc_en %>
<% max_seats ? `max_seats: ${max_seats}` : "" %>
<% max_mass ? `max_mass_kg: ${max_mass}` : "" %>
equivalent_classes: {}
confidence: high
extracted_by: manual
tags:
  - type/vehicle-class
  - veh/<% class_id %>
---

# <% class_id %> —— <% desc_zh %>

## 定义

<% desc_zh %>

<% desc_en ? `(${desc_en})` : "" %>

## 跨体系对应

| 体系 | 对应分类 |
|---|---|
| ECE (WP.29) | <% class_id %> |
| US FMVSS | <!-- PC / MPV / LDT / HDT --> |
| GB 国标 | <!-- 乘用车 / 客车 / 货车 / 挂车 --> |
| JIS | <!-- 日本分类 --> |

## 适用于此车型的法规

```dataview
TABLE WITHOUT ID
  link(file.link, reg_id) AS "法规",
  region AS "地区",
  latest_version AS "最新版",
  status AS "状态"
FROM "01_Wiki/regulations"
WHERE contains(vehicle_classes, "<% class_id %>")
SORT region ASC, reg_id ASC
```

## 典型车型（可选）

<!-- 列举几辆代表性车型做锚点 -->
