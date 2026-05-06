"""
Stage 0 · OCR

输入：manifest 中 state=pending 的源文件
输出：.staging/{hash}/raw.md（每份文件一份 markdown）
输出状态：state → ocr_done / failed
"""
from __future__ import annotations

import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

# 允许 pipeline 模块以 `python -m stages.s0_ocr` 或 `python ingest.py run --stage 0` 运行
sys.path.insert(0, str(Path(__file__).parent.parent))

from manifest import Manifest, FileRecord
from ocr import route_ocr, OCR_LAYER

console = Console()

ROOT = Path(__file__).parent.parent
STAGING_DIR = ROOT / ".staging"
RAW_ROOT = Path(os.getenv("RAW_SOURCE_DIR", "D:/CcVault/00_Raw/标准库"))


def _staging_path(rec: FileRecord) -> Path:
    """Staging dir for one file, based on content hash"""
    return STAGING_DIR / rec.content_hash[:2] / rec.content_hash


def run_single(rec: FileRecord, mf: Manifest, *, force: bool = False) -> bool:
    """处理单个文件。返回 True 表示成功。"""
    stage_dir = _staging_path(rec)
    out = stage_dir / "raw.md"

    if out.exists() and not force and rec.state != "pending":
        # 已处理过，skip
        return True

    # 跳过重复副本
    if rec.duplicate_of:
        rec.advance_to("skipped", note=f"duplicate_of {rec.duplicate_of}")
        return True

    pdf_path = RAW_ROOT / rec.path
    if not pdf_path.exists():
        rec.mark_failed(f"Source file not found: {pdf_path}")
        return False

    # 非 PDF 文件暂不处理（Word/Excel 让 Day 2 专门处理）
    if pdf_path.suffix.lower() != ".pdf":
        rec.advance_to("skipped", note=f"non-PDF ({pdf_path.suffix})")
        return True

    # 调 OCR router
    try:
        result = route_ocr(pdf_path)
    except Exception as e:
        rec.mark_failed(f"OCR exception: {e}")
        return False

    if not result.success:
        rec.mark_failed(f"OCR failed ({result.layer_used.value}): {'; '.join(result.warnings)}")
        return False

    # 写 staging
    stage_dir.mkdir(parents=True, exist_ok=True)
    out.write_text(result.markdown, encoding="utf-8")

    # 记录元数据
    meta = stage_dir / "ocr_meta.yaml"
    meta.write_text(
        f"layer_used: {result.layer_used.value}\n"
        f"page_count: {result.page_count}\n"
        f"cost_cny: {result.cost_cny}\n"
        f"warnings: {result.warnings}\n",
        encoding="utf-8",
    )

    rec.advance_to("ocr_done", note=f"{result.layer_used.value} page={result.page_count}")
    return True


def run_batch(
    mf: Manifest,
    *,
    limit: Optional[int] = None,
    max_workers: int = 4,
    dry_run: bool = False,
) -> dict:
    """批量处理 manifest 中 state=pending 的文件"""
    pending = mf.files_in_state("pending")
    if limit:
        pending = pending[:limit]

    if dry_run:
        console.print(f"[yellow]DRY-RUN[/yellow] would OCR {len(pending)} files")
        return {"total": len(pending), "dry_run": True}

    console.print(f"[cyan]OCR batch:[/cyan] {len(pending)} files, {max_workers} workers")

    stats = {"success": 0, "failed": 0, "skipped": 0}
    save_interval = 50  # 每 50 份 save 一次 manifest
    processed = 0
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("OCR", total=len(pending))
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {pool.submit(run_single, rec, mf): rec for rec in pending}
            for fut in as_completed(futures):
                rec = futures[fut]
                try:
                    ok = fut.result()
                    if rec.state == "skipped":
                        stats["skipped"] += 1
                    elif ok:
                        stats["success"] += 1
                    else:
                        stats["failed"] += 1
                except Exception as e:
                    rec.mark_failed(f"Unhandled: {e}")
                    stats["failed"] += 1
                progress.advance(task)
                processed += 1
                if processed % save_interval == 0:
                    mf.save()

    mf.save()
    console.print(f"[green]OCR done:[/green] {stats}")
    return stats


if __name__ == "__main__":
    mf = Manifest.load_or_create()
    if len(mf) == 0:
        console.print("[yellow]Manifest empty, scanning raw dir first...[/yellow]")
        added = mf.scan_raw_dir()
        console.print(f"  Added {added} files")
        mf.save()
    run_batch(mf)
