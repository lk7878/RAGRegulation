---
type: maintenance_guide
tags:
- type/guide
- scope/maintenance
---

# CcVault 维护指南

> 一键维护脚本 `_daily_maintenance.py` 的使用与自动化配置。

## 一、脚本概览

**位置**：`D:\CcVault\99_SystemScripts\auto_reg_index\_daily_maintenance.py`

**能做什么（5 阶段）**：

| 阶段 | 内容 | 触发条件 |
|---|---|---|
| **A · Ingest** | OCR 新 PDF → Extract → Write | manifest 里有 pending / ocr_done |
| **B · 质量复核** | 补字段 + Cross-check + 假告警降级 | 有新 note |
| **C · 导航层** | 聚类 + 主题页 + 等价映射 + 替代链 | 总是跑（幂等） |
| **D · 索引层** | Graph + BM25 重建 | 总是跑 |
| **E · 变化报告** | 前后快照对比 | 总是跑 |

**日志**：自动写到 `99_SystemScripts/auto_reg_index/logs/maintenance_<ts>.log`

## 二、日常使用模式

### 模式 1：有新 PDF 要入库（完整跑）

把新 PDF 放到 `D:\CcVault\00_Raw\标准库\<region>\` 后：

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _daily_maintenance.py
```

**耗时估算**：
- 10 条新 PDF：约 5-10 分钟，成本 ~¥0.7
- 100 条：约 30-60 分钟，成本 ~¥7

### 模式 2：库内无新 PDF，只想刷新索引（快）

手工编辑过 note 后想重建索引：

```powershell
.\.venv\Scripts\python.exe _daily_maintenance.py --only-index
```

耗时：约 25 秒（只跑 Graph + BM25）

### 模式 3：周末快跑（跳过 LLM，省钱）

```powershell
.\.venv\Scripts\python.exe _daily_maintenance.py --skip-llm
```

跳过 OCR / Extract / Cross-check 等 API 调用，只跑规则化的步骤（聚类 / 映射 / 索引）。

### 模式 4：干跑检查

```powershell
.\.venv\Scripts\python.exe _daily_maintenance.py --dry-run
```

列出会做什么，不实际执行。

## 三、参数速查

| 参数 | 作用 |
|---|---|
| `--dry-run` | 只列计划不执行 |
| `--skip-ingest` | 跳过阶段 A |
| `--skip-llm` | 跳过所有 LLM 调用 |
| `--skip-quality` | 跳过阶段 B |
| `--skip-navigation` | 跳过阶段 C |
| `--only-index` | **只跑阶段 D**（最快，25s） |
| `--log PATH` | 指定日志文件路径 |

## 四、Windows Task Scheduler 自动化

### 推荐的 3 种调度

| 任务 | 频率 | 命令 | 用途 |
|---|---|---|---|
| **每日索引刷新** | 每晚 23:00 | `_daily_maintenance.py --only-index` | 25s，把白天手改的 note 同步到索引 |
| **每周完整维护** | 周日 02:00 | `_daily_maintenance.py --skip-ingest` | 定期跑聚类/复核/索引（假设一周没新 PDF） |
| **按需全量** | 手动 | `_daily_maintenance.py` | 放入新 PDF 后手动触发 |

### 配置步骤（推荐"每日索引刷新"）

#### 1. 打开 Task Scheduler

- `Win+R` 输入 `taskschd.msc` 回车
- 或：开始菜单搜索 "Task Scheduler" / "任务计划程序"

#### 2. 创建基本任务

- 右栏点 **Create Task**（不是 Create Basic Task，我们需要高级选项）
- 弹窗 "General" 标签：
  - **Name**: `CcVault Daily Index Refresh`
  - **Description**: `每日 23:00 重建 BM25 + Graph 索引`
  - **Run whether user is logged on or not** ✓（这样睡眠也能跑）
  - **Run with highest privileges** ✓

#### 3. 设置触发时间

- 切换到 **Triggers** 标签 → **New**
- **Begin the task**: On a schedule
- **Daily**, 每 1 天
- **Start**: 今天日期，时间 `23:00:00`
- **Enabled** ✓
- OK

#### 4. 设置动作

- 切换到 **Actions** 标签 → **New**
- **Action**: Start a program
- **Program/script**:
  ```
  D:\CcVault\99_SystemScripts\auto_reg_index\.venv\Scripts\python.exe
  ```
- **Add arguments**:
  ```
  D:\CcVault\99_SystemScripts\auto_reg_index\_daily_maintenance.py --only-index
  ```
- **Start in**:
  ```
  D:\CcVault\99_SystemScripts\auto_reg_index
  ```
- OK

#### 5. 条件（可选但推荐）

- 切换到 **Conditions** 标签
- 勾选 **Start the task only if the computer is on AC power**（笔记本可选）
- 勾选 **Wake the computer to run this task**（从睡眠唤醒执行）

#### 6. 保存并测试

- OK 保存
- 在 Task Scheduler 主列表里找到 `CcVault Daily Index Refresh`
- 右键 → **Run**（立刻跑一次验证）
- 完成后查看 `99_SystemScripts/auto_reg_index/logs/` 里有新日志

### 每周完整维护（同样步骤）

替换触发器为：
- **Weekly**, 每 1 周
- **Start**: 下个周日 `02:00:00`

动作改为：
```
Add arguments: D:\CcVault\99_SystemScripts\auto_reg_index\_daily_maintenance.py --skip-ingest
```

## 五、监控与告警

### 检查最近一次跑的结果

```powershell
Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\maintenance_*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | ForEach-Object { Get-Content $_.FullName -Tail 30 }
```

### 检查失败

```powershell
Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\maintenance_*.log | ForEach-Object { if (Get-Content $_.FullName | Select-String -Pattern "FAILED|EXCEPTION|TIMEOUT") { Write-Host "FAIL: $($_.Name)" -ForegroundColor Red } }
```

### 设置邮件告警（可选）

Task Scheduler 原生支持，但官方现在推荐用 PowerShell：

创建 `D:\CcVault\99_SystemScripts\auto_reg_index\_notify_if_failed.ps1`：

```powershell
$log = Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\maintenance_*.log |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (Get-Content $log.FullName | Select-String -Pattern "FAILED|EXCEPTION") {
    Send-MailMessage -To "you@example.com" -From "ccvault@local" `
        -Subject "CcVault Maintenance FAILED" -Body (Get-Content $log.FullName -Raw) `
        -SmtpServer "smtp.example.com"
}
```

把这个加到 Task Scheduler 里 `--only-index` 任务之后执行即可。

## 六、故障处理

### 任务不触发

- Task Scheduler → History 标签查看最近运行状态
- 如果显示 `0x1`：命令路径或参数错误 → 检查 **Actions** 标签三个字段
- 如果显示 `0x101`：权限问题 → General → Run with highest privileges 勾上

### 任务跑但立即失败（rc != 0）

查看日志：
```powershell
Get-Content "D:\CcVault\99_SystemScripts\auto_reg_index\logs\maintenance_*.log" -Tail 50
```

常见原因：
- `.venv` 路径错误 → 改 Actions 里的 `Program/script`
- DeepSeek API key 失效 → 更新 `.env`
- 磁盘空间不足 → 清理 `.staging/` 或 `.stage2-5/` 缓存

### OCR 阶段卡死

查日志发现 stuck 在 OCR：
```powershell
# 先 kill 当前任务
Get-Process python | Where-Object { $_.Path -like "*CcVault*" } | Stop-Process -Force

# 然后 skip-ingest 再跑
.\.venv\Scripts\python.exe _daily_maintenance.py --skip-ingest
```

### manifest.json 损坏

如果脚本报 `JSON decode error`：
```powershell
# 备份
Copy-Item D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json manifest.backup.json
# 或从近期 git 恢复
cd D:\CcVault\99_SystemScripts\auto_reg_index; git checkout manifest.json
```

## 七、维护节奏建议

### 轻度使用（每月新增 < 10 条）

- **手动全量**：每次加 PDF 后跑 `_daily_maintenance.py` 即可
- **每日自动**：`--only-index` 定时任务
- 无需设每周任务

### 中度使用（每月新增 20-100 条）

- **每日**：`--only-index`（23:00）
- **每周**：`--skip-ingest`（周日 02:00）
- **按需全量**：放新 PDF 后手工触发

### 重度使用（每月新增 > 100 条）

- **每日完整**：`_daily_maintenance.py` 全跑（凌晨 03:00）
- **实时监控**：给 `_ingest/` 加文件系统 watcher（需要额外开发）

## 八、首次跑完整任务的建议

1. **先 dry-run**：确认脚本和路径对
   ```powershell
   .\.venv\Scripts\python.exe _daily_maintenance.py --dry-run
   ```

2. **再 only-index**：验证 Stage D 能跑（25s）
   ```powershell
   .\.venv\Scripts\python.exe _daily_maintenance.py --only-index
   ```

3. **再 skip-llm**：验证 B/C 阶段能跑（约 1-2 分钟）
   ```powershell
   .\.venv\Scripts\python.exe _daily_maintenance.py --skip-llm
   ```

4. **放一份新 PDF 做端到端测试**：全跑（约 10 秒-1 分钟 per file）
   ```powershell
   # 放 1 份 PDF 到 D:\CcVault\00_Raw\标准库\cn\ 后
   .\.venv\Scripts\python.exe _daily_maintenance.py
   ```

5. **通过后再设 Task Scheduler**

## 九、清理建议

### 日志滚动

`logs/` 目录会越长越多，定期清理：

```powershell
# 保留最近 30 天
Get-ChildItem D:\CcVault\99_SystemScripts\auto_reg_index\logs\*.log |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
    Remove-Item -Force
```

### Staging 缓存

`.staging/` 保留所有历史 OCR 产物，可删但会导致补跑时重新 OCR（成本）：

- **建议保留**：几百 MB 空间换多次免费重试
- **必要清理**：只在磁盘不足时删

### Stage 缓存

`.stage2` 到 `.stage5` 是各阶段中间产物，删除后下次跑会重建：

```powershell
Remove-Item D:\CcVault\99_SystemScripts\auto_reg_index\.stage* -Recurse -Force
```

---

**总结**：脚本 `_daily_maintenance.py` 是你唯一需要记住的维护命令。配合 Task Scheduler 可实现零维护自动化。
