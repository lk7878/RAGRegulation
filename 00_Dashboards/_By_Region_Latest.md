---
type: dashboard
purpose: region_timeline
tags:
- type/dashboard
- region/latest
---

# 按区域最新发布

> 每个 region 最近 20 条法规，按 `publication_date` 倒序。便于跟踪各国监管动态。

## 中国 GB / GB/T（462 条）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "发布",
    status AS "状态",
    standard_body AS "机构"
FROM "01_Wiki/regulations/cn"
WHERE type != "type/moc"
SORT publication_date DESC
LIMIT 20
```

## UN / ECE（959 条）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    status AS "Status",
    type AS "Type"
FROM "01_Wiki/regulations/ece"
SORT publication_date DESC
LIMIT 20
```

## 欧盟 EU（5 条）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    publication_date AS "Published",
    status AS "Status"
FROM "01_Wiki/regulations/eu"
SORT publication_date DESC
```

## 其他区域（ru-eaeu / cl / jp / us / au / br / gcc / id / kr / my / sa / th / za）

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    region AS "Region",
    publication_date AS "Published",
    title AS "Title"
FROM "01_Wiki/regulations"
WHERE !contains(list("cn", "ece", "eu"), region)
SORT publication_date DESC
LIMIT 30
```
