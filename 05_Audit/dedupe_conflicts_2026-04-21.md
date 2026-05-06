---
type: audit_report
created: 2026-04-21
resolved: 2026-04-22
resolver: cascade
category: dedupe_conflict
severity: high
status: resolved
tags: [audit/dedupe, audit/conflict, audit/resolved]
---

# Dedupe Conflicts · 2026-04-21  【已处理 2026-04-22】

共 16 组需人工决定保留哪份。**Opus 4.6 审阅后已于 2026-04-22 执行决议**：

- 🔄 _dup 替换 canonical · **2 组完成**（原 canonical 移 `.trash/*_replaced_2026-04-22.md`）
- 📑 _dup 重命名为 (EN) · **12 组完成**（ECE R13_dup1.md 不存在，跳过）
- ❓ `(EU) 2018/858` · **保留未动**（_dup 实为多法规汇编，reg_id 可能标错，需人工）

处理脚本：`@D:\CcVault\99_SystemScripts\auto_reg_index\_apply_dedupe_decisions.py`
处理建议详见：`@D:\CcVault\05_Audit\dedupe_resolution_proposal_2026-04-21.md`

---

## 原始冲突列表（已历史化）

## 判定标准
- Loser body 长度 >= Winner 的 1.5x，且 confidence >= Winner
- 通常意味着 _dup 可能是更完整的版本
- 建议对比两份 body 后决定

---

## `(EU) 2018/858`

- Winner 候选: `eu\(EU) 2018 858.md`
- Loser 候选: `eu\(EU) 2018 858_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=15828, loser conf=2 body=25775; CONFLICT: loser body much longer + higher confidence

## `ECE R102`

- Winner 候选: `ece\ECE R102.md`
- Loser 候选: `ece\ECE R102_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2642, loser conf=3 body=10826; CONFLICT: loser body much longer + higher confidence

## `ECE R108`

- Winner 候选: `ece\ECE R108.md`
- Loser 候选: `ece\ECE R108_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=2400, loser conf=3 body=48347; CONFLICT: loser body much longer + higher confidence

## `ECE R114`

- Winner 候选: `ece\ECE R114.md`
- Loser 候选: `ece\ECE R114_dup.md` — winner=canonical, loser=_dup; winner conf=2 body=3059, loser conf=2 body=10884; CONFLICT: loser body much longer + higher confidence

## `ECE R122`

- Winner 候选: `ece\ECE R122.md`
- Loser 候选: `ece\ECE R122_dup.md` — winner=canonical, loser=_dup; winner conf=3 body=2686, loser conf=3 body=5300; CONFLICT: loser body much longer + higher confidence

## `ECE R13`

- Winner 候选: `ece\ECE R13.md`
- Loser 候选: `ece\ECE R13 Rev4 Am2.md` — winner conf=3 body=2477, loser conf=1 body=569; CONFLICT: both files are non-_dup (reg_id mismatch?)
- Loser 候选: `ece\ECE R13_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2477, loser conf=2 body=3941

## `ECE R21 Rev2`

- Winner 候选: `ece\ECE R21 Rev2.md`
- Loser 候选: `ece\ECE R21 Rev2_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=5450, loser conf=3 body=11391; CONFLICT: loser body much longer + higher confidence

## `ECE R42`

- Winner 候选: `ece\ECE R42.md`
- Loser 候选: `ece\ECE R42_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=3334, loser conf=3 body=13008; CONFLICT: loser body much longer + higher confidence

## `ECE R55 Rev1 Corr1`

- Winner 候选: `ece\ECE R55 Rev1 Corr1.md`
- Loser 候选: `ece\ECE R55 Rev1 Corr1_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=896, loser conf=3 body=2492; CONFLICT: loser body much longer + higher confidence

## `ECE R59`

- Winner 候选: `ece\ECE R59.md`
- Loser 候选: `ece\ECE R59_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2896, loser conf=3 body=10603; CONFLICT: loser body much longer + higher confidence

## `ECE R68`

- Winner 候选: `ece\ECE R68.md`
- Loser 候选: `ece\ECE R68_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=1684, loser conf=3 body=17620; CONFLICT: loser body much longer + higher confidence

## `ECE R84`

- Winner 候选: `ece\ECE R84.md`
- Loser 候选: `ece\ECE R84_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2384, loser conf=3 body=6029; CONFLICT: loser body much longer + higher confidence

## `ECE R89`

- Winner 候选: `ece\ECE R89.md`
- Loser 候选: `ece\ECE R89_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=1624, loser conf=3 body=5784; CONFLICT: loser body much longer + higher confidence

## `ECE R93`

- Winner 候选: `ece\ECE R93.md`
- Loser 候选: `ece\ECE R93_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=479, loser conf=3 body=16222; CONFLICT: loser body much longer + higher confidence

## `GB 21670-2008`

- Winner 候选: `cn\GB 21670-2008.md`
- Loser 候选: `cn\GB 21670-2008_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=5568, loser conf=2 body=20236; CONFLICT: loser body much longer + higher confidence

## `GB/T 38892-2020`

- Winner 候选: `cn\GB T 38892-2020.md`
- Loser 候选: `cn\GB T 38892-2020_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=3574, loser conf=3 body=10272; CONFLICT: loser body much longer + higher confidence
