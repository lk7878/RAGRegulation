"""
CcVault Pipeline · 主入口 CLI

Usage:
    python ingest.py sample --reg "GB 4785"
    python ingest.py run --all
    python ingest.py run --stage 1
    python ingest.py run --dry-run
    python ingest.py status
    python ingest.py cost-report
    python ingest.py resume
    python ingest.py retry-failed
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Optional

import click
import yaml
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

# Load environment
ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

console = Console()


# =============================================================
# Configuration loader
# =============================================================
def load_config(path: Path = ROOT / "config.yaml") -> dict:
    """Load YAML config. Fail loudly if missing."""
    if not path.exists():
        console.print(f"[red]ERROR[/red] Config file not found: {path}")
        sys.exit(1)
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def require_env(*keys: str) -> dict:
    """Ensure required env vars are set. Return a dict of values."""
    missing = [k for k in keys if not os.getenv(k)]
    if missing:
        console.print(f"[red]ERROR[/red] Missing env vars: {missing}")
        console.print("  Copy .env.template to .env and fill in your keys.")
        sys.exit(1)
    return {k: os.getenv(k) for k in keys}


# =============================================================
# CLI Root
# =============================================================
@click.group()
@click.pass_context
def cli(ctx):
    """CcVault Pipeline - 法规知识库自动索引"""
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config()


# =============================================================
# Command: sample (Phase 1 样板验证)
# =============================================================
@cli.command()
@click.option("--reg", required=True, help="法规编号（不含版本），如 'GB 4785'")
@click.option("--limit", type=int, default=None, help="只处理前 N 个匹配（按路径字典序）")
@click.option("--skip-ocr", is_flag=True, help="跳过 OCR（假设 .staging 已有）")
@click.option("--dry-run", is_flag=True, help="不调真实 API，只列出要处理的文件")
@click.pass_context
def sample(ctx, reg: str, limit: Optional[int], skip_ocr: bool, dry_run: bool):
    """对某法规做全流程，Phase 1 样板验证（OCR → DeepSeek 抽取 → 写入 01_Wiki）"""
    if not dry_run:
        require_env("DEEPSEEK_API_KEY")

    # Local imports to avoid loading heavy deps for --help
    sys.path.insert(0, str(ROOT))
    from manifest import Manifest
    from stages import s0_ocr, s1_extract
    from writers import obsidian_writer
    from llm import DeepSeekClient

    console.print(f"[bold cyan]Sample run for:[/bold cyan] {reg}")

    mf = Manifest.load_or_create()
    if len(mf) == 0:
        console.print("[dim]Manifest empty, scanning raw dir...[/dim]")
        added = mf.scan_raw_dir()
        console.print(f"  Found {added} files")
        mf.save()

    files = mf.find_files_for_regulation(reg)
    if not files:
        console.print(f"[red]No files match '{reg}' in manifest[/red]")
        console.print("  Check that 00_Raw/标准库/ contains files with this prefix,")
        console.print("  or run: python ingest.py status")
        return

    total_matched = len(files)
    if limit and total_matched > limit:
        files = files[:limit]
        console.print(f"Matched {total_matched} files, [yellow]limited to first {limit}[/yellow]:")
    else:
        console.print(f"Matched [bold]{len(files)}[/bold] files:")
    for f in files:
        console.print(f"  - {f.path}  [dim]({f.state})[/dim]")

    if dry_run:
        console.print("\n[yellow]--dry-run, not actually processing[/yellow]")
        return

    # Stage 0: OCR
    if not skip_ocr:
        console.print("\n[bold]── Stage 0: OCR ──[/bold]")
        for rec in files:
            if rec.state == "pending":
                ok = s0_ocr.run_single(rec, mf)
                console.print(f"  {rec.path}: {'[green]✓[/green]' if ok else '[red]✗[/red]'} → {rec.state}")
        mf.save()

    # Stage 1: DeepSeek Extract
    console.print("\n[bold]── Stage 1: DeepSeek Extract ──[/bold]")
    client = DeepSeekClient(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL"),
    )
    for rec in files:
        if rec.state == "ocr_done":
            ok = s1_extract.run_single(rec, mf, client)
            console.print(f"  {rec.path}: {'[green]✓[/green]' if ok else '[red]✗[/red]'} → {rec.state}")
    mf.save()

    # Stage 2 (cross-check) is skipped in sample mode — needs Batch API with 12h turnaround.
    # Run separately: python -m stages.s2_cross_check submit && ... apply

    # Write to 01_Wiki
    console.print("\n[bold]── Write to 01_Wiki ──[/bold]")
    for rec in files:
        if rec.state in {"extracted", "verified", "needs_review"}:
            target = obsidian_writer.write_note(rec, mf)
            if target:
                try:
                    rel = target.relative_to(Path(os.getenv("VAULT_ROOT", "D:/CcVault")))
                except ValueError:
                    rel = target
                console.print(f"  [green]✓[/green] {rel}")
    mf.save()

    console.print("\n[bold green]✓ Sample done![/bold green]")
    console.print("\n[bold]下一步[/bold]：")
    console.print("  1. 在 Obsidian 里打开 01_Wiki/，review 生成的 notes")
    console.print("  2. 对比 02_Schema/03_frontmatter_schema.md 的 schema，看字段齐全度")
    console.print("  3. 如果质量 OK，跑: [cyan]python ingest.py run --dry-run[/cyan]")
    console.print("  4. 再跑: [cyan]python ingest.py run --all[/cyan]（全量 1537 份）")


# =============================================================
# Command: run (Phase 2 批量)
# =============================================================
@cli.command()
@click.option("--all", "run_all", is_flag=True, help="跑完整流水线")
@click.option("--stage", type=click.Choice(["0", "1", "2", "3", "4", "5", "write"]),
              help="只跑某一阶段（0=OCR / 1=Extract / 2=CrossCheck / 3=Equivalence / 4=Topic / 5=GraphRAG / write=WriteToWiki）")
@click.option("--dry-run", is_flag=True, help="不调真实 API，只 log 计划")
@click.option("--limit", type=int, default=None, help="只处理前 N 份（测试用）")
@click.option("--workers", type=int, default=None, help="并发 workers 数（OCR 默认 4，extract 默认 10）")
@click.option("--async-batch", is_flag=True,
              help="Batch API 只提交不等，12h 后手动跑 `python -m stages.sN apply`")
@click.pass_context
def run(ctx, run_all: bool, stage: Optional[str], dry_run: bool, limit: Optional[int],
        workers: Optional[int], async_batch: bool):
    """全量批处理。用法：
       python ingest.py run --stage 0 --limit 50    # 先试 50 份 OCR
       python ingest.py run --stage 1               # DeepSeek 全量抽取
       python ingest.py run --stage 2 --async-batch # Sonnet cross-check 只提交
       python ingest.py run --all                   # 全部串行，约 24-48 小时
    """
    if not (run_all or stage):
        console.print("[red]ERROR[/red] Must specify --all or --stage N")
        sys.exit(1)

    # 按 stage 需求 require env（stage 0 OCR 不需要 API key）
    if not dry_run:
        needs_deepseek = run_all or stage in {"1", "write"}
        needs_anthropic = run_all or stage in {"2", "3", "4", "5"}
        required: list[str] = []
        if needs_deepseek:
            required.append("DEEPSEEK_API_KEY")
        if needs_anthropic:
            required.append("ANTHROPIC_API_KEY")
        if required:
            require_env(*required)

    config = ctx.obj["config"]
    cost_cap = config.get("cost_monitoring", {}).get("daily_cap_usd", 100)
    console.print(f"[bold cyan]Pipeline run[/bold cyan]")
    console.print(f"  mode     = {'ALL' if run_all else f'STAGE {stage}'}")
    console.print(f"  dry_run  = {dry_run}")
    console.print(f"  limit    = {limit or 'none'}")
    console.print(f"  cost cap = ${cost_cap}")
    console.print(f"  async    = {async_batch}")

    sys.path.insert(0, str(ROOT))
    from manifest import Manifest
    from stages import s0_ocr, s1_extract, s2_cross_check, s3_equivalence, s4_topic_summary, s5_graphrag
    from writers import obsidian_writer

    mf = Manifest.load_or_create()
    if len(mf) == 0:
        console.print("[dim]Manifest empty, scanning raw dir...[/dim]")
        added = mf.scan_raw_dir()
        console.print(f"  Found {added} files")
        mf.save()

    stages_to_run = [stage] if stage else ["0", "1", "write", "2", "3", "4", "5"]

    for s in stages_to_run:
        console.print(f"\n[bold]══ Stage {s} ══[/bold]")

        try:
            if s == "0":
                s0_ocr.run_batch(
                    mf, limit=limit, dry_run=dry_run,
                    max_workers=workers or 8,
                )
            elif s == "1":
                s1_extract.run_batch(
                    mf, limit=limit, dry_run=dry_run,
                    max_workers=workers or 10,
                )
            elif s == "write":
                obsidian_writer.run_batch(mf, limit=limit)
            elif s == "2":
                s2_cross_check.submit(mf, limit=limit, dry_run=dry_run)
                if not async_batch and not dry_run:
                    s2_cross_check.apply(mf, wait=True)
            elif s == "3":
                s3_equivalence.submit(mf, limit=limit, dry_run=dry_run)
                if not async_batch and not dry_run:
                    s3_equivalence.apply(mf, wait=True)
            elif s == "4":
                s4_topic_summary.submit(mf, limit=limit, dry_run=dry_run)
                if not async_batch and not dry_run:
                    s4_topic_summary.apply(wait=True)
            elif s == "5":
                s5_graphrag.submit()
                if not async_batch and not dry_run:
                    s5_graphrag.apply(wait=True)
        except KeyboardInterrupt:
            console.print(f"\n[yellow]Interrupted at stage {s}[/yellow]")
            mf.save()
            console.print("[dim]Manifest saved. Resume with: python ingest.py resume[/dim]")
            sys.exit(130)
        except Exception as e:
            console.print(f"[red]Stage {s} error:[/red] {e}")
            mf.save()
            if run_all:
                console.print("[yellow]Continuing to next stage (manifest state preserved)[/yellow]")
                continue
            raise

    console.print(f"\n[bold green]✓ Pipeline run completed[/bold green]")
    console.print("  Use [cyan]python ingest.py status[/cyan] 和 [cyan]cost-report[/cyan] 查看结果")


# =============================================================
# Command: status
# =============================================================
@cli.command()
def status():
    """打印 manifest 的当前状态"""
    from manifest import Manifest
    mf = Manifest.load_or_create()
    summary = mf.summary()

    table = Table(title="Manifest Status", show_lines=True)
    table.add_column("状态", style="cyan")
    table.add_column("数量", justify="right")
    for state, count in summary.items():
        table.add_row(state, str(count))
    console.print(table)


# =============================================================
# Command: cost-report
# =============================================================
@cli.command(name="cost-report")
def cost_report():
    """从 cost_log.jsonl 汇总成本"""
    import json
    from collections import defaultdict

    log_path = ROOT / "logs" / "cost_log.jsonl"
    if not log_path.exists():
        console.print("[yellow]No cost log yet.[/yellow]")
        return

    by_provider = defaultdict(float)
    total = 0.0
    with log_path.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            by_provider[rec.get("provider", "unknown")] += rec.get("cost_usd", 0)
            total += rec.get("cost_usd", 0)

    table = Table(title="Cost Report", show_lines=True)
    table.add_column("Provider", style="cyan")
    table.add_column("Cost (USD)", justify="right")
    for p, c in sorted(by_provider.items(), key=lambda x: -x[1]):
        table.add_row(p, f"${c:.2f}")
    table.add_row("[bold]Total[/bold]", f"[bold]${total:.2f}[/bold]")
    console.print(table)


# =============================================================
# Command: resume
# =============================================================
@cli.command()
@click.pass_context
def resume(ctx):
    """从上次中断处续跑"""
    console.print("[cyan]Resuming from last checkpoint...[/cyan]")
    # TODO(Day 3): 读取 manifest，找到每阶段的 pending/failed，继续处理
    console.print("[yellow]TODO:[/yellow] implement resume logic")


# =============================================================
# Command: retry-failed
# =============================================================
@cli.command(name="retry-failed")
@click.option("--reg", default=None, help="只重试匹配此法规编号的 failed 文件")
@click.option("--stage", type=click.Choice(["ocr", "extract", "all"]), default="all",
              help="只重试某阶段的 failed（ocr/extract/all）")
@click.pass_context
def retry_failed(ctx, reg: Optional[str], stage: str):
    """把 failed 状态的文件重置到上一阶段的就绪状态，等待 sample/run 重新处理。

    规则：
      - 若 .staging/{hash}/extracted.md 存在 → state="extracted"（跳过 OCR 和 extract）
      - 若 .staging/{hash}/raw.md 存在 → state="ocr_done"（只重跑 extract）
      - 否则 → state="pending"（从 OCR 重来）
    """
    sys.path.insert(0, str(ROOT))
    from manifest import Manifest

    mf = Manifest.load_or_create()
    if reg:
        targets = [r for r in mf.find_files_for_regulation(reg) if r.state == "failed"]
    else:
        targets = mf.files_in_state("failed")

    if not targets:
        console.print("[yellow]No failed records to retry[/yellow]")
        return

    staging_root = ROOT / ".staging"
    reset_counts = {"pending": 0, "ocr_done": 0, "extracted": 0, "skipped": 0}
    for rec in targets:
        # 阶段过滤
        err = (rec.error or "").lower()
        if stage == "ocr" and "ocr" not in err:
            reset_counts["skipped"] += 1
            continue
        if stage == "extract" and ("deepseek" not in err and "extract" not in err):
            reset_counts["skipped"] += 1
            continue

        stage_dir = staging_root / rec.content_hash[:2] / rec.content_hash
        if (stage_dir / "extracted.md").exists():
            new_state = "extracted"
        elif (stage_dir / "raw.md").exists():
            new_state = "ocr_done"
        else:
            new_state = "pending"

        rec.state = new_state
        rec.error = None
        reset_counts[new_state] += 1

    mf.save()
    console.print(f"[green]Reset {len(targets) - reset_counts['skipped']} failed records:[/green]")
    for state, count in reset_counts.items():
        if count:
            console.print(f"  → {state}: {count}")
    console.print("\nNow run: [cyan]python ingest.py sample --reg '...'[/cyan] or [cyan]run --all[/cyan]")


# =============================================================
# Command: smart-composer-setup
# =============================================================
@cli.command(name="smart-composer-setup")
def smart_composer_setup():
    """输出 Smart Composer 插件配置"""
    require_env("ANTHROPIC_API_KEY")

    import json
    config = {
        "models": {
            "default_complex": {
                "provider": "anthropic",
                "model": os.getenv("CLAUDE_OPUS_MODEL", "claude-opus-4-7"),
                "temperature": 0.2,
            },
            "default_simple": {
                "provider": "anthropic",
                "model": os.getenv("CLAUDE_SONNET_MODEL", "claude-sonnet-4-6"),
                "temperature": 0.2,
            },
        },
        "rag": {
            "vault_root": os.getenv("VAULT_ROOT", "D:/CcVault"),
            "enabled_folders": ["01_Wiki"],
            "excluded_folders": ["00_Raw", "99_SystemScripts", ".obsidian"],
            "chunk_size": 500,
            "chunk_overlap": 50,
            "retrieval_top_k": 8,
        },
        "routing": {
            "rule": "if question contains ['对比', 'compare', '等效', '图谱', 'graph', '综述'] "
                    "then default_complex else default_simple",
        },
    }
    console.print_json(json.dumps(config, indent=2, ensure_ascii=False))
    console.print("\n[green]Copy the above JSON into Smart Composer plugin settings.[/green]")


# =============================================================
# Main
# =============================================================
if __name__ == "__main__":
    cli(obj={})
