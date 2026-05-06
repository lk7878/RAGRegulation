---
audit_id: 2026-04-23_oversized_pdfs
created: 2026-04-23
status: resolved
resolved: 2026-04-25
resolver: cascade
severity: medium
category: completeness
owner: self
priority: P2
target_eta: 2026-04-24
tags:
  - type/audit
  - mineru_upgrade
  - audit/resolved
related:
  - '[[ECE R37 Rev8]]'
  - '[[ECE R96 Rev3]]'
  - '[[ECE R96 Rev3 Am2]]'
  - '[[ECE R49 Rev6]]'
  - '[[GB 18352.6-2016]]'
  - '[[ECE R154 Rev1]]'
  - '[[ECE R13 Rev8]]'
  - '[[ECE R83]]'
---

# MinerU 200 页限制 · 8 条大 PDF 需拆分专项 ✅ RESOLVED

> **Resolution（2026-04-25 早 8:35）**：
> 全部 8 条超页 PDF 已完成 Phase 1 拆分 + Phase 2 OCR + Phase 3 合并到 note。
>
> **执行结果**：
> - **22 parts 拆分** · `_split_work/` · `@D:\CcVault\99_SystemScripts\mineru_upgrade\_split_large_pdfs.py`
> - **22/22 parts OCR 成功** · 累计 3033 页 · 14 分钟（分 2 批：10 + 12）· `@D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_oversized.py`
> - **8/8 reg_id 合并到 note** · 累计 109 表 + 177 公式 + 96 图 · `@D:\CcVault\99_SystemScripts\mineru_upgrade\_merge_split_mineru.py`
>
> **note body 增长**：
> - `[[ECE R37 Rev8]]` · 6,313 → 49,462 (~7.8x)
> - `[[ECE R96 Rev3]]` · 6,071 → 37,933 (~6.2x)
> - `[[ECE R96 Rev3 Am2]]` · 5,997 → 31,447 (~5.2x)
> - `[[ECE R49 Rev6]]` · 5,559 → **135,344 (~24x)** ← 重型柴油机排放，最大
> - `[[GB 18352.6-2016]]` · 2,779 → 28,175 (~10x)
> - `[[ECE R154 Rev1]]` · 4,252 → 48,152 (~11x)
> - `[[ECE R13 Rev8]]` · 2,552 → 24,452 (~10x)
> - `[[ECE R83]]` · 4,613 → 35,508 (~7.7x)
>
> **后续验证**：QC 0 问题（907 upgraded notes），daily_maintenance 重建索引/拓扑/topics，BM25 包含最新 body。
>
> **额外副产出**：永久基础设施 3 脚本（split / oversized batch / merge_split）+ QC 顺手修正支持 `mineru_split` 标记。

---

# 原始问题描述 · MinerU 200 页限制 · 8 条大 PDF 需拆分专项（已解决）

## 背景

MinerU 云 OCR 单次硬限制 **200 页**，超过会立即报错：
> `number of pages exceeds limit (200 pages), please split the file and try again`

这 8 条 PDF 页数超过 200，在 `_mineru_state.json` 的 `failed` 中永久存在，**常规重跑无法解决**。

> **错误信息差异说明**：超页 PDF 通常会直接报 `200 pages exceeds limit`；但部分中文 PDF 会先尝试 OCR 5 次后报 `retry limit reached (5 attempts)`（如 ECE R83），实际页数验证后**也是超页**。两类报错本质相同，统一归入此 audit。

## 受影响清单

| # | reg_id | 页数 | Size | PDF 相对路径 | 拆成 (≤200p) | MinerU 报错 |
|---|---|---:|---:|---|---:|---|
| 1 | ECE R37 Rev8 | 217 | 4.8 MB | `国外法规/ECE标准/标准法规-UNECE/0~40/37/R037r8e.pdf` | 2 块 | exceeds 200 |
| 2 | ECE R96 Rev3 | 416 | 4.7 MB | `国外法规/ECE标准/标准法规-UNECE/81~120/96/R096r3e.pdf` | 3 块 | exceeds 200 |
| 3 | ECE R96 Rev3 Am2 | 455 | 5.1 MB | `国外法规/ECE标准/标准法规-UNECE/81~120/96/R096r3am2e.pdf` | 3 块 | exceeds 200 |
| 4 | ECE R49 Rev6 | 434 | 3.3 MB | `国外法规/ECE标准/标准法规-UNECE/41～80/49/R049r6e.pdf` | 3 块 | exceeds 200 |
| 5 | GB 18352.6-2016 | 407 | 4.5 MB | `国内法规/国内标准/GB 18352.6-2016_upload_*.pdf` | 3 块 | exceeds 200 |
| 6 | ECE R154 Rev1 | >200 | 8.0 MB | `国外法规/ECE标准/标准法规-UNECE/121~160/154/R154r1e.pdf` | 2-3 块 | exceeds 200 |
| 7 | ECE R13 Rev8 | >200 | 2.2 MB | `国外法规/ECE标准/标准法规-UNECE/0~40/13/R013r8e.pdf` | 2-3 块 | exceeds 200 |
| 8 | ECE R83 | **274** | 1.4 MB | `国外法规/ECE标准/11.ECE法规（中文）/法规83号/83.pdf` | 2 块 | retry limit reached (中文 OCR) |

共 8 PDF、需约 **20-22 次 MinerU 调用 + 8 次 note 合并**。

## 修订历史

- **2026-04-23 创建**：5 条超页（R37 Rev8, R96 Rev3, R96 Rev3 Am2, R49 Rev6, GB 18352.6-2016）
- **2026-04-24 更新**：新增 ECE R154 Rev1（今日批次触发）。`_daily_batch.py` 已改为自动跳过 `status: mineru_failed`，避免重复浪费预算
- **2026-04-25 更新（早）**：新增 ECE R13 Rev8（制动法规 Rev8 完整本）
- **2026-04-25 更新（晚）**：补录 ECE R83 —— 实际 274 页，但 MinerU 报错为 `retry limit reached`，本次审查时核对 `_mineru_state.json` 与 audit 不一致后发现并补入

## 技术路径

### Phase 1 · 拆分 (1 小时)

新建 `@D:\CcVault\99_SystemScripts\mineru_upgrade\_split_large_pdfs.py`：

```python
import pypdf
from pathlib import Path

RAW = Path(r"D:\CcVault\00_Raw\标准库")
WORK = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_split_work")
WORK.mkdir(exist_ok=True)

TARGETS = [
    ("ECE R37 Rev8",        "国外法规/ECE标准/标准法规-UNECE/0~40/37/R037r8e.pdf"),
    ("ECE R96 Rev3",        "国外法规/ECE标准/标准法规-UNECE/81~120/96/R096r3e.pdf"),
    ("ECE R96 Rev3 Am2",    "国外法规/ECE标准/标准法规-UNECE/81~120/96/R096r3am2e.pdf"),
    ("ECE R49 Rev6",        "国外法规/ECE标准/标准法规-UNECE/41～80/49/R049r6e.pdf"),
    ("GB 18352.6-2016",     "国内法规/国内标准/GB 18352.6-2016_upload_1b653a88-219a-412e-acb3-923dd4f1af30.pdf"),
    ("ECE R154 Rev1",       "国外法规/ECE标准/标准法规-UNECE/121~160/154/R154r1e.pdf"),
    ("ECE R13 Rev8",        "国外法规/ECE标准/标准法规-UNECE/0~40/13/R013r8e.pdf"),
    ("ECE R83",             "国外法规/ECE标准/11.ECE法规（中文）/法规83号/83.pdf"),
]
CHUNK_SIZE = 180  # 留 20 页缓冲

for reg_id, rel in TARGETS:
    src = RAW / rel
    reader = pypdf.PdfReader(str(src))
    n = len(reader.pages)
    for i, start in enumerate(range(0, n, CHUNK_SIZE), 1):
        writer = pypdf.PdfWriter()
        for p in range(start, min(start + CHUNK_SIZE, n)):
            writer.add_page(reader.pages[p])
        out = WORK / f"{reg_id}__part{i}.pdf"
        with out.open("wb") as f:
            writer.write(f)
        print(f"  {out.name}  ({min(CHUNK_SIZE, n-start)}p)")
```

### Phase 2 · 逐块 MinerU (晚上 15-30 min)

写 `_mineru_oversized.py`：上传 `_split_work/*.pdf`，落到 `outputs/<reg_id>_part<N>/`。

### Phase 3 · 合并到单条 note (30 min)

写 `_merge_split_mineru.py`：把 `outputs/<reg_id>_part*/` 的 `auto_content.md` / 图片等拼成一个 "原文参考" 段，追加到对应 note。

## 预算

- **MinerU 页数**：约 21 × 180p = 3,780 页（一日预算 1800p 的 2 倍，需分 2-3 天跑完）
- **时间**：约 3-4 小时（拆分 + 上传 + 合并，实际干活）

## 推迟原因

- 主力任务是跑完剩余 111 条常规 PDF（截至 2026-04-25 已完成 92%）
- 拆分专项可独立于主流程，等主流程稳定后再做
- 这 8 条即使缺 MinerU 升级段，note 基础字段也已完备（title / topic / status），搜索可用
- `_daily_batch.py` 已加 `permanently_failed` 排除，**这 8 条不会再消耗每日预算**

## 预计处理时间

**2026-04-26 ~ 2026-04-28**，在主流程跑完剩余 111 条后。

## 附加发现

`_mineru_state.json` 中 `failed` 共 **369 条**，分布如下（见 `@D:\CcVault\99_SystemScripts\mineru_upgrade\_analyze_failures.py`）：

| 错误类 | 总数 | 根因 | 解决 |
|---|---:|---|---|
| `timeout` (pending/running) | 285 | MinerU 服务器拥塞 | 晚上重跑（已部分恢复） |
| `upload_error` (SSL/连接断) | 53 | 白天带宽拥塞 | 自动重跑 |
| `download_error` | 23 | 偶发 | 自动重跑 |
| **`mineru_failed` (>200页/重试上限)** | **8** | **硬限制** | **本 audit** |

约 **98%（361 条）**为网络/拥塞类，可通过 `_daily_batch.py` 自动重跑恢复（已实现）。
仅 **2%（8 条）**需人工拆分，即本 audit 范围。
