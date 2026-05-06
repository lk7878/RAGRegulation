---
type: dashboard
purpose: semantic_search_howto
stage: 5b
tags:
- type/dashboard
- stage/5b
- search/bm25
---

# 语义检索（Stage 5b · BM25 + jieba）

> 零 GPU / 零 API 成本的本地检索工具。适合"按意图找法规"的场景。
> 位置：`@D:\CcVault\99_SystemScripts\auto_reg_index\_semantic_search.py`

## 快速开始

```bash
cd D:\CcVault\99_SystemScripts\auto_reg_index

# 1. 基础查询
.\.venv\Scripts\python.exe _semantic_search.py "国六 轻型车 排放"

# 2. 按主题过滤
.\.venv\Scripts\python.exe _semantic_search.py "ALKS 车道保持" --topic adas_driver_assist

# 3. 按区域过滤
.\.venv\Scripts\python.exe _semantic_search.py "儿童约束" --region cn --limit 5

# 4. 只看高可信度
.\.venv\Scripts\python.exe _semantic_search.py "EMC 电磁兼容" --min-confidence high

# 5. 强制重建索引（schema 变动时）
.\.venv\Scripts\python.exe _semantic_search.py --rebuild
```

## 典型查询示例

| 查询 | Top 命中 |
|---|---|
| `"国六 轻型车 排放"` | `GB 18352.6-2016`（国六 b 限值） |
| `"ALKS lane keeping automated"` (+ adas 过滤) | `ECE R157 Am4` / `Rev1 Am3` 全家族 |
| `"儿童约束 ISOFIX 安全座椅"` | `GB 14166-2024`, `GB 14167-2013`, `GB 27887-2024` |
| `"动力电池 热失控"` | `GB 38031-2020`, `GB/T 31467.3-2015` |
| `"转向 EPS 电动助力"` | `GB 17675` + ECE R79 家族 |
| `"前照灯 LED"` | `ECE R112`, `R113`, `GB 4599-2024` |

## 检索原理

**BM25 评分** = `f(term_frequency, inverse_document_frequency, document_length)`

字段权重（通过重复 token 实现）：
- `reg_id` × 3
- `title` × 3
- `title_en` × 2
- `topic` × 1
- `scope` × 1
- `summary` × 1

**分词**：`jieba.cut_for_search` 中文切词 + 英文 whitespace/正则

## 与其它检索路径对比

| 方法 | 适用场景 | 速度 |
|---|---|---|
| **文件名 / reg_id 直达** | 知道精确法规号 | 即时 |
| **Obsidian 全文搜索 (Ctrl+Shift+F)** | 找 body 中某关键词 | <1s |
| **Dataview DQL（[[_Dashboards MOC]]）** | 按 FM 字段过滤/排序 | 实时 |
| **BM25 语义检索（本工具）** | 按意图 / 主题 / 功能找 | ~0.5s |
| **向量检索（未启用）** | 语义相似 / 陌生主题发现 | 需 embedding 基础设施 |

## 索引状态

- **Corpus**: 1429 notes（迁出 15 条非法规后）
- **Index size**: `.stage5/bm25_index.pkl` ~3MB
- **Rebuild trigger**: 
  - 新增 notes 到 `01_Wiki/regulations/`
  - Stage 4 聚类重跑（topic 变化）
  - FM schema 重大改动

## 何时升级到向量检索

当前 BM25 足够时的信号：
- ✅ 能通过关键词组合找到目标
- ✅ 主题/区域过滤后结果准确率 >80%

考虑升级到 embedding 的信号：
- ❌ 想做"这条法规相似的有哪些"
- ❌ 跨语言查询（中文 query → 英文 ECE 结果）
- ❌ 自动发现新的跨区域等价关系
- ❌ 做 RAG 聊天（查询 → 检索 → LLM 综合答案）

如需升级，推荐路径：
- 本地 `BAAI/bge-small-zh-v1.5`（免费，~100MB，Chinese-optimized）
- 或 DashScope `text-embedding-v3`（~¥0.7/1M tokens，云端稳定）

## 脚本

- `_semantic_search.py` — 本工具
- 索引：`.stage5/bm25_index.pkl`
- 依赖：`rank_bm25==0.2.2`, `jieba==0.42.1`（已在 venv）
