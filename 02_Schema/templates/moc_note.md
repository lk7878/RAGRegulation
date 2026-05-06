<%*
// 安全检查
const currentFile = app.workspace.getActiveFile();
if (currentFile && !currentFile.name.startsWith("Untitled")) {
  new Notice("⚠️ Template aborted: 当前文件不是新建 Untitled。");
  return;
}

const topic_kw = await tp.system.prompt("主题关键词（snake_case，如 HBM_evolution）");
const title = await tp.system.prompt("主题地图标题（中文，如 人体模型在碰撞中的演化）");
const topic_tag = await tp.system.prompt("粗粒度主题 tag（如 hbm, thorax, crash_test）") || "unknown";

const moc_id = `MOC_${topic_kw}`;
await tp.file.rename(moc_id);
await tp.file.move(`01_Wiki/literature/mocs/${moc_id}`);
-%>
---
type: moc
moc_id: <% moc_id %>
title: <% title %>
topic: <% topic_tag %>
covered_papers: 0
covered_concepts: 0
last_updated: <% tp.date.now("YYYY-MM-DD") %>
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - moc
  - topic/<% topic_tag %>
---

# <% title %>

> MOC (Map of Content)：本文档把围绕"<% title %>"主题的所有原子笔记 (Permanent Notes) 和文献 (Literature Notes) 串联起来。
> **触发创建条件**：当 `concepts/` 下围绕此主题的 PN ≥ 10 条时。

## 概述

*(一两段话写清楚这个主题是什么、为什么重要、争议焦点在哪)*

## 时间线 / 方法演化

*(可选：按时间或技术范式列举)*

```dataview
TABLE year AS "年", first_author AS "作者", title AS "标题"
FROM "01_Wiki/literature/papers"
WHERE topic = "<% topic_tag %>"
SORT year ASC
```

## 核心概念

*(手工列举本主题最重要的 5-10 条 PN)*

- [[concept_id_1]] — 一句话说明
- [[concept_id_2]] — 一句话说明

## 争议 / 开放问题

*(如果 PN 中有 status = debated 的，在这里汇总)*

- **争议 1**: ...
- **开放问题**: ...

## 相关法规

```dataview
LIST
FROM "01_Wiki/regulations"
WHERE contains(file.tags, "topic/<% topic_tag %>")
SORT reg_id ASC
```

## 我的 Synthesis

*(这是 MOC 的灵魂：你看完所有 PN 后，把它们串成一个故事。这步 LLM 替代不了)*

## 外链

- [[概念 MOC]]
- [[方法 MOC]]
