---
description: 新 PDF 入库 - 检测 raw 目录新文件，跑完整 pipeline，报告变化
---

# /ingest — 新 PDF 入库

## 触发场景

用户把一批新 PDF 放入 `D:\CcVault\00_Raw\标准库\<region>\` 后调用本 workflow。

## 执行步骤

### 1. 入库前快照

读取并告诉用户当前库状态：
- 统计 `01_Wiki/regulations/` 各 region 的文件数
- 检查 `manifest.json` 里 pending / ocr_done 文件数
// turbo

### 2. 干跑检查

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _daily_maintenance.py --dry-run
```
// turbo

确认：
- 会 OCR 的文件数
- 预计成本（DeepSeek + Baidu OCR）
- 会跑的后续步骤

### 3. 向用户确认

如果预计成本超过 ¥10，**先问用户是否继续**；否则直接跑。

### 4. 完整跑 pipeline

```powershell
.\.venv\Scripts\python.exe _daily_maintenance.py
```

该命令会自动跑：
- 阶段 A · Ingest（OCR + Extract + Write）
- 阶段 B · Quality（Cross-check + 假告警降级）
- 阶段 C · Navigation（聚类 + 主题页 + 等价 + supersession）
- 阶段 D · Indices（Graph + BM25）
- 阶段 E · 变化报告

### 5. 读日志摘要

找到最新的日志文件并读 tail 50 行：
```powershell
Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\maintenance_*.log | 
    Sort-Object LastWriteTime -Descending | Select-Object -First 1 | 
    ForEach-Object { Get-Content $_.FullName -Tail 50 }
```
// turbo

### 6. 抽查新 note 质量

对新入库的 3 条 note（按 publication_date DESC 或 manifest state=extracted 的最新）：
1. 读 FM 检查 reg_id / title / region / status / publication_date 是否完整
2. 检查 `cross_check_overall_confidence` 字段
3. 检查 tags 是否含 `topic/<key>`

如果有任何字段缺失或 confidence=low，标记给用户。

### 7. 报告

用以下格式给用户：

```markdown
# Ingest 完成报告

## 数字变化
- regulations: X → Y (+N)
- cn: X → Y / ece: X → Y / 其他 regions: ...
- topics: 37 → 37 (no structure change)

## 新入库（前 5 条）
1. <reg_id> <title> — confidence: <high/medium/low>
2. ...

## 需要关注
- X 条 low-confidence（建议人工复核）
- Y 条 title 缺失（已标 status/needs-review）
- Z 条触发了 continuation pass（超长文档）

## 新发现的跨区域映射（如有）
- GB XXX ↔ ECE RXX (relation=equivalent)

## 后续建议
- 查看 `00_Dashboards/_Needs_Review.md` 处理 low-confidence
- 若某条明显错分 → 调用 /fix_classification
```

### 8. （可选）向量索引重建

如果用户之前启用了向量检索（`.stage5/embeddings.npy` 存在）：
```powershell
.\.venv\Scripts\python.exe _embed_notes.py --incremental
```
否则跳过。

## 失败处理

- **OCR 失败**：读 `logs/` 看哪个文件；检查 PDF 是否损坏
- **DeepSeek API 失败**：等 10 分钟重试；确认 `.env` key 有效
- **manifest 损坏**：不要手动改；建议用户从 git 恢复

## 成本参考

- 10 条新 PDF ≈ ¥0.7
- 100 条 ≈ ¥7
- 1000 条 ≈ ¥70
