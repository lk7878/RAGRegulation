---
type: dashboard
purpose: ev_tracking
tags:
- type/dashboard
- topic/ev
---

# 新能源车法规监控

> 跟踪 EV / HEV / PHEV / FCV / 动力电池 / EV 充电 / EV 客车 / 电动自行车相关法规。

## 国内电动汽车整车 / 电池安全

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    implementation_date_new_vehicle AS "实施",
    title AS "标题"
FROM "01_Wiki/regulations/cn"
WHERE contains(reg_id, "18384") OR contains(reg_id, "38031") OR contains(reg_id, "38032") OR contains(reg_id, "19234") OR contains(reg_id, "19751") OR contains(reg_id, "19752") OR contains(reg_id, "21668")
SORT publication_date DESC
```

## 国内电动自行车安全

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    title AS "标题"
FROM "01_Wiki/regulations/cn"
WHERE contains(reg_id, "17761") OR contains(reg_id, "24155") OR contains(reg_id, "42295") OR contains(reg_id, "42296") OR contains(reg_id, "43854")
SORT publication_date DESC
```

## ECE R100 电动车高压安全（整车 + 动力电池）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R100")
SORT publication_date DESC
LIMIT 15
```

## ECE R134 氢燃料电池车

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R134")
SORT publication_date DESC
```

## ECE R136 L 类电动车 + R156 OTA

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations/ece"
WHERE contains(reg_id, "R136") OR contains(reg_id, "R156") OR contains(reg_id, "R148")
SORT publication_date DESC
```

## 跨主题关联

- [[hv_battery_ev - 电动车 · 动力电池 · 充电保护]] — 直接 EV 主题（4 条）
- [[electronics_emc - 电气电子与 EMC]] — 含 R100/R136/R134（22 条）
- [[special_vehicles - 特种 · 危险车辆]] — 含 GB 21668 危险品 EV 运输车
