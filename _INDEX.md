---
type: master_index
updated: 2026-04-19
tags:
- type/index
---

# CcVault · 全局主索引

> 知识库的**单一真源导航**。无论谁（你、未来的 agent、新 AI 工具）要理解或操作本库，从这里开始。
> 对应 Karpathy LLM Wiki 的 `wiki/index.md` 概念。

---

## 🏃 1 分钟认识 CcVault

**定位**：全球汽车法规结构化知识库 · Obsidian vault · 元数据驱动
**规模**：1429 条法规 notes · 37 主题 · 62 跨区域映射 · 10 活面板
**状态**：87.4% verified · Phase 2 复核完成
**建设成本**：¥102 / $14.33

---

## 📚 主要文档

### 给用户看（你自己）

| 文档 | 路径 | 用途 |
|---|---|---|
| 使用说明 | `@D:\CcVault\_使用说明.md` | ★ **从这里开始**。14 章 + 附录 |
| 维护指南 | `@D:\CcVault\99_SystemScripts\auto_reg_index\_MAINTENANCE.md` | 一键脚本 + Task Scheduler |
| 项目 README | `@D:\CcVault\README.md` | 概览 + 目录结构 |
| 变更日志 | `@D:\CcVault\_CHANGELOG.md` | 人读版月度变更 |

### 给 Agent 看（Claude Code / Cascade / Cursor / ...）

| 文档 | 路径 | 用途 |
|---|---|---|
| Agent 操作手册 | `@D:\CcVault\CLAUDE.md` | ★ Agent 必读。FM schema + 规则 + 禁令 |
| FM 权威 schema | `@D:\CcVault\02_Schema\03_frontmatter_schema.md` | 字段定义 |
| 设计文档 | `@D:\CcVault\02_Schema\DESIGN.md` | 整体架构 |
| Taxonomy | `@D:\CcVault\02_Schema\02_taxonomy.md` | 主题 + 区域分类 |
| Pipeline README | `@D:\CcVault\99_SystemScripts\auto_reg_index\README.md` | 脚本系统 |

---

## 🗂️ 核心资产入口

### 法规 Notes（1429 条）

| 路径 | 数量 | 说明 |
|---|---:|---|
| `@D:\CcVault\01_Wiki\regulations\cn\` | 462 | GB / GB/T 中国国标 |
| `@D:\CcVault\01_Wiki\regulations\ece\` | 959 | UN / ECE 联合国法规 |
| `@D:\CcVault\01_Wiki\regulations\eu\` | 若干 | EU Framework + Directives |
| `@D:\CcVault\01_Wiki\regulations\us\` | 若干 | FMVSS + NHTSA |
| `@D:\CcVault\01_Wiki\regulations\jp\` | 若干 | 日本安保基准 |
| `@D:\CcVault\01_Wiki\regulations\kr\` | 若干 | 韩国 KMVSS |
| 其他 | 若干 | asean/gcc/ru-eaeu/in/br/au/za/cl/th |

### 非法规命名空间

| 路径 | 数量 | 说明 |
|---|---:|---|
| `@D:\CcVault\02_Wiki\non_automotive\` | 9 | 自行车/塔吊/工业仪器/消防水带 |
| `@D:\CcVault\02_Wiki\references\` | 6 | 书籍/内部文档 |

### 学术文献 Zettelkasten（新增 2026-04-22）

| 路径 | 数量 | 说明 |
|---|---:|---|
| `@D:\CcVault\01_Wiki\literature\papers\` | 0 | 文献笔记 LN（一篇一条，待入库）|
| `@D:\CcVault\01_Wiki\literature\concepts\` | 0 | 原子笔记 PN（主张/方法/概念）|
| `@D:\CcVault\01_Wiki\literature\mocs\` | 0 | 主题地图 MOC |

**文档**：
- `@D:\CcVault\01_Wiki\literature\README.md` — namespace 概览
- `@D:\CcVault\02_Schema\literature_schema.md` — FM schema 权威定义

**模板**（Alt+N 插入）：
- `@D:\CcVault\02_Schema\templates\literature_note.md`
- `@D:\CcVault\02_Schema\templates\concept_note.md`
- `@D:\CcVault\02_Schema\templates\moc_note.md`

---

## 🧭 3 大导航层（MOC）

| MOC | 内容 | 入口 |
|---|---|---|
| 主题索引 | 37 个技术主题索引页 + 综述 + 跨区域速查 | `@D:\CcVault\04_Topics\_Topics MOC.md` |
| 等价映射 | 62 条 GB ↔ ECE/EU/ISO 对应 | `@D:\CcVault\03_Equivalence\_Equivalence MOC.md` |
| 活面板 | 10 个 Dataview 动态查询 | `@D:\CcVault\00_Dashboards\_Dashboards MOC.md` |

---

## 🎯 10 个 Dashboard

按优先级：

1. `@D:\CcVault\00_Dashboards\_Needs_Review.md` — 低置信度复核清单
2. `@D:\CcVault\00_Dashboards\_By_Region_Latest.md` — 各区最近 20 条
3. `@D:\CcVault\00_Dashboards\_Emissions_Watch.md` — 排放跟踪
4. `@D:\CcVault\00_Dashboards\_EV_BEV_Watch.md` — 新能源/电池
5. `@D:\CcVault\00_Dashboards\_Supersession_Chains.md` — 替代链
6. `@D:\CcVault\00_Dashboards\_Cross_Region_Matrix.md` — 跨区域对标
7. `@D:\CcVault\00_Dashboards\_Recent_Amendments.md` — 最近 3 月 Am
8. `@D:\CcVault\00_Dashboards\_High_Confidence_Index.md` — 高质量索引
9. `@D:\CcVault\00_Dashboards\_Graph_Insights.md` — 关系网分析（静态）
10. `@D:\CcVault\00_Dashboards\_Semantic_Search.md` — BM25 使用说明

---

## 🤖 5 个 Agent Workflow

在 Cascade / Claude Code 里用 `/slash` 调用：

| 命令 | 文件 | 用途 |
|---|---|---|
| `/ingest` | `@D:\CcVault\.windsurf\workflows\ingest.md` | 新 PDF 入库 + 变化报告 |
| `/add_note` | `@D:\CcVault\.windsurf\workflows\add_note.md` | 手动新增法规 note |
| `/fix_classification` | `@D:\CcVault\.windsurf\workflows\fix_classification.md` | 修正分类错误 |
| `/weekly_check` | `@D:\CcVault\.windsurf\workflows\weekly_check.md` | 健康巡检 |
| `/process_audits` | `@D:\CcVault\.windsurf\workflows\process_audits.md` | 批量处理人工反馈 audit |

## 🔍 Audit Loop（人工反馈闭环）

阅读 notes 时发现错误：
1. 在 `05_Audit/` 建条 audit 条目（模板：`05_Audit/_template.md`）
2. 累积后 `/process_audits` 批量处理

入口：`@D:\CcVault\05_Audit\_Audit MOC.md`
Templater 配置：`@D:\CcVault\02_Schema\06_audit_templater_setup.md`

---

## Obsidian Copilot（日常 RAG + 轻编辑入口）

配置：`@D:\CcVault\02_Schema\07_obsidian_copilot_setup.md`

**分工**：
- **Copilot** ← 日常问答、选中段落改写、生成 audit 候选（90% 场景）
- **Cascade** ← `/process_audits`, `/weekly_check`, 索引重建（复杂维护）
- **Python scripts** ← batch pipeline（全自动处理）

---

## GraphRAG 社区索引（Stage 5 · 2026-04 新增）

**入口**：`@D:\CcVault\04_Topics\communities\_Communities MOC.md`

Louvain 算法自动把 1,429 条 notes 的关系图划分为 **33 个主题社区**（均 6.9 节点），每个社区由 DeepSeek V3 生成 **800–1500 字深度综述**（成员总览 + 关系结构 + mermaid 图 + 同类对比 + 矛盾议题）。

**层级检索**：

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _graphrag_search.py "乘用车制动系统要求"
```

返回 top-K 社区（含综述预览）+ 每社区内 top-N 最相关 notes。

---

## ReAct Agent · 自然语言问答（Stage 5 · 2026-04 新增）

**入口**：`D:\CcVault\99_SystemScripts\auto_reg_index\_agent_chat.py`

把 12 个查询工具（BM25 / GraphRAG / 统计 / 版本链 / 等价映射 / 审计）暴露给 LLM，让 LLM **自主编排调用**回答复杂问题（包括统计题、全量扫描、多步推理）。

**三种接入方式**：

```powershell
# 1. 终端 CLI
.\.venv\Scripts\python.exe _agent_chat.py "国六排放相关的社区里有多少条中国法规"
.\.venv\Scripts\python.exe _agent_chat.py            # REPL 对话

# 2. HTTP 服务（给 Obsidian Copilot 用，OpenAI 兼容）
.\.venv\Scripts\python.exe _agent_server.py          # http://127.0.0.1:7777/v1

# 3. MCP Server（给 Cascade / Claude Desktop / Cursor 用）
#    不手动跑，各客户端配置文件里指定启动命令后自动 spawn
```

默认用 DeepSeek V3，每次查询成本 ≈ $0.001–0.007。详见 `agent/README.md`。

---

## 🛠️ Pipeline 脚本（30+）

位置：`@D:\CcVault\99_SystemScripts\auto_reg_index\`

### 最常用
- `_daily_maintenance.py` — ★ 一键维护
- `_semantic_search.py` — BM25 检索
- `_graphrag_search.py` — GraphRAG 层级检索
- `_agent_chat.py` — ★ ReAct Agent（自然语言问答）
- `ingest.py` — 完整 pipeline CLI

### 数据建设
- `stages/s0_ocr.py` / `stages/s1_extract.py`
- `_backfill_titles.py` / `_run_cross_check.py` / `_reclassify_false_mismatches.py`

### 导航层
- `_cluster_topics.py` / `_write_topic_pages.py`
- `_extract_topic_equivalences.py` / `_write_equivalence_page.py` / `_apply_equivalences_to_notes.py`
- `_build_supersession_chain.py`

### Stage 5
- `_build_graph.py` / `_graph_analytics.py`

### 辅助
- `_stage2_stats.py` / `_topic_digest.py` / `_qc_full.py`
- `_manifest_sync.py` / `_fix_existing_notes.py` / `_migrate_non_automotive.py`

---

## 🎬 从零起步（新 agent 必读顺序）

1. 读本文件 `_INDEX.md`（整体地图）
2. 读 `CLAUDE.md`（agent 操作手册）
3. 读 `_使用说明.md`（用户视角）
4. 读 `02_Schema/03_frontmatter_schema.md`（数据契约）
5. 扫最近一次 `99_SystemScripts/auto_reg_index/logs/maintenance_*.log`（近况）
6. 准备接受用户任务

---

## 📊 数据质量快照（定期更新）

| 指标 | 数值 | 目标 |
|---|---:|---|
| regulations total | 1429 | - |
| high confidence | 70.4% | ≥70% ✓ |
| medium confidence | 22.9% | - |
| low confidence | 6.0% | ≤10% ✓ |
| unknown confidence | 0.6% | ≤1% ✓ |
| verified tag | 87.4% | ≥85% ✓ |

---

## 🔗 外部参考

- [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) — 开源参考实现
- [Obsidian Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf) — 可选抓取工具

---

**最后校对**：2026-04-19
**下次自动更新建议**：每完成一次重大 pipeline 变更后
