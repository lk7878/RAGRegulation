"""
Stage 4 · Topic 综述（Sonnet 4.6 Batch API）

输入：扫描 01_Wiki/regulations/ 下所有 .md，按 frontmatter.topics 分组
输出：01_Wiki/topics/<topic>.md

流程：submit → apply
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent.parent))

from manifest import Manifest
from llm import ClaudeClient
from llm.prompts import load_prompt

console = Console()

ROOT = Path(__file__).parent.parent
WIKI_ROOT = Path(os.getenv("WIKI_OUTPUT_DIR", "D:/CcVault/01_Wiki"))
LOGS_DIR = ROOT / "logs"
BATCH_LOG = LOGS_DIR / "batch_ids.jsonl"

BATCH_SIZE = 30
MIN_REGULATIONS_PER_TOPIC = 3     # 少于 3 个关联法规的 topic 不做综述
MAX_INPUT_CHARS_PER_TOPIC = 80_000  # 限制输入大小，防止超 token


# =============================================================
# Collect topic groups
# =============================================================
def _read_frontmatter(md_path: Path) -> Optional[dict]:
    try:
        content = md_path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None
        fm = yaml.safe_load(parts[1]) or {}
        fm["_body_snippet"] = parts[2][:2000]
        return fm
    except Exception:
        return None


def _collect_topic_groups() -> dict[str, list[dict]]:
    """
    扫描 regulations/ 下所有 .md，按 topic 分组
    返回：{topic_id: [frontmatter, ...]}
    只考虑 type/regulation 和 type/version 节点
    """
    reg_dir = WIKI_ROOT / "regulations"
    if not reg_dir.exists():
        return {}

    groups: dict[str, list[dict]] = defaultdict(list)
    for md in reg_dir.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        fm = _read_frontmatter(md)
        if not fm:
            continue
        node_type = fm.get("type", "")
        if node_type not in {"type/regulation", "type/version"}:
            continue
        topics = fm.get("topics", []) or []
        for t in topics:
            groups[t].append(fm)
    return dict(groups)


def _format_group_for_prompt(topic_id: str, members: list[dict]) -> str:
    """把一组 frontmatter 格式化成 user template 里的 aggregated_frontmatters_and_summaries"""
    # 按 region 排序
    members = sorted(members, key=lambda m: (m.get("region", "zzz"), m.get("reg_id", "")))

    parts = []
    char_budget = MAX_INPUT_CHARS_PER_TOPIC
    for fm in members:
        block = f"""
### {fm.get('reg_id', 'UNKNOWN')} ({fm.get('region', '?')})

- title: {fm.get('title', '')}
- status: {fm.get('status', '')}
- implementation: {fm.get('implementation_date_new_vehicle', '')}
- vehicle_classes: {fm.get('vehicle_classes', [])}
- equivalent_to: {fm.get('equivalent_to', [])}

正文摘要：
{fm.get('_body_snippet', '')[:1500]}
---
"""
        if len(block) > char_budget:
            parts.append(f"\n(further {len(members) - len(parts)} entries truncated due to token budget)\n")
            break
        parts.append(block)
        char_budget -= len(block)

    return "\n".join(parts)


# =============================================================
# Submit
# =============================================================
def submit(mf: Manifest, *, limit: Optional[int] = None, dry_run: bool = False) -> list[str]:
    groups = _collect_topic_groups()

    # 过滤：数量 >= MIN_REGULATIONS_PER_TOPIC
    filtered = {
        t: mems for t, mems in groups.items()
        if len(mems) >= MIN_REGULATIONS_PER_TOPIC
    }
    if limit:
        filtered = dict(list(filtered.items())[:limit])

    if not filtered:
        console.print(f"[yellow]No topics have >= {MIN_REGULATIONS_PER_TOPIC} regulations[/yellow]")
        return []

    console.print(f"[cyan]Topic summary submit:[/cyan] {len(filtered)} topics")
    for t, mems in sorted(filtered.items(), key=lambda x: -len(x[1]))[:10]:
        console.print(f"  {t}: {len(mems)} regulations")

    prompt = load_prompt("topic_summary")

    requests = []
    for topic_id, members in filtered.items():
        aggregated = _format_group_for_prompt(topic_id, members)
        user = prompt.render_user(
            topic_id=topic_id,
            count=len(members),
            aggregated_frontmatters_and_summaries=aggregated,
        )
        requests.append({
            "custom_id": topic_id.replace("/", "_"),
            "system": prompt.system.replace("{topic_id}", topic_id),
            "user": user,
            "max_tokens": 4096,
            "temperature": 0.3,
        })

    if dry_run:
        total_input = sum(len(r["system"]) + len(r["user"]) for r in requests) // 3
        total_output_est = len(requests) * 2000
        cost = (total_input * 3.0 / 1_000_000 + total_output_est * 15.0 / 1_000_000) * 0.5
        console.print(f"[yellow]DRY-RUN[/yellow]")
        console.print(f"  requests = {len(requests)}")
        console.print(f"  est cost (Sonnet batch) ≈ ${cost:.2f}")
        return []

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]ERROR[/red] ANTHROPIC_API_KEY not set")
        return []

    client = ClaudeClient(api_key=api_key, base_url=os.getenv("ANTHROPIC_BASE_URL"))
    model = os.getenv("CLAUDE_SONNET_MODEL", "claude-sonnet-4-6")

    batch_ids = []
    for i in range(0, len(requests), BATCH_SIZE):
        chunk = requests[i:i + BATCH_SIZE]
        batch_id = client.submit_batch(chunk, model=model)
        batch_ids.append(batch_id)
        console.print(f"  batch {i//BATCH_SIZE + 1}: {batch_id} ({len(chunk)} req)")

        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        with BATCH_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "stage": "s4_topic_summary",
                "batch_id": batch_id,
                "request_count": len(chunk),
                "custom_ids": [r["custom_id"] for r in chunk],
                "status": "submitted",
            }, ensure_ascii=False) + "\n")

    console.print(f"[green]Submitted {len(batch_ids)} batches[/green]")
    return batch_ids


# =============================================================
# Apply
# =============================================================
def apply(*, wait: bool = True) -> dict:
    if not BATCH_LOG.exists():
        console.print("[yellow]No submitted batches[/yellow]")
        return {}

    pending = []
    with BATCH_LOG.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if rec.get("stage") == "s4_topic_summary" and rec.get("status") == "submitted":
                pending.append(rec)

    if not pending:
        console.print("[yellow]No pending topic batches[/yellow]")
        return {}

    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = ClaudeClient(api_key=api_key, base_url=os.getenv("ANTHROPIC_BASE_URL"))

    topics_dir = WIKI_ROOT / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)

    stats = {"written": 0, "failed": 0}
    for b in pending:
        batch_id = b["batch_id"]
        console.print(f"[cyan]Fetching {batch_id}...[/cyan]")
        if wait:
            results = client.wait_for_batch(batch_id, poll_interval_seconds=60)
        else:
            results = client.fetch_batch(batch_id)
            if results is None:
                console.print("  [yellow]Still running, skip[/yellow]")
                continue

        for resp in results:
            custom_id = (resp.raw_response or {}).get("custom_id", "")
            client.log_cost(
                stage="s4_topic_summary",
                response=resp,
                reg_id=custom_id,
            )

            if not resp.content.strip():
                stats["failed"] += 1
                continue

            # 生成的内容本身就是 frontmatter + body（by prompt design）
            # 从 custom_id 还原 topic_id 作为文件名
            topic_id = custom_id.replace("_", "/")
            # 生成文件名：用 topic 的最后一段做 stem
            stem = topic_id.split("/")[-1]
            target = topics_dir / f"{_safe_filename(stem)}.md"

            # 写入（不覆盖 manually-edited）
            if target.exists() and "status/manually-edited" in target.read_text(encoding="utf-8"):
                conflict = target.with_suffix(".conflict.md")
                conflict.write_text(resp.content, encoding="utf-8")
                console.print(f"  [yellow]conflict[/yellow] {conflict.name}")
            else:
                target.write_text(resp.content, encoding="utf-8")
                stats["written"] += 1

    console.print(f"[green]Topic summary done:[/green] {stats}")
    return stats


def _safe_filename(name: str) -> str:
    import re
    return re.sub(r'[\\/:*?"<>|]+', "", name).strip()


if __name__ == "__main__":
    import click

    @click.group()
    def cli():
        pass

    @cli.command(name="submit")
    @click.option("--limit", type=int)
    @click.option("--dry-run", is_flag=True)
    def _submit(limit, dry_run):
        mf = Manifest.load_or_create()
        submit(mf, limit=limit, dry_run=dry_run)

    @cli.command(name="apply")
    @click.option("--no-wait", is_flag=True)
    def _apply(no_wait):
        apply(wait=not no_wait)

    cli()
