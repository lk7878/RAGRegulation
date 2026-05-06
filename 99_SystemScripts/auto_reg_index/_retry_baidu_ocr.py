"""
对 state=failed 的记录强制走 Baidu OCR 重试。

用法：
  # 先跑 3 份小样验证：
  python _retry_baidu_ocr.py --limit 3

  # 小批量确认成本合理：
  python _retry_baidu_ocr.py --limit 20 --max-pages 50

  # 全量：
  python _retry_baidu_ocr.py
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

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
load_dotenv(ROOT / ".env")
sys.path.insert(0, str(ROOT))

from manifest import Manifest, FileRecord  # noqa: E402
from ocr import OCR_LAYER  # noqa: E402
from ocr.baidu_ocr import extract as baidu_extract  # noqa: E402
from ocr.router import OCRResult  # noqa: E402

console = Console()
RAW_ROOT = Path(os.getenv("RAW_SOURCE_DIR", r"D:\CcVault\00_Raw\标准库"))
STAGING_DIR = ROOT / ".staging"


def _staging_path(rec: FileRecord) -> Path:
    return STAGING_DIR / rec.content_hash[:2] / rec.content_hash


def _count_pages(pdf: Path) -> int:
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        n = len(doc)
        doc.close()
        return n
    except Exception:
        return 0


def retry_record(rec: FileRecord, *, max_pages: int = 0) -> tuple[bool, float, str]:
    """强制对单份 PDF 走 Baidu OCR。返回 (success, cost_cny, message)。"""
    pdf = RAW_ROOT / rec.path
    if not pdf.exists():
        return False, 0.0, f"file not found: {pdf}"
    if pdf.suffix.lower() != ".pdf":
        return False, 0.0, f"non-PDF: {pdf.suffix}"
    if max_pages > 0:
        n = _count_pages(pdf)
        if n > max_pages:
            return False, 0.0, f"skipped: {n} pages > max_pages {max_pages}"

    try:
        result: OCRResult = baidu_extract(pdf)
    except Exception as e:
        rec.mark_failed(f"Baidu OCR exception: {e}")
        return False, 0.0, f"exception: {e}"

    if not result.success:
        rec.mark_failed(f"Baidu OCR failed: {'; '.join(result.warnings[:3])}")
        return False, result.cost_cny, "; ".join(result.warnings[:3]) or "no result"

    # 写 staging
    stage_dir = _staging_path(rec)
    stage_dir.mkdir(parents=True, exist_ok=True)
    out = stage_dir / "raw.md"
    out.write_text(result.markdown, encoding="utf-8")

    meta = stage_dir / "ocr_meta.yaml"
    meta.write_text(
        f"layer_used: {result.layer_used.value}\n"
        f"page_count: {result.page_count}\n"
        f"cost_cny: {result.cost_cny}\n"
        f"warnings: {result.warnings}\n",
        encoding="utf-8",
    )

    rec.advance_to("ocr_done", note=f"baidu page={result.page_count}")
    return True, result.cost_cny, f"ok ({result.page_count} pages)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="处理条数上限，0=全量")
    ap.add_argument("--max-pages", type=int, default=0, help="单份 PDF 页数上限（超过则跳过），0=不限")
    ap.add_argument("--cost-cap-cny", type=float, default=50.0, help="累计成本上限（¥），超过则停止")
    ap.add_argument("--sort-by-size", action="store_true", help="按 size 升序处理（小文件优先）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mf = Manifest.load_or_create()
    failed = [rec for rec in mf.records.values() if rec.state == "failed"]
    if args.sort_by_size:
        failed.sort(key=lambda r: r.size_bytes or 0)
    if args.limit:
        failed = failed[: args.limit]

    if args.dry_run:
        console.print(f"[yellow]DRY-RUN[/yellow] would retry {len(failed)} failed records")
        return 0

    console.print(f"[cyan]Baidu OCR retry:[/cyan] {len(failed)} records, cost cap ¥{args.cost_cap_cny}")

    total_cost = 0.0
    stats = {"success": 0, "failed": 0, "skipped": 0}
    save_interval = 10

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total} ¥{task.fields[cost]:.2f}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Baidu OCR", total=len(failed), cost=0.0)
        for i, rec in enumerate(failed, 1):
            if total_cost >= args.cost_cap_cny:
                console.print(f"[yellow]Cost cap ¥{args.cost_cap_cny} reached, stopping[/yellow]")
                break
            ok, cost, msg = retry_record(rec, max_pages=args.max_pages)
            total_cost += cost
            if ok:
                stats["success"] += 1
            elif "skipped" in msg:
                stats["skipped"] += 1
            else:
                stats["failed"] += 1
                console.print(f"  [dim red]{rec.path[:60]}: {msg}[/dim red]")

            progress.update(task, advance=1, cost=total_cost)
            if i % save_interval == 0:
                mf.save()

    mf.save()
    console.print(f"\n[green]Done:[/green] {stats}  total cost ¥{total_cost:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
