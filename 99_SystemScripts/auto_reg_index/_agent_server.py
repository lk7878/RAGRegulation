"""启动 CcVault Agent HTTP 服务（OpenAI 兼容），供 Obsidian Copilot / OpenAI SDK 等调用。

用法：
    python _agent_server.py                         # 127.0.0.1:7777
    python _agent_server.py --port 7788
    python _agent_server.py --host 0.0.0.0          # 局域网可访问
    python _agent_server.py --reload                # 开发模式热重载

配置 Obsidian Copilot：
    Custom Model:
      name:     CcVault Agent
      base_url: http://127.0.0.1:7777/v1
      api_key:  dummy
      model:    ccvault-agent
"""
from __future__ import annotations

import argparse


def main() -> int:
    ap = argparse.ArgumentParser(description="CcVault Agent HTTP server")
    ap.add_argument("--host", default="127.0.0.1",
                    help="监听地址（默认 127.0.0.1，设为 0.0.0.0 开放局域网）")
    ap.add_argument("--port", type=int, default=7777, help="监听端口（默认 7777）")
    ap.add_argument("--reload", action="store_true", help="开发模式：改代码自动重启")
    args = ap.parse_args()

    print(f"╭─ CcVault Agent Server")
    print(f"│  URL:       http://{args.host}:{args.port}")
    print(f"│  /v1/models        → 列模型")
    print(f"│  /v1/chat/completions → OpenAI 兼容聊天接口")
    print(f"│  /health           → 健康检查")
    print(f"│  /docs             → Swagger UI")
    print(f"╰─ Obsidian Copilot 配置: base_url=http://{args.host}:{args.port}/v1, model=ccvault-agent")

    from agent.server import run
    run(host=args.host, port=args.port, reload=args.reload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
