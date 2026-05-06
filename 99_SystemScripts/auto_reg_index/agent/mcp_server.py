"""MCP (Model Context Protocol) 服务器 - 把 CcVault 的 12 个 agent tools 暴露给任何 MCP 客户端。

MCP 是 Anthropic 推出的协议，让 LLM 客户端统一调用外部工具。
支持 MCP 的客户端：Claude Desktop / Cursor / Cascade / 其他符合协议的。

本 server 通过 stdio 通信，客户端启动子进程读写 stdin/stdout 即可。

配置示例（Claude Desktop ~/.claude_desktop_config.json）：
    {
      "mcpServers": {
        "ccvault": {
          "command": "D:\\\\CcVault\\\\99_SystemScripts\\\\auto_reg_index\\\\.venv\\\\Scripts\\\\python.exe",
          "args": ["D:\\\\CcVault\\\\99_SystemScripts\\\\auto_reg_index\\\\_agent_mcp.py"]
        }
      }
    }
"""
from __future__ import annotations

import asyncio
import json
import sys
from typing import Any

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

from .tools import ALL_TOOLS

# ---------------------------------------------------------------------------
# 建立 name -> tool 查表
# ---------------------------------------------------------------------------
_TOOL_MAP = {t.name: t for t in ALL_TOOLS}


def _mk_mcp_tool(lc_tool) -> types.Tool:
    """把 LangChain @tool 对象转成 MCP Tool schema。"""
    schema = {"type": "object", "properties": {}}
    if lc_tool.args_schema is not None:
        try:
            schema = lc_tool.args_schema.model_json_schema()
        except Exception:
            pass

    # MCP 要求 description 不能太长（一般 ≤1024），截断
    desc = (lc_tool.description or "").strip()
    if len(desc) > 1024:
        desc = desc[:1020] + "..."

    return types.Tool(
        name=lc_tool.name,
        description=desc,
        inputSchema=schema,
    )


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

server = Server("ccvault-agent")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """列出所有可用工具。"""
    return [_mk_mcp_tool(t) for t in ALL_TOOLS]


@server.call_tool()
async def handle_call_tool(
    name: str,
    arguments: dict[str, Any] | None,
) -> list[types.TextContent]:
    """执行单个工具调用。"""
    tool = _TOOL_MAP.get(name)
    if not tool:
        return [types.TextContent(
            type="text",
            text=f"[mcp error] Unknown tool: {name!r}. Available: {list(_TOOL_MAP.keys())}",
        )]

    args = arguments or {}
    try:
        # LangChain tool 的调用接口：tool.invoke(dict_of_args)
        # 异步调用：runloop 里用 to_thread 避免 block
        result = await asyncio.to_thread(tool.invoke, args)
    except Exception as e:
        return [types.TextContent(type="text", text=f"[tool error] {name}: {e}")]

    text = str(result) if result is not None else "(空输出)"
    return [types.TextContent(type="text", text=text)]


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

async def run_stdio() -> None:
    """stdio 模式运行，供 Claude Desktop / Cursor / Cascade 等调用。"""
    # 启动日志到 stderr（stdout 被 MCP 占用）
    print(f"[ccvault-mcp] 启动成功，注册 {len(ALL_TOOLS)} 个 tools", file=sys.stderr)
    for t in ALL_TOOLS:
        print(f"  - {t.name}", file=sys.stderr)

    async with stdio_server() as (read, write):
        await server.run(
            read,
            write,
            server.create_initialization_options(),
        )


def main() -> None:
    asyncio.run(run_stdio())


if __name__ == "__main__":
    main()
