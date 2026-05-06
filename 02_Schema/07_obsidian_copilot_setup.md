---
title: Obsidian Copilot 配置指南
tags: [setup, obsidian, copilot, llm]
created: 2026-04-19
---

# Obsidian Copilot 配置指南

> **用途**：在 Obsidian 内嵌 AI 助手，做 RAG 问答 + 单 note 编辑。
> **分工**：
> - Copilot = 日常 90% 场景（读、问、轻编辑、选中文本处理）
> - Cascade / Claude Code = 10% 复杂场景（`/process_audits`、`/ingest`、索引重建）
> - Python scripts = 全自动 pipeline

---

## 一、资源与成本

### 这个方案用什么
- **Chat 模型**：Claude Sonnet 4.6（走你已有的 `bruder.yukinoapi.com` 中转）
- **Embedding 模型**：`nomic-embed-text`（本地 Ollama，完全免费离线）
- **插件**：`logancyang/obsidian-copilot`（免费版，非 Plus）

### 成本预估
- Chat: 每次问答 $0.003-0.01（Sonnet 4.6 定价）
- Embedding: 0（本地）
- 日常每天 10-30 次问答 ≈ 月成本 ¥5-20
- 首次建索引 ≈ 0（embedding 本地）

### 已验证状态（2026-04-19）
| 组件 | 状态 |
|---|---|
| 中转 `bruder.yukinoapi.com` | ✅ Chat 可用（仅 `[K]claude-sonnet-4-6`） |
| 中转 Embedding | ❌ 不支持任何 embedding 模型 |
| 本地 Ollama | ✅ 已装 v0.20.7（未启动） |
| `nomic-embed-text` 模型 | ⏸ 未下载（本指南会带你拉） |

---

## 二、准备工作（Obsidian 之外）

### 步骤 1 — 启动 Ollama

Ollama 已装但服务未跑。打开一个**独立 PowerShell 窗口**（保持开启，不要关）：

```powershell
ollama serve
```

看到 `Listening on 127.0.0.1:11434` 就成功了。**这个窗口不要关**，关了 Ollama 就停。

> 💡 想要 Ollama 开机自启？Win+R → `shell:startup` → 放一个 `start_ollama.bat`，内容：`ollama serve`

### 步骤 2 — 拉 embedding 模型

另开一个 PowerShell 窗口（让步骤 1 那个继续跑）：

```powershell
ollama pull nomic-embed-text
```

这是一个 **274 MB** 的开源 embedding 模型，拉完会存在本地。
- 768 维向量
- 支持多语言（含中文）
- 质量接近 OpenAI `text-embedding-3-small`

拉完验证：
```powershell
ollama list
# 应该看到 nomic-embed-text
```

### 步骤 3 — 测试 Ollama 能响应

```powershell
curl http://localhost:11434/api/embeddings -d '{\"model\":\"nomic-embed-text\",\"prompt\":\"hello\"}'
```

返回一个长向量就说明 Ollama + 模型 OK。

---

## 三、安装 Copilot 插件

### 步骤 4 — 在 Obsidian 里装插件

1. Obsidian → 设置 (Ctrl+,) → **第三方插件**
2. 关闭"安全模式"（如果开着）
3. **浏览** → 搜索 `Copilot` → 找 **"Copilot"** by **Logan Yang**（7k+ 下载）
4. Install → Enable

> ⚠️ 注意作者：有多个 copilot 插件，要选 **Logan Yang** 的，不是 "Smart Connections" 或 "TextGenerator"。

### 步骤 5 — 打开 Copilot 面板

Ctrl+P 命令面板 → 搜 `Copilot: Open Copilot Chat` → 回车。右侧会出现聊天面板。

---

## 四、配置 Chat 模型（Claude 中转）

**设置 → Copilot Settings → Models → Chat Models → "Add Custom Model"**

填写：

| 字段 | 值 |
|---|---|
| **Model Display Name** | `Claude Sonnet 4.6 (中转)` |
| **Model Name** | `[K]claude-sonnet-4-6` |
| **Provider** | `OpenAI Format`（下拉里选） |
| **Base URL** | `http://bruder.yukinoapi.com/v1` |
| **API Key** | 从 `99_SystemScripts/auto_reg_index/.env` 里的 `ANTHROPIC_API_KEY` 复制 |
| **Enable CORS** | ✅ 勾上（有些中转需要） |

保存后，把这个模型拖到 "Chat Models" 列表第一位，设为默认。

> ⚠️ **重要**：`Model Name` 必须带 `[K]` 前缀，否则中转拒绝（probe 已验证）。

### 验证 Chat
在 Copilot Chat 面板输入：`你好，简短回复 OK` → 回车。
- 看到 `OK` 或类似 → ✅ 成功
- 看到 502 或 model_not_found → ⚠️ 检查 Model Name 前缀

---

## 五、配置 Embedding 模型（Ollama 本地）

**设置 → Copilot Settings → Models → Embedding Models → "Add Custom Model"**

填写：

| 字段 | 值 |
|---|---|
| **Model Display Name** | `Nomic Embed (local)` |
| **Model Name** | `nomic-embed-text` |
| **Provider** | `Ollama`（下拉里选） |
| **Base URL** | `http://localhost:11434` |
| **API Key** | 留空 |

保存 → 拖到 Embedding Models 列表第一位 → 设为默认。

> 💡 **Ollama 必须在跑**（步骤 1 的那个窗口），否则 Copilot 建索引时会报 `ECONNREFUSED`。

---

## 六、建 Vault QA 向量索引

### 步骤 6 — 首次索引

Ctrl+P → `Copilot: Index vault for QA`

Copilot 会扫描所有 1429 条 notes，用 nomic-embed-text 转成向量。

预期耗时：**5-15 分钟**（看 CPU 性能，本地运行）。期间可以看到进度条。

完成后索引存在 `.obsidian/plugins/copilot/vault-qa-index.json`（或类似路径）。

### 步骤 7 — 切换到 Vault QA 模式

Copilot 面板顶部有下拉，三种模式：
- **Chat**：普通对话（不搜 vault）
- **Vault QA**：每次问题都先搜 vault 再回答 ← **主要用这个**
- **Copilot Plus**：付费功能（暂不用）

选 **Vault QA**，问一条：
```
GB 4785 规定了什么？
```

Copilot 应该：
1. 用 embedding 检索相关 notes
2. 把相关 notes 内容 + 你的问题喂给 Claude
3. 返回带引用的回答

### 步骤 8 — 增量更新索引

以后你新加了 notes，不需要重建全部，只需：

Ctrl+P → `Copilot: Refresh vault index` → 只处理改动过的文件

---

## 七、推荐的 Custom Prompts

**设置 → Copilot → Custom Prompts**（或 Ctrl+P 搜 "custom prompts"）

以下是适配 CcVault 的几个 prompt 模板。**复制整段**贴到 custom prompts 里：

### Prompt 1 — 总结选中法规
```
标题: 法规摘要
Prompt: 请基于选中文本（一条汽车法规 note），生成一段 120 字以内的中文摘要。
要求：
1. 第一句：这条法规管什么（M/N/O 类？哪个系统？）
2. 第二句：核心技术要求 2-3 条
3. 第三句：与国际标准的等价关系（ECE/ISO），如果有

选中文本：
{{selection}}
```

### Prompt 2 — 检查 frontmatter 合规
```
标题: FM 合规检查
Prompt: 这是一条 CcVault 法规 note。请检查它的 frontmatter 是否合规。
参考 schema: 02_Schema/03_frontmatter_schema.md

检查点：
- reg_id 格式
- title / title_en 是否填齐
- region / topic / status 有效值
- scope / dates / confidence 是否合理

输出：合规 | 有问题（列出哪条、建议改什么）

Note 全文：
{{activeFile}}
```

### Prompt 3 — 跨区域对比
```
标题: 跨区域对标
Prompt: 基于 vault 里的现有 notes，对比选中法规跟对应国际标准的异同。
输出结构：
1. 选中法规的 reg_id 与核心要求
2. 对应 ECE/ISO/EU 标准（从 03_Equivalence/ 找等价关系）
3. 3-5 条技术差异（数值、范围、实施时间）
4. 引用 wikilinks

选中法规：
{{selection}}
```

### Prompt 4 — 生成 audit 候选
```
标题: 发现问题
Prompt: 你正在审查这条 CcVault 法规 note。如果发现任何问题（摘要错、FM 字段缺失、分类可疑、等价映射错），输出一个或多个 audit 条目（YAML 格式）。
如果看起来没问题，回答 "无问题"。

audit 模板：
---
target_file: <path>
target_reg_id: <reg_id>
severity: critical|high|medium|low
category: accuracy|completeness|classification|link|formatting|other
status: open
issue: <问题描述>
expected: <期望状态>
---

Note 全文：
{{activeFile}}
```

---

## 八、日常使用场景

### 场景 A — 读法规时问问题
1. 打开任意 note（比如 `GB 4785-2019.md`）
2. Ctrl+P → `Copilot: Open Copilot Chat` 切到 Vault QA 模式
3. 直接问："这条法规跟 ECE R48 的主要差异是什么？"
4. Copilot 会搜相关 notes 并答，附 wikilinks

### 场景 B — 选中一段快速操作
1. 在 note 里选中一段文字
2. 右键 → Copilot → 选预设动作（summary / translate / rewrite）
3. 或者 Ctrl+P → "Copilot: Apply custom prompt to selection"

### 场景 C — 全 vault 搜索 + 回答
- 问："所有关于刹车的法规里，哪条的实施日期最晚？"
- Copilot 用 Vault QA 搜所有含刹车的 notes，读它们的 dates 字段，排序回答

### 场景 D — 发现 note 有问题
1. 用 Prompt 4 让 Copilot 生成 audit 候选
2. 复制输出的 YAML
3. 在 Obsidian 里 `Alt+N` → 选 audit 模板 → 用 Copilot 给的内容填充
4. 累积后用 Cascade 跑 `/process_audits`

---

## 九、故障排查

| 症状 | 可能原因 | 解决 |
|---|---|---|
| Chat 返回 502 | 中转模型名错 | 确认 `[K]claude-sonnet-4-6` 前缀 |
| Chat 返回 "model_not_found" | 渠道被删 | 联系中转提供方换渠道 |
| Embedding 建索引时 "ECONNREFUSED" | Ollama 没跑 | 确认 `ollama serve` 那个窗口还在 |
| Embedding "model not found" | 没拉模型 | `ollama pull nomic-embed-text` |
| Vault QA 回答不相关 | 索引老旧或模型差 | 重建索引 / 换 bge-m3 更好（`ollama pull bge-m3`） |
| 回答都是英文 | system prompt 没带中文要求 | 在 Copilot 设置里加 "请用中文回答" 到 system prompt |
| API key 泄露 | `.env` 被提交 git | `.gitignore` 已保护；用户误发 issue 截图需注意 |

---

## 十、与 CcVault 协同要点

### Copilot 能做
- ✅ 问答（RAG）：问任何法规相关的问题
- ✅ 选中文本改写、翻译、总结
- ✅ 生成 audit 候选（用上面的 Prompt 4）
- ✅ 辅助写新 note（用 Template + 问 Copilot 补齐）

### Copilot **不能**做
- ❌ 运行 Python 脚本（`_cluster_topics.py`, `_qc_full.py` 等）
- ❌ 跑 `.windsurf/workflows/*.md` 里的 workflow（需要 Cascade 或 Claude Code）
- ❌ 大规模重构（比如批量改 200 个 notes 的 topic）
- ❌ 访问 `00_Raw/标准库/` 里的 PDF 源文件（Copilot 只看 markdown）

### 绝不要让 Copilot 做
- ❌ 批量 `delete`（它会"很乐意"帮你删文件）
- ❌ 直接改 `manifest.json` 或 `.stage4/` 下的索引文件
- ❌ 改 `CLAUDE.md` 或 `02_Schema/` 下的权威文档（这些要人审核）

---

## 十一、备选 Embedding（如果 Ollama 不想用）

| 方案 | 成本 | 代理要求 | 推荐度 |
|---|---|---|---|
| **Ollama nomic-embed-text** | 0 | 无 | ★★★★★（本指南） |
| **Ollama bge-m3** | 0 | 无 | ★★★★（更大更准，568 MB） |
| 智谱 GLM `embedding-3` | ¥0.5/M tokens | 无 | ★★★（需额外 key） |
| Cohere `embed-multilingual-v3` | 免费 1000/月 | 需代理 | ★★ |
| OpenAI `text-embedding-3-small` | $0.02/M | 需代理 | ★（你没 OpenAI key） |

---

## 附录 — 参考

- 插件主页：https://github.com/logancyang/obsidian-copilot
- Ollama 官方：https://ollama.com
- nomic-embed 模型卡：https://huggingface.co/nomic-ai/nomic-embed-text-v1.5
- 中转接口：见 `99_SystemScripts/auto_reg_index/.env` 里的 `ANTHROPIC_BASE_URL`

---

**维护者**：当中转模型名变更（比如渠道换了），记得更新本文件第四节的 Model Name。
