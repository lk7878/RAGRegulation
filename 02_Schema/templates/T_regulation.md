<%*
const reg_id = await tp.system.prompt("标准号（不含版本），如 GB 4785");
const title = await tp.system.prompt("完整中文标题");
const title_short = await tp.system.prompt("简称（用于 wikilink，可留空）") || "";
const region = await tp.system.suggester(
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"],
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"]
);
const standard_body = await tp.system.prompt("归口单位（SAC/TC 114 / WP.29 / NHTSA …）") || "";
const category = await tp.system.suggester(
  ["mandatory", "recommended", "draft"],
  ["mandatory", "recommended", "draft"]
);
const veh_raw = await tp.system.prompt("适用车型，空格分隔（M1 M2 N1 …）") || "M1";
const vehicle_classes = veh_raw.split(/\s+/).filter(Boolean);
const topic = await tp.system.prompt("主题 tag（如 topic/lighting）") || "topic/unknown";
-%>
---
type: type/regulation
reg_id: <% reg_id %>
title: <% title %>
title_short: <% title_short %>
region: <% region %>
standard_body: <% standard_body %>
category: <% category %>
latest_version: null
all_versions: []
all_amendments: []
equivalent_to: []
vehicle_classes: [<% vehicle_classes.join(", ") %>]
topics:
  - <% topic %>
confidence: high
extracted_by: manual
tags:
  - type/regulation
  - status/manually-edited
  - reg/<% region %>
  - <% topic %>
<%* for (const v of vehicle_classes) { tR += `  - veh/${v}\n`; } -%>
---

# <% title %>

## 概述

<!-- 3-5 行介绍本法规的目的、适用对象、在该区域法规体系中的位置 -->

## 版本演进

```dataview
TABLE WITHOUT ID
  link(file.link, reg_id) AS "版本",
  publication_date AS "发布",
  implementation_date_new_vehicle AS "实施",
  status AS "状态"
FROM "01_Wiki/regulations"
WHERE parent_regulation = "[[<% reg_id %>]]"
SORT publication_date DESC
```

## 修改单

```dataview
LIST
FROM "01_Wiki/regulations"
WHERE type = "type/amendment" AND contains(parent_version, "<% reg_id %>")
SORT publication_date DESC
```

## 跨区等效

```dataview
TABLE WITHOUT ID
  L.ref AS "参照法规",
  L.version AS "版本",
  L.relation AS "关系",
  L.confidence AS "置信度"
FROM "01_Wiki/regulations/<% region %>"
FLATTEN equivalent_to as L
WHERE reg_id = "<% reg_id %>" OR contains(all_versions, "<% reg_id %>")
```

## 备注

<!-- 人工补充的背景、争议、实践要点 -->
