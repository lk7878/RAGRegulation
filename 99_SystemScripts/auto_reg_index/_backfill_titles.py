"""
对缺 title 的 notes 从 .staging/raw.md 前 1500 字 + DeepSeek 补齐 title。
同时可选补齐 publication_date。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
sys.path.insert(0, str(ROOT))

from llm import DeepSeekClient  # noqa: E402

console = Console()
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STAGING = ROOT / ".staging"
MF_PATH = ROOT / "manifest.json"


def _find_staging_raw(source_pdf: str, manifest: dict) -> Path | None:
    src_norm = source_pdf.replace("\\", "/").lstrip("/")
    for h, rec in manifest["records"].items():
        p = str(rec.get("path", "")).replace("\\", "/").lstrip("/")
        if p == src_norm or p.endswith(src_norm) or src_norm.endswith(p):
            raw = STAGING / h[:2] / h / "raw.md"
            if raw.exists():
                return raw
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--also-dates", action="store_true", help="同时补齐缺失的 publication_date")
    ap.add_argument("--also-status", action="store_true", help="同时推断缺失的 status（active/withdrawn/superseded/draft/under_revision）")
    args = ap.parse_args()

    mf = json.loads(MF_PATH.read_text(encoding="utf-8"))

    targets: list[tuple[Path, dict, str]] = []  # (note_path, fm, raw_snippet)
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        fm = yaml.safe_load(txt[4:end]) or {}

        needs_title = not (fm.get("title") and str(fm.get("title")).strip())
        needs_date = args.also_dates and not fm.get("publication_date")
        cur_status = fm.get("status")
        needs_status = args.also_status and (
            not cur_status or str(cur_status).strip().lower() in ("unknown", "none", "null", "")
        )
        if not (needs_title or needs_date or needs_status):
            continue

        src = fm.get("source_pdf") or fm.get("source_file")
        if not src:
            continue
        raw_md = _find_staging_raw(str(src), mf)
        if not raw_md:
            continue
        raw_text = raw_md.read_text(encoding="utf-8", errors="replace")
        # 取前 2000 字作为上下文（封面信息通常在此）
        snippet = raw_text[:2000].strip()
        if len(snippet) < 50:
            continue
        targets.append((p, fm, snippet))

    if args.limit:
        targets = targets[: args.limit]

    console.print(f"[cyan]Backfill candidates:[/cyan] {len(targets)} notes")
    if args.dry_run:
        console.print("[yellow]DRY-RUN — sample 3:[/yellow]")
        for p, fm, snip in targets[:3]:
            console.print(f"  {p.name}: reg_id={fm.get('reg_id')} title={fm.get('title')!r}")
            console.print(f"    snippet: {snip[:100]!r}")
        return 0

    client = DeepSeekClient(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL"),
    )
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    n_ok = 0
    n_skipped = 0
    n_title_filled = 0
    n_date_filled = 0
    n_status_filled = 0

    with Progress(console=console) as progress:
        task = progress.add_task("Backfill", total=len(targets))
        for note_path, fm, snippet in targets:
            reg_id = fm.get("reg_id", "UNKNOWN")
            needs_title = not (fm.get("title") and str(fm.get("title")).strip())
            needs_date = args.also_dates and not fm.get("publication_date")
            cur_status = fm.get("status")
            needs_status = args.also_status and (
                not cur_status or str(cur_status).strip().lower() in ("unknown", "none", "null", "")
            )

            fields = []
            if needs_title:
                fields.append("title (用原始语言全称，不要翻译)")
            if needs_date:
                fields.append("publication_date (ISO YYYY-MM-DD)")
            if needs_status:
                fields.append("status (只能取: active/withdrawn/superseded/draft/under_revision; 默认 active 除非明确看到作废/被替代/修订中标志)")

            prompt = f"""你是法规元数据抽取助手。下面是一份法规文档的首 2000 字文本。

reg_id: {reg_id}
region: {fm.get('region')}

需要抽取的字段：{', '.join(fields)}

只返回 YAML 格式，不要其他说明。若字段无法从文本确定，填 null。
例如：
title: "道路车辆 电气/电子部件抗干扰试验"
publication_date: 2023-05-12

--- 文档首段 ---
{snippet}
--- END ---

只输出 YAML，字段名与 reg_id/region 无关，只包含上面需要的字段。"""

            try:
                response = client.chat(
                    system="你是法规元数据抽取助手，只返回 YAML，不添加解释。",
                    user=prompt,
                    model=model,
                    max_tokens=200,
                    temperature=0.0,
                )
            except Exception as e:
                console.print(f"  [red]LLM error {note_path.name}: {e}[/red]")
                n_skipped += 1
                progress.advance(task)
                continue

            text = response.content.strip()
            # 移除 ```yaml fences
            import re as _re
            text = _re.sub(r"^```(?:yaml)?\s*", "", text)
            text = _re.sub(r"\s*```\s*$", "", text)
            try:
                parsed = yaml.safe_load(text) or {}
            except yaml.YAMLError:
                n_skipped += 1
                progress.advance(task)
                continue

            changed = False
            if needs_title and parsed.get("title"):
                fm["title"] = str(parsed["title"]).strip()
                n_title_filled += 1
                changed = True
            if needs_date and parsed.get("publication_date"):
                # 接受 date 或 str
                fm["publication_date"] = parsed["publication_date"]
                n_date_filled += 1
                changed = True
            if needs_status and parsed.get("status"):
                val = str(parsed["status"]).strip().lower()
                if val in ("active", "withdrawn", "superseded", "draft", "under_revision"):
                    fm["status"] = val
                    n_status_filled += 1
                    changed = True
                    # 同步 tags
                    tags = fm.get("tags") or []
                    if isinstance(tags, list):
                        tags = [t for t in tags if not (isinstance(t, str) and t.startswith("status/"))]
                        tags.append(f"status/{val.replace('_', '-')}")
                        fm["tags"] = tags

            if changed:
                # 写回 note（保留 body）
                full = note_path.read_text(encoding="utf-8", errors="replace")
                end = full.find("\n---", 4)
                body = full[end + 4 :] if end >= 0 else ""
                new_content = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---" + body
                note_path.write_text(new_content, encoding="utf-8")
                n_ok += 1

            progress.advance(task)

    console.print(f"\n[green]Done:[/green] {n_ok} notes updated "
                  f"(title: +{n_title_filled}, date: +{n_date_filled}, status: +{n_status_filled}, skipped: {n_skipped})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
