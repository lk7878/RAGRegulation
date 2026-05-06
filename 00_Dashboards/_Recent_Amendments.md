---
type: dashboard
purpose: recent_ece_amendments
tags:
- type/dashboard
- ece/amendments
---

# 近期 ECE 修正案跟踪

> WP.29 每年约发布 50-80 条 R 系列 Amendment / Revision，是跟踪国际汽车法规演进的主渠道。本页按最新日期排序。

## 2023 年以来 ECE 修正案（按发布日期）

```dataview
TABLE WITHOUT ID
    file.link AS "Amendment",
    reg_id AS "reg_id",
    publication_date AS "Published"
FROM "01_Wiki/regulations/ece"
WHERE contains(type, "amendment") AND publication_date >= date(2023-01-01)
SORT publication_date DESC
LIMIT 60
```

## 2024+ 最新一年

```dataview
TABLE WITHOUT ID
    file.link AS "Amendment",
    publication_date AS "Published",
    cross_check_overall_confidence AS "Conf"
FROM "01_Wiki/regulations/ece"
WHERE contains(type, "amendment") AND publication_date >= date(2024-01-01)
SORT publication_date DESC
LIMIT 40
```

## 按 R 号聚合（Top 10 最活跃）

由 Stage 4 分析得知：近 5 年修订最密集的 ECE 系列（手工整理）：

| reg_id 家族 | 修正案数 | 技术域 |
| --- | --: | --- |
| `R13` (Rev.8/9 系列) | 15+ | 制动 → [[brakes - 制动系统]] |
| `R116` | 10+ | 防盗 → [[anti_theft_security - 防盗与安全防护]] |
| `R106` | 10+ | 农用轮胎 → [[tires_wheels - 轮胎与车轮]] |
| `R55` (Rev.1/2) | 10+ | 联结装置 → [[special_vehicles - 特种 · 危险车辆]] |
| `R129` (Rev.3/4) | 8+ | 儿童约束 → [[restraints_airbags - 安全带与乘员约束]] |
| `R101` (Rev.3) | 10+ | WLTP CO2 → [[emissions_exhaust - 排放与燃料]] |
| `R121` (Rev.1/2) | 12+ | 操纵件标识 → [[operator_controls_indicators - 操纵件 · 指示器位置]] |
| `R152` | 6+ | M1 AEBS → [[brakes - 制动系统]] |

## ECE 修正案类型说明

- **Rev**：大修订，可独立取代旧 Rev 版本
- **Am**：增量修正案，附加到特定 Rev 上
- **Corr**：勘误（通常是技术性小改）
- **Add**：附录追加（在后期版本不常用）
