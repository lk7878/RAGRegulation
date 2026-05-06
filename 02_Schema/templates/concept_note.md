<%*
// 安全检查
const currentFile = app.workspace.getActiveFile();
if (currentFile && !currentFile.name.startsWith("Untitled")) {
  new Notice("⚠️ Template aborted: 当前文件不是新建 Untitled。");
  return;
}

const concept_id = await tp.system.prompt("概念 ID（snake_case，如 HIC_threshold_1000）");
const category = await tp.system.suggester(
  [
    "injury_criterion", "test_methodology", "fe_model", "experimental_protocol",
    "regulatory_interpretation", "theoretical_framework", "data_point",
    "controversy", "historical_fact"
  ],
  [
    "injury_criterion", "test_methodology", "fe_model", "experimental_protocol",
    "regulatory_interpretation", "theoretical_framework", "data_point",
    "controversy", "historical_fact"
  ]
);
const claim = await tp.system.prompt("一句话主张（必须可证伪，不要写\"我认为\"）");
const status = await tp.system.suggester(
  ["established", "debated", "emerging", "deprecated"],
  ["established", "debated", "emerging", "deprecated"]
);
const evidence_strength = await tp.system.suggester(
  ["high", "medium", "low"],
  ["high", "medium", "low"]
);
const sources_raw = await tp.system.prompt("来源 paper_id（空格分隔，如 Yang2023_HBM Kleiven2007_brain）");
const regs_raw = await tp.system.prompt("相关法规（空格分隔，如 ECE-R94 FMVSS-208，留空则无）") || "";

const sources_list = sources_raw.split(/\s+/).filter(Boolean).map(s => `  - "[[${s}]]"`).join("\n");
const regs_list = regs_raw.split(/\s+/).filter(Boolean).map(r => `  - "[[${r.replace(/-/g, " ")}]]"`).join("\n");

await tp.file.rename(concept_id);
await tp.file.move(`01_Wiki/literature/concepts/${concept_id}`);
-%>
---
type: concept
concept_id: <% concept_id %>
category: <% category %>

claim: >-
  <% claim %>

sources:
<% sources_list %>

related_concepts: []
related_regs:
<% regs_list %>
opposing_concepts: []
supports_concepts: []

status: <% status %>
evidence_strength: <% evidence_strength %>

tags:
  - type/concept
  - concept/<% category %>

created: <% tp.date.now("YYYY-MM-DD") %>
last_reviewed: <% tp.date.now("YYYY-MM-DD") %>
author: me
---

# <% concept_id %>

## 主张

<% claim %>

## 证据

*(列出每个 source，一句话说明它如何支持本主张)*

<% sources_raw.split(/\s+/).filter(Boolean).map(s => `- [[${s}]]：`).join("\n") %>

## 反对证据 / 局限

*(如果 status = debated/deprecated，说清争议)*

- 

## 我的思考

*(此条对我研究的意义？下一步怎么用？)*

- 

## 引用到的法规

<% regs_raw.split(/\s+/).filter(Boolean).map(r => `- [[${r.replace(/-/g, " ")}]]：`).join("\n") %>
