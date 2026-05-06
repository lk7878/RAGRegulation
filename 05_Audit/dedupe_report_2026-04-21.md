---
type: audit_report
created: 2026-04-21
category: dedupe
tags: [audit/dedupe, audit/p0_fix]
---

# Dedupe Report · 2026-04-21

**总组数（含 _dup 或同 reg_id 多文件）**: 27
**自动处理（移入 trash）**: 11
**⚠️ 冲突（需人工审）**: 16

## 自动处理清单

### `ECE R1 Rev4`
- **Winner** (保留): `ece\ECE R1 Rev4.md`
- **Loser** (→ trash): `ece\ECE R1 Rev4_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=6003, loser conf=2 body=8724_
- **Loser** (→ trash): `ece\ECE R1 Rev4_dup2.md` — _winner=canonical, loser=_dup; winner conf=3 body=6003, loser conf=2 body=1139_

### `ECE R28`
- **Winner** (保留): `ece\ECE R28.md`
- **Loser** (→ trash): `ece\ECE R28_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=8497, loser conf=3 body=5342_

### `ECE R32 Rev1`
- **Winner** (保留): `ece\ECE R32 Rev1.md`
- **Loser** (→ trash): `ece\ECE R32 Rev1_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=5517, loser conf=2 body=4355_

### `ECE R33 Rev1`
- **Winner** (保留): `ece\ECE R33 Rev1.md`
- **Loser** (→ trash): `ece\ECE R33 Rev1_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=6096, loser conf=3 body=4747_

### `ECE R35 Rev1`
- **Winner** (保留): `ece\ECE R35 Rev1.md`
- **Loser** (→ trash): `ece\ECE R35 Rev1_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=3664, loser conf=2 body=256_

### `ECE R46`
- **Winner** (保留): `ece\ECE R46.md`
- **Loser** (→ trash): `ece\ECE R46_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=3791, loser conf=3 body=2062_

### `ECE R61`
- **Winner** (保留): `ece\ECE R61.md`
- **Loser** (→ trash): `ece\ECE R61_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=5672, loser conf=2 body=5277_

### `GB 4785-2006`
- **Winner** (保留): `cn\GB 4785-2006.md`
- **Loser** (→ trash): `cn\GB 4785-2006_dup2.md` — _winner=canonical, loser=_dup; winner conf=2 body=34405, loser conf=1 body=6024_
- **Loser** (→ trash): `cn\GB 4785-2006_dup1.md` — _winner=canonical, loser=_dup; winner conf=2 body=34405, loser conf=1 body=217_

### `GB 4785-2019`
- **Winner** (保留): `cn\GB 4785-2019.md`
- **Loser** (→ trash): `cn\GB 4785-2019_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=3307, loser conf=3 body=4696_

### `Regulation (EU) 2018/858`
- **Winner** (保留): `cn\Regulation (EU) 2018 858.md`
- **Loser** (→ trash): `cn\Regulation (EU) 2018 858_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=3553, loser conf=2 body=11338_

### `TR CU 018/2011`
- **Winner** (保留): `ru-eaeu\TR CU 018 2011.md`
- **Loser** (→ trash): `ru-eaeu\TR CU 018 2011_dup1.md` — _winner=canonical, loser=_dup; winner conf=3 body=4345, loser conf=3 body=4132_


## ⚠️ 冲突清单（不自动处理）

### `(EU) 2018/858`
- Winner 候选: `eu\(EU) 2018 858.md`
- Loser 候选: `eu\(EU) 2018 858_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=15828, loser conf=2 body=25775; CONFLICT: loser body much longer + higher confidence

### `ECE R102`
- Winner 候选: `ece\ECE R102.md`
- Loser 候选: `ece\ECE R102_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2642, loser conf=3 body=10826; CONFLICT: loser body much longer + higher confidence

### `ECE R108`
- Winner 候选: `ece\ECE R108.md`
- Loser 候选: `ece\ECE R108_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=2400, loser conf=3 body=48347; CONFLICT: loser body much longer + higher confidence

### `ECE R114`
- Winner 候选: `ece\ECE R114.md`
- Loser 候选: `ece\ECE R114_dup.md` — winner=canonical, loser=_dup; winner conf=2 body=3059, loser conf=2 body=10884; CONFLICT: loser body much longer + higher confidence

### `ECE R122`
- Winner 候选: `ece\ECE R122.md`
- Loser 候选: `ece\ECE R122_dup.md` — winner=canonical, loser=_dup; winner conf=3 body=2686, loser conf=3 body=5300; CONFLICT: loser body much longer + higher confidence

### `ECE R13`
- Winner 候选: `ece\ECE R13.md`
- Loser 候选: `ece\ECE R13 Rev4 Am2.md` — winner conf=3 body=2477, loser conf=1 body=569; CONFLICT: both files are non-_dup (reg_id mismatch?)
- Loser 候选: `ece\ECE R13_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2477, loser conf=2 body=3941

### `ECE R21 Rev2`
- Winner 候选: `ece\ECE R21 Rev2.md`
- Loser 候选: `ece\ECE R21 Rev2_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=5450, loser conf=3 body=11391; CONFLICT: loser body much longer + higher confidence

### `ECE R42`
- Winner 候选: `ece\ECE R42.md`
- Loser 候选: `ece\ECE R42_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=3334, loser conf=3 body=13008; CONFLICT: loser body much longer + higher confidence

### `ECE R55 Rev1 Corr1`
- Winner 候选: `ece\ECE R55 Rev1 Corr1.md`
- Loser 候选: `ece\ECE R55 Rev1 Corr1_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=896, loser conf=3 body=2492; CONFLICT: loser body much longer + higher confidence

### `ECE R59`
- Winner 候选: `ece\ECE R59.md`
- Loser 候选: `ece\ECE R59_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2896, loser conf=3 body=10603; CONFLICT: loser body much longer + higher confidence

### `ECE R68`
- Winner 候选: `ece\ECE R68.md`
- Loser 候选: `ece\ECE R68_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=1684, loser conf=3 body=17620; CONFLICT: loser body much longer + higher confidence

### `ECE R84`
- Winner 候选: `ece\ECE R84.md`
- Loser 候选: `ece\ECE R84_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=2384, loser conf=3 body=6029; CONFLICT: loser body much longer + higher confidence

### `ECE R89`
- Winner 候选: `ece\ECE R89.md`
- Loser 候选: `ece\ECE R89_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=1624, loser conf=3 body=5784; CONFLICT: loser body much longer + higher confidence

### `ECE R93`
- Winner 候选: `ece\ECE R93.md`
- Loser 候选: `ece\ECE R93_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=479, loser conf=3 body=16222; CONFLICT: loser body much longer + higher confidence

### `GB 21670-2008`
- Winner 候选: `cn\GB 21670-2008.md`
- Loser 候选: `cn\GB 21670-2008_dup1.md` — winner=canonical, loser=_dup; winner conf=2 body=5568, loser conf=2 body=20236; CONFLICT: loser body much longer + higher confidence

### `GB/T 38892-2020`
- Winner 候选: `cn\GB T 38892-2020.md`
- Loser 候选: `cn\GB T 38892-2020_dup1.md` — winner=canonical, loser=_dup; winner conf=3 body=3574, loser conf=3 body=10272; CONFLICT: loser body much longer + higher confidence
