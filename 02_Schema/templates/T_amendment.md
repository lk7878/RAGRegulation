<%*
const amendment_id = await tp.system.prompt("修改单 ID，如 GB 4785-2007 修改单-1");
const parent_version = await tp.system.prompt("父版本（wikilink 形式，如 GB 4785-2007）");
const amendment_number = await tp.system.prompt("第几号修改单（数字）") || "1";
const pub_date = await tp.system.prompt("发布日期 YYYY-MM-DD") || "";
const impl_date = await tp.system.prompt("实施日期 YYYY-MM-DD") || "";
const scope = await tp.system.suggester(
  ["full-withdrawal", "transitional-coexistence", "partial-replacement"],
  ["full-withdrawal", "transitional-coexistence", "partial-replacement"]
);
const region = await tp.system.suggester(
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"],
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"]
);
-%>
---
type: type/amendment
amendment_id: <% amendment_id %>
parent_version: "[[<% parent_version %>]]"
amendment_number: <% amendment_number %>
publication_date: <% pub_date %>
implementation_date: <% impl_date %>
scope: <% scope %>
modified_clauses: []
confidence: high
source_pdf: null
source_lang: [zh]
extracted_by: manual
tags:
  - type/amendment
  - status/manually-edited
  - reg/<% region %>
---

# <% amendment_id %>

**针对**：[[<% parent_version %>]]
**范围**：<% scope %>
**实施**：<% impl_date %>

## 变更的条款

<!-- 逐条列出：
- **4.3.1** 原文"旧规定..." → 新规定"..."
- **5.2** 新增了...
- **附录 A.2** 删除了...
-->

## 变更背景

<!-- 简要说明为什么发这份修改单（技术更新 / 与国际接轨 / 发现原版错误） -->

## 与原版并存期

<!-- 如果 scope = transitional-coexistence，说明并存期多久 -->
