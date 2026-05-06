---
type: namespace_readme
namespace: literature
created: 2026-04-22
tags:
- type/namespace
- zettelkasten
---

# Literature · 学术文献 Zettelkasten

> 这是 CcVault 的**文献分支**，跟 `regulations/` 平级。
> 设计用于把 50+ 篇学术文献（车辆工程 + 生物损伤力学 + 人体建模等）
> 以 Zettelkasten 方式沉淀为可跨链接的知识网络。

## 为什么单独做？

法规（规范性） ≠ 文献（研究性）：
- 法规: 强制标准、条款清单、版本演化、跨区对标 → FM 由 `reg_id/region/status` 主导
- 文献: 研究成果、作者观点、方法实验、论证主张 → FM 由 `authors/year/methodology` 主导

两者在**主题上重合**（例如 ECE R94 的碰撞测试 vs. 某论文对该测试工况的评价），所以我们用 Obsidian wikilink **双向互引**，而不是做两个孤立库。

## 目录结构

```
literature/
├── README.md              (本文件)
├── papers/                ← 文献笔记 LN (Literature Note)
│                           · 每篇 PDF 一条
│                           · body = MinerU 原文解析 + LLM 提取的 abstract
│                           · 纯资料层，不做深度加工
│
├── concepts/              ← 原子笔记 PN (Permanent Note)
│                           · 每个可引用的"主张/方法/概念"一条
│                           · body = 你自己提炼的思路（Zettelkasten 精髓）
│                           · sources 字段链回 papers/ 里的来源文献
│                           · 最终构成知识网络的骨架
│
├── mocs/                  ← 结构笔记 (Map of Content)
│                           · 主题地图。等 concepts/ 某主题有 ≥ 10 条时再写
│                           · 例如 MOC_HBM_evolution / MOC_thorax_injury
│                           · body = 索引 + 评论 + 你的洞察
│
└── _mineru_assets/        ← MinerU 抽取的图表（共享资产）
```

## 三层工作流

### Phase A · 文献入库（可自动化）
1. 把 PDF 扔进 `D:\Literature_Inbox\`
2. 跑 `_mineru_batch_lit.py`（复用 CcVault 的 MinerU 基础设施）
3. 跑 `_extract_lit_fm.py`：DeepSeek 从 MinerU `full.md` 抽 authors/year/DOI/abstract/keywords
4. 自动生成 `papers/<paper_id>.md` with FM 完整 + body 含全文 + 图表
5. 自动扫正文，发现 `ECE R\d+` / `FMVSS \d+` / `GB\s*\d+` 建 wikilink 回 regulations/

### Phase B · 原子提炼（必须人在其中）
LLM **不能**代替你做这步。阅读 LN 后，决定哪些"主张"/"方法"/"数据"值得独立成条：

```yaml
# concepts/HIC_threshold_1000.md
type: concept
concept_id: HIC_threshold_1000
category: injury_criterion
claim: "HIC 值 ≥ 1000 对应 AIS≥3 头部损伤概率 ~16%"
sources:
  - "[[Yang2023_HBM_thorax]]"
  - "[[Kleiven2007_brain_injury]]"
related_concepts:
  - "[[HIC_criterion]]"
  - "[[thorax_deflection]]"
related_regs:
  - "[[ECE R94]]"
  - "[[FMVSS 208]]"
status: established
```

每篇 LN 可能派生 2-10 条 PN。

### Phase C · MOC 涌现（按需）
当一个主题积累足够多 PN 后，写一条 MOC 把它们串起来：

```markdown
# MOC 人体模型在碰撞中的演化

## 时间线
- 1970s [[Hybrid III 假人]] 物理测试时代
- 1990s [[THUMS 第一代]] FE 模型兴起
- 2000s [[GHBMC]] 细节化
- 2010s+ [[参数化 HBM]] 群体变化

## 争议
- [[HBM_validation_challenge]] 验证方法论
- [[HBM_personalization]] 个性化差异

## 主要贡献者
- UMTRI / Wayne State
- ZF / Lab Research Center
```

## FM Schema 权威定义

见 `@D:\CcVault\02_Schema\literature_schema.md`

## 与 regulations/ 的整合

- **正向**：文献 note 的 `related_regs` 字段含 `[[ECE R94]]` 等 wikilink
- **反向**：将来可跑 `_back_fill_literature_refs.py`，在相关法规 note 末尾追加：
  ```markdown
  ## 相关文献
  - [[Yang2023_HBM_thorax]] — 评价 R94 斜 25° 碰撞工况下的胸部损伤预测
  - [[Kleiven2007_brain_injury]] — 挑战 R94 默认假人的脑损伤灵敏度
  ```

## 当前状态

- ✅ 基础设施：目录结构、Schema 文档、模板
- ⏸ Phase A 脚本：待用户触发（需要 PDF 路径）
- ⏸ 50 篇文献：未入库

## 触发方式

1. 用户把 PDF 放入某路径（例如 `D:\Literature_Inbox\`）
2. 用户说：**"开工文献入库，路径是 X"**
3. Cascade 按 Phase A 脚本处理
