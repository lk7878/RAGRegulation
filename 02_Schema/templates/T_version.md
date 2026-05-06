<%*
const reg_id = await tp.system.prompt("版本 ID，如 GB 4785-2019");
const parent = await tp.system.prompt("父主条目（wikilink 形式，如 GB 4785 外部照明安装规定）");
const title = await tp.system.prompt("本版本标题") || parent;
const region = await tp.system.suggester(
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"],
  ["cn", "ece", "eu", "us", "jp", "kr", "asean", "gcc", "ru-eaeu", "in", "br", "au", "za"]
);
const pub_date = await tp.system.prompt("发布日期 YYYY-MM-DD") || "";
const impl_new = await tp.system.prompt("新车实施日期 YYYY-MM-DD") || "";
const impl_use = await tp.system.prompt("在用车实施日期 YYYY-MM-DD（可选）") || "";
const supersedes = await tp.system.prompt("替代的旧版本（wikilink 或留空）") || "";
const source_lang = await tp.system.suggester(
  ["[zh]", "[en]", "[zh, en]"],
  ["[zh]", "[en]", "[zh, en]"]
);
-%>
---
type: type/version
reg_id: <% reg_id %>
parent_regulation: "[[<% parent %>]]"
title: <% title %>
region: <% region %>
publication_date: <% pub_date %>
publication_date_conf: high
implementation_date_new_vehicle: <% impl_new %>
implementation_date_new_vehicle_conf: high
implementation_date_in_use: <% impl_use %>
withdrawn_date: null
status: active
supersedes: <% supersedes ? `"[[${supersedes}]]"` : "null" %>
superseded_by: null
equivalent_to: []
amendments_applied: []
vehicle_classes: []
topics: []
confidence: high
source_pdf: null
source_lang: <% source_lang %>
extracted_by: manual
tags:
  - type/version
  - status/manually-edited
  - reg/<% region %>
---

# <% title %>

## 适用范围

<!-- 原文第一章 / scope -->

## 规范性引用文件

<!-- Normative References —— 用 [[wikilink]] 互连 -->

## 术语和定义

<!-- Key definitions -->

## 技术要求

<!-- 每条规则一个有序列表项
1. **[条款号]** 标题
   - 限值：...
   - 试验方法：[[...]]
   - confidence: high
-->

## 试验方法

## 附录

## 版本差异（相较上一版）

<!-- 如果此版本替代了更早版本，写明主要变化 -->
