"""所有工具的集中导出点。

agent.py 通过 `from agent.tools import ALL_TOOLS` 拿到全部 tool 列表。
"""
from __future__ import annotations

from .search import SEARCH_TOOLS
from .stats import STATS_TOOLS
from .structure import STRUCTURE_TOOLS
from .audit import AUDIT_TOOLS

ALL_TOOLS = [
    *SEARCH_TOOLS,
    *STATS_TOOLS,
    *STRUCTURE_TOOLS,
    *AUDIT_TOOLS,
]

__all__ = ["ALL_TOOLS"]
