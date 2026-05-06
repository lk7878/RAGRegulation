"""
Stage 5c — GraphRAG · 社区摘要生成

读 `.stage5/communities.json` + `.stage5/graph.json`，对每个 ready 社区调 Claude Sonnet
生成深度综述，写入 `04_Topics/communities/community_<id>.md`。

用法：
  python _graphrag_summarize.py                       # 处理全部 ready 社区
  python _graphrag_summarize.py --community 0 5 10    # 只处理指定 id
  python _graphrag_summarize.py --limit 3             # 只处理前 3 个（试水）
  python _graphrag_summarize.py --dry-run             # 只打印 prompt 不调用
  python _graphrag_summarize.py --force               # 覆盖已存在的 community_*.md
  python _graphrag_summarize.py --model "[K]claude-sonnet-4-6"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from llm.claude_client import ClaudeClient
from llm.deepseek_client import DeepSeekClient

# override=True：强制用 .env 的值覆盖已存在的系统环境变量
# （系统可能有历史遗留的 ANTHROPIC_BASE_URL 指向其他中转服务）
load_dotenv(override=True)

console = Console()

ROOT = Path(__file__).parent
STAGE5 = ROOT / ".stage5"
VAULT = Path(r"D:\CcVault")
OUT_DIR = VAULT / "04_Topics" / "communities"

# Provider 默认 deepseek（2026-04 中转 claude 账号池不稳定）
PROVIDER_DEFAULTS = {
    "deepseek": {
        "model_env": "DEEPSEEK_MODEL",
        "model_fallback": "deepseek-chat",
        "key_env": "DEEPSEEK_API_KEY",
        "base_env": "DEEPSEEK_BASE_URL",
        "generated_by": "deepseek-chat",
    },
    "claude": {
        "model_env": "CLAUDE_SONNET_MODEL",
        "model_fallback": "claude-sonnet-4-6",
        "key_env": "ANTHROPIC_API_KEY",
        "base_env": "ANTHROPIC_BASE_URL",
        "generated_by": "claude-sonnet",
    },
}

# ----------------------------------------------------------------------------
# Prompt
# ----------------------------------------------------------------------------

SYSTEM_PROMPT = """\
你是汽车法规的跨文档推理专家。给定一个实体社区（一组紧密关联的法规/版本/修正案），
写一份深度综述。

要求：
1. 找出社区的"核心节点"（引用最多的 top-3，已在输入中提供）
2. 描述社区内部关系结构（版本链、采标关系、引用链）
3. 对比同类不同实例的差异（如同是制动法规但 EU 与 CN 限值不同）
4. 指出潜在矛盾或未解决议题
5. 给社区打一个 3-5 个中文关键词的 canonical label（用 " / " 连接）

**必须严格输出 YAML frontmatter + markdown body**，格式如下（不要任何额外说明）：

---
community_id: <输入里给的数字>
label: <3-5 个中文关键词 用 / 连接>
core_nodes:
  - "[[<reg_id>]]"
  - "[[<reg_id>]]"
  - "[[<reg_id>]]"
member_count: <输入给的数字>
edge_count: <输入给的数字>
top_region: <输入给的>
top_topic: <输入给的>
generated_at: <ISO 8601 UTC 时间>
generated_by: claude-sonnet
confidence: high
---

# 社区综述：<label>

## 1. 成员总览
<按区域或类型分类列出所有成员，每条 1 行，格式：`- [[reg_id]] — title`>

## 2. 内部关系结构
<用文字或 mermaid 图描述版本链、采标、引用关系>

## 3. 同类对比
<核心对比：同一指标/试验方法在不同法规中的差异。如无明显对比则说明原因>

## 4. 关键议题与潜在矛盾
<至少 **3 条**具体洞察。禁止"当前社区内未发现明显矛盾"类套话。>
<每条必须基于 input 数据给出**具体**观察，格式：**<主题>**：<具体现象> → <影响/风险>>
<合格话题（选其中 ≥3 类组合）：>
- **限值差异**：同主题不同法规的数字限值/测试条件差异（如国六 vs 欧VI PN 限值）
- **时间延迟**：等效采标 GB 与源 ECE 修订版的年差
- **覆盖缺口**：某 ECE 主题在 GB 体系里无对应标准
- **定义冲突**：术语/分类在不同法规中的不一致
- **版本并存**：同一 reg 多版本同时处于 active 的过渡期风险
- **范围差异**：法规 scope 覆盖车型/场景的异同
- **引用滞后**：A 法规引用的 B 已废止或有更新版
- **语言/翻译**：中英文版本在关键术语上的歧义

## 5. 版本演进时间线
<按时间顺序列出社区内重要节点，格式：`- <year>: <reg_id> — <发布/生效/废止/修订 事件>`>
<至少 4 条。若 input 未提供日期则用 reg_id 年份推断>

## 6. 相关查询示例
<3 条用户可能对该社区提的问题，每条 1 行>

规则：
- 语言：中文；全文 1000-1800 字
- 只引用 input 给出的 reg_id，绝不编造
- "关键议题"一节绝不允许写"未发现矛盾"之类占位语；如内容真的一致，改用"演进脉络观察"列具体现象
- 如成员信息过少无法综述，在相应段落短说明并降低 confidence=medium
"""


USER_TEMPLATE = """\
社区 ID：{community_id}
成员数：{member_count}
内部边数：{edge_count}
主导区域：{top_region}
主导主题：{top_topic}
核心节点（度数最高）：{core_nodes}

社区成员（frontmatter 精简）：
<<<
{members}
>>>

社区内部边（关系图 JSON）：
<<<
{edges}
>>>
"""


# ----------------------------------------------------------------------------
# 数据加载
# ----------------------------------------------------------------------------

def load_graph_data() -> tuple[dict, dict]:
    """返回 (communities_data, graph_data)。"""
    cpath = STAGE5 / "communities.json"
    gpath = STAGE5 / "graph.json"
    if not cpath.exists():
        raise FileNotFoundError(f"{cpath} 不存在。先跑 python _graphrag_communities.py")
    if not gpath.exists():
        raise FileNotFoundError(f"{gpath} 不存在。先跑 python _build_graph.py")
    c = json.loads(cpath.read_text(encoding="utf-8"))
    g = json.loads(gpath.read_text(encoding="utf-8"))
    return c, g


def load_note_fm(reg_id: str, graph_data: dict) -> dict:
    """从 graph.json 的 node 数据读 FM（已含精简字段）。"""
    node = graph_data["nodes"].get(reg_id, {})
    return {
        "reg_id": reg_id,
        "title": node.get("title", "")[:120],
        "region": node.get("region", "unknown"),
        "type": node.get("type", "unknown"),
        "status": node.get("status", "unknown"),
        "date": node.get("date", ""),
        "topic": node.get("topic", ""),
    }


def load_note_body_summary(reg_id: str, graph_data: dict) -> str:
    """从 vault 原 note 的正文提取 ## 摘要 段。"""
    node = graph_data["nodes"].get(reg_id, {})
    path = node.get("path", "")
    if not path or not Path(path).exists():
        return ""
    try:
        txt = Path(path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    # 去除 FM
    if txt.startswith("---"):
        end = txt.find("\n---", 4)
        if end >= 0:
            txt = txt[end + 4:]
    # 抓 "## 摘要" 到下一个 ##
    m = re.search(r"##\s*摘要\s*\n([\s\S]*?)(?=\n##\s|\Z)", txt)
    if m:
        s = m.group(1).strip()
        # 限制 400 字
        return s[:400]
    return ""


def build_edges_subset(members: set[str], graph_data: dict) -> list[dict]:
    """提取社区内部边。"""
    out = []
    for e in graph_data["edges"]:
        if e["src"] in members and e["dst"] in members:
            out.append({
                "src": e["src"],
                "dst": e["dst"],
                "rel": e.get("rel", ""),
            })
    return out


# ----------------------------------------------------------------------------
# Prompt 构造
# ----------------------------------------------------------------------------

def build_user_prompt(community: dict, graph_data: dict) -> str:
    members_set = set(community["members"])
    member_rows = []
    for reg_id in community["members"]:
        fm = load_note_fm(reg_id, graph_data)
        summary = load_note_body_summary(reg_id, graph_data)
        row = f"- reg_id: {fm['reg_id']}\n"
        row += f"  region: {fm['region']}, type: {fm['type']}, status: {fm['status']}\n"
        row += f"  title: {fm['title']}\n"
        row += f"  date: {fm['date']}, topic: {fm['topic']}\n"
        if summary:
            row += f"  摘要: {summary}\n"
        member_rows.append(row)

    edges = build_edges_subset(members_set, graph_data)
    edges_json = json.dumps(edges, ensure_ascii=False)

    return USER_TEMPLATE.format(
        community_id=community["id"],
        member_count=community["size"],
        edge_count=community["internal_edges"],
        top_region=community.get("top_region", ""),
        top_topic=community.get("top_topic", ""),
        core_nodes=", ".join(community.get("core_nodes", [])),
        members="\n".join(member_rows),
        edges=edges_json,
    )


# ----------------------------------------------------------------------------
# 输出写入
# ----------------------------------------------------------------------------

FM_SPLIT_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$")


def parse_claude_output(content: str) -> tuple[dict, str]:
    """把 Claude 返回的 `---YAML---\n# ...` 分离成 (fm_dict, body)。"""
    content = content.strip()
    # Claude 有时加 ```markdown``` 包裹，去掉
    if content.startswith("```"):
        content = re.sub(r"^```[a-zA-Z]*\s*\n", "", content)
        content = re.sub(r"\n```\s*$", "", content)
    m = FM_SPLIT_RE.match(content)
    if not m:
        return {}, content
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    body = m.group(2).strip()
    return fm, body


def write_community_md(community: dict, fm: dict, body: str, out_dir: Path, generated_by: str = "claude-sonnet") -> Path:
    """合并 fm + body 写到 04_Topics/communities/community_<id>.md。"""
    # 确保关键字段齐全
    fm["community_id"] = community["id"]
    fm["member_count"] = community["size"]
    fm["edge_count"] = community["internal_edges"]
    if "top_region" not in fm:
        fm["top_region"] = community.get("top_region", "")
    if "top_topic" not in fm:
        fm["top_topic"] = community.get("top_topic", "")
    # generated_at / generated_by 强制覆盖（LLM 可能幻觉填错时间或 provider 名）
    fm["generated_at"] = datetime.now(timezone.utc).isoformat()
    fm["generated_by"] = generated_by
    if "confidence" not in fm:
        fm["confidence"] = "high"

    # Obsidian tags
    fm["tags"] = sorted(set(fm.get("tags", []) + [
        "type/graphrag_community",
        f"topic/{community.get('top_topic', 'uncategorized') or 'uncategorized'}",
    ]))

    fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    out = out_dir / f"community_{community['id']:03d}.md"
    out_dir.mkdir(parents=True, exist_ok=True)
    out.write_text(f"---\n{fm_yaml}\n---\n\n{body}\n", encoding="utf-8")
    return out


# ----------------------------------------------------------------------------
# 主流程
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--community", type=int, nargs="*",
                    help="只处理指定 community id 列表")
    ap.add_argument("--limit", type=int, default=None,
                    help="只处理前 N 个 ready 社区（试水）")
    ap.add_argument("--force", action="store_true",
                    help="覆盖已存在的 community_*.md")
    ap.add_argument("--dry-run", action="store_true",
                    help="只打 prompt 不调用 LLM")
    ap.add_argument("--provider", choices=["deepseek", "claude"], default="deepseek",
                    help="LLM provider（默认 deepseek，中文综述能力与 Sonnet 相当、成本更低、中转无关）")
    ap.add_argument("--model", default=None,
                    help="LLM 模型；不给则用 provider 默认 env")
    ap.add_argument("--sleep", type=float, default=0.0,
                    help="每次调用间 sleep 秒数（避免 rate limit，并发时通常用 0）")
    ap.add_argument("--concurrency", type=int, default=5,
                    help="并发线程数（DeepSeek 官方一般可起 10，保守给 5）")
    args = ap.parse_args()

    # 解析 provider 默认
    pconf = PROVIDER_DEFAULTS[args.provider]
    model = args.model or os.getenv(pconf["model_env"], pconf["model_fallback"])

    comms, graph = load_graph_data()
    ready = [c for c in comms["communities"] if c["status"] == "ready"]

    # 过滤
    if args.community:
        ids = set(args.community)
        ready = [c for c in ready if c["id"] in ids]
    if args.limit:
        ready = ready[: args.limit]

    if not ready:
        console.print("[yellow]没有需要处理的 ready 社区[/yellow]")
        return 0

    console.print(f"[bold cyan]准备处理 {len(ready)} 个社区[/bold cyan]")
    console.print(f"  Provider: {args.provider}")
    console.print(f"  Model: {model}")
    console.print(f"  Output: {OUT_DIR}")
    console.print(f"  Force overwrite: {args.force}")
    console.print()

    if args.dry_run:
        c = ready[0]
        user = build_user_prompt(c, graph)
        console.print(f"[yellow]DRY-RUN — Community #{c['id']} sample prompt (provider={args.provider}, model={model}):[/yellow]\n")
        console.print(user[:2000] + ("..." if len(user) > 2000 else ""))
        return 0

    # 初始化 client
    api_key = os.getenv(pconf["key_env"])
    base_url = os.getenv(pconf["base_env"]) or None
    if not api_key:
        console.print(f"[red]{pconf['key_env']} 未设置[/red]")
        return 1

    if args.provider == "claude":
        client = ClaudeClient(api_key=api_key, base_url=base_url)
    else:
        client = DeepSeekClient(api_key=api_key, base_url=base_url)

    total_cost = 0.0
    total_in = 0
    total_out = 0
    n_ok = 0
    n_skip = 0
    n_fail = 0

    stats_lock = threading.Lock()

    def process_one(c: dict) -> tuple[str, dict]:
        """worker：处理一个社区。返回 (status, info)。"""
        out_file = OUT_DIR / f"community_{c['id']:03d}.md"
        if out_file.exists() and not args.force:
            return "skip", {"id": c["id"], "reason": "exists"}

        user = build_user_prompt(c, graph)
        try:
            resp = client.chat(
                system=SYSTEM_PROMPT,
                user=user,
                model=model,
                max_tokens=4096,
                temperature=0.2,
                enable_cache=True,
            )
        except Exception as e:
            return "fail", {"id": c["id"], "err": str(e)[:160]}

        fm, body = parse_claude_output(resp.content)
        if not body:
            return "fail", {"id": c["id"], "err": "empty body"}

        write_community_md(c, fm, body, OUT_DIR, generated_by=pconf["generated_by"])
        if args.provider == "claude":
            cost = client.calculate_cost_usd(
                resp.input_tokens, resp.output_tokens,
                cached_tokens=resp.cached_tokens, model=model, is_batch=False,
            )
        else:
            cost = client.calculate_cost_usd(
                resp.input_tokens, resp.output_tokens,
                cached_tokens=resp.cached_tokens, model=model,
            )
        if args.sleep > 0:
            time.sleep(args.sleep)
        return "ok", {
            "id": c["id"], "size": c["size"],
            "label": fm.get("label", "?")[:40],
            "in": resp.input_tokens, "out": resp.output_tokens,
            "cost": cost,
        }

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        console=console,
    ) as prog:
        task = prog.add_task("summarize", total=len(ready))

        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futs = {ex.submit(process_one, c): c for c in ready}
            for fut in as_completed(futs):
                status, info = fut.result()
                with stats_lock:
                    if status == "ok":
                        n_ok += 1
                        total_in += info["in"]
                        total_out += info["out"]
                        total_cost += info["cost"]
                        console.print(
                            f"  [green]ok[/green] #{info['id']:3d} ({info['size']:2d} nodes) "
                            f"{info['label']:42s} "
                            f"in={info['in']:5d} out={info['out']:4d} ${info['cost']:.4f}"
                        )
                    elif status == "skip":
                        n_skip += 1
                        console.print(f"  [dim]skip[/dim] #{info['id']} ({info['reason']})")
                    else:
                        n_fail += 1
                        console.print(f"  [red]fail[/red] #{info['id']}: {info['err']}")
                    prog.advance(task)

    console.print()
    console.print(f"[bold green]=== Summary ==={'': <20}[/bold green]")
    console.print(f"  ok:     {n_ok}")
    console.print(f"  skip:   {n_skip}")
    console.print(f"  fail:   {n_fail}")
    console.print(f"  tokens: in={total_in:,} out={total_out:,}")
    console.print(f"  cost:   ${total_cost:.4f}")
    console.print(f"  dir:    {OUT_DIR}")

    return 0 if n_fail == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
