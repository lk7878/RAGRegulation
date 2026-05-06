---
description: 批量处理 05_Audit/ 下所有 open audits - 读取、定位、修改、标记 resolved
---

# /process_audits — 批量处理 audit 反馈

## 触发场景

用户在 `05_Audit/` 累积了若干 audit 条目，要求 agent 统一处理。典型表达：
- "/process_audits"
- "处理一下 audit"
- "把 audit 里的问题都改了"
- "audit: process the open comments"

---

## 执行步骤

### 1. 扫描所有 open audits

```powershell
Get-ChildItem D:\CcVault\05_Audit -Filter "*.md" | 
    Where-Object { $_.Name -notmatch "^(_|README)" } |
    ForEach-Object {
        $content = Get-Content $_.FullName -First 30 | Out-String
        if ($content -match "status:\s*open") {
            Write-Host $_.Name
        }
    }
```
// turbo

统计：
- 总 open 数
- 按 severity 分布（critical / high / medium / low）
- 按 category 分布

### 2. 排序处理优先级

**处理顺序**（严格遵守）：
1. `severity: critical` 先处理
2. `severity: high` 次之
3. `severity: medium` 再次
4. `severity: low` 最后

同 severity 内按 `created` 时间升序（先进先出）。

### 3. 按 target_file 分组

同一个 note 上的多条 audit **合并处理**（一次读 note + 一次写回），节省 token。

### 4. 告诉用户计划

```markdown
# /process_audits 计划

待处理 audits: N 条
  - critical: N1
  - high: N2
  - medium: N3
  - low: N4

涉及 M 个 notes:
  - GB 4785-2019.md (3 audits)
  - ECE R48.md (1 audit)
  - ...

预计耗时: ~5-30 分钟（取决于涉及 notes 数量）

开始处理？
```

### 5. 处理每一条 audit

对每个 target_file：

#### 5a. 标记 in_progress
```yaml
status: in_progress
```
（可选 —— 批处理时可跳过此步直接 resolved）

#### 5b. 读 audit 完整内容
- `target_file` / `target_reg_id` / `target_section` / `target_anchor`
- `severity` / `category`
- Issue 段 + Expected 段

#### 5c. 定位目标 note
- 打开 `D:\CcVault\<target_file>`
- 如果有 `target_section`，跳到该 section
- 如果有 `target_anchor`，在 section 内 grep 原文片段

#### 5d. 评估 Issue 的有效性

**必须做**：
- 如果 agent 读原文发现 audit 的 Issue 描述**不准确**（例如用户记错了），**不要**盲目改
- 标 `status: wont_fix` 并在 Resolution 里解释为什么

**标准情况**：
- 原文确实有问题 → 按 Expected 改

#### 5e. 修改 note

按 audit category 执行对应操作：
- `accuracy` → 改 body 里的错误表述
- `completeness` → 补充缺失内容
- `classification` → 改 FM 的 tags（topic/status）+ 同步 `_cluster_topics.py` 若是规则级问题
- `link` → 改 wikilinks / supersedes / equivalent_to
- `formatting` → 调整排版

#### 5f. 更新 audit 为 resolved

在原 audit 文件里修改：
```yaml
---
...原有字段...
status: resolved
resolved: 2026-04-19T14:30:00
resolver: cascade
tags:
  - audit/resolved       # 改
  - audit/severity-...   # 保持
  - audit/category-...   # 保持
---

## Issue
（保持不变）

## Expected
（保持不变）

## Resolution

<填写：实际改了什么。举例>
- 在 GB 4785-2019.md 摘要段"适用于 M 类车辆" 改为 "适用于 M/N/O 类车辆"
- 参考原文 Section 1.1

## Related
（保持）
```

### 6. 重建索引（若涉及）

若处理过程中改动了：
- FM 字段（tags / region / status）→ 必须 `_semantic_search.py --rebuild`
- supersedes / equivalent_to → 必须 `_build_supersession_chain.py`
- 主题聚类规则 → 必须 `_cluster_topics.py` + `_write_topic_pages.py`

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _daily_maintenance.py --only-index
```
// turbo

### 7. 追加到 _CHANGELOG.md

如果本次处理 >= 5 条 audits 或有 critical/high 级别被修复，追加一条变更日志：

```markdown
## <YYYY-MM-DD> · Audit 批量处理

**类型**：修复

**变更**：
- 处理 N 条 audits（critical: X, high: Y, medium: Z, low: W）
- 涉及 M 个 notes
- 典型修复：<2-3 个代表性例子>

**未解决**：
- N 条标为 wont_fix（原因: <简述>）
```

### 8. 报告用户

```markdown
# Audit 处理报告

## 总览
- 总处理: N 条
- resolved: X
- wont_fix: Y
- 跳过（audit 本身无效）: Z

## 按严重度
- critical: X/X ✓
- high: X/X ✓
- medium: X/X ✓
- low: X/X ✓

## 涉及文件
- `@<file_path>` — <N> audit 修复，主要改动：<简述>
- ...

## wont_fix 说明
- `@<audit_path>` — <为什么不改>

## 索引重建
- BM25: ✓
- Supersession: ✓（如涉及）
- Topic clustering: ✓（如涉及）

## 剩余 open audits
- <如有 severity=low 被跳过的，列出>

## 建议
- <如本批发现普遍问题，建议加规则 / 改 cluster_topics / 建 dashboard 等>
```

---

## 处理规则

### ✅ Agent 应该

1. **严格按 Issue + Expected 改** — 不要脑补扩展修改范围
2. **保留 audit 完整历史** — 不删除 resolved audits，留作版本记录
3. **遇到不确定时标 `status: needs_clarification`** 而不是猜测
4. **同一个 note 上的多 audit 一起改** — 合并 I/O
5. **改动后跑索引重建** — 保证查询层一致

### ❌ Agent 禁止

1. **不要批量标 wont_fix** — 每条都要 Resolution 里说清楚原因
2. **不要删 audit 文件** — 即使 duplicate 也保留（指向原始 audit 即可）
3. **不要修改 audit 原有的 Issue / Expected 段** — 那是用户的原始反馈，保留
4. **不要跳过 critical / high** —— 除非标 wont_fix 并说明
5. **不要扩大修改范围** — 只改 audit 指出的问题，其他问题用户会另建 audit

---

## 批量模式 vs 单条模式

### 批量模式（默认）
- 用户说 `/process_audits` 无参数
- Agent 读所有 open 的 audits，全处理
- 耗时：5-30 分钟，取决于数量

### 单条模式
- 用户说 `/process_audits <filename>` 或 `/process_audits critical`
- Agent 只处理符合条件的 audits
- 耗时：<1 分钟

### 预览模式（dry-run）
- 用户说 `/process_audits --dry-run`
- Agent 列出会改什么但不实际改
- 用于评估影响面

---

## 成本估算

- 单条 audit 处理：~¥0.01-0.05（DeepSeek）
- 一批 20 条：~¥0.5
- 涉及重建索引：额外 25-40 秒但 0 成本

---

## 与其他 workflow 的关系

- **`/fix_classification`**：如果多条 audits 都是分类错误且有共同 pattern，改用 `/fix_classification` 做规则级修复
- **`/weekly_check`**：巡检时会统计 audit 积压数量
- **`/ingest`**：新 PDF 入库不自动处理 audits，用户需要显式触发
