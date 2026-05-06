<%*
// 安全检查：防止意外覆盖已有文件
const currentFile = app.workspace.getActiveFile();
if (currentFile && !currentFile.name.startsWith("Untitled")) {
  new Notice("⚠️ Template aborted: 当前文件不是新建 Untitled。拒绝覆盖现有文件。");
  return;
}

const firstAuthor = await tp.system.prompt("第一作者姓（如 Yang）");
const year = await tp.system.prompt("出版年份");
const topic_kw = await tp.system.prompt("主题关键词（用于 paper_id，如 HBM_thorax）");
const title = await tp.system.prompt("完整标题（英文原标题）");
const authors_raw = await tp.system.prompt("所有作者（; 分隔，如 Yang, J.; Zhang, X.）");
const journal = await tp.system.prompt("期刊/会议名") || "";
const doi = await tp.system.prompt("DOI（可留空）") || "";
const paper_type = await tp.system.suggester(
  ["research_article", "review", "case_study", "proceedings", "thesis", "textbook"],
  ["research_article", "review", "case_study", "proceedings", "thesis", "textbook"]
);
const language = await tp.system.suggester(["en", "zh", "de", "ja", "other"], ["en", "zh", "de", "ja", "other"]);
const importance = await tp.system.suggester(["high", "medium", "low"], ["high", "medium", "low"]);

const paper_id = `${firstAuthor}${year}_${topic_kw}`;
const filename = paper_id;
const authors_list = authors_raw.split(";").map(a => `  - ${a.trim()}`).join("\n");
await tp.file.rename(filename);
await tp.file.move(`01_Wiki/literature/papers/${filename}`);
-%>
---
type: literature
paper_id: <% paper_id %>
authors:
<% authors_list %>
year: <% year %>
title: >-
  <% title %>
journal: <% journal %>
volume: null
issue: null
pages: null
doi: <% doi %>
pmid: null
arxiv: null
publisher: null
language: <% language %>

paper_type: <% paper_type %>
methodology: []
subjects: []

abstract: ""
keywords: []

topic: <% topic_kw %>
tags:
  - type/literature
  - literature/<% topic_kw %>

related_regs: []
cites: []
cited_by: []
permanent_notes: []

pdf_path: ""
reading_status: to_read
my_rating: null
importance: <% importance %>
notes_progress: 0

created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% title %>

## 元信息

- **作者**: <% authors_raw %>
- **出版**: <% journal %>, <% year %>
- **DOI**: <% doi ? `[${doi}](https://doi.org/${doi})` : "（无）" %>
- **类型**: <% paper_type %>
- **语言**: <% language %>

## 摘要

*(读完后补全，或用 `_extract_lit_fm.py` 让 LLM 抽)*

## 我的阅读笔记

*(初读时的 fleeting thoughts，不要求结构化)*

- 一句话贡献：
- 方法新颖性：
- 数据可信度：
- 跟我研究的关系：
- 值得保留的金句：

## 从本文派生的原子笔记 (Permanent Notes)

*(读完后，挑 2-5 个最值得独立成条的主张，用 `[[concept_id]]` 引用到 `concepts/` 下)*

- [[  ]]

## 原文参考（MinerU 云解析）

*(由 pipeline 自动追加表格/公式/图像，手动创建时此节为空)*
