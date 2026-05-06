---
type: type/index
title: CcVault 法规库入口
created: 2026-04-17
---

# CcVault · 全球汽车法规知识库

> 个人工具箱 · 论文脚手架 · 职业竞争力 · 持续学习
>
> 完整设计见 [[DESIGN]]（位于 02_Schema/）

## 快速导航

- 🏛 **按地区浏览** → [[#所有法规]]
- 🎯 **按主题浏览** → [[#按主题聚合]]
- 🚗 **按车型浏览** → [[#按车型聚合]]
- 📋 **待审条目** → [[_review_queue]]
- 📈 **版本演进** → 见各主条目内 dataview 块

---

## 所有法规

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "标题",
  reg_id AS "编号",
  region AS "地区",
  status AS "状态",
  latest_version AS "最新版",
  implementation_date_new_vehicle AS "新车生效"
FROM "01_Wiki/regulations"
WHERE type = "type/regulation"
SORT region ASC, reg_id ASC
```

## 按主题聚合

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "主题",
  length(file.inlinks) AS "关联法规数"
FROM "01_Wiki/topics"
SORT length(file.inlinks) DESC
```

## 按车型聚合

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "车型",
  description AS "说明",
  length(file.inlinks) AS "适用法规数"
FROM "01_Wiki/vehicle-classes"
```

## 最新处理

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "条目",
  type AS "类型",
  file.mtime AS "更新"
FROM "01_Wiki"
WHERE type != "type/index"
SORT file.mtime DESC
LIMIT 20
```

## 统计

```dataview
TABLE WITHOUT ID
  type AS "类型",
  length(rows) AS "数量"
FROM "01_Wiki"
WHERE type
GROUP BY type
SORT length(rows) DESC
```

---

## 使用提示

- **查条文细节**：开 PDF++ 侧栏，点击 frontmatter 里的 `source_pdf` 字段跳转原文
- **跨区对比**：在法规主条目下方有 `equivalent_to` 字段，自动 dataview 展开等效法规
- **问复杂问题**：打开 Smart Composer 侧栏，它会走 Opus 4.7；简单问题走 Sonnet 自动路由
- **找不到的法规**：检查 [[_review_queue]] 是否在待审

## Pipeline 状态

- **Phase 1**（样板）：🟡 进行中（GB 4785 验证）
- **Phase 2**（批量）：⚪ 未开始
- **Phase 3**（GraphRAG）：⚪ 未开始

详见 `02_Schema/DESIGN.md` 第 8 节。
