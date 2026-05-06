"""
Stage 2 Phase 2 —— 针对 143 条残余 low-confidence 的 DeepSeek 二次复核。

不同于 _run_cross_check.py 的全量 cross-check，本脚本:
  1. 只处理 cross_check_overall_confidence=low 的 notes
  2. 对现有 mismatch flags 做"第二意见"评估：真 mismatch / 应降为 normalized / 应降为 unsure
  3. 用紧凑 prompt (仅 OCR 原文 + 当前 flag 清单)，大幅减少 token
  4. 写回 updated flag 状态 + 新的 overall_confidence

预算 ~$0.5（~143 notes × ~3500 tokens input + ~600 tokens output）

用法：
  python _recheck_low_confidence.py --limit 5 --cost-cap-usd 0.1   # 冒烟
  python _recheck_low_confidence.py                                  # 全量
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

import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env", override=True)
sys.path.insert(0, str(ROOT))

from llm import DeepSeekClient  # noqa: E402

console = Console()
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STAGING = ROOT / ".staging"
MF_PATH = ROOT / "manifest.json"

RECHECK_PROMPT = """你是汽车法规数据质量审核员。

一条汽车标准的提取数据经过 Stage 1 LLM 抽取 + Stage 2 LLM cross-check 后，仍被标记为 low confidence。
现在需要你做 **第二意见复核**：针对每条 cross_check_flag（status=mismatch），判断：

- `still_mismatch`: 确实是抽取数据与原文矛盾（真错）
- `normalized`:    抽取数据做了规范化（如 "4 March 1994" → "1994-03-04"、"GB11555-94" → "GB 11555-1994"），实质一致
- `unsure`:        原文中没有该字段或原文数据不清，无法判断

同时给出 updated overall_confidence: high / medium / low / unknown
  - high:   所有关键字段（reg_id, title, publication_date）都无 still_mismatch
  - medium: 关键字段无 still_mismatch，但有一些 unsure
  - low:    至少一个关键字段 still_mismatch

返回 YAML（---包围）：
---
overall_confidence: high | medium | low | unknown
flag_updates:
  - field: <field_name>
    new_status: still_mismatch | normalized | unsure
    reason: <短解释>
---

---
**数据 A（Stage 1 抽取 + Stage 2 flag 清单）**:
{extracted_summary}

**原文 OCR 片段**（仅前 8000 字符）:
```
{raw_snippet}
```
---
请只返回 YAML，不要其他解释。
"""


def load_manifest_map() -> dict[str, str]:
    data = json.loads(MF_PATH.read_text(encoding="utf-8"))
    return {
        h: str(r.get("path") or "").replace("\\", "/").lstrip("/")
        for h, r in data["records"].items()
    }


def find_raw_md(source_pdf: str, mf: dict) -> Path | None:
    norm = str(source_pdf).replace("\\", "/").lstrip("/")
    for h, p in mf.items():
        if p == norm or p.endswith(norm) or norm.endswith(p):
            raw = STAGING / h[:2] / h / "raw.md"
            if raw.exists():
                return raw
    return None


def gather_low_conf_notes(mf: dict) -> list[tuple[Path, dict, str, str]]:
    """返回 (note_path, fm, extracted_summary, raw_snippet)。"""
    out = []
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        try:
            fm = yaml.safe_load(txt[4:end]) or {}
        except yaml.YAMLError:
            continue
        if fm.get("cross_check_overall_confidence") != "low":
            continue
        flags = fm.get("cross_check_flags") or []
        real_mm = [f for f in flags if isinstance(f, dict) and f.get("status") == "mismatch"]
        if not real_mm:
            continue
        src = fm.get("source_pdf") or fm.get("source_file")
        if not src:
            continue
        raw_md = find_raw_md(str(src), mf)
        if not raw_md:
            continue
        raw_snippet = raw_md.read_text(encoding="utf-8", errors="replace")[:8000]

        # 紧凑摘要：reg_id / title / publication / implementation_date + 所有 mismatch 字段
        compact = {
            "reg_id": fm.get("reg_id"),
            "title": (fm.get("title") or "")[:100],
            "publication_date": str(fm.get("publication_date") or ""),
            "implementation_date_new_vehicle": str(fm.get("implementation_date_new_vehicle") or ""),
            "standard_body": fm.get("standard_body"),
            "current_mismatch_flags": [
                {
                    "field": f.get("field"),
                    "extracted": str(f.get("extracted", ""))[:100],
                    "original": str(f.get("original", ""))[:200],
                    "note": str(f.get("note", ""))[:200],
                }
                for f in real_mm
            ],
        }
        extracted_summary = yaml.safe_dump(compact, allow_unicode=True, sort_keys=False)
        out.append((p, fm, extracted_summary, raw_snippet))
    return out


def parse_response(text: str) -> dict | None:
    """提取 YAML 回复。"""
    s = text.strip()
    # 去掉 ``` 包裹
    s = re.sub(r"^```(?:yaml)?\s*", "", s)
    s = re.sub(r"\s*```\s*$", "", s)
    # 取 --- 之间
    parts = s.split("---")
    yaml_str = parts[1] if len(parts) >= 3 else (parts[1] if len(parts) == 2 else s)
    try:
        r = yaml.safe_load(yaml_str) or {}
        if isinstance(r, dict):
            return r
    except yaml.YAMLError:
        pass
    # 回退：正则
    m = re.search(r"overall_confidence:\s*(high|medium|low|unknown)", yaml_str)
    conf = m.group(1) if m else None
    updates = []
    for match in re.finditer(
        r"-\s*field:\s*(\S+)\s*\n\s*new_status:\s*(\w+)",
        yaml_str,
    ):
        updates.append({"field": match.group(1), "new_status": match.group(2), "reason": ""})
    if conf or updates:
        return {"overall_confidence": conf, "flag_updates": updates}
    return None


def apply_updates(path: Path, fm: dict, result: dict) -> bool:
    """把 LLM 回复应用到 note FM。返回是否修改。"""
    new_conf = result.get("overall_confidence")
    updates = result.get("flag_updates") or []
    if not new_conf and not updates:
        return False

    changed = False

    # 更新 flag status
    flags = fm.get("cross_check_flags") or []
    update_map = {u["field"]: u["new_status"] for u in updates if isinstance(u, dict)}
    for f in flags:
        if not isinstance(f, dict):
            continue
        fld = f.get("field")
        if fld in update_map:
            old_status = f.get("status")
            new_status = update_map[fld]
            if new_status in ("still_mismatch", "normalized", "unsure") and old_status == "mismatch":
                # still_mismatch 保持 mismatch，其余降级
                if new_status == "still_mismatch":
                    # 标注 recheck 确认
                    f["recheck_verdict"] = "confirmed_mismatch"
                elif new_status in ("normalized", "unsure"):
                    f["status"] = new_status
                    # 找对应 update reason
                    for u in updates:
                        if u.get("field") == fld:
                            f["recheck_reason"] = u.get("reason", "")[:200]
                            break
                changed = True

    # 更新 overall_confidence
    if new_conf and new_conf in ("high", "medium", "low", "unknown"):
        old_conf = fm.get("cross_check_overall_confidence")
        if new_conf != old_conf:
            fm["cross_check_overall_confidence"] = new_conf
            fm["recheck_at"] = time.strftime("%Y-%m-%d")
            # Tag 更新
            tags = fm.get("tags") or []
            if isinstance(tags, list):
                if new_conf in ("high", "medium"):
                    if "status/needs-review" in tags:
                        tags.remove("status/needs-review")
                    if "status/verified" not in tags:
                        tags.append("status/verified")
                    fm["tags"] = tags
            changed = True

    return changed


def write_fm(path: Path, fm: dict):
    txt = path.read_text(encoding="utf-8", errors="replace")
    end = txt.find("\n---", 4)
    body = txt[end + 4 :]
    new_content = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---" + body
    path.write_text(new_content, encoding="utf-8")


def worker(client: DeepSeekClient, task: tuple, dry_run: bool) -> dict:
    path, fm, extracted_summary, raw_snippet = task
    prompt = RECHECK_PROMPT.format(
        extracted_summary=extracted_summary,
        raw_snippet=raw_snippet,
    )
    try:
        resp = client.chat(
            system="你是汽车法规数据质量审核员，严格按要求输出 YAML。",
            user=prompt,
            model="deepseek-chat",
            temperature=0.0,
            max_tokens=800,
        )
    except Exception as e:
        return {"path": str(path), "error": str(e)}

    content = resp.content
    usage = {"prompt_tokens": resp.input_tokens, "completion_tokens": resp.output_tokens}
    result = parse_response(content)
    if not result:
        return {
            "path": str(path),
            "error": "parse_failed",
            "response_preview": content[:300],
            "usage": usage,
        }

    changed = apply_updates(path, fm, result)
    if changed and not dry_run:
        write_fm(path, fm)

    return {
        "path": str(path),
        "reg_id": fm.get("reg_id"),
        "result": result,
        "changed": changed,
        "usage": usage,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = unlimited")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--cost-cap-usd", type=float, default=1.0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mf = load_manifest_map()
    candidates = gather_low_conf_notes(mf)
    console.print(f"[cyan]Found {len(candidates)} low-conf notes with mismatch flags[/cyan]")

    if args.limit:
        candidates = candidates[: args.limit]
        console.print(f"[yellow]Limited to {len(candidates)}[/yellow]")

    if not candidates:
        return 0

    client = DeepSeekClient(api_key=os.environ["DEEPSEEK_API_KEY"])

    total_cost = 0.0
    cost_cap = args.cost_cap_usd
    upgraded = 0
    confirmed = 0
    errors = 0
    all_results = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[cyan]{task.completed}/{task.total}"),
        TextColumn("[green]${task.fields[cost]:.3f}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        t_id = progress.add_task("Rechecking...", total=len(candidates), cost=0.0)
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(worker, client, c, args.dry_run): c for c in candidates}
            for fut in as_completed(futures):
                r = fut.result()
                all_results.append(r)
                if "error" in r:
                    errors += 1
                else:
                    usage = r.get("usage") or {}
                    # DeepSeek pricing
                    cost = (usage.get("prompt_tokens", 0) * 0.00000027
                            + usage.get("completion_tokens", 0) * 0.00000110)
                    total_cost += cost
                    if r["changed"]:
                        conf = r["result"].get("overall_confidence")
                        if conf in ("high", "medium"):
                            upgraded += 1
                        else:
                            confirmed += 1
                    progress.update(t_id, advance=1, cost=total_cost)
                if total_cost >= cost_cap:
                    console.print(f"[red]Cost cap hit ${total_cost:.3f} >= ${cost_cap}[/red]")
                    for f in futures:
                        f.cancel()
                    break

    console.print(f"\n[bold]Summary:[/bold]")
    console.print(f"  Upgraded low → medium/high: [green]{upgraded}[/green]")
    console.print(f"  Confirmed real mismatches:  [yellow]{confirmed}[/yellow]")
    console.print(f"  Errors / parse fails:        [red]{errors}[/red]")
    console.print(f"  Total cost:                  [cyan]${total_cost:.4f}[/cyan]")

    # Save report
    (ROOT / ".stage5" / "recheck_results.json").write_text(
        json.dumps(all_results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
