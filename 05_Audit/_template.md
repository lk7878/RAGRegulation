---
# ─── 定位（必填）───
target_file: 01_Wiki/regulations/<region>/<reg_id>.md
target_reg_id: <reg_id>

# ─── 可选定位信息 ───
target_section: ""          # 例: "## 摘要" 或 "## 关键要求"
target_anchor: ""           # 原文片段（帮助 agent 快速定位）

# ─── 分类（必填）───
severity: medium            # low | medium | high | critical
category: accuracy          # accuracy | completeness | classification | link | formatting | other
status: open                # 新建时始终为 open

# ─── 时间 ───
created: 2026-04-19T00:00:00
resolved: null
resolver: null

# ─── Tags ───
tags:
  - audit/open
  - audit/severity-medium
  - audit/category-accuracy
---

## Issue

<描述发现的问题，2-5 句>

## Expected

<期望怎么改，1-3 句>

## Resolution

<agent 处理时填，描述实际改动>

## Related

<可选：相关 audit 链接 / 参考文档 / 原文截图>
