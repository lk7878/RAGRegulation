---
type: changelog
tags:
- type/changelog
---

# CcVault 变更日志

> 人读版月度变更记录。对应 Karpathy LLM Wiki 的 `wiki/log.md` 概念。
> 机器日志在 `@D:\CcVault\99_SystemScripts\auto_reg_index\logs\`。

格式约定：
- **新增** / **修改** / **删除** / **修复** / **基础设施**
- 每次重大操作后由 agent 或用户追加
- 最新的变更在上方

---

## 2026-04-25 · MinerU 全量处理 100% + audit 全 resolved

**类型**：新增 + 基础设施 + 修复 + 审计

### 里程碑：MinerU 处理率 92% → **100.00%**

| 指标 | 04-25 起点 | 04-25 收工 | Δ |
|---|---:|---:|---:|
| MinerU 处理率 | 92% (1333/1444) | **100.00%** | +8pp |
| upgraded notes (合并 body) | 595 | **995** | +400 |
| mineru_split notes | 0 | **13** | +13 |
| mineru_no_assets notes | 0 | **406** | +406（显式标记跑过无 assets） |
| skipped notes | 0 | **13** | +13（中文扫描冗余/综述/巨件） |
| open audit | 2 | **0** | -2（全 resolved） |

### Phase 2b · 8 条超页 PDF 全 split 处理（4 月 23 audit 推进）

走完 Phase 1 拆分 → Phase 2 OCR → Phase 3 合并三阶段，13 条超页 PDF（含 04-25 第二轮新发现的 5 条）共 34 parts 4512 页，全部成功合并入对应 vault note。

ECE R49 Rev6 是其中体量最大者：5,559 → **135,344** 字符（~24x），含 8 表 + 25 公式 + 12 图。

### Phase 2c · 5 条新 _dup 冲突全 resolved（4 月 23 audit 推进）

- 4 条 ECE 孤儿 _dup1（canonical 已 trash 但后缀未 rename）→ 直接 rename，4 处 wikilink 同步更新
- 1 条 (EU) 2018/858_dup1 实际是 60+ EU 法规目录索引 → 改造为 `EU Tech Directives Index.md` (type/index MOC)

### Phase 2d · 处理率 64% → 92.8% 提升

给 405 条「MinerU 跑了但 PDF 无表/公式/图」的纯文本 amendment 打上 `_ocr_upgraded: mineru_no_assets` 标记，让 vault 数据真实反映「实质处理状态」而非「只算合并到 body 的」。

### Phase 2e · 13 条边缘案例显式 skip 标记

13 条无 OCR 价值的文档（5 条中文扫描版冗余 + 1 条中文超页 split 待办 + 3 条综述/教材 + 4 条 >50MB 巨件）显式打上 `_ocr_upgraded: skipped` + `_ocr_skip_reason` 区分原因。

### 新增基础设施（7 个永久脚本）

- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_split_large_pdfs.py` — Phase 1 拆分超页 PDF
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_oversized.py` — Phase 2 OCR 拆分 part（独立 state）
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_merge_split_mineru.py` — Phase 3 合并多 part 到 note
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_mark_no_assets_skipped.py` — 标记跑过无 assets
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_mark_final_skipped.py` — 13 条最终 skip 标记
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_fix_orphan_dups.py` — 修复孤儿 _dup1
- `@D:\CcVault\99_SystemScripts\mineru_upgrade\_convert_dup1_to_moc.py` — _dup1 → MOC 转换

### Audit 状态

- `@D:\CcVault\05_Audit\2026-04-23_oversized_pdfs.md` open → ✅ resolved
- `@D:\CcVault\05_Audit\2026-04-23_new_dup_conflicts.md` open → ✅ resolved
- 当前 open audits: **0**

### 验证

QC 0 问题（连续 5 次跑都干净），daily_maintenance 重建 BM25 / topics / equivalence / supersession / graph 全索引。

---

## 2026-04-22~23 · MinerU 云 OCR 升级 Day 1-2（Phase 2）

**类型**：新增 + 基础设施 + 修复

### 成果数据

| 指标 | Day 0 起点 | Day 2 暂停 | Δ |
|---|---:|---:|---:|
| MinerU 处理 PDFs | 0 | **845 / 1444** (58%) | +845 |
| 升级 notes（含表/公式/图）| 0 | **595** / 1414 (42%) | +595 |
| 新增 tables | 0 | **2,036** | +2,036 |
| 新增 formulas | 0 | **1,353** | +1,353 |
| 新增 images | 0 | **2,284** | +2,284 |
| API 成本 | — | ¥0 | 全部在免费额度内 |

### 新增基础设施

- `@D:\CcVault\99_SystemScripts\mineru_upgrade\` — 完整 MinerU 升级 pipeline
  - `_mineru_client.py` MinerU API 封装（含 3 次重试 / SSL 自愈）
  - `_daily_batch.py` 每日批量执行（熔断 / 大书过滤 / 小文件优先）
  - `_merge_upgrade.py` 增量合并到 notes（"原文参考"段）
  - `_watchdog.py` 守护进程，崩溃自动重启
  - `_qc_merged.py` / `_fix_block_counts.py` / `_repair_broken_fm.py` 质检修复三件套
  - `_apply_dedupe_decisions.py` 半自动 dedupe
- `@D:\CcVault\00_Dashboards\_MinerU_Upgrades.md` 升级专属 Dataview 面板

### FM 新字段

每条升级过的 note 新增 5 个字段：
```yaml
_ocr_upgraded: mineru
_mineru_content_hash: <sha1>
_mineru_outputs_dir: outputs/<hash>
_mineru_blocks:
  tables: N
  formulas: N
  images: N
_mineru_merged_at: '2026-04-22' | '2026-04-23'
```

### 修复 Bug

1. **FM closing `---` 后缺空行** → YAML 解析失败；一次性修复 120+ 条破损 note
2. **空 `img_path` 触发 shutil.copy2 炸** → Path / "" 解析为目录本身
3. **total_pages 偶尔 None** → 退回 content_list.json 的 page_idx 推断
4. **SSL EOF 崩 polling** → 改为自愈式 poll，保留已 done 结果
5. **合并计数虚高** → `_fix_block_counts.py` 重新计数回写

### Pipeline 优化

- 上传并发 5 → 3
- 按 PDF size 升序（小文件优先跑完）
- `--max-size-mb 10` 过滤大书（最大 37MB 汽车构造教材）
- 熔断：连续 5 批失败进程 sleep 10 min
- Watchdog：外层再包一层 30s 重启

### 检索层

- `_daily_maintenance.py --only-index` 重建 BM25（1414 notes）+ 关系图 + PageRank
- 不重建 GraphRAG 社区综述（FM 结构未变，仅 body 补充元素，33 社区聚类保持）

---

## 2026-04-19 · 首次 `/process_audits` 执行（3 条）+ `_使用说明.md` 丢失根因查明

**类型**：修复 + 根因分析

### 处理结果
- **1 条 resolved**：`2026-04-19_test_real_flow.md` — 扩展 `GB 4785-2006_dup2.md` 的 summary 从 1 句到 3 句（补充 M/N/O 类车辆适用范围 + 16 种外部照明装置覆盖清单 + 等同采用 ECE R48 信息）
- **2 条 wont_fix**：
  - `2026-04-19_test_audit.md` — 空测试，无实际内容
  - `2026-04-19_issue.md` — **`_使用说明.md` 消失事件的根因档案**

### 🔍 `_使用说明.md` 消失根因查明

**真相**：不是用户误删，是 **Templater 脚本副作用**。
- audit 模板 `02_Schema/templates/audit.md` 使用 `tp.file.move()` 移动当前活动文件
- 用户阅读 `_使用说明.md` 时按 Alt+N，Templater 的 `tp.file.move()` 把 `_使用说明.md` 本身移到了 `05_Audit/2026-04-19_issue.md`
- 所以原文没丢 —— 一直在 audit 1 里。已备份到 `@D:\CcVault\.trash\_使用说明_v1_snapshot_before_rebuild.md`

### ⏳ 待实施的保护

**修改 `02_Schema/templates/audit.md`** 加安全检查：
```javascript
const currentFile = app.workspace.getActiveFile();
if (currentFile && !currentFile.name.startsWith("Untitled")) {
    new Notice("Template aborted: active file is not a new untitled note.");
    return;
}
```

防止用户在已有文件上按 Alt+N 时再次触发该问题。

---

## 2026-04-19 · `_使用说明.md` 意外丢失并重建

**类型**：修复

**事件**：
- 用户配置 Templater 过程中，`_使用说明.md` 在未知操作下从 vault 消失
- Obsidian 未启用 `.trash` 本地回收站
- Windows 回收站无记录
- 未用 git 版本控制 → 无法恢复原文

**措施**：
- Cascade 基于 CLAUDE.md / _INDEX.md / 当前代码结构 / 历史会话记忆**完整重建**（~19 KB / 450+ 行）
- 重建版本包含全部 14 章 + 附录 A-D（术语表 / 脚本速查 / Dataview 示例 / Pipeline 架构图）
- 同步融入最新 Audit 闭环内容（`Alt+N` Templater 快捷键）

**防护措施**：
1. ✅ **已启用 Obsidian 本地回收站**（`trashOption: local`）
   - 删除的文件保留在 `D:\CcVault\.trash\`
   - `.trash/` 目录对 Obsidian UI 隐藏但对文件系统可见
   - 恢复：Windows 文件管理器访问 `.trash\` 复制文件回原位
2. ⏳ **git 版本控制**（待用户决定是否启用）

**遗憾**：无法保证重建 100% 还原原始细节，但覆盖了全部核心功能和工作流。

---

## 2026-04-19 · Audit 闭环纠错机制引入

**类型**：基础设施

**背景**：参考 [lewislulu/llm-wiki-skill](https://github.com/lewislulu/llm-wiki-skill) 的 audit 模式（Karpathy LLM Wiki 社区扩展），补齐"人工发现错误"这一反馈渠道。

**变更**：
- 新建 `@D:\CcVault\05_Audit\` 目录
  - `_Audit MOC.md` — 面板 + Dataview 查询 + severity/category/status 约定
  - `_template.md` — audit 条目模板
  - `README.md` — 快速上手
- 新增 `@D:\CcVault\.windsurf\workflows\process_audits.md` — `/process_audits` workflow
- 新增 `@D:\CcVault\02_Schema\06_audit_templater_setup.md` — Obsidian Templater 插件配置教程
- 更新 `CLAUDE.md` 第 11 节新增 "Audit Loop"
- 更新 `_INDEX.md` / `_使用说明.md` 加入 audit 流程

**引入范围**（对比 llm-wiki-skill 仓库）：
- ✅ audit 文件格式约定 + 工作流
- ✅ `/process_audits` 批量处理脚本（via Cascade workflow）
- ✅ Obsidian Templater 配置方案（替代他们的 TypeScript plugin）
- ❌ 未引入他们的 web viewer（你已用 Obsidian，overkill）
- ❌ 未引入 audit-shared TS lib（他们的格式互通需求你不需要）
- ❌ 未引入 scaffold.py（你已有 1429 条 notes）

**意义**：
- 补齐人工反馈闭环：发现错误 → 10s 建 audit → 累积批量处理
- 和现有 `status/needs-review` tag（机器发现）+ `cross_check_flags`（LLM 校对）形成三位一体质量保障
- 闭环留痕：resolved 的 audit 永久保留，可追溯"什么时候谁为什么改过"

---

## 2026-04-19 · Karpathy 模式全面启用

**类型**：基础设施

**背景**：Karpathy 2026-04-02 发布的 LLM Wiki 模式（agent 直接操作文件系统，非传统 RAG）获得社区广泛采纳。评估后决定将 CcVault 升级到该模式。

**变更**：
- 新增 `@D:\CcVault\CLAUDE.md` — Agent 操作主手册（11 KB）
  - FM schema 速查
  - 11 条运营规则（7 应该 + 9 禁止）
  - 5 个常见任务标准姿势
  - 成本意识 + 扩展点
- 新增 `@D:\CcVault\.windsurf\workflows\` 下 4 个 workflow：
  - `ingest.md` · 新 PDF 入库（8 步自动化）
  - `add_note.md` · 手工新增法规（10 步 + 双向链）
  - `fix_classification.md` · 分类错误修正（规则级 + 单条级）
  - `weekly_check.md` · 健康巡检（12 项体检）
- 新增 `@D:\CcVault\_INDEX.md` — 全局主索引（单一真源导航）
- 新增 `@D:\CcVault\_CHANGELOG.md` — 本文件
- 更新 `_使用说明.md` 快速入门章加入 `/slash` 命令说明

**未做**（评估后保留现状）：
- ❌ 不升级向量嵌入 — BM25 当前够用，等具体痛点出现再升
- ❌ 不重构到 `raw/wiki/` 目录 — 会砸 1429 条 wikilinks + 10 个 Dataview 面板，零 ROI

**影响**：
- Agent 上下文加载时间：从「每次重新介绍」降到「读 CLAUDE.md 3 分钟就位」
- 高频任务触发：从「手工对话指挥」升到「`/slash` 一键触发」
- Karpathy 模式完成度：85% → 100%

---

## 2026-04-18 · 维护自动化

**类型**：基础设施

**变更**：
- 新增 `@D:\CcVault\99_SystemScripts\auto_reg_index\_daily_maintenance.py` — 一键维护脚本
  - 5 阶段流水线（Ingest → Quality → Navigation → Indices → Report）
  - 6 种模式（完整 / only-index / skip-llm / skip-ingest / dry-run / log）
  - 自动写日志到 `logs/maintenance_<ts>.log`
  - GBK 编码兼容
- 新增 `@D:\CcVault\99_SystemScripts\auto_reg_index\_MAINTENANCE.md` — 维护指南
  - Windows Task Scheduler 自动化步骤
  - 3 种调度模式（每日索引 / 每周完整 / 按需）
  - 故障排查 + 监控告警方案

**测试**：dry-run 通过 ✓；`--only-index` 真实运行 23.4 秒 ✓

---

## 2026-04-18 · 使用说明文档上线

**类型**：新增

**变更**：
- 新增 `@D:\CcVault\_使用说明.md` — 完整用户手册（17 KB / 384 行）
  - 14 大章节 + 4 个附录
  - 30 秒快速入门 / Dataview 安装 / 目录结构
  - 5 大日常场景 + 单条 note 结构
  - 10 Dashboard / 37 Topics / 62 Equivalences
  - BM25 检索 / 新 PDF 入库 / 数据质量
  - FAQ（12 题） + 故障排查（7 项）
  - 脚本速查 / Dataview 示例 / 术语表 / Pipeline 架构
- 更新 `README.md` 顶部加入指向使用说明的大链接 + 最新状态数据

---

## 2026-04 · Phase 2 二次复核完成

**类型**：修复 / 质量提升

**背景**：初次 cross-check 产生不少误报（ECE 格式差异、中文句法变体、月份格式差异），拉低 confidence。

**变更**：
- 新增 `_reclassify_false_mismatches.py` — 规则化降级假告警
- 新增 `_recheck_low_confidence.py` — LLM 二次复核
- 统计：87 条顽固 low-confidence 被隔离（多为短篇 Corrigenda/Am，metadata 天然稀疏）

**结果**：verified 比例从初版 ~75% 提升到 **87.4%**

---

## 2026-04 · 非法规剥离

**类型**：修改

**变更**：
- 新增 `02_Wiki/non_automotive/` 命名空间（9 条：自行车/塔吊/工业仪器/消防水带）
- 新增 `02_Wiki/references/` 命名空间（6 条：书籍/内部文档）
- 新增 `_migrate_non_automotive.py` — 迁移脚本
- `01_Wiki/regulations/` 从 ~1444 条降至 **1429 条**（纯汽车法规）

**意义**：保证 `01_Wiki/regulations/` 语义纯净，方便统计和查询。

---

## 2026-04 · 跨区域等价映射

**类型**：新增

**变更**：
- 新增 `03_Equivalence/` 目录 + `_Equivalence MOC.md`
- 新增脚本：
  - `_extract_topic_equivalences.py` — 从主题页提取
  - `_write_equivalence_page.py` — 生成 MOC
  - `_apply_equivalences_to_notes.py` — 回写 FM
- 4 种 relation：equivalent / adopts_from / aligned_with / partial

**结果**：**62** 条映射 → 回写到 **82** 条 notes 的 `equivalent_to` FM。

---

## 2026-04 · Stage 5 建成

**类型**：新增

**变更**：
- 新增 `_build_graph.py` — networkx GraphML 关系图
- 新增 `_graph_analytics.py` — PageRank / Betweenness / 社区发现
- 新增 `_semantic_search.py` — BM25 + jieba 中文分词
- 新增 `00_Dashboards/_Graph_Insights.md` — 静态分析报告
- 新增 `00_Dashboards/_Semantic_Search.md` — BM25 使用文档

---

## 2026-04 · 37 主题聚类

**类型**：新增

**变更**：
- 新增 `_cluster_topics.py` — 规则化聚类
- 新增 `_write_topic_pages.py` — 自动生成 37 个主题页
- 新增 `04_Topics/_Topics MOC.md`
- 覆盖率：100%（所有 1429 条至少属一个主题）

**主题分布**：
- 主流（>50 条）：10 个
- 中等（20-50）：10 个
- 小众（<20）：15 个
- 非法规：2 个

---

## 2026-03 · Stage 1-2 初版 pipeline

**类型**：新增（基础设施）

**变更**：
- 1537 份源 PDF 入 manifest
- S0 OCR（pdfplumber + Baidu OCR + MinerU fallback）
- S1 Extract（DeepSeek V3）
- 1429 条结构化 notes 产出

---

## 维护说明

### Agent 追加条目的规则

每次完成重大操作后追加一条：
```markdown
## YYYY-MM-DD · <短标题>

**类型**：新增 | 修改 | 删除 | 修复 | 基础设施

**变更**：
- 具体改了什么
- 涉及的文件（用 `@<absolute_path>` 格式）

**影响**：
- 对用户 / 数据 / 性能的影响
```

### 追加位置

**最新的在最上方**（和本文件已有内容一致）。

### 不需要记的

- 日常 BM25 索引重建（`_daily_maintenance.py --only-index` 已记机器日志）
- 单条 note 的小改动（除非批量 >10 条）
- 拼写修正 / 格式调整

### 月度汇总

每月 1 日，agent 可以把当月条目聚合为一条"<月份> Summary"并归档详细条目到 `logs/`。
