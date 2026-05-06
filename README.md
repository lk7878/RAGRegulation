# CcVault

全球汽车法规知识库（Global Automotive Regulation Knowledge Base）

**🧭 [全局主索引 → _INDEX.md](_INDEX.md)** — 导航地图（从这里开始）
**📖 [完整使用说明 → _使用说明.md](_使用说明.md)** — 用户手册
**🤖 [Agent 操作手册 → CLAUDE.md](CLAUDE.md)** — 给 AI 用

**定位**：个人工具箱 + 论文脚手架 + 职业竞争力 + 持续学习，四用途一体的 Obsidian 结构化知识库。

## 当前状态（2026-04）

- **1429** 条汽车法规 notes（100% 主题覆盖）
- **15** 条非法规已迁到 `02_Wiki/` 独立命名空间
- **62** 条跨区域等价映射
- **37** 个技术主题索引
- **10** 个 Dataview 活数据面板
- **87.4% verified**（Phase 2 复核后）
- 总成本 **¥102 / $14.33**

## 快速入口

| 需求 | 打开 |
|---|---|
| 完整使用说明 | [[_使用说明]] |
| 某技术域全貌 | [[04_Topics/_Topics MOC]] |
| GB ↔ ECE 对应 | [[03_Equivalence/_Equivalence MOC]] |
| 活数据面板 | [[00_Dashboards/_Dashboards MOC]] |

## 目录结构

```
CcVault/
├── 00_Raw/               # 源文件（1537 份 PDF/Word/Excel，只读不动）
├── 01_Wiki/              # 结构化 wiki notes
│   ├── regulations/      # 按地区分的法规主条目 + 版本页 + 修改单
│   │   ├── cn/   ece/   eu/   us/   jp/   kr/
│   │   ├── asean/   gcc/   ru-eaeu/   in/   br/   au/   za/
│   ├── test-methods/     # 试验方法节点（如 MDB 侧碰、HIC 计算）
│   ├── dummies/          # 假人节点（Hybrid III / Q3 / WorldSID / THOR）
│   ├── injury-metrics/   # 损伤指标节点（HIC15 / 胸压 / NIC / BrIC）
│   ├── vehicle-classes/  # 车型分类节点（M1 / M3 / N1 / L / O）
│   ├── topics/           # 主题综述页（正面碰撞 / 外部照明 / 制动 …）
│   ├── _index.md         # vault 首页 / 入口
│   └── _review_queue.md  # 低置信度待审队列
├── 02_Schema/            # 设计文档 + Schema + 模板
│   ├── DESIGN.md         # 完整设计文档（读这份）
│   ├── 01_compile_instructions.md
│   ├── 02_taxonomy.md
│   ├── 03_frontmatter_schema.md
│   ├── 04_self_check_rules.md
│   └── templates/        # Templater 模板（8 种节点类型）
└── 99_SystemScripts/
    └── auto_reg_index/   # Python pipeline
        ├── ingest.py     # 主入口
        ├── ocr/          # OCR 分层（pdfplumber / 百度云 / MinerU）
        ├── llm/          # DeepSeek / Sonnet / Opus 客户端
        ├── prompts/      # Prompt 模板
        └── .env.template # API key 模板
```

## 模型分工

| 环节             | 模型                                                 |
| -------------- | -------------------------------------------------- |
| OCR            | pdfplumber（电子 PDF）+ 百度云 OCR（扫描件）+ MinerU CPU（复杂表格） |
| 批量结构化抽取        | **DeepSeek V3**                                    |
| Cross-check 审校 | **Claude Sonnet 4.6** via batch API                |
| 跨区等效关系判定       | **Claude Opus 4.7** via batch API                  |
| Topic 综述       | **Claude Sonnet 4.6** via batch API                |
| GraphRAG 社区摘要  | **Claude Opus 4.7** via batch API                  |
| 日常问答           | **Opus 4.7 / Sonnet 4.6**（Smart Composer 触发）       |

## 使用

1. 读 `02_Schema/DESIGN.md` 了解完整设计
2. 在 `99_SystemScripts/auto_reg_index/.env` 填入 API keys（参见 `.env.template`）
3. 运行 `python 99_SystemScripts/auto_reg_index/ingest.py --phase 1 --sample-reg "GB 4785"` 跑样板
4. 样板通过后运行 `python ingest.py --phase 2 --batch-all` 跑全量

详细使用说明见 `99_SystemScripts/auto_reg_index/README.md`。
