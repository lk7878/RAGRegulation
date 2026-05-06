"""CLI 入口。支持单次问答、REPL 连续对话、verbose 模式。

用法：
    python _agent_chat.py "vault 里有多少条中国法规"       # 单次
    python _agent_chat.py                                   # 进 REPL
    python _agent_chat.py -v "最近一周改了哪些 notes"      # 显示 tool 调用轨迹
    python _agent_chat.py --provider claude "..."          # 切模型
"""
from __future__ import annotations

import argparse
import sys
import time
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def _print_tool_calls(calls: list[dict]) -> None:
    if not calls:
        return
    console.print("\n[dim]── tool trace ──[/dim]")
    for i, c in enumerate(calls, 1):
        name = c.get("name", "?")
        args = c.get("args", {})
        args_str = ", ".join(f"{k}={v!r}" for k, v in (args or {}).items())
        if len(args_str) > 100:
            args_str = args_str[:97] + "..."
        console.print(f"[dim]  [{i}] {name}({args_str})[/dim]")


def _single_query(
    agent,
    question: str,
    history: list[tuple[str, str]],
    *,
    verbose: bool,
) -> tuple[str, list[dict]]:
    from .agent import run_once

    t0 = time.time()
    result = run_once(agent, question, history)
    elapsed = time.time() - t0

    answer = result["answer"] or "(空回答)"
    console.print()
    console.print(Panel(
        Markdown(answer),
        title=f"[bold green]Answer[/bold green] [dim]({elapsed:.1f}s)[/dim]",
        border_style="green",
    ))

    if verbose:
        _print_tool_calls(result["tool_calls"])

    return answer, result["tool_calls"]


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="cascade agent",
        description="CcVault ReAct agent CLI",
    )
    ap.add_argument("question", nargs="?", help="问题内容；留空进入 REPL 模式")
    ap.add_argument("--provider", "-p", choices=["deepseek", "claude"], default="deepseek",
                    help="LLM provider，默认 deepseek")
    ap.add_argument("--verbose", "-v", action="store_true", help="显示 tool call 轨迹")
    ap.add_argument("--temperature", "-t", type=float, default=0.0)
    args = ap.parse_args()

    console.print(f"[cyan]Building agent (provider={args.provider}, temp={args.temperature})...[/cyan]")
    from .agent import build_agent

    try:
        agent = build_agent(args.provider, args.temperature)
    except Exception as e:
        console.print(f"[red]Agent 构建失败: {e}[/red]")
        return 1

    console.print("[green]✓ Agent ready.[/green] "
                  "[dim]Tools: 12 个 CcVault 检索/统计/结构/审计工具[/dim]")

    history: list[tuple[str, str]] = []

    # 单次模式
    if args.question:
        answer, _ = _single_query(agent, args.question, history, verbose=args.verbose)
        return 0

    # REPL 模式
    console.print("\n[bold]REPL 模式[/bold] — 输入问题，Ctrl-C 或输入 /exit 退出；"
                  "/clear 清空历史；/verbose 切换 trace。")
    verbose = args.verbose
    while True:
        try:
            q = console.input("\n[bold blue]>[/bold blue] ").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[yellow]bye.[/yellow]")
            return 0
        if not q:
            continue
        if q in ("/exit", "/quit"):
            console.print("[yellow]bye.[/yellow]")
            return 0
        if q == "/clear":
            history.clear()
            console.print("[yellow]对话历史已清空。[/yellow]")
            continue
        if q == "/verbose":
            verbose = not verbose
            console.print(f"[yellow]verbose={'on' if verbose else 'off'}[/yellow]")
            continue
        if q == "/help":
            console.print(
                "[dim]可用命令: /exit /clear /verbose /help[/dim]\n"
                "[dim]示例问题:[/dim]\n"
                "  [dim]- vault 里有多少条 ECE 法规？[/dim]\n"
                "  [dim]- 国六排放相关的社区是哪个？[/dim]\n"
                "  [dim]- GB 4785 的历代版本有哪些？[/dim]\n"
                "  [dim]- 低置信度 notes 前 10 条[/dim]"
            )
            continue

        answer, _ = _single_query(agent, q, history, verbose=verbose)
        # 累加到历史
        history.append(("human", q))
        history.append(("ai", answer))
        # 限制历史长度（防 context 爆）
        if len(history) > 20:
            history = history[-20:]


if __name__ == "__main__":
    raise SystemExit(main())
