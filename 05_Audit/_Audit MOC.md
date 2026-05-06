---
type: audit_moc
tags:
- type/moc
- scope/audit
---

# Audit MOC · 人工反馈闭环

> 基于 [Karpathy LLM Wiki + lewislulu/llm-wiki-skill](https://github.com/lewislulu/llm-wiki-skill) 的 audit 模式，适配 CcVault。
> 用于**人工发现的错误 / 改进建议**的累积和批量处理。

---

## 什么是 Audit？

**痛点**：阅读 note 时发现问题，不想中断阅读去对话改，又怕忘记。

**解法**：
1. 在 `05_Audit/` 新建一条 audit 条目（10-30 秒）
2. 写清楚 target / issue / expected
3. 累积一批后调用 `/process_audits` 让 agent 批量处理

---

## 使用流程

### 1. 新建 audit

**方式 A**：手工复制模板
- 复制 `05_Audit/_template.md` 为 `05_Audit/2026-04-19_<brief>.md`
- 填 FM（target_file / severity / category）+ Issue + Expected

**方式 B**：Obsidian Templater 插件（推荐，秒级）
- 见 `@D:\CcVault\02_Schema\06_audit_templater_setup.md` 配置指南
- 快捷键 `Ctrl+Shift+A` 一键建

### 2. 累积

连续阅读库时不断新增 audits（可持续几天到几周）。

### 3. 批量处理

在 Cascade 里：
```
/process_audits
```

Agent 会：
- 扫所有 `status: open` 的 audits
- 按 target_file 分组
- 逐条读 + 改对应 note
- 把 audit 标 `resolved` 并填 Resolution
- 给你总报告

### 4. 归档

resolved 的 audit 保留在原目录作为历史记录，用 Dataview 过滤。

---

## 📊 当前面板

### 待处理 Audits（按严重度）

```dataview
TABLE WITHOUT ID
    file.link AS "Audit",
    target_reg_id AS "Target",
    severity AS "Severity",
    category AS "Category",
    dateformat(created, "yyyy-MM-dd") AS "Created"
FROM "05_Audit"
WHERE status = "open"
SORT severity DESC, created ASC
```

### 按严重度统计

```dataview
TABLE WITHOUT ID
    severity AS "Severity",
    length(rows) AS "Count"
FROM "05_Audit"
WHERE status = "open"
GROUP BY severity
SORT severity DESC
```

### 最近 30 天 resolved

```dataview
TABLE WITHOUT ID
    file.link AS "Audit",
    target_reg_id AS "Target",
    dateformat(resolved, "yyyy-MM-dd") AS "Resolved",
    resolver AS "By"
FROM "05_Audit"
WHERE status = "resolved" AND resolved >= date(today) - dur(30 days)
SORT resolved DESC
LIMIT 20
```

### 按目标文件聚合（看哪些 note 被反馈最多）

```dataview
TABLE WITHOUT ID
    target_reg_id AS "Reg",
    length(rows) AS "# Audits"
FROM "05_Audit"
WHERE status = "open"
GROUP BY target_reg_id
SORT length(rows) DESC
LIMIT 10
```

---

## 🏷️ Severity 约定

| 级别 | 含义 | 例子 |
|---|---|---|
| `critical` | 数据错误影响决策 | reg_id 错误 / 区域归属错误 |
| `high` | 主要字段错误 | title 错字 / 日期错 / supersedes 链错 |
| `medium` | 摘要或内容错 | summary 遗漏关键点 / scope 描述不全 |
| `low` | 格式或可读性 | 排版 / 术语不统一 |

## 📁 Category 约定

| 类别 | 含义 |
|---|---|
| `accuracy` | 内容准确性问题 |
| `completeness` | 内容完整性（缺失关键信息） |
| `classification` | 分类 tag 错（topic/status） |
| `link` | wikilink / supersedes / equivalent_to 错 |
| `formatting` | 排版格式问题 |
| `other` | 其他 |

## 🔄 Status 生命周期

```
open → in_progress → resolved
                  ↘ wont_fix
                  ↘ duplicate
                  ↘ deferred           (有 target_eta，明确推迟)
                  ↘ needs_human_confirm (agent 给出方案等用户点头)
```

- `open`：新建，等处理
- `in_progress`：agent 正在处理（通常只在 agent 跑 `/process_audits` 时短暂出现）
- `resolved`：已解决，填了 Resolution
- `wont_fix`：确认是意向错误或无法修复
- `duplicate`：和已有 audit 重复，指向原始 audit
- `deferred`：承认问题但主动推迟（必须有 `target_eta` 字段）—— 如等待外部依赖 / 后续 phase / 预算窗口
- `needs_human_confirm`：agent 准备了方案但涉及不可逆或重大改动，等人工点头再执行

---

## 🔗 相关

- Workflow：`@D:\CcVault\.windsurf\workflows\process_audits.md`
- 模板：`@D:\CcVault\05_Audit\_template.md`
- Templater 配置：`@D:\CcVault\02_Schema\06_audit_templater_setup.md`
- CLAUDE.md 第 12 节：Audit Loop 运营规则

---

**最后更新**：2026-04-23
