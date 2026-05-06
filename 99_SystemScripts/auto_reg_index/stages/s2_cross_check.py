"""
Stage 2 · Sonnet 4.6 Cross-check

输入：state=extracted 的关键法规
输出：更新 .staging/{hash}/extracted.md 的字段 confidence + status tag
状态：state → verified / needs_review
成本优化：用 Batch API（50% 折扣），Prompt Caching（system prompt 缓存）

两步流程：
  1. submit  — 把所有 request 打包提交 batch，得到 batch_id，存 logs/batch_ids.jsonl
  2. apply   — 轮询等待 batch 完成，拉结果，应用到 extracted.md 和 manifest
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent.parent))

from manifest import Manifest, FileRecord
from llm import ClaudeClient
from llm.prompts import load_prompt

console = Console()

ROOT = Path(__file__).parent.parent
STAGING_DIR = ROOT / ".staging"
LOGS_DIR = ROOT / "logs"
BATCH_LOG = LOGS_DIR / "batch_ids.jsonl"

# Cross-check 关键法规筛选规则（对应 config.yaml 的 batch_order priority <= 2）
KEY_REGION_PREFIXES = ("cn", "ece")
BATCH_SIZE = 100


def _staging_path(rec: FileRecord) -> Path:
    return STAGING_DIR / rec.content_hash[:2] / rec.content_hash


def _is_key_regulation(rec: FileRecord) -> bool:
    """判断是否进入 cross-check 名单（省 Sonnet token）"""
    if not rec.region:
        return False
    return rec.region in KEY_REGION_PREFIXES


def _build_user_message(rec: FileRecord) -> Optional[str]:
    """构造 cross-check 的 user 消息：A=extracted, B=raw 关键段"""
    stage_dir = _staging_path(rec)
    extracted = stage_dir / "extracted.md"
    raw = stage_dir / "raw.md"
    if not (extracted.exists() and raw.exists()):
        return None

    extracted_text = extracted.read_text(encoding="utf-8")
    raw_text = raw.read_text(encoding="utf-8")

    # 只取 raw 的前 20k 字符作 B（关键段通常在首章，+ 附录太长会爆 token）
    raw_snippet = raw_text[:20000]

    prompt = load_prompt("cross_check")
    return prompt.render_user(
        extracted_yaml_and_body=extracted_text,
        selected_raw_chunks=raw_snippet,
    )


# =============================================================
# Submit
# =============================================================
def submit(
    mf: Manifest,
    *,
    limit: Optional[int] = None,
    dry_run: bool = False,
    include_written: bool = True,
    regions: Optional[list[str]] = None,
) -> list[str]:
    """提交 batch，返回 batch_id 列表"""
    # 默认同时包含 extracted 和 written（整条线都可能需要 cross-check）
    states = ["extracted"]
    if include_written:
        states.append("written")
    candidates: list[FileRecord] = []
    for st in states:
        candidates.extend(mf.files_in_state(st))
    # region 过滤
    key_regions = tuple(regions) if regions else KEY_REGION_PREFIXES
    candidates = [rec for rec in candidates if rec.region in key_regions and not rec.duplicate_of]
    if limit:
        candidates = candidates[:limit]

    if not candidates:
        console.print("[yellow]No eligible files for cross-check[/yellow]")
        return []

    console.print(f"[cyan]Cross-check submit:[/cyan] {len(candidates)} files")

    prompt = load_prompt("cross_check")

    # 准备请求
    requests = []
    for rec in candidates:
        user_msg = _build_user_message(rec)
        if user_msg is None:
            continue
        requests.append({
            "custom_id": rec.content_hash,
            "system": prompt.system,
            "user": user_msg,
            "max_tokens": 4096,
            "temperature": 0.0,
        })

    if dry_run:
        # 粗略估算 token（中文字符 ~0.5 tok/char, 英文 ~0.25 tok/char，混合取 ~0.4）
        total_input_chars = sum(len(r["system"]) + len(r["user"]) for r in requests)
        total_input = int(total_input_chars * 0.4)
        total_output_est = len(requests) * 1000  # 平均 1000 token 输出
        # Sonnet: $3/M in, $15/M out
        cost_sync = total_input * 3.0 / 1_000_000 + total_output_est * 15.0 / 1_000_000
        cost_batch = cost_sync * 0.5
        # cache 优化：大部分 system prompt 复用，估算 80% 命中率
        cached = int(total_input * 0.8)
        fresh = total_input - cached
        cost_cached = (fresh * 3.0 + cached * 0.30) / 1_000_000 + total_output_est * 15.0 / 1_000_000
        console.print(f"[yellow]DRY-RUN[/yellow]")
        console.print(f"  requests      = {len(requests)}")
        console.print(f"  est input tok = {total_input:,}")
        console.print(f"  est output tok= {total_output_est:,}")
        console.print(f"  est cost (sync, no cache)  ≈ ${cost_sync:.2f}")
        console.print(f"  est cost (batch, no cache) ≈ ${cost_batch:.2f}")
        console.print(f"  est cost (sync + cache 80%) ≈ ${cost_cached:.2f}")
        return []

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]ERROR[/red] ANTHROPIC_API_KEY not set")
        return []

    client = ClaudeClient(
        api_key=api_key,
        base_url=os.getenv("ANTHROPIC_BASE_URL"),
    )
    model = os.getenv("CLAUDE_SONNET_MODEL", "claude-sonnet-4-6")

    # 切分批次（Anthropic batch API 每批最多 100k 请求，但我们每批 100 便于监控）
    batch_ids = []
    for i in range(0, len(requests), BATCH_SIZE):
        chunk = requests[i:i + BATCH_SIZE]
        batch_id = client.submit_batch(chunk, model=model)
        batch_ids.append(batch_id)
        console.print(f"  batch {i//BATCH_SIZE + 1}: {batch_id} ({len(chunk)} req)")

        # 记录到 log
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        with BATCH_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "stage": "s2_cross_check",
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
def apply(mf: Manifest, *, wait: bool = True) -> dict:
    """拉取 batch 结果，应用到 staging"""
    if not BATCH_LOG.exists():
        console.print("[yellow]No submitted batches found[/yellow]")
        return {}

    # 收集所有未 finished 的 s2 batches
    pending_batches = []
    with BATCH_LOG.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if rec.get("stage") == "s2_cross_check" and rec.get("status") == "submitted":
                pending_batches.append(rec)

    if not pending_batches:
        console.print("[yellow]No pending cross-check batches[/yellow]")
        return {}

    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = ClaudeClient(api_key=api_key, base_url=os.getenv("ANTHROPIC_BASE_URL"))

    stats = {"verified": 0, "needs_review": 0, "failed": 0}
    for b in pending_batches:
        batch_id = b["batch_id"]
        console.print(f"[cyan]Fetching batch {batch_id}...[/cyan]")

        if wait:
            results = client.wait_for_batch(batch_id, poll_interval_seconds=60)
        else:
            results = client.fetch_batch(batch_id)
            if results is None:
                console.print(f"  [yellow]Still running, skip for now[/yellow]")
                continue

        # 应用每个结果
        for resp in results:
            custom_id = (resp.raw_response or {}).get("custom_id")
            if not custom_id:
                continue
            rec = mf.records.get(custom_id)
            if not rec:
                continue

            # log cost
            client.log_cost(
                stage="s2_cross_check",
                response=resp,
                reg_id=rec.reg_id,
            )

            # 解析 Sonnet 返回的 YAML
            outcome = _parse_cross_check_output(resp.content)
            if not outcome:
                rec.advance_to("needs_review", note="cross-check output unparseable")
                stats["needs_review"] += 1
                continue

            # 把 cross-check 结果应用到 extracted.md
            _apply_outcome_to_extracted(rec, outcome)

            if outcome.get("recommend_review"):
                rec.advance_to("needs_review", note="cross-check recommended review")
                stats["needs_review"] += 1
            else:
                rec.advance_to("verified", note=f"conf={outcome.get('overall_confidence')}")
                stats["verified"] += 1

    mf.save()
    console.print(f"[green]Apply done:[/green] {stats}")
    return stats


def _parse_cross_check_output(text: str) -> Optional[dict]:
    """从 Sonnet 回复中提取 YAML"""
    import re
    text = text.strip()
    text = re.sub(r"^```(?:yaml)?\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    parts = text.split("---")
    yaml_str = parts[1] if len(parts) >= 2 else text
    try:
        return yaml.safe_load(yaml_str)
    except yaml.YAMLError:
        return None


def _apply_outcome_to_extracted(rec: FileRecord, outcome: dict):
    """把 cross-check 结果合并到 extracted.md 的 frontmatter"""
    stage_dir = _staging_path(rec)
    extracted = stage_dir / "extracted.md"
    if not extracted.exists():
        return

    content = extracted.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
    _, yaml_str, body = parts
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        return

    # 合并 cross-check 结果
    fm["verified_by"] = "sonnet-4.6"
    fm["cross_check_overall_confidence"] = outcome.get("overall_confidence")
    fm["cross_check_results"] = outcome.get("cross_check_result", [])

    # 按 cross-check 结果调整 _conf
    for r in outcome.get("cross_check_result", []):
        field = r.get("field")
        status = r.get("status")
        if not field:
            continue
        if status == "mismatch":
            fm[f"{field}_conf"] = "low"
            fm[f"{field}_cross_check_note"] = r.get("note", "")
        elif status == "unsure":
            # 降一档
            current = fm.get(f"{field}_conf", "high")
            if current == "high":
                fm[f"{field}_conf"] = "medium"

    # 更新 tags
    tags = fm.get("tags", []) or []
    if outcome.get("recommend_review"):
        if "status/needs-review" not in tags:
            tags.append("status/needs-review")
        if "status/draft" in tags:
            tags.remove("status/draft")
    else:
        if "status/verified" not in tags:
            tags.append("status/verified")
        if "status/draft" in tags:
            tags.remove("status/draft")
    fm["tags"] = tags

    extracted.write_text(
        "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body,
        encoding="utf-8",
    )


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
        mf = Manifest.load_or_create()
        apply(mf, wait=not no_wait)

    cli()
