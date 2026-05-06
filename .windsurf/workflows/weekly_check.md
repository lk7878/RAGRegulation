---
description: 每周健康巡检 - 检查数据质量、索引一致性、MOC 完整性，输出体检报告
---

# /weekly_check — 每周健康巡检

## 触发场景

用户请求例行检查，或首次接手维护前的全面体检。典型表达：
- "帮我巡检一下库"
- "这周库有啥异常吗"
- "健康度怎么样"

## 执行步骤

### 1. 基础数字盘点

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index

# 总数
Write-Host "regulations: $((Get-ChildItem D:\CcVault\01_Wiki\regulations -Recurse -Filter '*.md').Count)"

# 按区域
Get-ChildItem D:\CcVault\01_Wiki\regulations -Directory | ForEach-Object {
    $count = (Get-ChildItem $_.FullName -Recurse -Filter '*.md').Count
    Write-Host "  $($_.Name): $count"
}

# 主题数
Write-Host "topics: $((Get-ChildItem D:\CcVault\04_Topics -Recurse -Filter '*.md').Count)"

# Dashboards
Write-Host "dashboards: $((Get-ChildItem D:\CcVault\00_Dashboards -Recurse -Filter '*.md').Count)"
```
// turbo

### 2. 置信度分布

```powershell
.\.venv\Scripts\python.exe _stage2_stats.py
```
// turbo

检查：
- `high` 比例 >= 70% ✓
- `low` 比例 <= 10% ✓
- `status/verified` tag >= 85% ✓

若恶化 → 标记需处理。

### 3. Manifest 一致性

检查是否有 manifest 里记了但 vault 里缺的 notes：

```powershell
.\.venv\Scripts\python.exe _manifest_sync.py --check-only
```
// turbo

若有 drift → 下次跑 `--fix`。

### 4. Wikilinks 失效检查

```powershell
# 找红色 wikilinks（指向不存在的文件）
# Obsidian 原生只在界面显示，命令行可写个快速 checker

$allLinks = @()
Get-ChildItem D:\CcVault\01_Wiki\regulations -Recurse -Filter '*.md' | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $matches = [regex]::Matches($content, '\[\[([^\]|]+)(\|[^\]]+)?\]\]')
    foreach ($m in $matches) {
        $allLinks += [PSCustomObject]@{
            Source = $_.Name
            Target = $m.Groups[1].Value
        }
    }
}

# 检查每个 target 是否存在
$existingStems = Get-ChildItem D:\CcVault -Recurse -Filter '*.md' | 
    ForEach-Object { $_.BaseName } | Select-Object -Unique
$broken = $allLinks | Where-Object { $_.Target -notin $existingStems }
Write-Host "Broken wikilinks: $($broken.Count)"
$broken | Select-Object -First 20
```
// turbo

### 5. MOC 完整性

**Topics MOC**：
```powershell
# 检查每个 Topic 文件是否在 _Topics MOC.md 里有链接
$mocContent = Get-Content "D:\CcVault\04_Topics\_Topics MOC.md" -Raw
$topicFiles = Get-ChildItem "D:\CcVault\04_Topics\*.md" | Where-Object { $_.Name -ne "_Topics MOC.md" }
foreach ($tf in $topicFiles) {
    if ($mocContent -notmatch [regex]::Escape($tf.BaseName)) {
        Write-Host "MISSING in Topics MOC: $($tf.Name)"
    }
}
```
// turbo

**Equivalence MOC**：检查 62 条映射都还有效（被映射的 notes 还存在）。

### 6. Orphan Notes（无引用的 notes）

```powershell
# 找既不被任何其他 note 引用、也不被 MOC 索引的 notes
# 这是可疑信号（可能是手工新增但忘更新 MOC）
```

### 7. 替代链健康

```powershell
# 检查 superseded_by 是否都有对应目标
.\.venv\Scripts\python.exe _build_supersession_chain.py --dry-run 2>&1 | Select-String "BROKEN|MISSING"
```
// turbo

### 8. BM25 索引时效性

```powershell
$indexFile = "D:\CcVault\99_SystemScripts\auto_reg_index\.stage5\bm25_index.pkl"
$lastNote = Get-ChildItem D:\CcVault\01_Wiki\regulations -Recurse -Filter '*.md' | 
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
$indexAge = (Get-Item $indexFile).LastWriteTime
$noteAge = $lastNote.LastWriteTime

if ($noteAge -gt $indexAge) {
    Write-Host "STALE INDEX: Last note $($lastNote.Name) edited $noteAge > index $indexAge"
    Write-Host "Recommend: run _semantic_search.py --rebuild"
}
```
// turbo

### 9. Logs 滚动

```powershell
# 超过 30 天的 log 建议清理
$oldLogs = Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\*.log | 
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) }
Write-Host "Old logs (>30d): $($oldLogs.Count) files, $([math]::Round(($oldLogs | Measure-Object Length -Sum).Sum / 1MB, 1)) MB"
```
// turbo

### 10. Staging 缓存大小

```powershell
$stagingSize = (Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\.staging -Recurse -File | 
    Measure-Object Length -Sum).Sum / 1MB
Write-Host "Staging: $([math]::Round($stagingSize, 1)) MB"
```
// turbo

### 11. 输出体检报告

```markdown
# CcVault 每周体检报告 — <YYYY-MM-DD>

## 基础数字
- regulations: X (cn: X, ece: Y, ...)
- topics: 37
- dashboards: 10
- equivalence mappings: 62

## 数据质量
- high confidence: X% (目标 >=70%) <✓/✗>
- low confidence: X% (目标 <=10%) <✓/✗>
- verified tags: X% (目标 >=85%) <✓/✗>

## 一致性
- broken wikilinks: N (建议修复前 5: ...)
- MOC missing entries: N
- supersession chain broken: N
- BM25 index freshness: <up-to-date / STALE>

## 维护建议
1. ... (按优先级排序)

## 无异常项
- ✓ 置信度指标全绿
- ✓ 无 orphan notes
- ✓ staging 缓存合理（X MB）
```

### 12. 自动修复建议

如果发现问题，**询问用户**是否要自动修复：
- 失效 wikilinks → 列出并逐个处理
- MOC 漏项 → 运行 `_write_topic_pages.py`
- BM25 过期 → 运行 `_daily_maintenance.py --only-index`
- 老 logs → 清理超过 30 天的

**不要**未经用户同意批量改动。

## 执行时长估计

- 全量检查：约 2-5 分钟
- 仅数字盘点 + 置信度：<30 秒

## 结果去向

可选：把体检报告追加到 `D:\CcVault\99_SystemScripts\auto_reg_index\logs\health_YYYY-MM-DD.md`，方便翻历史趋势。
