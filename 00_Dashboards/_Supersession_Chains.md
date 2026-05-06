---
type: dashboard
purpose: supersession_tracking
tags:
- type/dashboard
- lineage/supersession
---

# 替代链溯源

> 跟踪所有已知的 `supersedes` / `superseded_by` 双向链接。64 条国内 GB 已建立反向链（由 `_build_supersession_chain.py` 自动写入）。

## 正向链：新版标准 → 被替代版本

```dataview
TABLE WITHOUT ID
    file.link AS "最新版",
    publication_date AS "发布",
    supersedes AS "替代了",
    region AS "Region"
FROM "01_Wiki/regulations"
WHERE supersedes != null
SORT publication_date DESC
LIMIT 40
```

## 反向链：旧版 → 被哪些新版替代

```dataview
TABLE WITHOUT ID
    file.link AS "旧版",
    publication_date AS "发布",
    superseded_by AS "被替代为",
    status AS "状态"
FROM "01_Wiki/regulations"
WHERE superseded_by != null
SORT publication_date DESC
LIMIT 40
```

## 多代演进实例（重点标准 3 代以上链条）

### GB 11551 正面碰撞演进
- [[GB 11551-2003]] → [[GB 11551-2014]]（当前）
- 相关主题：[[crash_impact - 碰撞与被动安全]]

### GB 14166 安全带 / 约束系统
- [[GB 14166-2003]] → [[GB 14166-2013]]（当前）
- 相关主题：[[restraints_airbags - 安全带与乘员约束]]

### GB 19578 乘用车燃料消耗量（CAFC）
- GB 19578-2004 → [[GB 19578-2014]] → [[GB 19578-2015]] → [[GB 19578-2021]] → [[GB 19578-2024]]（当前）
- 相关主题：[[emissions_exhaust - 排放与燃料]] [[energy_labeling - 能耗 · 油耗标识]]

### GB 17354 前碰 / 燃料系统（历史拆分）
- [[GB 17354]] 已拆分为 [[GB 11551]]（碰撞）+ [[GB 18296]]（燃料箱）
- 相关主题：[[crash_impact - 碰撞与被动安全]] [[fuel_lpg_cng - 燃料装置（液体 · 气体）]]

## 孤立预测者（未收录）

`.stage4/supersession_chain.json` 中 `orphans` 字段列出 94 条预测但本库缺失的旧标准（如 GB 14761.4-1993, GB 11340-1989 等）。如需完整链条，应补采此类历史标准 PDF。

## 脚本

- `_build_supersession_chain.py` — 扫描 supersedes，写回 superseded_by
- 运行方式：`python _build_supersession_chain.py [--dry-run]`
