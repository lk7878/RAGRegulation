---
type: graphrag_moc
generated_by: stage5_orchestrator
updated: 2026-04-19
tags:
  - type/moc
  - stage/5
  - graphrag
---

# GraphRAG 社区索引 MOC

> Stage 5 · GraphRAG · 基于 **Louvain 算法** 把 1,429 条 notes 构成的关系图划分为若干主题社区，每个社区由 **DeepSeek V3** 生成深度综述（800–1500 字，含关系结构、同类对比、矛盾议题）。
>
> 与 37 个人工 topic 的区别：**topic** 按关键词规则分组（工程师心智），**community** 按显式关系边分组（版本链 / 采标 / 引用 / 替代）。二者互补。

---

## 如何使用

### 场景 1 · 想快速了解某领域的整体格局
用 `_graphrag_search.py` 做 **层级检索**：先命中相关社区 → 读综述 → 跳到具体 note。

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _graphrag_search.py "乘用车制动系统要求"
```

返回 top-3 相关社区 + 每个社区内 top-5 最相关 notes。

### 场景 2 · 直接浏览某社区
从下方列表点进去即可。社区综述含：
1. **成员总览**（按区域/类型分类列出所有成员）
2. **内部关系结构**（文字 + mermaid 图）
3. **同类对比**（差异分析）
4. **矛盾与未解议题**
5. **相关查询示例**

### 场景 3 · 重建社区（新 PDF 入库后）

```powershell
.\.venv\Scripts\python.exe stages/s5_graphrag.py          # 完整 pipeline
.\.venv\Scripts\python.exe stages/s5_graphrag.py --skip-build --skip-communities --force  # 只重跑 LLM 综述
```

---

## 全部社区清单（按成员数降序）

```dataview
TABLE WITHOUT ID
  community_id AS "#ID",
  label AS "主题",
  member_count AS "成员",
  edge_count AS "边",
  top_region AS "区域",
  file.link AS "综述"
FROM "04_Topics/communities"
WHERE type = "graphrag_community"
SORT member_count DESC
```

---

## 按主导主题分组

```dataview
TABLE WITHOUT ID
  top_topic AS "主题",
  length(rows) AS "社区数",
  sum(rows.member_count) AS "总成员"
FROM "04_Topics/communities"
WHERE type = "graphrag_community"
GROUP BY top_topic
SORT length(rows) DESC
```

---

## 技术指标

| 指标 | 数值 |
|---|---:|
| 图节点数 | 1,399 |
| 图边数 | 288 |
| 社区总数（初检测） | 1,163 |
| `ready` 社区（size ≥ 3） | 33 |
| `too_small` 社区（size < 3） | 1,130 |
| 进入社区的 notes | 229（16%） |
| 平均社区大小 | 6.9 |
| 最大社区 | 23 节点 |
| 算法 | Louvain（networkx `louvain_communities`） |
| Resolution | 1.0 |
| LLM provider | DeepSeek V3 (deepseek-chat) |
| 生成成本 | **$0.065**（33 社区，含幻觉 retry） |
| 生成耗时 | 5 分 38 秒（5 并发） |

> **覆盖率 16%** 的说明：当前图只有 288 条边（包括 supersedes / equivalent_to / references），大部分 notes 是孤立节点。后续补充更多跨区等价映射后，覆盖率会提升。

---

## 脚本

| 脚本 | 职责 |
|---|---|
| `_build_graph.py` | Step 1 · 从 FM 抽出关系边，构建 NetworkX 图 |
| `_graphrag_communities.py` | Step 2 · Louvain 社区检测 + 大社区递归拆分 |
| `_graphrag_summarize.py` | Step 3 · 每社区调 DeepSeek / Claude 生成综述 |
| `_graphrag_search.py` | Step 4（查询时）· 层级检索（社区 + 成员） |
| `stages/s5_graphrag.py` | Orchestrator · 一键跑 Step 1→3 |

---

## 相关文档

- [[_Topics MOC]] — 37 个人工主题索引（可与本 MOC 互补）
- [[_Equivalence MOC]] — 62 条跨区域等价映射
- `@D:\CcVault\CLAUDE.md` — Agent 操作手册 §6.x GraphRAG 小节
