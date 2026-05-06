---
type: setup_guide
tags:
- type/guide
- scope/audit
---

# Obsidian Templater 配置：一键建 audit

> 让你在 Obsidian 里按 `Ctrl+Shift+A` 秒级创建 audit 条目。

---

## 为什么用 Templater

手动复制 `_template.md` 再改名要 30 秒+。用 Templater 只需 5 秒：
- 自动填 `target_file`（当前打开的 note 路径）
- 自动填 `target_reg_id`（从 FM 读）
- 自动填 `created`（当前时间）
- 自动命名文件 `YYYY-MM-DD_<brief>.md`

---

## 第 1 步：安装 Templater 插件

1. Obsidian 左下角齿轮 → **Community plugins**
2. 若第一次，先 **Turn on community plugins**
3. **Browse** → 搜 `Templater` → Install → Enable

---

## 第 2 步：配置 Templater

插件启用后左栏会多出 Templater 设置：

1. **Template folder location**：设为 `02_Schema/templates`
   - 如果目录不存在，先在 Obsidian 里创建 `02_Schema/templates/` 空目录
2. **Trigger Templater on new file creation**：勾选（可选，加速流程）

---

## 第 3 步：创建 audit 模板

在 `02_Schema/templates/` 目录下创建新文件 `audit.md`，内容如下：

```markdown
<%*
// 获取当前活动文件作为 target
const activeFile = app.workspace.getActiveFile();
const targetPath = activeFile ? activeFile.path : "";
const cache = activeFile ? app.metadataCache.getFileCache(activeFile) : null;
const targetRegId = cache?.frontmatter?.reg_id || "";

// 询问 severity（可选）
const severity = await tp.system.suggester(
  ["critical", "high", "medium", "low"],
  ["critical", "high", "medium", "low"],
  false,
  "Severity?"
) || "medium";

// 询问 category
const category = await tp.system.suggester(
  ["accuracy", "completeness", "classification", "link", "formatting", "other"],
  ["accuracy", "completeness", "classification", "link", "formatting", "other"],
  false,
  "Category?"
) || "accuracy";

// 询问 brief
const brief = await tp.system.prompt("Brief (3-8 words, for filename):") || "issue";
const briefSlug = brief.toLowerCase().replace(/\s+/g, "_").replace(/[^a-z0-9_]/g, "");

// 当前时间
const now = tp.date.now("YYYY-MM-DDTHH:mm:ss");
const dateOnly = tp.date.now("YYYY-MM-DD");

// 文件名
const filename = `${dateOnly}_${briefSlug}`;
await tp.file.rename(filename);
await tp.file.move(`05_Audit/${filename}`);
-%>---
target_file: <% targetPath %>
target_reg_id: <% targetRegId %>
target_section: ""
target_anchor: ""

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

```

---

## 第 4 步：快捷键（已内置 `Alt+N`）

**Templater 默认已把 `Alt+N` 绑定到 `Create new note from template`**，**无需额外绑定**。

直接按 `Alt+N` 即可弹出模板选择列表。

### 如果想换成其他快捷键

1. Obsidian 设置 → **Hotkeys**
2. 搜索 `Templater: Create new note from template`
3. 先点 ❌ 清除默认 `Alt+N`
4. 点 **+** 按下你想要的组合（避开 `Alt+A` 截图冲突）

推荐备选（按优先级）：
- `Alt+Q` — 左手单手，无常见冲突
- `Alt+W` — 同上
- `F4` — 单键最快
- `Ctrl+'` — 无冲突

### 避坑

- ❌ `Alt+A` — 微信/QQ 截图
- ❌ `Ctrl+A` — 全选
- ❌ `Ctrl+N` — Obsidian 内置"新建空 note"
- ❌ `F2` — Obsidian 内置"重命名"

---

## 第 5 步：使用

**场景**：正在读 `01_Wiki/regulations/cn/GB 4785-2019.md`，发现摘要漏了 N 类车辆。

1. 按 `Alt+N`
2. 弹出对话框：选 `audit`（默认在第一位）
3. 选 severity（medium）
4. 选 category（completeness）
5. 输入 brief："GB4785 missing N class"
6. 自动跳到新文件的 Issue 段，光标就位
7. 写"摘要只提 M 类，原文还含 N/O 类"
8. Tab 到 Expected 写"补充 M/N/O"
9. 保存 → 完成

整个流程约 15-30 秒。

---

## 故障排查

### Templater 没创建 05_Audit/ 下的文件？

确认：
- `05_Audit/` 目录存在（已由本次初始化创建）
- 模板中 `tp.file.move(\`05_Audit/${filename}\`)` 路径正确

### `target_reg_id` 是空的？

确认当前打开的 note FM 里有 `reg_id:` 字段（所有 `01_Wiki/regulations/` 下的 note 都应有）。

### 时间格式不对？

Templater 的 `tp.date.now()` 默认依赖系统时区，检查 Obsidian 设置 → About → Language & region。

### 不想用 Templater？

直接手动：
1. 复制 `05_Audit/_template.md`
2. 粘贴到 `05_Audit/`
3. 手动改名 `YYYY-MM-DD_xxx.md`
4. 手动填字段

多花 20 秒但不需要插件。

---

## 进阶：选中文本自动填 target_anchor

在模板开头加：
```javascript
const selection = tp.file.selection();
// 在 FM 里用：target_anchor: "<% selection %>"
```

这样你在 note 里**选中**某段错文本后 `Ctrl+Shift+A`，audit 就自动记下原文片段。agent 处理时能精准定位。

---

**最后更新**：2026-04-19
