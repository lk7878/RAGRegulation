---
type: dashboard
purpose: mineru_upgrade_index
tags:
- type/dashboard
- status/mineru_enhanced
updated: 2026-04-25
---

# MinerU 云 OCR 升级索引

> 2026-04-22 起用 MinerU 云 API 重 OCR 原始 PDF，补全传统 pipeline 丢失的**表格、LaTeX 公式、原图**。2026-04-25 达到全量 100% 处理率。
>
> **MinerU 状态字段 `_ocr_upgraded`**：
> - `mineru`：合并出结构化内容（表/公式/图），body 结尾含 `## 原文参考`。
> - `mineru_split`：超页 PDF 拆分后多 part 合并 — 全部表/公式/图于单一 note。
> - `mineru_no_assets`：OCR 跑了但 PDF 无表/公式/图（纯文本 amendment）。
> - `skipped`：中文扫描版冗余 / 综述书 / >50MB 巨件 — FM 含 `_ocr_skip_reason`。

---

## 全库处理状态总览

```dataview
TABLE WITHOUT ID
    _ocr_upgraded AS "状态",
    length(rows.file.link) AS "notes",
    sum(rows._mineru_blocks.tables) AS "表格",
    sum(rows._mineru_blocks.formulas) AS "公式",
    sum(rows._mineru_blocks.images) AS "图像"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded
GROUP BY _ocr_upgraded
SORT length(rows.file.link) DESC
```

## 含结构化资产的 notes 总量（mineru + mineru_split）

```dataview
TABLE WITHOUT ID
    length(rows.file.link) AS "升级 notes",
    sum(rows._mineru_blocks.tables) AS "累计表格",
    sum(rows._mineru_blocks.formulas) AS "累计公式",
    sum(rows._mineru_blocks.images) AS "累计图像"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split"
GROUP BY "total"
```

---

## Top 30 含元素最丰富的升级

> 按 **表格数 + 公式数 + 图像数** 总和排序。这些是**最值得引用**的 notes。

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    _ocr_upgraded AS "来源",
    _mineru_blocks.tables AS "表",
    _mineru_blocks.formulas AS "公式",
    _mineru_blocks.images AS "图",
    (_mineru_blocks.tables + _mineru_blocks.formulas + _mineru_blocks.images) AS "合计"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split"
SORT (_mineru_blocks.tables + _mineru_blocks.formulas + _mineru_blocks.images) DESC
LIMIT 30
```

---

## 按主题看 MinerU 覆盖率

> 能看出哪些技术领域已补强，哪些还缺。

```dataview
TABLE WITHOUT ID
    topic AS "主题",
    length(rows.file.link) AS "升级数",
    sum(rows._mineru_blocks.tables) AS "表",
    sum(rows._mineru_blocks.formulas) AS "公式",
    sum(rows._mineru_blocks.images) AS "图"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split"
GROUP BY topic
SORT length(rows.file.link) DESC
```

---

## 按区域看 MinerU 覆盖率

```dataview
TABLE WITHOUT ID
    region AS "区域",
    length(rows.file.link) AS "升级数",
    sum(rows._mineru_blocks.tables) AS "表",
    sum(rows._mineru_blocks.formulas) AS "公式",
    sum(rows._mineru_blocks.images) AS "图"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split"
GROUP BY region
SORT length(rows.file.link) DESC
```

---

## 富公式 notes（公式 ≥ 5）

> 含大量 LaTeX 公式的 notes，适合工程计算公式检索。

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    _mineru_blocks.formulas AS "公式数",
    topic AS "主题"
FROM "01_Wiki/regulations"
WHERE (_ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split") AND _mineru_blocks.formulas >= 5
SORT _mineru_blocks.formulas DESC
```

---

## 富表格 notes（表格 ≥ 5）

> 含大量数据表的 notes，适合查具体限值、阈值、等级划分。

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    _mineru_blocks.tables AS "表格数",
    topic AS "主题"
FROM "01_Wiki/regulations"
WHERE (_ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split") AND _mineru_blocks.tables >= 5
SORT _mineru_blocks.tables DESC
```

---

## 富图像 notes（图像 ≥ 5）

> 含大量原图的 notes（示意图、结构图、原理图）。

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    _mineru_blocks.images AS "图像数",
    topic AS "主题"
FROM "01_Wiki/regulations"
WHERE (_ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split") AND _mineru_blocks.images >= 5
SORT _mineru_blocks.images DESC
```

---

## 按日期追踪

> 每次 MinerU 运行补多少条。

```dataview
TABLE WITHOUT ID
    _mineru_merged_at AS "合并日",
    length(rows.file.link) AS "当日新增",
    sum(rows._mineru_blocks.tables) AS "表",
    sum(rows._mineru_blocks.formulas) AS "公式",
    sum(rows._mineru_blocks.images) AS "图"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru" OR _ocr_upgraded = "mineru_split"
GROUP BY _mineru_merged_at
SORT _mineru_merged_at DESC
```

---

## 已 skip 的 notes 及原因

> 13 条中文扫描冗余 / 综述书 / 超大件。已在 FM 标记 `_ocr_skip_reason`。

```dataview
TABLE WITHOUT ID
    file.link AS "Note",
    reg_id AS "reg_id",
    _ocr_skip_reason AS "跳过原因",
    _ocr_skip_note AS "说明"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "skipped"
SORT _ocr_skip_reason ASC
```

## 仅运行了 OCR 但无结构化资产的 notes（纯文本 amendment）

> 406 条，按 region/topic 看分布。这些 notes 本身已是净文本，无需 OCR 进一步处理。

```dataview
TABLE WITHOUT ID
    region AS "区域",
    length(rows.file.link) AS "notes"
FROM "01_Wiki/regulations"
WHERE _ocr_upgraded = "mineru_no_assets"
GROUP BY region
SORT length(rows.file.link) DESC
```

---

## 使用建议

- **引用 / 写论文**：优先挑**表格+公式+图像合计最多**的 notes，内容最丰富
- **查具体数值**：用 `_mineru_blocks.tables >= 5` 筛选
- **查理论/计算公式**：用 `_mineru_blocks.formulas >= 5` 筛选
- **看结构图**：打开 note 后跳到"## 原文参考（MinerU 云解析）"末尾的"### 图像"节

## FM 字段参考

```yaml
# 1. 常规 MinerU 升级
_ocr_upgraded: mineru              # 含表/公式/图
_mineru_content_hash: abc123...    # PDF hash 去重
_mineru_outputs_dir: outputs/abc123 # 原始 MinerU 输出位置
_mineru_blocks:
  tables: 10
  formulas: 3
  images: 8
_mineru_merged_at: '2026-04-22'

# 2. 超页 PDF 多 part 合并
_ocr_upgraded: mineru_split
_mineru_split_parts:
  - part: 1
    pages: 180
    outputs_dir: outputs\ECE_R37_Rev8__part1
  - part: 2
    pages: 37
    outputs_dir: outputs\ECE_R37_Rev8__part2
_mineru_blocks: {tables: 13, formulas: 2, images: 12}

# 3. OCR 跑了但无结构化内容的小文件补标记
_ocr_upgraded: mineru_no_assets
_mineru_done_at: '2026-04-25'
_mineru_outputs_dir: outputs/<hash>

# 4. 显式跳过的边缘案例
_ocr_upgraded: skipped
_ocr_skip_reason: skip_redundant_chinese | skip_split_pending | skip_non_regulation | skip_oversize_unprocessable
_ocr_skip_note: "<人读说明>"
_ocr_skipped_at: '2026-04-25'
```

## 相关资产

- 原始 MinerU 输出：`@D:\CcVault\99_SystemScripts\mineru_upgrade\outputs\<hash>\`
- 图像资产：`@D:\CcVault\01_Wiki\regulations\_mineru_assets\<reg_id>\`
- 管道脚本：`@D:\CcVault\99_SystemScripts\mineru_upgrade\`
- 升级日志：`@D:\CcVault\_MINERU_UPGRADE_LOG_2026-04-22.md`
