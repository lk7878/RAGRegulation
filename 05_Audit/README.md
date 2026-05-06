---
type: folder_readme
tags:
- type/readme
---

# 05_Audit/ — 人工反馈闭环

> 此目录存放**人工发现的 note 问题**，供 agent 批量处理。

## 快速上手

1. 看到某条 note 有错：**复制** `_template.md` → 命名为 `YYYY-MM-DD_<brief>.md`
2. 填 FM 里的 `target_file` / `severity` / `category` + 写 Issue / Expected
3. 累积到 N 条后，在 Cascade 里打 `/process_audits` 批量处理
4. Agent 会改 note + 标 resolved + 报告

## 命名约定

**文件名**：`YYYY-MM-DD_<3-8单词brief>.md`

**例子**：
- `2026-04-19_GB4785_missing_NO_class.md`
- `2026-04-20_ECE_R48_wrong_date.md`
- `2026-04-22_brake_topic_misclassified.md`

**brief** 要简短能一眼看出问题。

## 详细说明

见 `@05_Audit/_Audit MOC.md`。
