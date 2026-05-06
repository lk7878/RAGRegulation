# 给导师的阅读指南 · CcVault 汽车法规知识库

> 这是一份持续迭代的**汽车法规结构化知识库**的打包快照（2026-04-23）。  
> 以下指南帮助您在 **5 分钟**内了解这个库的结构和亮点。

---

## 1. 用什么打开？

**推荐**：[Obsidian](https://obsidian.md/)（免费，开源笔记工具）

### 最快路径（2 分钟）
1. 安装 Obsidian
2. 在 Obsidian 里选 "Open folder as vault"，选中解压出来的 `CcVault/` 目录
3. 首次打开会提示是否启用第三方插件 → **选"启用"**（否则 Dashboard 无法看）
4. 打开 `_INDEX.md` 作为入口

### 纯文本也能看
如果不想装 Obsidian，所有 `.md` 文件都是纯 Markdown 文本，用 VS Code / 记事本都能打开。但 Dashboard 页（`00_Dashboards/`）里的 Dataview 查询块只是一行代码，不会自动渲染。

---

## 2. 先看哪 4 份文档（15 分钟快速了解）

| 优先级 | 文件 | 看什么 |
|---|---|---|
| 1 | `_INDEX.md` | 整体地图 + 规模 + 核心资产入口 |
| 2 | `_MINERU_UPGRADE_LOG.md` | 最新一次升级（MinerU 云 OCR）的成果与技术细节 |
| 3 | `_CHANGELOG.md` | 按日期倒序的变更日志（近期重要迭代）|
| 4 | `_完整手册.md` | 系统设计完整说明（3 万字，可选）|

如果要看**今日成果**：直接看 `_CHANGELOG.md` 最上方的"2026-04-22~23 · MinerU 云 OCR 升级 Day 1-2"。

---

## 3. 核心资产在哪

### 3.1 法规知识库（1414 条）

```
01_Wiki/regulations/
├── ece/       ← 951 条 UN-ECE 法规
├── cn/        ← 443 条国标（GB / GB/T）
├── eu/        ← 6 条 EU 指令
├── us/        ← 3 条 FMVSS
├── jp/kr/au/...  ← 其他区域
└── _mineru_assets/  ← 图片 / 图表资产（MinerU 升级产物）
```

**每条 note 的结构示例**（以 `ECE R13-H` 为例）：

- YAML FrontMatter 元数据：`reg_id`, `region`, `topic`, `status`, `publication_date`, `equivalent_to`, `supersedes` / `superseded_by`, `_mineru_blocks` 等
- **中文摘要**（LLM 生成的 2-3 句话快速说明）
- 适用范围 / 关键条款 / 试验要求（结构化字段）
- **原文参考（MinerU 云解析）** ← 今日 Phase 2 升级新增，含原 PDF 的表格 / 公式 / 图像

### 3.2 Dashboard（可视化总览）

`00_Dashboards/` 下有 10+ 个 Dataview 面板：

| 面板 | 用途 |
|---|---|
| `_Dashboards MOC.md` | 面板总索引 |
| `_MinerU_Upgrades.md` | 本次 MinerU 升级专属面板（进度 / 富信息 notes / 主题覆盖）|
| `_High_Confidence_Index.md` | 高置信度 note 列表 |
| `_Regulations_by_Region.md` | 按区域分布 |
| `_Regulations_by_Topic.md` | 按主题（37 个细分主题）分布 |

**Dashboard 用 Dataview 实时查询**，所以数字是自动计算的、永远与 FM 同步。

### 3.3 结构化关系

- `03_Equivalence/` — 跨区域等价映射 MOC（例如 ECE R13 ↔ GB 12676）
- `04_Topics/` — 37 个主题页（每个主题下的法规自动归类）
- `05_Audit/` — 数据质量审计记录

---

## 4. 技术亮点（一句话版）

1. **全量 LLM 结构化**：1444 个 PDF → 1414 条 YAML + Markdown note，自动提取 `reg_id`/`topic`/`status`/`equivalent_to` 等 20+ 字段
2. **双层检索**：BM25 全文 + GraphRAG 社区聚类（33 个社区，基于 `supersedes`/`equivalent_to`/`references` 关系图 Louvain 聚类）
3. **MinerU 云 OCR 补齐**（本次迭代重点）：把原 pipeline 丢失的 **2,036 个表格 / 1,353 个公式 / 2,284 张图** 增量补回 note 正文，不破坏原摘要
4. **MCP 工具层**（`ccvault` server）：19 个工具暴露给 LLM 直接调用（`search_regulations_bm25` / `get_equivalence` / `get_supersession_chain` 等）
5. **每日自维护**：`_daily_maintenance.py` 自动重建索引 + 置信度复检 + MOC 同步

---

## 5. 数据规模（截至打包时刻）

| 类别 | 数量 |
|---|---:|
| 法规 notes 总数 | **1,414** |
| 已 MinerU 升级（含表/公式/图） | **595** (42%) |
| ECE / 国标 / 其他 | 951 / 443 / 20 |
| 37 个主题分类 | 100% 覆盖 |
| 跨区域等价映射 | ~220 组 |
| GraphRAG 社区数 | 33 |

---

## 6. 本次打包不含什么

| 不含 | 原因 |
|---|---|
| `00_Raw/` 1444 个原始 PDF（1.86 GB） | 版权 & 体积 |
| `99_SystemScripts/` pipeline 源码 | 如需审阅技术实现，我可以单独提供 |
| MinerU 原始 OCR 中间产物（2.5 GB） | 中间产物，已全部合并入 notes |
| API key / token / 虚拟环境 | 敏感信息，必须剔除 |

如需其中任何一项，请告知我。

---

## 7. 快速演示建议路径（如果要现场展示）

1. 打开 `_INDEX.md`（1 分钟看规模）
2. 跳到 `00_Dashboards/_MinerU_Upgrades.md`（看升级量化成果）
3. 随机点开一条 ECE 重点法规（如 `ECE R13-H.md`）→ 看摘要 + 原文参考段
4. 跳到 `04_Topics/brakes.md`（看主题聚合）
5. 最后回 `_CHANGELOG.md` 看迭代时间线

---

**联系**：任何问题随时反馈。
