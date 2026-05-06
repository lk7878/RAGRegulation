"""
Stage 3 · Opus 4.7 跨区等效关系判定（Batch API）

输入：state=verified 或 needs_review 的法规，frontmatter.equivalent_to 有候选关系
产出：精化 equivalent_to 字段：添加 relation / version / confidence

两步流程（同 s2）：
  submit → apply
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
WIKI_ROOT = Path(os.getenv("WIKI_OUTPUT_DIR", "D:/CcVault/01_Wiki"))
LOGS_DIR = ROOT / "logs"
BATCH_LOG = LOGS_DIR / "batch_ids.jsonl"

BATCH_SIZE = 50   # Opus 贵，每批小一点便于监控


def _staging_path(rec: FileRecord) -> Path:
    return STAGING_DIR / rec.content_hash[:2] / rec.content_hash


# =============================================================
# Build equivalence pair candidates
# =============================================================
def _collect_candidate_pairs(mf: Manifest) -> list[dict]:
    """
    扫描所有已抽取的 note，从 frontmatter.equivalent_to 提取候选对：
      { a_rec, a_frontmatter, b_ref_text }
    b 是字符串引用（如 "ECE R48"），由 Opus 后续推断精确版本。
    """
    pairs = []
    seen = set()  # 去重：同一对 (a_reg_id, b_ref) 只判定一次
    eligible = [
        rec for rec in mf.records.values()
        if rec.state in {"verified", "needs_review", "written"}
        and not rec.duplicate_of
    ]

    for rec in eligible:
        extracted = _staging_path(rec) / "extracted.md"
        if not extracted.exists():
            continue
        try:
            content = extracted.read_text(encoding="utf-8")
            parts = content.split("---", 2)
            if len(parts) < 3:
                continue
            fm = yaml.safe_load(parts[1]) or {}
        except Exception:
            continue

        reg_id = fm.get("reg_id", "")
        equivs = fm.get("equivalent_to") or []
        if not equivs:
            continue

        for e in equivs:
            if not isinstance(e, dict):
                continue
            b_ref = e.get("ref")
            if not b_ref:
                continue
            key = (reg_id, b_ref)
            if key in seen:
                continue
            seen.add(key)

            pairs.append({
                "a_rec_hash": rec.content_hash,
                "a_reg_id": reg_id,
                "a_frontmatter": parts[1],
                "a_body_snippet": parts[2][:5000],
                "b_ref": b_ref,
                "b_version_hint": e.get("version"),
                "current_relation": e.get("relation"),
            })

    return pairs


# =============================================================
# Submit
# =============================================================
def submit(mf: Manifest, *, limit: Optional[int] = None, dry_run: bool = False) -> list[str]:
    pairs = _collect_candidate_pairs(mf)
    if limit:
        pairs = pairs[:limit]
    if not pairs:
        console.print("[yellow]No equivalence candidate pairs[/yellow]")
        return []

    console.print(f"[cyan]Equivalence submit:[/cyan] {len(pairs)} pairs")

    prompt = load_prompt("equivalence")

    # 找每对中 B 的 frontmatter（若 B 也在我们库里）
    requests = []
    for i, pair in enumerate(pairs):
        # 查 B 是否在 manifest 中
        b_rec = _find_regulation_by_ref(mf, pair["b_ref"])
        if b_rec:
            b_stage = _staging_path(b_rec) / "extracted.md"
            if b_stage.exists():
                bc = b_stage.read_text(encoding="utf-8").split("---", 2)
                b_frontmatter = bc[1] if len(bc) >= 2 else ""
                b_body = bc[2][:5000] if len(bc) >= 3 else ""
            else:
                b_frontmatter = f"(not in our library yet)\nref: {pair['b_ref']}"
                b_body = "(not available)"
        else:
            # B 不在库里，只给 Opus 一点 hint 让它靠 world knowledge
            b_frontmatter = f"(not in our library)\nref: {pair['b_ref']}"
            b_body = "(not available; use your world knowledge)"

        user = prompt.render_user(
            a_reg_id=pair["a_reg_id"],
            a_frontmatter=pair["a_frontmatter"],
            a_key_clauses=pair["a_body_snippet"],
            b_reg_id=pair["b_ref"],
            b_frontmatter=b_frontmatter,
            b_key_clauses=b_body,
        )
        requests.append({
            "custom_id": f"{pair['a_rec_hash']}::{i}::{pair['b_ref'].replace(' ', '_')}",
            "system": prompt.system,
            "user": user,
            "max_tokens": 2048,
            "temperature": 0.0,
        })

    if dry_run:
        total_input = sum(len(r["system"]) + len(r["user"]) for r in requests) // 3
        total_output_est = len(requests) * 800
        # Opus batch: $5/M in * 0.5, $25/M out * 0.5
        cost = (total_input * 5.0 / 1_000_000 + total_output_est * 25.0 / 1_000_000) * 0.5
        console.print(f"[yellow]DRY-RUN[/yellow]")
        console.print(f"  requests = {len(requests)}")
        console.print(f"  est input = {total_input:,}")
        console.print(f"  est output = {total_output_est:,}")
        console.print(f"  est cost (batch) ≈ ${cost:.2f}")
        return []

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]ERROR[/red] ANTHROPIC_API_KEY not set")
        return []

    client = ClaudeClient(api_key=api_key, base_url=os.getenv("ANTHROPIC_BASE_URL"))
    model = os.getenv("CLAUDE_OPUS_MODEL", "claude-opus-4-7")

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
                "stage": "s3_equivalence",
                "batch_id": batch_id,
                "request_count": len(chunk),
                "custom_ids": [r["custom_id"] for r in chunk],
                "status": "submitted",
            }, ensure_ascii=False) + "\n")

    console.print(f"[green]Submitted {len(batch_ids)} batches[/green]")
    return batch_ids


def _find_regulation_by_ref(mf: Manifest, ref: str) -> Optional[FileRecord]:
    """根据 ref 字符串找对应的 FileRecord"""
    normalized = ref.lower().replace(" ", "")
    for rec in mf.records.values():
        if rec.reg_id and rec.reg_id.lower().replace(" ", "").startswith(normalized):
            return rec
    return None


# =============================================================
# Apply
# =============================================================
def apply(mf: Manifest, *, wait: bool = True) -> dict:
    if not BATCH_LOG.exists():
        console.print("[yellow]No submitted batches[/yellow]")
        return {}

    pending = []
    with BATCH_LOG.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if rec.get("stage") == "s3_equivalence" and rec.get("status") == "submitted":
                pending.append(rec)

    if not pending:
        console.print("[yellow]No pending equivalence batches[/yellow]")
        return {}

    api_key = os.getenv("ANTHROPIC_API_KEY")
    client = ClaudeClient(api_key=api_key, base_url=os.getenv("ANTHROPIC_BASE_URL"))

    stats = {"applied": 0, "failed": 0}
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
            custom_id = (resp.raw_response or {}).get("custom_id") or ""
            if not custom_id:
                continue
            a_rec_hash = custom_id.split("::")[0]
            rec = mf.records.get(a_rec_hash)
            if not rec:
                continue

            client.log_cost(
                stage="s3_equivalence",
                response=resp,
                reg_id=rec.reg_id,
            )

            outcome = _parse_equivalence_output(resp.content)
            if outcome:
                _apply_equivalence(rec, outcome, custom_id)
                stats["applied"] += 1
            else:
                stats["failed"] += 1

    mf.save()
    console.print(f"[green]Equivalence apply done:[/green] {stats}")
    return stats


def _parse_equivalence_output(text: str) -> Optional[dict]:
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


def _apply_equivalence(rec: FileRecord, outcome: dict, custom_id: str):
    """把 relation 结果写回 extracted.md 的 equivalent_to 字段"""
    b_ref = custom_id.split("::")[-1].replace("_", " ")

    stage = _staging_path(rec) / "extracted.md"
    if not stage.exists():
        return

    content = stage.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
    _, yaml_str, body = parts
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        return

    equivs = fm.get("equivalent_to") or []
    for e in equivs:
        if isinstance(e, dict) and e.get("ref", "").replace(" ", "_").lower() == b_ref.replace(" ", "_").lower():
            e["relation"] = outcome.get("relation", e.get("relation"))
            e["version"] = outcome.get("b_version", e.get("version"))
            e["confidence"] = outcome.get("confidence", "medium")
            e["reasoning"] = outcome.get("reasoning", "")
            e["key_differences"] = outcome.get("key_differences", [])
            break
    fm["equivalent_to"] = equivs

    stage.write_text(
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
