---
type: audit_report
created: 2026-04-21
category: dedupe_resolution_proposal
severity: medium
status: resolved
resolved: 2026-04-23
resolver: cascade
tags: [audit/dedupe, audit/proposal, audit/llm_review, audit/resolved]
---

> **Resolution 追加（2026-04-23）**：
>
> 全 vault 扫描确认，原 proposal 中 12 组 "📑 两份都留（重命名为 (EN)）" 的建议**已全部执行完毕**：
> 对应的 `01_Wiki/regulations/ece/ECE R* (EN).md` 共 12 份文件均已在位（见下方清单）。
> 剩余 4 组（`ECE R13` reg_id 修正、`GB/T 38892-2020` 替换、`GB 21670-2008` 替换需核实、`(EU) 2018/858` 需拆分）**未执行**，归为后续 backlog 另起 audit 处理。
>
> **已落地的 12 份 (EN) 文件**：
> - `[[ECE R108 (EN)]]` (72KB)
> - `[[ECE R102 (EN)]]` (13KB)
> - `[[ECE R114 (EN)]]` (13KB)
> - `[[ECE R122 (EN)]]` (13KB)
> - `[[ECE R55 Rev1 Corr1 (EN)]]` (5KB)
> - `[[ECE R21 Rev2 (EN)]]` (16KB)
> - `[[ECE R42 (EN)]]` (16KB)
> - `[[ECE R68 (EN)]]` (22KB)
> - `[[ECE R59 (EN)]]` (14KB)
> - `[[ECE R84 (EN)]]` (8KB)
> - `[[ECE R89 (EN)]]` (8KB)
> - `[[ECE R93 (EN)]]` (19KB)
>
> **注意事项**：这 12 份文件的 FM 里**没有** `language: en` 或 `_dedupe_renamed_from` 审计字段，建议后续补一次批量元数据补齐（不紧急）。
>
> **本次扫描新发现的 5 个新 _dup 文件**（不在原 proposal 范围，2026-04-21 之后新增）：
> - `ECE R125_dup1.md` (30.6 KB, 2026-04-22)
> - `ECE R127_dup1.md` (10 KB, **2026-04-23 今日新增**)
> - `ECE R135_dup1.md` (43.1 KB, 2026-04-22)
> - `ECE R144_dup1.md` (8.1 KB, 2026-04-18)
> - `(EU) 2018 858_dup1.md` (66 KB, 2026-04-22) — 可能就是原 proposal 未处理的 🔴 需拆分项，已转移到 01_Wiki 未 trash
>
> **后续 audit**：应针对这 5 个新 _dup 触发一轮 `/dedupe` 或手工审阅，写到新的 audit 文件。

# Dedupe 冲突处理建议（Claude Opus 审阅）

> 从 `dedupe_conflicts_2026-04-21.md` 的 16 组冲突里，Opus 4.6 逐组审阅两份 FM + body 给出处理建议。
> **本报告不执行任何动作**，仅供人工快速决策。成本 $1.44。

## 决策汇总

| 决策 | 组数 | 说明 |
| --- | ---: | --- |
| 🗑️ 删 _dup（canonical 足够） | 0 | |
| 🔄 _dup 替换 canonical | 2 | |
| 📑 两份都留（_dup 重命名） | 13 | |
| 🔀 合并 _dup 到 canonical | 0 | |
| ❓ 需要人工判断 | 1 | |

## 操作说明

1. 逐条读 Opus 的 reason + diff_summary
2. 同意 → 按 decision 执行（手工或写脚本）
3. 不同意 → 标注后交给人工流程（`/process_audits`）

## 🔄 _dup 替换 canonical  · 2 组

### `GB/T 38892-2020` 🟢

- **canonical**：`cn\GB T 38892-2020.md` (body=3574, conf=high)
- **dup**：`cn\GB T 38892-2020_dup1.md` (body=10272, conf=high)
- **判定**：🔄 _dup 替换 canonical · 风险 low
- **差异摘要**：canonical 为摘要压缩版（3574字），对各条款仅做概括描述，引用文件未列出具体版本号；_dup 为接近原文的展开版（10272字），引用文件含完整版本号，术语定义含公式和注释，条款编号细化至小节，整体结构更贴近标准原文。
- **理由**：_dup 的 body 总长度为 10272，是 canonical 的 2.87 倍，且内容结构更完整：引用文件列出了完整的标准名称和版本号，术语定义包含公式和详细注释，各条款编号精确到小节级别（如 5.1.1）。canonical 仅为摘要式压缩描述，_dup 则保留了原文逐条表述，信息密度和完整性均明显优于 canonical。两者 confidence 同为 high，语言相同，来源为同一标准，_dup 可直接替换 canonical。

### `GB 21670-2008` 🟡

- **canonical**：`cn\GB 21670-2008.md` (body=5568, conf=medium)
- **dup**：`cn\GB 21670-2008_dup1.md` (body=20236, conf=medium)
- **判定**：🔄 _dup 替换 canonical · 风险 medium
- **差异摘要**：两份均为中文同一标准，标题相同。_dup body 约为 canonical 的3.6倍，包含完整的前言差异列表、起草单位/人员名单、规范性引用文件完整条文、术语定义逐条展开等；canonical 仅有摘要式描述。FM 差异：canonical status=active，_dup status=superseded，需人工核实。
- **理由**：_dup 的 body 长度为 20236，是 canonical（5568）的约3.6倍。_dup 前言部分逐条列出了与ECE R13-H的差异明细、附录归属说明、起草单位及起草人名单等完整信息，而 canonical 仅作摘要性描述。_dup 的术语定义条目展开为独立编号条款，结构更完整规范。两者语言相同、来源同一标准，_dup 明显是更完整的提取版本，canonical 是其摘要残缺版。唯一差异是 FM 中 status 字段：canonical 为 active，_dup 为 superseded，此点需在替换后人工核实确认以哪个为准。

## 📑 两份都留（_dup 重命名）  · 13 组

### `ECE R108` 🟢

- **canonical**：`ece\ECE R108.md` (body=2400, conf=medium)
- **dup**：`ece\ECE R108_dup1.md` (body=48347, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A 为中文摘要版，body 仅2400字，confidence medium，来源于ECE中文法规文件夹；B 为英文完整原文，body 达48347字，confidence high，来源于官方英文PDF（R108e.pdf）。内容覆盖范围相同但语言不同，B 包含远比 A 详尽的条款原文。
- **理由**：A 为中文译本（来源于ECE中文法规文件夹），B 为英文原版官方文件（R108e.pdf，文件名含'e'标准英文后缀）。两份 title 一中一英，source_file 路径完全不同，属于典型的同一法规不同语言版本。B 的 body 长度（48347）约为 A（2400）的20倍，confidence 也更高（high vs medium），说明 B 是全文英文原版，A 是中文摘要译本，两者均有独立保存价值，不应互相替代或合并。
- **建议重命名**：`ECE R108 (EN).md`

### `ECE R102` 🟢

- **canonical**：`ece\ECE R102.md` (body=2642, conf=high)
- **dup**：`ece\ECE R102_dup1.md` (body=10826, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：canonical 为中文摘要版，结构化归纳各章节要点，body 约 2642 字；_dup 为英文原版全文（r102e.pdf 提取），含逐条条款编号（2.1.1、5.1 等），body 约 10826 字，内容更完整详细，并有 publication_date 等额外元数据。两者语言不同，详略差异显著。
- **理由**：两份 note 标题一份为中文、一份为英文，分别来自不同来源（canonical 无 source_file，_dup 来自官方英文 PDF r102e.pdf）。_dup 是英文原版法规全文（body 长达 10826 字，含完整条款编号结构），canonical 是中文摘要性翻译（2642 字，信息经过提炼压缩）。两者语言不同、详略程度不同，各有独立保留价值，不应相互替换或丢弃。
- **建议重命名**：`ECE R102 (EN).md`

### `ECE R114` 🟢

- **canonical**：`ece\ECE R114.md` (body=3059, conf=medium)
- **dup**：`ece\ECE R114_dup.md` (body=10884, conf=medium)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：canonical 为中文译本（3059字），结构以摘要形式呈现关键条款；_dup 为英文原版（10884字），按条款编号逐条展开全文，内容更完整详细。标题语言不同，正文语言完全不同，属于同一法规的中英双语版本。
- **理由**：canonical 为中文译本，_dup 为英文原版，两者标题语言不同、body 语言完全不同，均为 ECE R114 的有效版本。_dup body 长度约为 canonical 的3.6倍，内容更完整，保留两份各有价值：中文版便于中文用户查阅，英文版提供原文权威性。两份 confidence 均为 medium，无明显质量差距。
- **建议重命名**：`ECE R114 (EN).md`

### `ECE R122` 🟢

- **canonical**：`ece\ECE R122.md` (body=2686, conf=high)
- **dup**：`ece\ECE R122_dup.md` (body=5300, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A为中文译本，body长2686字，来自ECE中文法规库，部分措辞存在翻译不准确（如内政部、负荷面积等）；B为英文原版R122e，body长5300字，内容更完整，条款编号更细致，来自UNECE官方英文PDF，发布日期略晚（2006-02-23 vs 2006-01-18）。
- **理由**：两份文件标题一份为中文（各类M、N及O型车辆加热系统认证的统一规定），一份为英文（Uniform technical prescriptions concerning the approval of vehicles of categories M, N and O with regard to their heating systems），来源PDF也不同（中文法规目录 vs UNECE英文原版R122e.pdf），属于典型的中译版与英文原版并存情形，两份均有独立保留价值。
- **建议重命名**：`ECE R122 (EN).md`

### `ECE R13` 🟡

- **canonical**：`ece\ECE R13.md` (body=2477, conf=high)
- **dup**：`ece\ECE R13 Rev4 Am2.md` (body=569, conf=low)
- **判定**：📑 两份都留（_dup 重命名） · 风险 medium
- **差异摘要**：canonical 是 ECE R13 中文完整版（2001年，09系列修正本，覆盖M/N/O类车辆），body 结构完整；_dup 实为 ECE R13-H 英文修正本（2021年，Rev4 Am2），仅含单条附录修正文字，reg_id 标注有误（被归入R13），两者法规性质、语言、版本、适用范围均不同。
- **理由**：两份文件实质上是不同法规：canonical 是 ECE R13（适用于M、N、O类车辆制动）的中文版，body 长达2477字，confidence high；_dup 实为 ECE R13-H（仅适用于乘用车制动）的英文修正本 Rev4 Am2，仅包含附录3第1.5.3.1条的单条修正文本，发布日期2021年，两者法规编号、适用范围、语言、版本及内容均不同，都有独立保存价值。
- **建议重命名**：`ECE R13-H Rev4 Am2 (EN).md`

### `ECE R55 Rev1 Corr1` 🟢

- **canonical**：`ece\ECE R55 Rev1 Corr1.md` (body=896, conf=high)
- **dup**：`ece\ECE R55 Rev1 Corr1_dup1.md` (body=2492, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A为中文译版，body 896字，来源明确为中文ECE法规PDF；B为英文原版，body 2492字，包含文件编号E/ECE/324 Rev.1/Add.54/Rev.1/Corr.1及更详细的范围说明和背景描述。核心更正内容一致，但语言和详略程度不同。
- **理由**：两份文件标题一份为中文（关于车辆组机械结合元件认证的统一规定），一份为英文（UNIFORM PROVISIONS CONCERNING THE APPROVAL OF MECHANICAL COUPLING COMPONENTS OF COMBINATIONS OF VEHICLES），内容语言完全不同，分别来自中文ECE法规库和英文原版文档。两份confidence均为high，body长度差异（896 vs 2492）是因为英文版包含更多上下文说明，而非质量问题。应作为独立语言版本分别保留。
- **建议重命名**：`ECE R55 Rev1 Corr1 (EN).md`

### `ECE R21 Rev2` 🟢

- **canonical**：`ece\ECE R21 Rev2.md` (body=5450, conf=high)
- **dup**：`ece\ECE R21 Rev2_dup1.md` (body=11391, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A 为中文意译版，body 5450 字，覆盖附件技术细节（测试装置、H 点程序等），无 source_file 记录；B 为英文原版 PDF 提取，body 11391 字，含完整 Scope、Definitions、Application for Approval 等正文条款，有明确 publication_date（1993-10-12）和 source_file，结构更接近官方原文。
- **理由**：A 为中文翻译版（body 以中文撰写，标题为中英混合），B 为英文原版（来自官方 PDF R021r2e_1.pdf，body 全英文，包含完整 Scope/Definitions/Application 等原文条款结构）。两者语言不同、来源不同，各有独立使用价值：中文版便于中文用户查阅，英文版保留原始法规措辞。B 的 body 长度（11391）约为 A（5450）的 2 倍，且含有 A 未覆盖的定义条款与申请流程原文，不宜丢弃任何一份。
- **建议重命名**：`ECE R21 Rev2 (EN).md`

### `ECE R42` 🟢

- **canonical**：`ece\ECE R42.md` (body=3334, conf=high)
- **dup**：`ece\ECE R42_dup1.md` (body=13008, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A 为中文翻译版，body 3334 字，无 source_file 记录，缺少目录和发布日期；B 为英文官方原版（R042e.pdf），body 13008 字，包含完整章节目录、附件清单及生效日期（1980-03-24），内容更完整，语言不同，来源 PDF 不同。
- **理由**：两份文件标题一份为中文（关于汽车前后保护装置认证的统一规定），一份为英文原版（UNIFORM PROVISIONS CONCERNING THE APPROVAL OF VEHICLES...），明显是同一法规的不同语言版本。_dup 来源于官方英文 PDF（R042e.pdf），body 长度达 13008 字符，约为 canonical 中文版（3334 字符）的 3.9 倍，且包含完整目录、附件列表及发布日期等 canonical 未收录的元信息，两者均有独立保留价值。
- **建议重命名**：`ECE R42 (EN).md`

### `ECE R68` 🟢

- **canonical**：`ece\ECE R68.md` (body=1684, conf=high)
- **dup**：`ece\ECE R68_dup1.md` (body=17620, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A为中文译本，body长度1684字，内容涵盖电动车辆相关定义及测试条款（含30min最高速度等），结构为中文摘要式。B为英文原版，body长度17620字（约为A的10倍），保留完整原文条款编号、附件结构及精确法规语言，且有明确发布日期1987-04-15。
- **理由**：两份文件一份为中文译本（来自ECE法规中文合集），一份为英文原版（来自UNECE官方PDF R068e.pdf），语言完全不同，均有独立保存价值。中文版供中文用户快速检索，英文版为权威原文。两份confidence均为high，无质量劣势之分，不应互相替代或丢弃。
- **建议重命名**：`ECE R68 (EN).md`

### `ECE R59` 🟢

- **canonical**：`ece\ECE R59.md` (body=2896, conf=high)
- **dup**：`ece\ECE R59_dup1.md` (body=10603, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：canonical为中文译本，body约2896字，结构完整但无附件详情；_dup为英文原版，body约10603字，包含完整目录、附件列表（Annex 1-4）及更详细的条款内容，另附有publication_date字段（1983-09-22），来源PDF不同。
- **理由**：两份文件标题分别为中文（关于替代消声系统认证的统一规定）和英文（UNIFORM PROVISIONS CONCERNING THE APPROVAL OF REPLACEMENT SILENCING SYSTEMS），来源不同（中文PDF vs 英文原版），内容均为同一法规的不同语言版本。_dup的body长度（10603）约为canonical（2896）的3.7倍，英文版还包含完整目录和附件列表，两者均有独立保留价值，不应丢弃任何一份。
- **建议重命名**：`ECE R59 (EN).md`

### `ECE R84` 🟢

- **canonical**：`ece\ECE R84.md` (body=2384, conf=high)
- **dup**：`ece\ECE R84_dup1.md` (body=6029, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：canonical为中文译本（body 2384字），含详细翻译信息、附录清单及中文注释，source明确为中文ECE法规库PDF；_dup为英文原版（body 6029字，约为canonical的2.5倍），结构更接近UN官方原文，无source_file字段。两者语言不同，内容详略有差异。
- **理由**：两份文件标题一份为中文（关于装用内燃机轿车和轻型载货汽车燃料消耗量测量认证的统一规定）、一份为英文（Uniform provisions concerning...），来源PDF不同，canonical明确标注来自ECE中文法规库且有翻译机构信息，_dup为英文原版。两者均为high confidence，内容结构对应同一法规但语言不同，各有独立保存价值，不应互相替代或丢弃。
- **建议重命名**：`ECE R84 (EN).md`

### `ECE R89` 🟢

- **canonical**：`ece\ECE R89.md` (body=1624, conf=high)
- **dup**：`ece\ECE R89_dup1.md` (body=5784, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：canonical为中文整理版，结构以法规章节目录为主，body较短（1624字），注明含OCR错误修正；_dup为英文原版提取，body更长（5784字），包含更多具体技术要求细节（如防篡改、制动系统不干预、加速踏板逻辑），并有publication_date字段。
- **理由**：两份文件标题一份为中文、一份为英文，分别对应ECE R89的中文译本与英文原版。canonical为中文整理版（含OCR修正说明），_dup为英文原文提取版，内容更详细（body长度5784 vs 1624），且包含中文版未涉及的具体技术条款细节（如不干预制动系统、加速踏板覆盖等）。两者均有独立价值，应作为独立note分别保留。
- **建议重命名**：`ECE R89 (EN).md`

### `ECE R93` 🟢

- **canonical**：`ece\ECE R93.md` (body=479, conf=high)
- **dup**：`ece\ECE R93_dup1.md` (body=16222, conf=high)
- **判定**：📑 两份都留（_dup 重命名） · 风险 low
- **差异摘要**：A为中文摘要版（body仅479字，含中文scope和结构性摘要），来源于ECE中文法规PDF；B为英文完整原文（body达16222字，含完整目录、条款编号及SCOPE原文），来源于UNECE官方英文PDF R093e，两者语言不同、详细程度差异极大。
- **理由**：A是中文译本（来自ECE中文法规文件夹，title为中文），B是英文原版官方文本（来自UNECE标准文件夹，title为英文全称，body长度16222远大于A的479）。两者均有独立保存价值：中文版供国内工程师查阅，英文版为权威原文参考。应将_dup重命名为独立note保留。
- **建议重命名**：`ECE R93 (EN).md`

## ❓ 需要人工判断  · 1 组

### `(EU) 2018/858` 🔴

- **canonical**：`eu\(EU) 2018 858.md` (body=15828, conf=medium)
- **dup**：`eu\(EU) 2018 858_dup1.md` (body=25775, conf=medium)
- **判定**：❓ 需要人工判断 · 风险 high
- **差异摘要**：canonical 是以 (EU) 2018/858 为主题的综述介绍文档（15828字），内容聚焦于欧盟认证流程与法规体系；_dup（25775字）来自不同PDF，body 实际包含多个不同 reg_id 的法规条目（如 2019/2144、2023/2867 等），与 (EU) 2018/858 无直接对应关系，疑似多法规汇编被错误赋予同一 reg_id。
- **理由**：两份文件虽然共享 reg_id (EU) 2018/858，但实质内容差异极大：canonical 是一份介绍欧盟汽车准入流程与法规体系的综述性文档，以 (EU) 2018/858 作为核心框架法规加以介绍；而 _dup 文件实际上是一个多法规汇编索引，body 前段已出现 reg_id (EU) 2019/2144、(EU) 2023/2867 等完全不同的法规条目，说明该 PDF 包含多条法规的提取结果，且其自身 FM 标注的 reg_id 也可能存在错误标注。需要人工确认 _dup 的 reg_id 是否系误标，以及该文件的正确拆分方式。

---

*由 `_resolve_dedupe_conflicts_llm.py` 生成 · 2026-04-21 · 模型: [渠道二-官-量]claude-opus-4-6*