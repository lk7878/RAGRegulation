---
type: dashboard
purpose: cross_region_equivalence
tags:
- type/dashboard
- equivalence/matrix
---

# 跨区域对标矩阵

> Stage 3 产出的 59 条 `GB ↔ ECE/EU/ISO` 映射。本页提供 **Dataview 实时查询**，可与 [[_Equivalence MOC|Equivalence MOC]] 静态表互补。

## 所有带 `equivalent_to` 字段的 notes

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    equivalent_to AS "Equivalents",
    region AS "Region"
FROM "01_Wiki/regulations"
WHERE equivalent_to
SORT reg_id ASC
LIMIT 100
```

## 按区域对分布

```dataview
TABLE WITHOUT ID
    file.link AS "CN Note",
    equivalent_to AS "等同于"
FROM "01_Wiki/regulations/cn"
WHERE equivalent_to
SORT file.name ASC
```

## ECE → GB 反向查询思路

由于 equivalent_to 存储在 GB note 上（指向 ECE），反向查找 "某 ECE 对应哪些 GB" 需要：

1. **快速方式**：看 [[_Equivalence MOC#反向索引：ECE/UN → GB|Equivalence MOC 反向索引表]]（静态）
2. **DQL 方式**：在 ECE note 页面下写：

```dataview
LIST
FROM "01_Wiki/regulations/cn"
WHERE contains(flat(equivalent_to.ref), this.file.name) OR contains(flat(equivalent_to.ref), "ECE " + this.reg_id)
```

## 关联脚本

- `_extract_topic_equivalences.py` — 从 34 主题页提取 `GB ≈ ECE` 模式
- `_write_equivalence_page.py` — 生成 `03_Equivalence/_Equivalence MOC.md`
- `_apply_equivalences_to_notes.py` — 把映射写回 note FM

## 覆盖度

- **59 条映射**（33 个主题涉及）
- **82 个 GB notes** 已写入 equivalent_to
- 仍有 ~380 个 GB notes 无 equivalent_to — 多为无明确 ECE 对应的国内特有标准（消防、润滑油、试验方法等）
