"""MCP Server 启动入口 - 通过 stdio 暴露 12 个 CcVault 工具给任何 MCP 客户端。

用法（通常不手动跑，由 MCP 客户端自动启动）：
    python _agent_mcp.py

配置到各个客户端：

## Cascade (Windsurf) — `~/.codeium/windsurf/mcp_config.json`
    {
      "mcpServers": {
        "ccvault": {
          "command": "D:/CcVault/99_SystemScripts/auto_reg_index/.venv/Scripts/python.exe",
          "args": ["D:/CcVault/99_SystemScripts/auto_reg_index/_agent_mcp.py"]
        }
      }
    }

## Claude Desktop — `%APPDATA%/Claude/claude_desktop_config.json`
同上

## Cursor — Settings > MCP
同上

详见 `agent/README.md` 的 "MCP 集成" 小节。
"""
from agent.mcp_server import main

if __name__ == "__main__":
    main()
