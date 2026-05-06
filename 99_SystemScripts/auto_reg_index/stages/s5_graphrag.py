"""
Stage 5 · GraphRAG Orchestrator

调度 GraphRAG 三步流程：
  1. `_build_graph.py` → `.stage5/graph.json`（节点 + 边）
  2. `_graphrag_communities.py` → `.stage5/communities.json`（Louvain 社区）
  3. `_graphrag_summarize.py` → `04_Topics/communities/community_*.md`（LLM 综述）

查询入口独立：
  4. `_graphrag_search.py "<query>"` → 层级检索（社区 + 成员 top-K）

实现历程：
  - 2026-04 Phase 1：骨架占位（NotImplementedError）
  - 2026-04 Phase 3（当前）：真实实现 + DeepSeek V3 生成综述
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent.parent))

console = Console()

ROOT = Path(__file__).parent.parent
PY = Path(sys.executable)  # 当前 venv 的 python.exe

# 社区检测参数（与 _graphrag_communities.py 保持同步）
MIN_COMMUNITY_SIZE = 3
MAX_COMMUNITY_SIZE = 30
COMMUNITY_ALGORITHM = "louvain"  # networkx 原生支持


def _run(cmd: list[str], *, description: str) -> int:
    """执行子命令并转发输出；返回 exit code。"""
    console.print(f"[cyan]▶ {description}[/cyan]")
    console.print(f"  [dim]$ {' '.join(cmd)}[/dim]")
    r = subprocess.run(cmd, cwd=str(ROOT))
    if r.returncode != 0:
        console.print(f"[red]✗ 失败（exit {r.returncode}）[/red]")
    return r.returncode


def build_graph() -> int:
    """Step 1: 构建 .stage5/graph.json（由 _build_graph.py 完成）。"""
    return _run(
        [str(PY), str(ROOT / "_build_graph.py")],
        description="Step 1/3 · 构建关系图",
    )


def detect_communities(*, resolution: float = 1.0, seed: int = 42) -> int:
    """Step 2: Louvain 社区检测 → .stage5/communities.json。"""
    return _run(
        [
            str(PY), str(ROOT / "_graphrag_communities.py"),
            "--resolution", str(resolution),
            "--seed", str(seed),
        ],
        description="Step 2/3 · Louvain 社区检测",
    )


def summarize(
    *,
    provider: str = "deepseek",
    concurrency: int = 5,
    force: bool = False,
) -> int:
    """Step 3: LLM 生成社区综述 → 04_Topics/communities/*.md。"""
    cmd = [
        str(PY), str(ROOT / "_graphrag_summarize.py"),
        "--provider", provider,
        "--concurrency", str(concurrency),
    ]
    if force:
        cmd.append("--force")
    return _run(cmd, description="Step 3/3 · 生成社区综述")


def apply(
    *,
    skip_build: bool = False,
    skip_communities: bool = False,
    skip_summarize: bool = False,
    provider: str = "deepseek",
    resolution: float = 1.0,
    concurrency: int = 5,
    force: bool = False,
) -> int:
    """完整 pipeline。返回 0 成功 / 非 0 失败。"""
    console.print("[bold cyan]=== Stage 5 GraphRAG Pipeline ===[/bold cyan]")

    if not skip_build:
        if build_graph() != 0:
            return 1
    else:
        console.print("[dim]⤷ 跳过 Step 1（--skip-build）[/dim]")

    if not skip_communities:
        if detect_communities(resolution=resolution) != 0:
            return 2
    else:
        console.print("[dim]⤷ 跳过 Step 2（--skip-communities）[/dim]")

    if not skip_summarize:
        if summarize(provider=provider, concurrency=concurrency, force=force) != 0:
            return 3
    else:
        console.print("[dim]⤷ 跳过 Step 3（--skip-summarize）[/dim]")

    console.print()
    console.print("[bold green]✓ GraphRAG pipeline 完成[/bold green]")
    console.print("  社区综述：D:/CcVault/04_Topics/communities/")
    console.print("  查询入口：python _graphrag_search.py \"<query>\"")
    return 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="GraphRAG Pipeline orchestrator")
    ap.add_argument("--skip-build", action="store_true",
                    help="跳过 Step 1（假设 .stage5/graph.json 已是最新）")
    ap.add_argument("--skip-communities", action="store_true",
                    help="跳过 Step 2（假设 .stage5/communities.json 已是最新）")
    ap.add_argument("--skip-summarize", action="store_true",
                    help="跳过 Step 3（只重建图和社区）")
    ap.add_argument("--provider", choices=["deepseek", "claude"], default="deepseek")
    ap.add_argument("--resolution", type=float, default=1.0,
                    help="Louvain resolution（>1 产生更小社区）")
    ap.add_argument("--concurrency", type=int, default=5)
    ap.add_argument("--force", action="store_true",
                    help="覆盖已有的 community_*.md")
    args = ap.parse_args()

    return apply(
        skip_build=args.skip_build,
        skip_communities=args.skip_communities,
        skip_summarize=args.skip_summarize,
        provider=args.provider,
        resolution=args.resolution,
        concurrency=args.concurrency,
        force=args.force,
    )


if __name__ == "__main__":
    raise SystemExit(main())
