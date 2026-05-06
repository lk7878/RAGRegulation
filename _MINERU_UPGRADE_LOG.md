---
type: system_log
project: mineru_ocr_upgrade
started: 2026-04-22
status: completed
last_updated: 2026-04-25
tags:
- log/mineru
- type/system
---

# MinerU 云 OCR 升级日志

> 用 MinerU 云 API 重 OCR 原始 PDFs，补回传统 pipeline（百度 OCR + 文本提取）丢失的**表格、LaTeX 公式、原图**。

## 🏆 Day 4 终态（2026-04-25 10:30 · 完成 100%）

| 指标 | 数值 |
|---|---:|
| **MinerU 处理率** | **1414 / 1414 = 100.00%** |
| 含表/公式/图的 upgraded notes | 982 (mineru) + 13 (mineru_split) = **995** |
| 跑了无 assets 的 notes | 406 (mineru_no_assets) |
| 显式 skip 的边缘案例 | 13 (skipped) |
| 累计新增表格（最终） | ~2,700 |
| 累计新增公式（最终） | ~1,850 |
| 累计新增图像（最终） | ~2,750 |
| 消耗页数（4 日累计） | ~22,000 |
| 直接花费 | **¥0**（MinerU 官方免费额度内） |
| QC | **0 问题** |
| 关联 audit | **2 全 resolved**（oversized_pdfs / new_dup_conflicts） |

### Day 4 主要工作（2026-04-25 早 07:14 → 10:30）

1. **常规 OCR + 合并**（07:14-07:42）：283 PDFs OCR 成功，304 notes 合并
2. **Phase 1+2+3 第 1 批**（08:07-08:35）：8 条超页 PDF 拆为 22 parts → OCR → 合并到 8 个 reg_id（ECE R37 Rev8 / R96 Rev3 / R96 Rev3 Am2 / R49 Rev6 / R154 Rev1 / R13 Rev8 / R83 / GB 18352.6-2016）
3. **第二轮捞底**（09:13-09:38）：跑 102 条 not_run 中 78 成功；处理率 64% → 92.8%
4. **第 2 批超页**（09:43-09:58）：3 条新发现超页 PDF split → OCR → 合并（ECE R110 Rev6 / R83 Rev5 / 3.2024版国际主流目录）
5. **第三轮捞底 + 第 3 批超页**（10:01-10:22）：8 条小但被 size_filter 跳过的 OCR + 2 条新超页 split；处理率 → 99.1%
6. **13 条边缘案例 skip 标记**（10:23-10:30）：处理率 → **100.00%**

### Day 4 新增基础设施（7 个永久脚本）

- `_split_large_pdfs.py` — Phase 1 拆分超页 PDF
- `_mineru_oversized.py` — Phase 2 OCR 拆分 part（独立 state）
- `_merge_split_mineru.py` — Phase 3 合并多 part 到 note
- `_mark_no_assets_skipped.py` — 标记跑过无 assets
- `_mark_final_skipped.py` — 13 条最终 skip 标记
- `_fix_orphan_dups.py` — 修复孤儿 _dup1
- `_convert_dup1_to_moc.py` — _dup1 → MOC 转换

---

## 目标

**问题**：原 pipeline 基于百度 OCR，文本提取为主，对**表格结构**、**数学公式**、**图像**的还原能力弱。这导致 notes 缺关键技术信息（比如 ECE R75 的轮胎规格表、GB 4785 的光学曲线）。

**方案**：
- 用 MinerU 云 API 重跑所有 PDFs → 产出带结构化表格/公式/图像的 Markdown
- 合并到现有 notes 的正文末尾新增节「## 原文参考（MinerU 云解析）」
- 保留原 body 不变（LLM 摘要仍是主入口），新增的是**技术细节补全**
- 每个 note FM 打 `_ocr_upgraded: mineru` 标记便于检索

## Day 2 成果（2026-04-23 07:20 · 主动暂停）

> 暂停原因：MinerU 服务器白天拥塞严重，02:00 之后持续 SSL EOF。保留 watchdog 代码，择日重启。

### 核心指标

| 指标 | 数值 |
|---|---:|
| **累计处理 PDFs** | **845 / 1444 (58.5%)** |
| **已合并 notes** | **595** |
| **累计新增表格** | **2,036** |
| **累计新增公式** | **1,353** |
| **累计新增图像** | **2,284** |
| **消耗页数** | 15,767（跨两日）|
| **API 失败** | ~370（含 SSL EOF 连环崩溃）|
| **直接花费** | ¥0（MinerU 官方免费额度内）|

### 跨日 delta

| 指标       | Day 1 (04-22 EOD) | Day 2 (04-23 07:20) |        Δ |
| -------- | ----------------: | ------------------: | -------: |
| 处理 PDFs  |               572 |                 845 | **+273** |
| 合并 notes |               367 |                 595 | **+228** |
| 累计表格     |             1,301 |               2,036 |     +735 |
| 累计公式     |               800 |               1,353 |     +553 |
| 累计图像     |             1,541 |               2,284 |     +743 |

### Day 1 历史指标（2026-04-22）

| 指标 | 数值 |
|---|---:|
| 当日处理 PDFs | 572 / 1444 (39%) |
| 当日合并 notes | 367 |
| 当日消耗页数 | 11,356 |

### Top 10 含元素最丰富的升级 notes

| Reg | 表格 | 公式 | 图像 | 主题 |
|---|---:|---:|---:|---|
| GB/T 40625-2021 | 10 | 20 | 8 | ADAS/HIL 测试 |
| ECE R101 Rev3 | 10 | 20 | 8 | 排放认证 |
| GB/T 44124-2024 | 10 | 20 | 5 | 新能源 |
| GB 18564.1-2006 | 10 | 11 | 8 | 危险品运输 |
| ECE R46 Rev4 | 6 | 15 | 8 | 视野 / 后视镜 |
| GB/T 19233-2020 | 3 | 20 | 5 | 模拟试验 |
| GB/T 12673-2019 | 10 | 10 | 8 | 尺寸参数 |
| GB 29753-2013 | 7 | 13 | 8 | 危险品运输 |
| ECE R66 Rev1 | 0 | 20 | 8 | 客车结构强度 |
| ECE R149 | 10 | 10 | 8 | 前大灯 |

### 5 波批次执行记录

| 波次 | 时间 | 选中 PDFs | 成功 | 累计页数 | 备注 |
|---|---|---:|---:|---:|---|
| Phase 1 | 07:00 | 6 | 6 | 23 | 技术验证 |
| Phase 2 | 07:05 | 44 | 44 | 402 | P1 批量 |
| Phase 3 | 07:15 | 149 | ~140 | 1232 | P1 扩大 |
| Phase 4 | 07:30 | 20 | 20 | ? | P1 收尾 |
| Phase 5 | 07:34 | 37 | 37 | 339 | P4/P5 补测 |
| Phase 6 | 08:03 | 500+ | ~220 | 7000+ | 大规模跑（中途意外中断）|
| Phase 7 | 09:12 | 942 | 进行中 | 进行中 | 续跑至完成 |

## 技术架构

### 数据流

```
00_Raw/标准库/*.pdf
    │
    ├─> _priority_selector.py     (按 FM 缺失严重性排优先级)
    │       ↓
    ├─> _daily_batch.py           (批量上传 MinerU 云, 25 files/batch)
    │       ↓  (MinerU Cloud API)
    │       ↓  (下载 zip)
    │       ↓  (解压到 outputs/<hash>/)
    │       ↓
    ├─> _merge_upgrade.py         (解析 content_list.json, 合并到 regulations/*.md)
    │       ↓
    └─> 01_Wiki/regulations/      (notes 正文末尾追加 "## 原文参考" 节)
        01_Wiki/regulations/_mineru_assets/<reg_id>/*.jpg  (图像资产)
```

### FM 新增字段

```yaml
_ocr_upgraded: mineru              # 升级标记
_mineru_content_hash: abc123...    # PDF SHA-1 hash
_mineru_outputs_dir: outputs/abc123 # 原始 MinerU 输出位置
_mineru_blocks:
  tables: 10
  formulas: 3
  images: 8
_mineru_merged_at: '2026-04-22'
```

### 核心脚本

- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_client.py` — MinerU 云 API 封装（批量上传、轮询、下载）
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_priority_selector.py` — 候选 PDFs 优先级排序
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_daily_batch.py` — 每日批量入口
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_merge_upgrade.py` — 合并到 notes
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_stats.py` — 统计报告
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_progress.py` — 实时进度
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_repair_broken_fm.py` — 修复 FM 破损（一次性）

## Bugs & 经验教训

### Bug 1（已修）：FM closing `---` 后缺空行

- **症状**：合并后 FM 结尾 `---` 直接贴 body 的 `# Title`，YAML 解析失败
- **根因**：合并脚本 `split("---\n\n", 2)` 只匹配两个换行，但 body 可能以 1 个换行开头
- **修复**：`_merge_upgrade.py` 改为显式 `closing + "\n\n" + body`，同时一次性修复已存在的 120 条破损

### Bug 2（已修）：图像 `img_path` 为空时 shutil.copy2 炸

- **症状**：MinerU content_list.json 偶尔有 `img_path: ""` 的条目，`Path / ""` 解析为目录本身，`shutil.copy2(dir, ...)` 在 Windows 报 PermissionError
- **修复**：`copy_image()` 开头加空值 + `is_file()` 双重判断

### Bug 3（已修）：`total_pages` 偶尔为 None

- **症状**：少数 PDF 的 MinerU 响应 `total_pages=null`，state.json 记 pages=0
- **修复**：若为 None，从 `content_list.json` 的 `page_idx` 最大值推断

### 经验 1：页数估算器偏保守

- `pages_per_mb=30` 估算总是比实际偏高 1.5-2.3 倍
- 实际 PDF 压缩率差异巨大（纯扫描 vs. 文本型）
- 目前仅用作"初始预算"，实际消耗后不再约束

### 经验 2：MinerU 服务器有排队限流（undocumented）

- 官方 docs 声明 10,000 文件/天免费，无页数限制
- 但当瞬时调用量大时，batch 会长时间停留在 `pending` 状态（>5 分钟）
- 脚本 poll 超时设为 15 分钟，超时后自动跳下一批
- 失败率 ~10%，失败文件记 state，后续重试

### 经验 3：批次大小 25 是甜点

- 太小：轮询开销大，总时间长
- 太大：一个"卡住"的文件连带拖慢整批
- 25 文件/批在吞吐量 vs. 尾延迟之间平衡最佳

## 新增基础设施（2026-04-22~23）

| 文件 | 作用 |
|---|---|
| `@D:\CcVault\99_SystemScripts\mineru_upgrade\_watchdog.py` | 守护进程，daily_batch 崩溃自动重启（30s 退避 + 连环崩保护） |
| `@D:\CcVault\99_SystemScripts\mineru_upgrade\_qc_merged.py` | 合并后 QC：检查 FM、元素计数、缺图、LaTeX 不配对 |
| `@D:\CcVault\99_SystemScripts\mineru_upgrade\_fix_block_counts.py` | 修正 FM 里 `_mineru_blocks` 的 tables/formulas/images 计数 |
| `@D:\CcVault\99_SystemScripts\mineru_upgrade\_repair_broken_fm.py` | 一次性修复 FM closing `---` 缺空行导致 YAML 解析失败 |
| `@D:\CcVault\99_SystemScripts\mineru_upgrade\_apply_dedupe_decisions.py` | 半自动 dedupe 决策执行（replace / rename_to_en） |

## 客户端优化（2026-04-22~23）

1. **上传重试**：`upload_one` 加 3 次重试 + 指数退避（2s / 4s / 8s），SSL EOF 自愈
2. **Polling 韧性**：`poll_batch` 遇 SSL 错误不崩，保留已 done 的结果
3. **Batch URL 请求重试**：`request_upload_urls` 加 3 次重试 + 10s/30s/60s 退避
4. **并发降级**：上传并发 5 → 3，减少 MinerU 服务器拒绝服务
5. **小文件优先 + 大书过滤**：按 size 升序 + `--max-size-mb 10` 跳过 17-37MB 大书
6. **批次熔断**：连续 5 批失败时进程 sleep 10 min，避免空转烧日志

## 待办事项

### Day 3+（择日继续）
- [ ] 剩余 599 PDFs 待升级（重启 `_watchdog.py` 即可）
- [ ] 重试阻塞中的 ~370 failed 记录（清除 state.failed 后再跑）
- [ ] QC 遗留 4 条小问题（2 占位图 / 1 LaTeX 不配对 / 1 计数差）

### 后续增强
- [ ] 重跑 `_cluster_topics.py`：body 变长后部分 notes 可能需要重新归类
- [ ] 重跑 `_graphrag_communities.py`：body 变化影响 BM25 和社区聚类
- [ ] 把 `_recheck_low_confidence.py` 对 MinerU 升级过的 low_conf notes 再跑一遍（内容更全，LLM 判断更准）
- [ ] Dashboard 持续看 `@D:\CcVault\00_Dashboards\_MinerU_Upgrades.md`

## 相关文档

- Dashboard: `@D:\CcVault\00_Dashboards\_MinerU_Upgrades.md`
- Pipeline README: `@D:\CcVault\99_SystemScripts\mineru_upgrade\README.md`（TODO）
- 官方文档: [mineru.net/doc/docs/limit](https://mineru.net/doc/docs/limit)
