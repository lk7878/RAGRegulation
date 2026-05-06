---
audit_id: 2026-04-23_new_dup_conflicts
created: 2026-04-23
status: resolved
resolved: 2026-04-25
resolver: cascade
severity: medium
category: dedupe
owner: self
priority: P2
tags:
  - type/audit
  - audit/dedupe
  - audit/resolved
---

# 新增 _dup 冲突 · 2026-04-21 之后产生的 5 份重复 ✅ RESOLVED

> **Resolution（2026-04-25 早 9:13）**：5 条全部处理完毕。
>
> **根因分析**：
> - 4 条 ECE _dup1 是 **dedupe trash 流程的遗留 bug**：canonical 已被移入 trash，但 `_dup1` 后缀文件名未被重命名 → vault 里看上去像「冲突」其实是「孤儿 _dup1」（该 reg_id 的唯一 note）。
> - 1 条 (EU) 2018/858_dup1 是 **类型识别错误**：实际是 EU 法规目录索引（60+ reg_id 条目），不是单一法规原文，最初被错误归类。
>
> **执行结果**：
> - **4 条 ECE rename**：`ECE R125_dup1.md` / `R127_dup1.md` / `R135_dup1.md` / `R144_dup1.md` → 去 `_dup1` 后缀。同步修复 4 处 wikilink（topic page）。脚本：`@D:\CcVault\99_SystemScripts\mineru_upgrade\_fix_orphan_dups.py`
> - **(EU) 2018/858_dup1 → MOC 转换**：rename 为 `EU Tech Directives Index.md`，reg_id 改为 `EU Tech Directives Index`，type 改为 `type/index`，body 完整保留（60+ 法规元数据汇编）。同步修复 2 处 wikilink。脚本：`@D:\CcVault\99_SystemScripts\mineru_upgrade\_convert_dup1_to_moc.py`
>
> **后续验证**：QC 0 问题（907 upgraded notes 不变 + 1 新 type/index），daily_maintenance 重建索引。
>
> **注意**：原 canonical `(EU) 2018 858.md` 是「欧盟法规体系综述」类，reg_id 标注 (EU) 2018/858 不准确（不是法规原文），暂保留现状未动 —— 后续低优先级可再优化。

---

# 原始问题描述 · 新增 _dup 冲突（已解决）

## 背景

在处理 `dedupe_resolution_proposal_2026-04-21.md` 收尾时扫描发现，`01_Wiki/regulations/` 下有 5 份 **2026-04-21 之后新产生的** `_dup` 文件，不在原 proposal 范围：

| 文件 | 大小 | 修改日期 | 疑似原因 |
|---|---:|---|---|
| `ece/ECE R125_dup1.md` | 30.6 KB | 2026-04-22 | MinerU 升级或新 ingest |
| `ece/ECE R127_dup1.md` | 10 KB | **2026-04-23** | 今日新增 |
| `ece/ECE R135_dup1.md` | 43.1 KB | 2026-04-22 | — |
| `ece/ECE R144_dup1.md` | 8.1 KB | 2026-04-18 | 早期遗留 |
| `eu/(EU) 2018 858_dup1.md` | 66 KB | 2026-04-22 | 疑似原 proposal 🔴 项转移，内容是多法规汇编错误合并为一条 |

## 为什么需要新一轮 dedupe

- `dedupe_conflicts_2026-04-21.md` 的检测脚本（推测是 `99_SystemScripts/auto_reg_index/` 下的 dedupe pipeline）**只看了 04-21 之前的状态**
- 04-22 到 04-23 期间，MinerU 升级流程和 ingest 流程**可能再次创建了 _dup**（比如同一 PDF 被不同 hash 两次处理）
- 需要追查根因：**为什么 dedupe 之后还会产生新 _dup**，不然永远修不完

## 建议行动

### Phase 1 · 根因分析（30 min）
查看 MinerU 升级流程是否会生成 `<reg_id>_dup1.md`。可能的触发点：
- `_merge_upgrade.py` 合并时 reg_id 冲突的保护
- `auto_reg_index` pipeline 的 dedupe 分支

### Phase 2 · 跑新一轮 dedupe（10 min）
```powershell
# 假设 dedupe 脚本在 auto_reg_index/
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _dedupe_scan.py  # 脚本名待查
```

### Phase 3 · LLM 审阅冲突（5 min / ~¥0.5）
对 5 组冲突调用 Opus 4.6（和上次一样），生成新的 `dedupe_resolution_proposal_2026-04-23.md`。

### Phase 4 · 用户决策 + 执行（15-30 min）
按 proposal 执行重命名 / 替换 / 拆分。

## 预计总工时

**1.5 小时**，可安排到本周内任何时段。

## 关联

- 前一轮 proposal：`[[dedupe_resolution_proposal_2026-04-21.md]]`（已 resolved）
- 特别关注 `(EU) 2018 858_dup1.md`：原 proposal 里就标的 🔴 需拆分项，需要从多法规汇编中抽取 (EU) 2019/2144、(EU) 2023/2867 等条目为独立 notes

## 优先级判断

**P2**（非紧急非阻塞）：5 份 _dup 不影响现有 1414 notes 的正常查询，只是占用冗余空间。晚上 MinerU 主流程跑完后一起收拾。
