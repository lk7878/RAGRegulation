# CcVault Agent Operating Manual

> 本文件是 **AI agent（Claude Code / Cascade / Cursor / Codex / Gemini CLI / 任何支持 filesystem 的 agent）** 维护本知识库时的操作手册。
> 基于 [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。
> 用户文档请读 [`_使用说明.md`](_使用说明.md)。

---

## 1. Vault 是什么

**CcVault** = 全球汽车法规结构化知识库。
- **1429** 条汽车法规 notes（`01_Wiki/regulations/`）
- **62** 条跨区域等价映射
- **37** 个技术主题索引
- **87.4% verified** 数据质量

定位：**元数据驱动 + 工程师视角的主题导航 + 跨区域对标**。
**不是** PDF 全文仓库，**不是** 百科全书。

---

## 2. 目录结构（Agent 必读）

```
D:\CcVault\
├── 00_Dashboards\          10 个 Dataview 活面板
├── 00_Raw\标准库\          源 PDF 只读备份（OCR 入口）
├── 01_Wiki\regulations\    【核心资产】1429 条汽车法规 notes
│   ├── cn\   462 条 GB / GB/T
│   ├── ece\  959 条 UN / ECE
│   ├── eu\ us\ jp\ kr\ au\ br\ asean\ gcc\ ru-eaeu\ in\ cl\ za\ th\
├── 02_Schema\              ★ Schema 权威文档
│   ├── DESIGN.md                     完整设计
│   ├── 02_taxonomy.md                主题/区域 taxonomy
│   ├── 03_frontmatter_schema.md      FM 字段定义（权威！）
│   └── 04_self_check_rules.md        数据自检规则
├── 02_Wiki\                非法规命名空间（15 条已剥离）
│   ├── non_automotive\     9 条（自行车/塔吊/工业仪器…）
│   └── references\         6 条（书籍/内部文档）
├── 03_Equivalence\         62 条 GB ↔ ECE/EU/ISO 映射 + MOC
├── 04_Topics\              37 个主题索引页 + MOC
│   └── communities\        33 个 GraphRAG 社区综述（Louvain + LLM 生成）
├── 99_SystemScripts\
│   └── auto_reg_index\     Python pipeline
├── README.md
├── _使用说明.md            ★ 用户指南
└── CLAUDE.md               ★ 本文件（agent 必读）
```

---

## 3. FM Schema（每条 note 必备）

**权威定义**：[`02_Schema/03_frontmatter_schema.md`](02_Schema/03_frontmatter_schema.md)

**简版速查**（agent 写新 note 时必须填齐）：

```yaml
---
# ─── 身份（必填）───
reg_id: GB 4785-2019              # 规范化唯一编号
title: 汽车及挂车外部照明...       # 中文/本地语
title_en: Prescription for ...     # 英文（若有）
type: version                      # regulation / version / amendment
region: cn                         # cn/ece/eu/us/jp/kr/...

# ─── 时间（强烈建议）───
status: active                     # active/superseded/under_revision/draft/withdrawn
publication_date: 2019-05-14
implementation_date: 2020-01-01

# ─── 关系（按需）───
supersedes:
  - GB 4785-2007                   # 列 reg_id，会被 wikilink 解析
superseded_by: []                  # 脚本自动双向维护，手工别填
equivalent_to:                     # 脚本自动从主题页提取
  - ref: ECE R48 Rev6
    relation: equivalent           # equivalent/adopts_from/aligned_with/partial
    source: "04_Topics/lighting_signaling"

# ─── 内容（建议）───
summary: 规定 M/N/O/L 类车辆...    # 2-3 句摘要
scope: 适用于 ...                  # 适用范围
keywords: [外部照明, 前照灯]       # 关键词

# ─── 元信息 ───
source_pdf: _ingest/cn/GB 4785-2019.pdf
cross_check_overall_confidence: high   # high/medium/low/unknown
cross_check_flags: []
tags:
  - reg/cn                         # reg/<region>
  - type/version                   # type/<type>
  - status/verified                # status/verified | status/needs-review
  - topic/lighting_signaling       # topic/<topic_key>（见 _cluster_topics.py TOPICS）
---

# <reg_id> <title>

## 摘要
...
## 范围
...
## 关键要求
...
## 试验与验证
...
```

---

## 4. Agent 最常用的命令速查

### 4.1 搜索已有内容

```powershell
# 精确找某 reg_id
Get-ChildItem -Path D:\CcVault\01_Wiki\regulations -Recurse -Filter "GB 4785*.md"

# 按关键词语义搜索
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _semantic_search.py "前照灯 LED" --topic lighting_signaling

# GraphRAG 层级检索（先命中相关社区，再在社区内做细粒度）
.\.venv\Scripts\python.exe _graphrag_search.py "乘用车制动系统要求"

# ★ ReAct Agent（自然语言问任何问题，包括统计/全量/多步推理）
.\.venv\Scripts\python.exe _agent_chat.py "vault 里有多少条中国法规？brakes 主题多少条？"
.\.venv\Scripts\python.exe _agent_chat.py            # REPL 对话模式

# ★ Agent HTTP 服务（给 Obsidian Copilot 用，OpenAI 兼容）
.\.venv\Scripts\python.exe _agent_server.py          # 127.0.0.1:7777
# 然后 Obsidian Copilot 加 custom model: base_url=http://127.0.0.1:7777/v1

# ★ Agent MCP Server（给 Cascade / Claude Desktop / Cursor 用）
.\.venv\Scripts\python.exe _agent_mcp.py             # stdio 通信，不手动跑

# 按 FM 字段查（Dataview 运行时）
# 或命令行：
.\.venv\Scripts\python.exe _semantic_search.py "EMC" --region cn --min-confidence high
```

### 4.2 触发 pipeline

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index

# 完整维护（新 PDF 后）
.\.venv\Scripts\python.exe _daily_maintenance.py

# 只重建索引（手改 note 后）
.\.venv\Scripts\python.exe _daily_maintenance.py --only-index

# 干跑（规划）
.\.venv\Scripts\python.exe _daily_maintenance.py --dry-run
```

### 4.3 单步脚本（排查问题时）

| 脚本 | 用途 |
|---|---|
| `_backfill_titles.py --also-dates --also-status` | 补 FM 缺失字段 |
| `_run_cross_check.py --provider deepseek` | 质量复核 |
| `_reclassify_false_mismatches.py` | 规则降级假告警 |
| `_cluster_topics.py` | 重跑主题聚类 |
| `_write_topic_pages.py` | 重生成主题页 |
| `_build_supersession_chain.py` | 更新双向链 |
| `_semantic_search.py --rebuild` | 重建 BM25 |
| `_stage2_stats.py` | 置信度分布统计 |
| `_build_graph.py` | 构建 `.stage5/graph.json`（GraphRAG Step 1） |
| `_graphrag_communities.py` | Louvain 社区检测（GraphRAG Step 2） |
| `_graphrag_summarize.py` | LLM 生成社区综述（GraphRAG Step 3） |
| `_graphrag_search.py "<query>"` | GraphRAG 层级检索（查询时） |
| `stages/s5_graphrag.py` | GraphRAG 一键 orchestrator |
| `_agent_chat.py "<question>"` | ★ ReAct Agent · 自然语言问任何问题（12 tools） |
| `_agent_server.py` | Agent HTTP 服务（OpenAI 兼容，Obsidian Copilot 接入） |
| `_agent_mcp.py` | Agent MCP Server（Cascade / Claude Desktop / Cursor 接入） |
| `agent/` | ReAct agent 实现目录（tools/ server.py mcp_server.py） |

---

## 5. Agent 操作规则

### ✅ Agent 应该做

1. **新增 note** — 按第 3 节 FM schema 填齐，放到 `01_Wiki/regulations/<region>/`
2. **修正 note 内容** — 改 body 或 FM 某字段
3. **修正分类错误** — 同时改 note tags + `_cluster_topics.py` 规则（防未来再错）
4. **添加 equivalence 映射** — 先更新主题页的"跨区域速查"段，再跑 `_extract_topic_equivalences.py` + `_apply_equivalences_to_notes.py`
5. **维护 MOC** — 新增/删除 note 后，确保 Topics MOC / Equivalence MOC / Dashboards 仍可解析
6. **跑维护脚本** — 每次重大改动后跑 `_daily_maintenance.py --only-index` 保证索引一致
7. **记录操作** — 在 `logs/` 下追加日志；重大结构变动更新 `_使用说明.md`

### ❌ Agent 禁止做

1. **不要改 `manifest.json`** 手动 —— 它是 OCR hash ↔ PDF 映射的唯一凭据，只能通过 pipeline 写
2. **不要重命名文件** 而不更新 wikilinks —— Obsidian 按 stem 解析，改名会大面积失效
3. **不要删除 historical versions** —— 老法规要保留并标 `status: superseded`
4. **不要混非法规到 `01_Wiki/regulations/`** —— 非汽车标准放 `02_Wiki/non_automotive/`
5. **不要在 `01_Wiki/regulations/` 下创建子目录** —— 只有 region 级子目录，不能再嵌套
6. **不要手改 `superseded_by` 字段** —— 脚本自动从 `supersedes` 反向生成
7. **不要在 `.stage*` 缓存目录里放重要文件** —— 随时可能被清除
8. **不要 commit `.env`** —— 已在 `.gitignore` 中
9. **不要假设用户装了插件** —— 除非 `_使用说明.md` 明确标"必装"（Dataview）
10. **不要批量删除或重命名文档** —— 尤其是根目录下的 `_*.md`、`CLAUDE.md`、`README.md`。如确需删除，先确认用户同意，并建议 **先备份到 `.trash/`** 而非直接删除

---

## 6. 常见任务的标准姿势

### 6.1 用户说"新增一条法规"

调用 workflow：`.windsurf/workflows/add_note.md`

或手动：
1. 确认 `reg_id` 唯一性（`grep` 已有 notes）
2. 读源 PDF（若有）或用户描述
3. 按 FM schema 写 `01_Wiki/regulations/<region>/<reg_id>.md`
4. 若替代了老版本 → 老版本 FM 加 `status: superseded` + `superseded_by: [<new_reg_id>]`
5. 若等价某外国法规 → 更新 `04_Topics/<topic>.md` 的"跨区域速查"段
6. 跑 `_daily_maintenance.py --only-index` 重建索引
7. 告诉用户："已新增 X；替代链更新 Y 条；索引已重建"

### 6.2 用户说"帮我对比 GB 4785 和 ECE R48"

1. `grep_search "GB 4785"` + `grep_search "ECE R48"` → 找到 note 文件
2. 读这两个 note 的 FM + body
3. 读对应主题页 (`04_Topics/lighting_signaling.md`) 看"跨区域速查"
4. 读 `03_Equivalence/_Equivalence MOC.md` 看 relation
5. 综合回答，引用 `@<file_path>:<lines>` 格式

### 6.3 用户说"库里总共多少 ECE 法规？"

**不要凭印象**，运行：
```powershell
(Get-ChildItem -Path D:\CcVault\01_Wiki\regulations\ece -Filter "*.md" -Recurse).Count
```
或者跑 Dataview 查询。

### 6.4 用户说"分析最近 3 个月的 ECE Am"

1. 打开 `00_Dashboards/_Recent_Amendments.md` 看 DQL 查询
2. 或用 `find_by_name` + FM 解析:
```powershell
# 手工查（若无 Dataview）
Get-ChildItem D:\CcVault\01_Wiki\regulations\ece\*.md -Recurse | 
  ForEach-Object { 
    $fm = Get-Content $_ -First 30 | Out-String
    if ($fm -match "publication_date:\s*(\d{4}-\d{2}-\d{2})") {
      [PSCustomObject]@{ File=$_.Name; Date=$matches[1] }
    }
  } | Where-Object { $_.Date -gt "2026-01-19" } | Sort-Object Date -Descending
```

### 6.5 用户说"有 N 条 note 分类错了"

1. 读用户描述的错误样本
2. 找出共同 pattern（某 reg_id 段？某关键词？）
3. 改 `_cluster_topics.py` 的 `TOPICS` 字典 —— 加新规则
4. 跑 `_cluster_topics.py` + `_write_topic_pages.py`
5. `_stage2_stats.py` 看是否改善
6. 告诉用户变化数字

---

## 7. 数据质量守则

### 置信度分布（目标）
- `high` >= 70%
- `low` <= 10%
- `verified` tag >= 85%

### 任何改动后的自检
agent 改完库后必须：
1. 检查改过的 note FM 完整（reg_id/title/region/status 必须非空）
2. 检查 wikilinks 没失效（改名后要全局替换引用）
3. 跑 `_stage2_stats.py` 看质量指标没恶化
4. 跑 `_semantic_search.py --rebuild` 保证索引同步

---

## 8. 成本意识

- DeepSeek V3：$8.55 已花，$0.27/M input tokens
- Baidu OCR：¥19 已花，每天免费 500 次
- Anthropic：**不要**用于批量任务，只用于复杂推理（~$3/M tokens）
- Gemini 2.5 Pro：可用于长上下文（~$1.25/M）但你还没配

**预算哲学**：能用规则就不用 LLM；能用 DeepSeek 就不用 Claude/Gemini。

---

## 9. Agent 会话开始时的必读清单

agent 每次被召唤做 CcVault 相关任务时，**先读**：
1. `_INDEX.md`（全局地图 —— 先看这里知道库里有什么）
2. 本文件 `CLAUDE.md`（整体认知）
3. `_使用说明.md`（用户视角）
4. `02_Schema/03_frontmatter_schema.md`（FM 权威）
5. `_CHANGELOG.md`（近期变更 —— 了解库的最新动向）
6. 最近一次的 `99_SystemScripts/auto_reg_index/logs/maintenance_*.log`（技术近况）

---

## 10. Agent 可调用的 Workflows

定义在 `.windsurf/workflows/` 下（Windsurf / Cascade 原生支持 `/slash` 调用；其他 agent 可读文件内容作为 prompt）：

| Workflow | 何时用 |
|---|---|
| `/ingest` | 用户把新 PDF 放入 `00_Raw/` 后 |
| `/add_note` | 用户要求新增一条法规 note |
| `/fix_classification` | 发现 N 条 note 分类错误 |
| `/weekly_check` | 周期性健康巡检 |
| `/process_audits` | 批量处理 `05_Audit/` 下人工反馈 |

---

## 12. Audit Loop（人工反馈闭环）

**位置**：`05_Audit/`

### 用途
用户阅读 notes 时发现错误，不中断阅读而是**留条 audit 条目**，累积后让 agent 批量处理。

### 目录约定
```
05_Audit/
├── _Audit MOC.md              # 面板 + 说明
├── _template.md               # 模板
├── README.md                  # 快速上手
└── <YYYY-MM-DD>_<brief>.md    # 实际 audit 条目
```

### Audit 文件 FM
```yaml
---
target_file: 01_Wiki/regulations/<region>/<reg_id>.md
target_reg_id: <reg_id>
target_section: ""           # 可选
target_anchor: ""            # 可选，原文片段

severity: medium             # critical | high | medium | low
category: accuracy           # accuracy | completeness | classification | link | formatting | other
status: open                 # open | in_progress | resolved | wont_fix | duplicate

created: YYYY-MM-DDTHH:mm:ss
resolved: null
resolver: null

tags:
  - audit/open
  - audit/severity-<level>
  - audit/category-<cat>
---

## Issue
<用户描述问题>

## Expected
<用户期望的修正>

## Resolution
<agent 处理后填>

## Related
<可选>
```

### Agent 处理规则

见 `@D:\CcVault\.windsurf\workflows\process_audits.md` 完整规则。核心：

1. **严格按 Issue + Expected 改** —— 不扩大修改范围
2. **保留原 Issue/Expected 段** —— 只加 Resolution
3. **同 note 多 audit 合并处理** —— 省 I/O
4. **改完跑索引重建**
5. **不删 audit 文件** —— 即使 wont_fix/duplicate 也保留

### 严重度优先级

critical > high > medium > low（严格按此顺序处理）

### 与 needs-review tag 的区别

| 机制 | 触发方 | 用途 |
|---|---|---|
| `status/needs-review` tag | **机器**（Pipeline 置信度算法） | 自动发现的低置信度 |
| `cross_check_flags` 字段 | **机器**（LLM 校对） | 自动发现的元数据异常 |
| `05_Audit/` | **人工** | 人类阅读时发现的问题 |

三个渠道互补，覆盖不同类型的质量问题。

---

## 12. 多 Agent 分工（2026-04 现状）

本 vault 目前使用三层 agent 协作维护。Agent 读本文件时应理解自己的角色：

### 12.1 分工表

| 工具 | 主战场 | 能做什么 | **不该**做什么 |
|---|---|---|---|
| **Obsidian Copilot**（插件，Logan Yang 版） | 日常 90% 场景 | RAG 问答、选中文本改写/总结、生成 audit 候选、辅助写新 note | 跑 Python 脚本、执行 workflow、批量 edit、改 schema |
| **Cascade / Claude Code**（本工具） | 10% 复杂场景 | `/process_audits`、`/ingest`、`/weekly_check`、索引重建、schema 修改 | 做 Copilot 能做的琐碎问答（浪费） |
| **Python scripts**（`99_SystemScripts/auto_reg_index/`） | 全自动 pipeline | 大规模抽取、分类、cross-check、QC（batch API） | 无人值守做内容编辑（只做机械处理） |

### 12.2 Copilot 配置状态

- ✅ Chat: `[K]claude-sonnet-4-6` via `http://bruder.yukinoapi.com/v1`（中转）
- ✅ Embedding: `nomic-embed-text` via 本地 Ollama（免费离线）
- ✅ 插件：`logancyang/obsidian-copilot`（免费版）
- 📖 配置指南：`@02_Schema/07_obsidian_copilot_setup.md`

### 12.3 工作流判断

**如果用户请求…**
- "帮我问一下 XX 法规怎么说" → 建议他用 **Copilot Vault QA**，不要自己费 Cascade 配额
- "处理一下积累的 audits" → **本工具（Cascade）直接跑 /process_audits**
- "重建索引" → **本工具跑 Python 脚本**
- "改 50 个 notes 的 topic" → **本工具分批跑**，不用 Copilot（它不自主）

---

## 13. Extension Points（未来扩展建议）

若用户决定升级，以下路径可由 agent 主导实施：

- **向量检索升级到 bge-m3**：更大模型，多语言更强（`ollama pull bge-m3`，改 Copilot 配置）
- **GraphRAG**：用 `.stage5/graph.graphml` 做关系增强检索
- **Agent Tool Use**：用 Claude/OpenAI function calling 把现有脚本封装为 tools
- **MCP servers**：为 Cascade/Claude Code 写 CcVault 专属 MCP（搜索、lint、统计）

---

**最后更新**：2026-04-19（加入 Obsidian Copilot 分工）
**Maintainer**：Cascade (你当前会话的 agent)
**参考**：[Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · [second-brain 参考实现](https://github.com/NicholasSpisak/second-brain)
