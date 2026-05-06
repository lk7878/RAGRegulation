# CcVault ReAct Agent

把现有脚本（BM25 / GraphRAG / FM 加载 / git log）封装成 LangChain `@tool`，给 LLM 装上**自主检索 + 统计 + 审计**能力。

这层**解决了 RAG 回答不了统计题/全量扫描题**的根本限制。用户可以用自然语言问任何问题，agent 自主决定调哪些工具。

---

## 🚀 30 秒快速上手

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index

# 单次问答
.\.venv\Scripts\python.exe _agent_chat.py "vault 里有多少条中国法规"

# REPL 连续对话模式
.\.venv\Scripts\python.exe _agent_chat.py

# 显示 tool call 轨迹（调试/好奇用）
.\.venv\Scripts\python.exe _agent_chat.py -v "国六排放相关的社区是哪个"

# 切到 Claude Sonnet（如果有 key）
.\.venv\Scripts\python.exe _agent_chat.py --provider claude "..."
```

---

## 🧰 12 个工具清单

### 检索类（3）

| Tool | 参数 | 用途 |
|---|---|---|
| `search_regulations_bm25` | query, region?, topic?, limit | 按关键词 BM25 点查 |
| `search_communities_graphrag` | query, topk_communities, topk_members | GraphRAG 层级检索（领域全景） |
| `read_regulation` | reg_id, body_chars | 按 reg_id 读完整 FM + body 前 N 字 |

### 统计类（4）

| Tool | 参数 | 用途 |
|---|---|---|
| `describe_vault` | (无) | 全局概览（总数、按区/按主题/按 status 分布） |
| `count_regulations` | region?, topic?, status?, year_from?, year_to?, confidence? | 按条件计数 |
| `stats_by_field` | field, top_n | 按字段分组（region/topic/status/year/confidence/source_type）|
| `list_recent_changes` | days, limit | 最近 N 天改动（git log + mtime fallback） |

### 结构类（4）

| Tool | 参数 | 用途 |
|---|---|---|
| `get_equivalence` | reg_id | 查某法规的跨区等价映射 |
| `get_supersession_chain` | reg_id | 查版本演化链（supersedes/superseded_by） |
| `get_community` | community_id | 查 GraphRAG 社区详情 + 成员 |
| `list_by_topic` | topic, limit | 列某 topic 下所有 notes |

### 审计类（1）

| Tool | 参数 | 用途 |
|---|---|---|
| `list_needs_review` | limit, confidence | 列出低置信度或 needs_review 的 notes |

---

## 🧪 真实测试样例

已经跑通的三个代表性问题：

### 1. 简单统计（2 次 tool 调用，18 秒）

> **Q**: vault 里有多少条中国法规？其中 brakes 主题有多少条？

```
tool trace:
  [1] describe_vault()
  [2] count_regulations(region='cn', topic='brakes')
```

> **A**: 中国法规 448 条，其中 brakes 主题 21 条（GB 12676 / GB 21670 / GB 13594 等）

### 2. 社区 + 统计组合（4 次 tool 调用，~30 秒）

> **Q**: 国六排放相关的社区是哪个？这个社区里有多少条中国法规？

```
tool trace:
  [1] search_communities_graphrag(query='国六排放', topk_communities=5)
  [2] get_community(community_id=3)
  [3] get_community(community_id=4)
  [4] count_regulations(region='cn')
```

> **A**: 两个社区 —— #3"排放限值/燃料消耗"（10 条 cn）+ #4"车辆分类/制动/尺寸"（含 GB 18352.6-2016 等），总 28 条

### 3. 版本链追溯（10 次 tool 调用，53 秒）

> **Q**: GB 4785 有哪些历史版本？最新版是哪一版？

```
tool trace:
  [1] get_supersession_chain(reg_id='GB 4785')           # 无精确匹配
  [2] search_regulations_bm25(query='GB 4785', ...)       # 找到所有版本
  [3-6] get_supersession_chain(reg_id='GB 4785-1998'/-2007/-2019)
  [7-9] read_regulation(...)                              # 确认发布日期
  [10] search_regulations_bm25(query='GB 4785-1984')      # 追溯最早版本
```

> **A**: 完整版本链 1984 → 1998 → 2007 → 2019，最新版 **GB 4785-2019**

---

## 🏗️ 架构

```
_agent_chat.py                   # 最外层入口
└── agent/
    ├── __init__.py
    ├── agent.py                 # build_agent() + run_once() + system_prompt
    ├── cli.py                   # argparse + REPL + rich 渲染
    ├── tools/
    │   ├── __init__.py          # ALL_TOOLS 汇总
    │   ├── _shared.py           # FM 加载、reg_id 匹配、截断、索引加载
    │   ├── search.py            # 3 个检索 tool
    │   ├── stats.py             # 4 个统计 tool
    │   ├── structure.py         # 4 个结构 tool
    │   └── audit.py             # 1 个审计 tool
    └── README.md                # 本文件
```

### 关键设计决策

1. **所有 tool 返回 string，且限制 ≤4000 字符** — 避免 LLM context 爆炸
2. **所有 tool 共用 `_shared.load_all_notes()`** — 一次扫 vault，LRU cache 住
3. **`topic` 从 `.stage4/cluster_assignment.json` 读** — 而非 FM 里的 `topic` 字段（后者大部分为空，真相在聚类结果里）
4. **System prompt 明确规范** — 永远先调 tool 再回答；引用具体 reg_id；中文回答
5. **DeepSeek V3 做默认 provider** — 成本低（$0.27/$1.10 per M）、中文好、已有 key

---

## 💰 成本参考

基于实测 DeepSeek V3：

| 问题复杂度 | tool 调用数 | 耗时 | tokens 估计 | 成本 |
|---|---:|---:|---:|---:|
| 简单统计 | 2 | 18s | ~2K in / 0.3K out | ≈ $0.001 |
| 中等（社区组合） | 4 | 30s | ~5K in / 0.8K out | ≈ $0.0025 |
| 复杂（版本链追溯） | 10 | 53s | ~15K in / 2K out | ≈ $0.007 |

100 次日常查询平均 ≈ **$0.2**（¥1.5）。

---

## 🔄 扩展新工具

想加新 tool，三步：

1. 在 `agent/tools/<category>.py` 写函数：

```python
from langchain.tools import tool

@tool
def my_new_tool(param1: str, param2: int = 10) -> str:
    """描述这个 tool 干什么（LLM 会读这里的 docstring 决定何时调用）。

    Args:
        param1: 第一个参数
        param2: 第二个参数，默认 10
    """
    # 实现...
    return "tool 输出的字符串（≤4000 字符）"
```

2. 在同文件末尾把它加进该 category 的 TOOLS 列表：

```python
MY_CATEGORY_TOOLS = [..., my_new_tool]
```

3. 如果是新 category，在 `tools/__init__.py` 加一行 `from .xxx import XXX_TOOLS` 并加到 `ALL_TOOLS`。

无需改 `agent.py` 或 `cli.py`。

---

## 🐛 Troubleshooting

| 问题 | 排查 |
|---|---|
| `BM25 index not found` | 先跑 `python _semantic_search.py --rebuild` 建索引 |
| `Community index not available` | 检查 `04_Topics/communities/` 是否有 `community_*.md` |
| `DEEPSEEK_API_KEY 未设置` | 在 `auto_reg_index/.env` 配 `DEEPSEEK_API_KEY` |
| LLM 不调 tool 直接瞎答 | 问题本身太闲聊（如"你好"），或问题表述不触发 tool 关键词 |
| Tool 调用失败 `[not found]` | reg_id 匹配逻辑优先精确，失败降级去空格小写匹配。用 `search_regulations_bm25` 先找正确 reg_id |

---

## 🎯 与其他工具的关系

| 场景 | 推荐工具 |
|---|---|
| 纯 QA（知道要什么） | `_semantic_search.py "query"` |
| 领域全景 | `_graphrag_search.py "query"` |
| **需要统计/全量/多步推理** | **`_agent_chat.py` ← 本层** |
| 批量维护/重建 | `_daily_maintenance.py` / `stages/s5_graphrag.py` |
| FM 精确查询 | Obsidian Dataview 面板 |

Agent 不是替代其他工具，而是**上层协调者**：它内部就是通过调用这些工具完成任务。

---

## 🌐 Obsidian Copilot 接入（HTTP OpenAI 兼容服务）

把 agent 包一层 FastAPI，暴露 OpenAI 兼容的 `/v1/chat/completions`，Obsidian Copilot 直接连。

### 1. 启动服务

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _agent_server.py

# 局域网其他设备访问
.\.venv\Scripts\python.exe _agent_server.py --host 0.0.0.0 --port 7777
```

输出类似：

```
╭─ CcVault Agent Server
│  URL:       http://127.0.0.1:7777
│  /v1/models                → 列模型
│  /v1/chat/completions      → OpenAI 兼容聊天接口
│  /health                   → 健康检查
│  /docs                     → Swagger UI
╰─ Obsidian Copilot 配置: base_url=http://127.0.0.1:7777/v1, model=ccvault-agent
INFO:     Uvicorn running on http://127.0.0.1:7777
```

### 2. Obsidian Copilot 配置

**Settings → Copilot → Model Settings → Add Custom Model**：

| 字段 | 值 |
|---|---|
| **Model Name** | `ccvault-agent` |
| **Provider** | `OpenAI Format`（OpenAI 兼容即可） |
| **Base URL** | `http://127.0.0.1:7777/v1` |
| **API Key** | `dummy`（服务端不校验） |
| **Model Capabilities** | Tool use ✓ （如果有这个选项） |

然后 **Verify** → 应该返回 ✓。

想加 Claude 版本（切底层模型），再加一条：
- Model Name: `ccvault-agent-claude`
- 其他不变

### 3. 使用

Copilot 聊天面板 → 底部模型下拉 → 选 `ccvault-agent` → 直接问：

```
> vault 里有多少条 ECE 法规？
→ 959 条（agent 自己调 describe_vault 得到）

> GB 4785 有哪些历史版本？
→ 1984 → 1998 → 2007 → 2019，最新 GB 4785-2019
```

### 4. 支持的参数

请求体兼容 OpenAI，额外支持：

```json
{
  "model": "ccvault-agent",          // 或 "ccvault-agent-claude"
  "messages": [{"role": "user", "content": "..."}],
  "stream": true,                    // 伪流式（分块推送）
  "temperature": 0,
  "provider": "deepseek"             // 可选，覆盖 model 名字的推断
}
```

### 5. 性能说明

- **非流式**（`stream=false`）：一次返回完整答案，简单 18s / 复杂 53s
- **伪流式**（`stream=true`）：agent 推理完后按每 20 字一块 SSE 推送，用户感官是**渐进出现**，但后台仍是一次性推理
- Agent 实例缓存：首次构建约 1s，之后请求复用

### 6. 关闭服务

Ctrl-C 或关闭窗口即可。服务无副作用。

---

## 🔌 MCP Server 接入（Cascade / Claude Desktop / Cursor）

MCP (Model Context Protocol) 是 Anthropic 标准，任何支持 MCP 的 LLM 客户端都能直接调用 CcVault 的 12 个工具。

### 1. 测试启动

```powershell
cd D:\CcVault\99_SystemScripts\auto_reg_index
.\.venv\Scripts\python.exe _agent_mcp.py
# 会看到 stderr 输出 "注册 12 个 tools"，stdin/stdout 保持打开等待 MCP 协议消息
# Ctrl-C 退出
```

### 2. 配置到 Cascade（Windsurf）

编辑 `~/.codeium/windsurf/mcp_config.json`（Windows 上是 `%USERPROFILE%\.codeium\windsurf\mcp_config.json`）：

```json
{
  "mcpServers": {
    "ccvault": {
      "command": "D:/CcVault/99_SystemScripts/auto_reg_index/.venv/Scripts/python.exe",
      "args": ["D:/CcVault/99_SystemScripts/auto_reg_index/_agent_mcp.py"]
    }
  }
}
```

重启 Cascade → 在对话中可以直接让 Cascade 调用这 12 个工具，不再需要用 `read_file` 一个个读 vault。

### 3. 配置到 Claude Desktop

编辑 `%APPDATA%/Claude/claude_desktop_config.json`（macOS 上是 `~/Library/Application Support/Claude/`）：

同上的 JSON 结构。重启 Claude Desktop。

### 4. 配置到 Cursor

Settings → MCP → Add new → 粘贴同样的 JSON。

### 5. 验证

客户端启动后，发一条消息试试：

> 用 ccvault 的工具查一下 vault 里有多少条中国法规

客户端会展示"调用 ccvault.describe_vault()"的工具调用，然后给出真实答案。

### 6. MCP vs HTTP 的区别

| 对比 | HTTP (OpenAI 兼容) | MCP |
|---|---|---|
| 协议 | REST + SSE | JSON-RPC over stdio |
| 客户端 | Obsidian Copilot / 任何 OpenAI SDK | Cascade / Claude Desktop / Cursor 等 |
| 是否常驻 | 手动启动 `_agent_server.py` | 客户端自动 spawn 子进程 |
| 并发 | 多客户端可共享 | 每个客户端独立进程 |
| 适用场景 | Obsidian 日常查询 | IDE 里让 AI 帮你维护 vault |

两套可**同时启用**，互不干扰。

