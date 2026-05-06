<%*
// ───────────────────────────────────────────────────────────
// CcVault Audit 条目快速生成模板（v2，加固版）
// 绑定 Alt+N (Templater 默认) 或通过命令面板调用
// 
// v2 修复：加入安全检查，防止 tp.file.move() 误移动用户文件。
// 历史教训：2026-04-19 曾因此导致 _使用说明.md 消失。
// ───────────────────────────────────────────────────────────

// ═══════════════════════════════════════════════════════════
// SECTION 1: 捕获目标文件（用户正在看的 note）
// ═══════════════════════════════════════════════════════════
let activeFile = app.workspace.getActiveFile();
let targetPath = activeFile?.path || "";
let targetRegId = "";

// 如果当前激活的是 Templater 新建的 Untitled，从最近打开文件找真实 target
if (activeFile && activeFile.name.startsWith("Untitled")) {
    const recent = app.workspace.getLastOpenFiles();
    for (const path of recent) {
        if (path.endsWith(".md") && !path.includes("Untitled") && path !== activeFile.path) {
            const tfile = app.vault.getAbstractFileByPath(path);
            if (tfile) {
                targetPath = path;
                const c = app.metadataCache.getFileCache(tfile);
                targetRegId = c?.frontmatter?.reg_id || "";
                break;
            }
        }
    }
} else if (activeFile) {
    const cache = app.metadataCache.getFileCache(activeFile);
    targetRegId = cache?.frontmatter?.reg_id || "";
}

// ═══════════════════════════════════════════════════════════
// SECTION 2: 读取选中文本作为 target_anchor（可选）
// ═══════════════════════════════════════════════════════════
let selection = "";
try {
    const editor = app.workspace.activeEditor?.editor;
    if (editor) selection = editor.getSelection() || "";
} catch (e) { selection = ""; }
selection = selection.replace(/\s+/g, " ").trim();
if (selection.length > 120) selection = selection.substring(0, 120) + "...";

// ═══════════════════════════════════════════════════════════
// SECTION 3: 询问 severity / category / brief
// ═══════════════════════════════════════════════════════════
const severity = await tp.system.suggester(
    ["critical (数据错误影响决策)", "high (主要字段错)", "medium (摘要或内容错)", "low (格式或可读性)"],
    ["critical", "high", "medium", "low"],
    false,
    "Severity?"
) || "medium";

const category = await tp.system.suggester(
    ["accuracy (内容准确性)", "completeness (完整性)", "classification (分类 tag)", "link (wikilinks)", "formatting (排版)", "other"],
    ["accuracy", "completeness", "classification", "link", "formatting", "other"],
    false,
    "Category?"
) || "accuracy";

const brief = await tp.system.prompt("Brief (3-8 words, for filename):") || "issue";
const briefSlug = brief
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .replace(/\s+/g, "_")
    .replace(/^_+|_+$/g, "")
    .substring(0, 50) || "issue";

// ═══════════════════════════════════════════════════════════
// SECTION 4: 时间戳 + 文件名
// ═══════════════════════════════════════════════════════════
const now = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const dateOnly = tp.date.now("YYYY-MM-DD");
const filename = `${dateOnly}_${briefSlug}`;
const targetFolder = "05_Audit";

// ═══════════════════════════════════════════════════════════
// SECTION 5: 【关键安全检查】防止误移动用户文件
// ═══════════════════════════════════════════════════════════
// tp.file.move() 移动"当前激活文件"。如果 Templater 因时序/bug 没有
// 及时切换到新建的 Untitled 文件就运行脚本，会把用户正在读的文件
// 移走。此处加防护：只有当前激活文件是 Untitled 时才允许 move。
const fileAtMoveTime = app.workspace.getActiveFile();
if (fileAtMoveTime && !fileAtMoveTime.name.startsWith("Untitled")) {
    new Notice(
        `⚠️ Audit 模板已终止！\n\n` +
        `当前活动文件是 "${fileAtMoveTime.name}"，不是新 Untitled 笔记。\n` +
        `继续会把这个文件移到 05_Audit/ 导致数据丢失。\n\n` +
        `正确流程：\n` +
        `1. 先关闭当前文件 (Ctrl+W)\n` +
        `2. 或在 Obsidian 空白处按 Alt+N\n\n` +
        `target_file 仍会自动填为你最近看的 note。`,
        20000
    );
    throw new Error("AUDIT_TEMPLATE_ABORTED: active file is not Untitled, tp.file.move would overwrite it.");
}

// 安全检查通过，移动新建的 Untitled 文件到 05_Audit/
await tp.file.move(`${targetFolder}/${filename}`);
-%>---
target_file: <% targetPath %>
target_reg_id: <% targetRegId %>
target_section: ""
target_anchor: "<% selection %>"

severity: <% severity %>
category: <% category %>
status: open

created: <% now %>
resolved: null
resolver: null

tags:
  - audit/open
  - audit/severity-<% severity %>
  - audit/category-<% category %>
---

## Issue

<% tp.file.cursor() %>

## Expected


## Resolution


## Related

