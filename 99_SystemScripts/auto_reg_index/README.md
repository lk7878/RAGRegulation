# CcVault Pipeline (`auto_reg_index`)

法规知识库的自动索引 pipeline。从 `00_Raw/标准库` 下的 1537 份 PDF/Word 文件，经 6 阶段处理，产出 `01_Wiki/` 下的结构化 Obsidian notes。

## 快速开始

### 1. 安装环境

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. 配置 API Keys

```powershell
copy .env.template .env
notepad .env
# 填入 ANTHROPIC_API_KEY 和 DEEPSEEK_API_KEY
```

### 3. 跑样板（Phase 1 · Day 2）

```powershell
python ingest.py sample --reg "GB 4785"
```

对 GB 4785 的 3 个版本 + 2 个修改单做全流程，约 15 分钟，消耗 < $1 + ¥5。产出：
- `.staging/GB 4785/` 下的中间产物（OCR markdown、抽取 JSON）
- `01_Wiki/regulations/cn/GB 4785 外部照明安装规定.md` 等 6 份 notes

你手动 review 这 6 份，确认模板、prompt、字段都合理。

### 4. 全量批处理（Phase 2 · Day 3）

```powershell
# 先 dry-run 看要调什么、预估多少成本
python ingest.py run --dry-run

# 确认后真跑
python ingest.py run --all
```

一天内跑完 1537 份。分步：

- 阶段 0（OCR）：本地 pdfplumber 并发（30 分钟） + 百度云异步（1 小时） + MinerU 挂机（几小时）
- 阶段 1（DeepSeek 抽取）：并发 10 线程，2-4 小时
- 阶段 2（Sonnet cross-check）：batch API 提交，12 小时返回
- 阶段 3-5（Opus 跨区 + topic + GraphRAG）：batch API，12 小时返回

总消耗：约 **$80 Claude + ¥320 DeepSeek + ¥60 OCR**。

### 5. Obsidian 集成（Phase 3 · Day 5）

```powershell
python ingest.py smart-composer-setup
```

输出 Smart Composer 插件配置 JSON，你贴到 Obsidian 设置里，即可在 Obsidian 中直接和 Opus 聊法规库。

---

## 目录结构

```
auto_reg_index/
├── README.md              # 你现在读的这份
├── requirements.txt       # Python 依赖
├── .env.template          # API key 模板
├── .env                   # 你真实的 keys（gitignored）
├── config.yaml            # pipeline 行为配置
├── ingest.py              # 主入口
├── manifest.py            # 文件清单（hash + 状态机）管理
├── llm/
│   ├── base.py            # 统一 LLM 客户端接口
│   ├── deepseek_client.py # DeepSeek V3
│   ├── claude_client.py   # Sonnet/Opus via batch API
│   └── prompts.py         # Prompt 加载器
├── ocr/
│   ├── router.py          # OCR 分层路由
│   ├── pdfplumber_extractor.py
│   ├── baidu_ocr.py
│   └── mineru_extractor.py
├── stages/
│   ├── s0_ocr.py
│   ├── s1_extract.py
│   ├── s2_cross_check.py
│   ├── s3_equivalence.py
│   ├── s4_topic_summary.py
│   └── s5_graphrag.py
├── writers/
│   └── obsidian_writer.py # 把结果写进 01_Wiki/
├── prompts/               # Prompt 模板（.md）
│   ├── extract.md
│   ├── cross_check.md
│   ├── equivalence.md
│   ├── topic_summary.md
│   └── graphrag_community.md
├── logs/                  # 运行日志（gitignored）
├── cache/                 # LLM 响应缓存（gitignored）
└── .staging/              # 中间产物（gitignored）
```

---

## CLI 命令

```
python ingest.py --help
```

### 主要命令

| 命令 | 说明 |
|---|---|
| `sample --reg <REG_ID>` | 对某法规做全流程，用于 Phase 1 样板验证 |
| `ocr-only` | 只跑 OCR 层，不调 LLM |
| `run --stage <0\|1\|2\|3\|4\|5>` | 只跑某一阶段 |
| `run --all` | 跑完整流水线 |
| `run --dry-run` | 不调真实 API，只 log 计划 |
| `resume` | 从上次中断处续跑（根据 manifest 状态） |
| `status` | 打印当前 manifest 状态：多少 pending/done/failed |
| `cost-report` | 汇总 cost_log.jsonl 生成报告 |
| `retry-failed` | 重试所有 failed 文件 |

---

## Manifest 状态机

每份源文件在 `manifest.json` 中的生命周期：

```
pending
  ↓  ocr 完成
ocr_done
  ↓  DeepSeek 抽取完成
extracted
  ↓  Sonnet cross-check 完成
verified  or  needs_review
  ↓  写入 01_Wiki
written
  ↓  （Phase 2-3）
equivalence_linked  → topic_summarized  → graph_included
```

状态机保证**断点续传**：任何阶段失败，下次 `resume` 从断点开始，不重跑已完成的。

---

## 成本监控

每次 API 调用都记录在 `logs/cost_log.jsonl`：

```json
{"ts": "2026-04-17T15:30:00Z", "stage": "s1_extract", "provider": "deepseek",
 "reg_id": "GB 4785-2019", "input_tokens": 45210, "output_tokens": 12400,
 "cost_usd": 0.028, "cached_tokens": 8500}
```

用 `python ingest.py cost-report` 随时查看：

```
累计成本：
  deepseek    $45.32
  sonnet-4.6  $24.18
  opus-4.7    $48.55
总计：$118.05 / 预算 $180
```

超预算 `config.yaml > cost_monitoring > daily_cap_usd` 自动停机。

---

## 故障排查

| 症状 | 原因 | 处理 |
|---|---|---|
| 某份 PDF 一直 pending | OCR 超时 | 检查 `logs/ocr_errors.log`；手动提交到百度云网页版 |
| Sonnet batch 12h 还没回 | batch API 排队 | 查 Anthropic console batch status |
| `confidence: low` 占比 > 30% | Prompt 不够明确 | 调 `prompts/extract.md` 后 `retry-failed` |
| 写入 01_Wiki 时文件冲突 | 同名重复 | 查 `manifest.json` 的 `duplicate_candidates` 字段 |

---

## 开发约定

- 所有 LLM 调用必须走 `llm/` 下的统一客户端，不要裸调 `openai` / `anthropic`
- 所有文件路径用 `pathlib.Path`，不用字符串拼接
- 所有阶段可独立测试：`python -m stages.s1_extract --input <path>`
- 禁止在 pipeline 中修改 `00_Raw/` 下的任何文件

