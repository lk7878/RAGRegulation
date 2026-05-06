---
description: 修正 note 分类错误 - 单条或批量修正 topic，同时更新 _cluster_topics.py 规则防止复发
---

# /fix_classification — 修正分类错误

## 触发场景

用户发现某条 note 或某批 notes 的 `topic/<key>` tag 错了。

典型用户表达：
- "GB 5135-2003 分到 fire_fighting_equipment 里了，但它是消防车用喷水器材"
- "所有 ECE R113 类都分到 lighting_signaling 了，但这类其实是前照灯 specific，应该单独"
- "这 10 条 GB/T XXX 系列应该分到 test_methods 不是 special_vehicles"

## 执行步骤

### 1. 定位错误样本

如果用户给的是单条：直接 `find_by_name` 定位。

如果是一批：先让用户列出几个典型样本，然后：
```powershell
# 查看当前 tag 分布
Get-Content "D:\CcVault\01_Wiki\regulations\<region>\<reg_id>.md" -First 30 | Select-String "topic/"
```
// turbo

### 2. 分析根因

**两种修法，必须二选一**：

**Case A：规则级错误**（推荐修规则）
- 多条同类 notes 都错了
- 有共同 pattern（某 reg_id 段 / 某关键词）
- 未来还会有同类入库
→ **修 `_cluster_topics.py` 的 TOPICS 字典**

**Case B：单条异常**（手改 tag）
- 就 1-2 条错
- 没有可归纳的 pattern（比如 title 特殊）
- 改规则会误伤其他正确分类
→ **直接改 note tags，并记录在"手工例外名单"**

用户没说清 → **主动问**哪种情况。

### 3. Case A：修规则

打开 `D:\CcVault\99_SystemScripts\auto_reg_index\_cluster_topics.py`

找到 `TOPICS` 字典，修改对应主题的规则：
```python
TOPICS = {
    "fire_fighting_equipment": {
        "label": "消防器材",
        "keywords": [r"消防", r"灭火", r"喷水"],
        # 新增排除规则
        "exclude_keywords": [r"消防车.*照明", r"消防车.*信号"],
        ...
    },
    "lighting_signaling": {
        # 新增优先匹配
        "priority_reg_ids": [r"^GB 5135"],  # 明确归入
        ...
    },
}
```

注意：
- 原脚本可能没有 `exclude_keywords` / `priority_reg_ids` 参数 → **先读源码**确认 API
- 改完规则要跑一遍看影响面

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _cluster_topics.py
```
// turbo

看输出的变化数字。

### 4. Case B：手改单条

直接编辑 note FM：
```yaml
tags:
  - reg/cn
  - type/version
  - status/verified
  - topic/<CORRECT_topic_key>   # 改这一行
```

**并且**在脚本顶部或一份独立文件记录：
```python
# _cluster_topics.py
MANUAL_OVERRIDES = {
    "GB 5135-2003": "lighting_signaling",  # 虽然含"消防"但实为消防车照明
    ...
}
```

然后在聚类逻辑里加：
```python
if reg_id in MANUAL_OVERRIDES:
    return MANUAL_OVERRIDES[reg_id]
```

### 5. 跑聚类 + 重生成主题页

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _cluster_topics.py
.\.venv\Scripts\python.exe _write_topic_pages.py
```
// turbo

### 6. 验证影响面

```powershell
# 看被影响的 notes 数量
.\.venv\Scripts\python.exe _stage2_stats.py

# 确认错分样本现在的 tag
Get-Content "D:\CcVault\01_Wiki\regulations\<region>\<reg_id>.md" -First 30 | Select-String "topic/"
```
// turbo

### 7. 重建索引

```powershell
.\.venv\Scripts\python.exe _semantic_search.py --rebuild
```
// turbo

### 8. 报告

```markdown
# 分类修正报告

## 问题根因
- 场景：<Case A 规则 / Case B 单条>
- 根因：<具体说明>

## 修改内容
- 文件：`@99_SystemScripts/auto_reg_index/_cluster_topics.py` (若 Case A)
- 规则变更：<diff 描述>
- 或 notes 手改：<文件列表>

## 影响面
- <N> 条 notes 重新分类
  - <topic_A> → <topic_B>: N1 条
  - <topic_C> → <topic_B>: N2 条
- 涉及主题页：`<topic>.md`（已重生成）

## 验证
- 典型样本 <reg_id> 现在的 topic = <new_topic> ✓
- 整体 stats 无明显恶化 ✓
- BM25 索引已重建 ✓
```

## 禁止事项

1. ❌ 不要改规则但不跑 cluster —— 否则 notes 的 tag 不会同步
2. ❌ 不要规则 + 手改混着来 —— 手改会被规则覆盖
3. ❌ 不要为了修一条错误引入更复杂的规则 —— 单条问题用 MANUAL_OVERRIDES
4. ❌ 不要删除 `misc` 主题（如果存在）—— 可能有兜底作用；先确认它为空
