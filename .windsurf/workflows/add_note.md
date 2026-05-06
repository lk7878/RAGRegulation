---
description: 手工新增一条法规 note - 根据用户描述或 PDF 补齐完整 FM 并建立双向链
---

# /add_note — 新增一条法规 note

## 触发场景

用户直接给出法规信息（不走 OCR pipeline），或手头有一份 PDF 但不想走完整入库流程。

典型用户表达：
- "新增 GB XXXXX-2026，替代 GB XXXXX-2019，属于 brakes 主题"
- "把这份 PDF 读一下建个 note"
- "新增 UN R158 Rev2 Am3，publication_date 2026-03-15"

## 执行步骤

### 1. 信息收集

如果用户描述不完整，**主动问**以下信息：
- **reg_id**（必填）：规范化编号（GB XX-YYYY / UN RXXX RevN AmM）
- **title**（必填）：标题（中文 + 英文更好）
- **region**（必填）：cn/ece/eu/us/...
- **type**：regulation / version / amendment（从 reg_id 推断）
- **publication_date** / **implementation_date**（若知道）
- **status**：active（默认）/ superseded / draft / ...
- **替代了什么**：supersedes 列表
- **对应外国法规**：equivalent_to（与 ref/relation）
- **所属主题**：topic key（见 `02_Schema/02_taxonomy.md`）
- **摘要和范围**（summary + scope 各 1-3 句）

### 2. 唯一性检查

```powershell
# 检查 reg_id 是否已存在
Get-ChildItem -Path D:\CcVault\01_Wiki\regulations -Recurse -Filter "*.md" | 
    ForEach-Object { 
        if ((Get-Content $_ -First 5 | Out-String) -match "reg_id:\s*$regId") {
            Write-Host "EXISTS: $($_.FullName)"
        }
    }
```
// turbo

若已存在 → 告诉用户具体路径，问是否要更新而非新增。

### 3. 确定文件路径

规则：
- CN: `D:\CcVault\01_Wiki\regulations\cn\<reg_id>.md`（空格代替 `/`）
- ECE: `D:\CcVault\01_Wiki\regulations\ece\<reg_id>.md`
- 其他：`D:\CcVault\01_Wiki\regulations\<region>\<reg_id>.md`

**文件名规范**：
- `GB 4785-2019.md`（不是 `GB/4785-2019.md` 或 `GB_4785-2019.md`）
- `UN R094 Rev4 Am1.md`（规范化 padding 到 3 位数字）
- 如果已有同名 → 加 `_dup1` / `_dup2`

### 4. 写新 note

按 `CLAUDE.md` 第 3 节 FM schema 写完整 note。参考模板：

```markdown
---
reg_id: <reg_id>
title: <中文标题>
title_en: <英文标题>
type: <regulation|version|amendment>
region: <region_code>
status: <active|superseded|...>
publication_date: YYYY-MM-DD
implementation_date: YYYY-MM-DD
source_pdf: <路径或空>
summary: <2-3 句中文摘要>
scope: <适用范围描述>
supersedes:
  - <旧版 reg_id 或空>
superseded_by: []
equivalent_to:
  - ref: <外国 reg_id>
    relation: equivalent
    source: manually_added
keywords: [<关键词列表>]
cross_check_overall_confidence: high
cross_check_flags: []
tags:
  - reg/<region>
  - type/<type>
  - status/verified
  - topic/<topic_key>
---

# <reg_id> <title>

## 摘要
<summary 展开>

## 范围
<scope 展开>

## 关键要求
<根据用户给的信息或 PDF 内容>

## 试验与验证
<若有>

## 参考
<外联法规 wikilinks>
```

### 5. 建立双向链

**如果 supersedes 有值**（替代了老版本）：
对每个被替代的 reg_id：
1. 找到老 note 文件
2. 在 FM 里：
   - `status: superseded`
   - `superseded_by: [<新 reg_id>]`（追加而非覆盖）
3. 如果老 note 的 tags 没有 `status/superseded` 则加上

```powershell
# 示例：找老版本
Get-ChildItem -Path D:\CcVault\01_Wiki\regulations -Recurse -Filter "<old_reg_id>.md"
```
// turbo

### 6. 更新主题页

找到对应 topic 的主题页：`04_Topics\<topic_label>.md`

在"完整索引"段的对应 region 下插入新 note 的 wikilink，按 publication_date 倒序。

### 7. 更新等价映射（若有 equivalent_to）

若新 note 引入了新的跨区域关系：
1. 读 `03_Equivalence/_Equivalence MOC.md`
2. 在对应主题的映射表里加一行
3. 调用 `_apply_equivalences_to_notes.py` 回写到 FM

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _apply_equivalences_to_notes.py
```
// turbo

### 8. 重建索引

```powershell
.\.venv\Scripts\python.exe _build_supersession_chain.py
.\.venv\Scripts\python.exe _semantic_search.py --rebuild
```
// turbo

### 9. 验证

1. 读回新 note 确认 FM 解析正确
2. 打开替代的老 note 确认双向链正确
3. 用 `_semantic_search.py` 搜新 reg_id 能找到

### 10. 报告

```markdown
# 新增 Note 完成

## 新创建
- `@<full_path>` — <reg_id> <title>

## 双向链更新
- <old_reg_id>.md: 添加 superseded_by → <new_reg_id>

## 主题页更新
- `@04_Topics/<topic>.md` — 新 note 已加入完整索引

## 等价映射（如有）
- <new_reg_id> ↔ <foreign_reg_id> (<relation>)

## 索引重建
- BM25 ✓ / Supersession chain ✓
```

## 禁止事项

1. ❌ 不要在没有用户确认的情况下手动改 `manifest.json`
2. ❌ 不要创建 `01_Wiki/regulations/` 下的子目录（region 级以外）
3. ❌ 不要省略 required FM 字段（reg_id / title / region / status）
4. ❌ 不要 hallucinate 日期或 title —— 不确定就问或留空
5. ❌ 如果 PDF 内容用户没给，不要自己编关键要求
