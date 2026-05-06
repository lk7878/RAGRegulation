"""
Stage 2 sync-mode cross-check（batch API 不可用时用）。

- 并发调 Claude Sonnet 核对 extracted FM vs raw OCR
- Prompt caching 80% 命中率降成本
- 结果直接写回 wiki note（追加 _conf/cross_check_* 字段 + tag）
- 支持 --limit, --cost-cap-usd, --workers, --regions, --only-needs-review

用法：
  python _run_cross_check.py --limit 10 --cost-cap-usd 1   # 冒烟
  python _run_cross_check.py --only-status-unknown         # 只验 13 条高风险
  python _run_cross_check.py --regions cn --cost-cap-usd 15
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env", override=True)
sys.path.insert(0, str(ROOT))

from llm import ClaudeClient, DeepSeekClient  # noqa: E402
from llm.prompts import load_prompt  # noqa: E402

console = Console()
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STAGING = ROOT / ".staging"
MF_PATH = ROOT / "manifest.json"

# 价格表（$/M tokens）
PRICING = {
    "claude": {"in": 3.0, "out": 15.0, "cache_read": 0.30, "cache_write_mult": 1.25},
    "deepseek": {"in": 0.27, "out": 1.10, "cache_read": 0.07, "cache_write_mult": 1.0},
}


def load_manifest_map() -> dict[str, str]:
    """build hash → source_pdf path map."""
    data = json.loads(MF_PATH.read_text(encoding="utf-8"))
    return {
        h: str(r.get("path") or "").replace("\\", "/").lstrip("/")
        for h, r in data["records"].items()
    }


def find_staging_raw(source_pdf: str, manifest_map: dict) -> tuple[str, Path] | tuple[None, None]:
    """source_pdf → (hash, raw.md path). None if not found."""
    norm = str(source_pdf).replace("\\", "/").lstrip("/")
    for h, p in manifest_map.items():
        if p == norm or p.endswith(norm) or norm.endswith(p):
            raw = STAGING / h[:2] / h / "raw.md"
            if raw.exists():
                return h, raw
    return None, None


def gather_candidates(
    *,
    regions: Optional[list[str]],
    only_status_unknown: bool,
    only_missing_title: bool,
    manifest_map: dict,
) -> list[tuple[Path, dict, str, str]]:
    """Return list of (note_path, fm, extracted_text, raw_snippet)."""
    candidates = []
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        fm = yaml.safe_load(txt[4:end]) or {}

        # Region filter
        if regions and fm.get("region") not in regions:
            continue

        # 跳过已 cross-checked
        if fm.get("verified_by"):
            continue

        # Risk filters
        if only_status_unknown:
            st = str(fm.get("status") or "").lower()
            if st not in ("unknown", "none", "null", ""):
                continue
        if only_missing_title and fm.get("title"):
            continue

        src = fm.get("source_pdf") or fm.get("source_file")
        if not src:
            continue
        h, raw_md = find_staging_raw(str(src), manifest_map)
        if not raw_md:
            continue
        raw_text = raw_md.read_text(encoding="utf-8", errors="replace")
        raw_snippet = raw_text[:18000]

        # 构造 A = extracted（截取 FM + 前 3k body）
        body = txt[end + 4 :]
        extracted_text = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n" + body[:3000]

        candidates.append((p, fm, extracted_text, raw_snippet))
    return candidates


def _parse_yaml_block(text: str) -> dict:
    """从 Claude 回复提取 YAML。容错：LLM 常写单行嵌套 / 带冒号的裸值。"""
    s = text.strip()
    s = re.sub(r"^```(?:yaml)?\s*", "", s)
    s = re.sub(r"\s*```\s*$", "", s)
    # 取首尾 --- 之间；否则整体
    parts = s.split("---")
    if len(parts) >= 3:
        yaml_str = parts[1]
    elif len(parts) == 2:
        yaml_str = parts[1]
    else:
        yaml_str = s

    # Attempt 1: direct parse
    try:
        result = yaml.safe_load(yaml_str) or {}
        if isinstance(result, dict):
            return result
    except yaml.YAMLError:
        pass

    # Attempt 2: quote unquoted colon values
    lines = []
    for ln in yaml_str.split("\n"):
        # 在 "key: value" 后面检测不规范值
        m = re.match(r"^(\s*-?\s*\w+):\s*(.+)$", ln)
        if m and not ln.rstrip().endswith((":", "|", ">", "-")):
            key, val = m.group(1), m.group(2).strip()
            # 跳过已经是 null/true/false/数字/引号/列表/YAML结构
            if val in ("null", "true", "false", "~") or val.startswith(("[", "{", '"', "'")):
                lines.append(ln)
                continue
            # 数字
            if re.match(r"^-?\d+(\.\d+)?$", val):
                lines.append(ln)
                continue
            # 日期
            if re.match(r"^\d{4}-\d{2}-\d{2}$", val):
                lines.append(ln)
                continue
            # 含裸冒号 → 引号包围
            if ":" in val or "," in val or "{" in val:
                val_quoted = val.replace('"', '\\"')
                lines.append(f"{key}: \"{val_quoted}\"")
                continue
        lines.append(ln)
    try:
        result = yaml.safe_load("\n".join(lines)) or {}
        if isinstance(result, dict):
            return result
    except yaml.YAMLError:
        pass

    # Attempt 3: 结构级回退 — 正则扒 overall_confidence + recommend_review
    out: dict = {}
    m = re.search(r"overall_confidence:\s*(high|medium|low|unknown)", yaml_str)
    if m:
        out["overall_confidence"] = m.group(1)
    m = re.search(r"recommend_review:\s*(true|false)", yaml_str)
    if m:
        out["recommend_review"] = m.group(1) == "true"
    m = re.search(r"recommend_review_reason:\s*(.+?)(?:\n|$)", yaml_str)
    if m:
        out["recommend_review_reason"] = m.group(1).strip().strip('"').strip("'")
    # 提取 field 级 mismatches（简版）
    field_blocks = re.findall(
        r"-\s*field:\s*(\S+).*?status:\s*(match|mismatch|unsure)",
        yaml_str,
        re.DOTALL,
    )
    if field_blocks:
        out["cross_check_result"] = [
            {"field": f, "status": s} for f, s in field_blocks
        ]
    return out


def apply_outcome(note_path: Path, fm: dict, outcome: dict, body_after_end: str, provider: str = "deepseek") -> None:
    """把 cross-check 结果合并回 note 的 FM，写回文件。"""
    fm["verified_by"] = "sonnet-4.6" if provider == "claude" else "deepseek-v3"
    fm["cross_check_overall_confidence"] = outcome.get("overall_confidence")
    results = outcome.get("cross_check_result") or []
    # 只保留 mismatch/unsure 字段的摘要，避免 FM 膨胀
    flagged = []
    for r in results:
        if not isinstance(r, dict):
            continue
        st = r.get("status")
        if st in ("mismatch", "unsure"):
            flagged.append({
                "field": r.get("field"),
                "status": st,
                "extracted": r.get("extracted_value"),
                "original": r.get("original_value"),
                "note": r.get("note"),
            })
            # 降一档置信度
            field = r.get("field")
            if field and st == "mismatch":
                fm[f"{field}_conf"] = "low"
    if flagged:
        fm["cross_check_flags"] = flagged

    # tags 同步
    tags = fm.get("tags") or []
    if isinstance(tags, list):
        tags = [t for t in tags if t not in ("status/needs-review", "status/verified")]
        if outcome.get("recommend_review"):
            tags.append("status/needs-review")
        else:
            tags.append("status/verified")
        fm["tags"] = tags

    new_content = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---" + body_after_end
    note_path.write_text(new_content, encoding="utf-8")


def worker(
    client,
    model: str,
    pricing: dict,
    system_prompt: str,
    user_template: str,
    item: tuple[Path, dict, str, str],
) -> tuple[Path, dict, dict | None, float, str]:
    """Process one note. Returns (path, fm, outcome, cost_usd, err)."""
    note_path, fm, extracted_text, raw_snippet = item
    user = user_template.format(
        extracted_yaml_and_body=extracted_text,
        selected_raw_chunks=raw_snippet,
    )
    try:
        resp = client.chat(
            system=system_prompt,
            user=user,
            model=model,
            max_tokens=2048,
            temperature=0.0,
            enable_cache=True,
        )
    except Exception as e:
        return note_path, fm, None, 0.0, f"api_error: {str(e)[:150]}"

    outcome = _parse_yaml_block(resp.content)
    if not outcome:
        return note_path, fm, None, 0.0, "yaml_parse_failed"

    # cost
    cache_read = resp.cached_tokens or 0
    cache_write = (resp.raw_response or {}).get("cache_write_tokens", 0) if resp.raw_response else 0
    fresh_in = max(resp.input_tokens - cache_read - cache_write, 0)
    cost = (
        fresh_in * pricing["in"] / 1_000_000
        + cache_read * pricing["cache_read"] / 1_000_000
        + cache_write * (pricing["in"] * pricing["cache_write_mult"]) / 1_000_000
        + resp.output_tokens * pricing["out"] / 1_000_000
    )
    return note_path, fm, outcome, cost, ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["deepseek", "claude"], default="deepseek")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--cost-cap-usd", type=float, default=30.0)
    ap.add_argument("--regions", nargs="+", default=None)
    ap.add_argument("--only-status-unknown", action="store_true")
    ap.add_argument("--only-missing-title", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=None, help="默认按 provider 自选")
    args = ap.parse_args()

    manifest_map = load_manifest_map()
    candidates = gather_candidates(
        regions=args.regions,
        only_status_unknown=args.only_status_unknown,
        only_missing_title=args.only_missing_title,
        manifest_map=manifest_map,
    )
    if args.limit:
        candidates = candidates[: args.limit]

    console.print(f"[cyan]Cross-check candidates:[/cyan] {len(candidates)}")
    if not candidates:
        return 0

    pricing = PRICING[args.provider]

    if args.dry_run:
        total_chars = sum(len(t[2]) + len(t[3]) for t in candidates)
        tok = int(total_chars * 0.4)
        out_tok = len(candidates) * 800
        cost_no_cache = tok * pricing["in"] / 1_000_000 + out_tok * pricing["out"] / 1_000_000
        # cache 80%: system prompt ~1.5k chars × 0.4 = 600 tok/req cached
        system_tok_cached = len(candidates) * 600 * 0.8
        cost_cached = (
            (tok - system_tok_cached) * pricing["in"] / 1_000_000
            + system_tok_cached * pricing["cache_read"] / 1_000_000
            + out_tok * pricing["out"] / 1_000_000
        )
        console.print(f"  provider: {args.provider}")
        console.print(f"  est input tok  = {tok:,}")
        console.print(f"  est output tok = {out_tok:,}")
        console.print(f"  est cost no cache    ≈ ${cost_no_cache:.2f}")
        console.print(f"  est cost w/ cache 80% ≈ ${cost_cached:.2f}")
        return 0

    prompt = load_prompt("cross_check")
    if args.provider == "claude":
        model = args.model or os.getenv("CLAUDE_SONNET_MODEL", "claude-sonnet-4-6")
        client = ClaudeClient(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            base_url=os.getenv("ANTHROPIC_BASE_URL"),
        )
    else:
        model = args.model or os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        client = DeepSeekClient(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
        )
    console.print(f"  provider: {args.provider}  model: {model}")
    console.print(f"  workers: {args.workers}, cost cap: ${args.cost_cap_usd}")

    stats = {"verified": 0, "flagged": 0, "errors": 0, "parse_fail": 0}
    total_cost = 0.0
    error_samples: list[str] = []
    flag_samples: list[str] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total} ${task.fields[cost]:.2f}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Cross-check", total=len(candidates), cost=0.0)

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(worker, client, model, pricing, prompt.system, prompt.user_template, it): it
                for it in candidates
            }
            for fut in as_completed(futures):
                note_path, fm, outcome, cost, err = fut.result()
                total_cost += cost
                if err:
                    if "yaml" in err:
                        stats["parse_fail"] += 1
                    else:
                        stats["errors"] += 1
                    if len(error_samples) < 5:
                        error_samples.append(f"{note_path.name}: {err}")
                elif outcome:
                    # 拿到 body（apply_outcome 需要分离 FM/body）
                    txt = note_path.read_text(encoding="utf-8", errors="replace")
                    end = txt.find("\n---", 4)
                    body_after = txt[end + 4 :] if end >= 0 else ""
                    apply_outcome(note_path, fm, outcome, body_after, args.provider)
                    if outcome.get("recommend_review"):
                        stats["flagged"] += 1
                        if len(flag_samples) < 5:
                            reasons = outcome.get("recommend_review_reason", "")
                            flag_samples.append(f"{note_path.name}: {str(reasons)[:80]}")
                    else:
                        stats["verified"] += 1

                progress.update(task, advance=1, cost=total_cost)
                if total_cost >= args.cost_cap_usd:
                    console.print(f"[yellow]Cost cap ${args.cost_cap_usd} reached, cancelling remaining...[/yellow]")
                    for f2 in futures:
                        if not f2.done():
                            f2.cancel()
                    break

    console.print(f"\n[green]Done:[/green] {stats}")
    console.print(f"  total cost: ${total_cost:.3f}")
    if flag_samples:
        console.print("\n  flagged (review recommended):")
        for s in flag_samples:
            console.print(f"    - {s}")
    if error_samples:
        console.print("\n  errors:")
        for s in error_samples:
            console.print(f"    - {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
