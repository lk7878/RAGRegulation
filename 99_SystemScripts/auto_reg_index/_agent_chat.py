"""CcVault ReAct Agent — 最外层 CLI 入口。

用法：
    python _agent_chat.py "vault 里有多少条中国法规"       # 单次
    python _agent_chat.py                                   # REPL 模式
    python _agent_chat.py -v "最近一周改了哪些 notes"      # verbose
    python _agent_chat.py --provider claude "..."          # 切 Claude

详见 agent/README.md。
"""
from __future__ import annotations

from agent.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
