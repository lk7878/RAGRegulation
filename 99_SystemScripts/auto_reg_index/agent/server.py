"""OpenAI 兼容的 FastAPI 服务，把 CcVault Agent 暴露为 /v1/chat/completions 端点。

让 Obsidian Copilot 或任何 OpenAI-SDK 客户端都能直接调用。

启动：
    python _agent_server.py             # 默认 127.0.0.1:7777
    python _agent_server.py --port 7788
    python _agent_server.py --host 0.0.0.0 --port 7777   # 局域网访问

端点：
    GET  /v1/models                     列出可用模型
    POST /v1/chat/completions           主接口，兼容 OpenAI schema
    GET  /health                        健康检查
"""
from __future__ import annotations

import json
import time
import uuid
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator, Literal, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from sse_starlette.sse import EventSourceResponse

# ---------------------------------------------------------------------------
# Agent 单例（启动时构建，请求间复用）
# ---------------------------------------------------------------------------
_AGENT_CACHE: dict = {}


def _get_agent(provider: str = "deepseek", temperature: float = 0.0):
    """按 (provider, temperature) 缓存 agent 实例。"""
    key = f"{provider}:{temperature}"
    if key not in _AGENT_CACHE:
        from .agent import build_agent
        _AGENT_CACHE[key] = build_agent(provider, temperature)
    return _AGENT_CACHE[key]


def _normalize_content(content: Any) -> str:
    """把 OpenAI 兼容的 content 规范成纯字符串。

    content 可能是：
      - 字符串（经典）: "hello"
      - 多模态数组: [{"type": "text", "text": "..."}, {"type": "image_url", ...}]
      - None / 其他
    """
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                t = item.get("type")
                if t == "text" and "text" in item:
                    parts.append(str(item["text"]))
                elif "text" in item:
                    parts.append(str(item["text"]))
                # 忽略 image_url / input_audio 等非文本模态
            elif isinstance(item, str):
                parts.append(item)
        return "\n".join(p for p in parts if p)
    return str(content)


# ---------------------------------------------------------------------------
# OpenAI 兼容 schema
# ---------------------------------------------------------------------------

class Message(BaseModel):
    """OpenAI 兼容的 message，宽松接受各种 client 变体。

    - role 用 str 不限定（developer/function/扩展角色都收）
    - content 支持 str（经典）或 list[dict]（OpenAI vision / multimodal 格式）
    - allow 额外字段（name / tool_calls / tool_call_id 等）
    """
    model_config = ConfigDict(extra="allow")

    role: str
    content: Any = ""


class ChatCompletionRequest(BaseModel):
    """OpenAI 兼容的请求体。allow 未知字段避免 422。"""
    model_config = ConfigDict(extra="allow")

    model: str = "ccvault-agent"
    messages: list[Message]
    stream: bool = False
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    # CcVault 自定义：切换底层 LLM provider
    provider: Optional[Literal["deepseek", "claude"]] = None


class Choice(BaseModel):
    index: int = 0
    message: Message
    finish_reason: str = "stop"


class Usage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: list[Choice]
    usage: Usage = Field(default_factory=Usage)


# ---------------------------------------------------------------------------
# FastAPI 生命周期
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时预热 agent，避免首次请求延迟
    try:
        _get_agent("deepseek", 0.0)
        print("[ccvault-agent] 预热完成：default provider=deepseek")
    except Exception as e:
        print(f"[ccvault-agent] 预热失败（不影响启动）: {e}")
    yield


app = FastAPI(
    title="CcVault Agent API",
    version="1.0.0",
    description="OpenAI 兼容的 CcVault ReAct Agent 服务",
    lifespan=lifespan,
)

# Obsidian Copilot 可能从 app:// 协议发起 CORS 请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def _validation_exc_handler(request: Request, exc: RequestValidationError):
    """422 时把 body + errors 打到日志，方便定位 client 发了什么。"""
    try:
        body_bytes = await request.body()
        body_preview = body_bytes.decode("utf-8", errors="replace")[:800]
    except Exception:
        body_preview = "(cannot read body)"
    print(f"\n[422] {request.method} {request.url.path}")
    print(f"  errors: {exc.errors()}")
    print(f"  body  : {body_preview}\n")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body_preview": body_preview},
    )


# ---------------------------------------------------------------------------
# 端点
# ---------------------------------------------------------------------------

@app.get("/health")
async def health():
    return {"status": "ok", "agents_cached": list(_AGENT_CACHE.keys())}


@app.get("/v1/models")
async def list_models():
    """Copilot 配 custom model 时会调此端点获取可用模型列表。"""
    now = int(time.time())
    return {
        "object": "list",
        "data": [
            {
                "id": "ccvault-agent",
                "object": "model",
                "created": now,
                "owned_by": "ccvault",
            },
            {
                "id": "ccvault-agent-claude",
                "object": "model",
                "created": now,
                "owned_by": "ccvault",
            },
        ],
    }


@app.post("/v1/chat/completions")
async def chat_completions(req: ChatCompletionRequest):
    """主接口 - OpenAI 兼容的 chat completions。

    支持 stream=true/false。stream=true 时返回 SSE，否则返回一次性 JSON。
    """
    # 分离 system / user / assistant 消息（content 统一规范成字符串）
    system_msgs: list[str] = []
    chat_msgs: list[tuple[str, str]] = []  # (role, text)
    for m in req.messages:
        text = _normalize_content(m.content)
        # 合并非标准角色到 user/assistant
        role = m.role.lower()
        if role == "developer":   # OpenAI 新的 developer 角色 → 当作 system
            role = "system"
        if role == "system":
            if text.strip():
                system_msgs.append(text)
        else:
            chat_msgs.append((role, text))

    if not chat_msgs:
        raise HTTPException(400, "messages 必须至少包含一条 user/assistant")

    # 找最后一条 user 消息作为当前问题（容错：Copilot 可能带 tool/assistant 结尾）
    question = ""
    last_user_idx = -1
    for i in range(len(chat_msgs) - 1, -1, -1):
        if chat_msgs[i][0] == "user":
            question = chat_msgs[i][1]
            last_user_idx = i
            break
    if not question:
        raise HTTPException(400, "messages 中未找到 user 消息")

    # 之前的 user/assistant 作为 history（只保留 user/assistant，过滤 tool）
    history: list[tuple[str, str]] = []
    for role, text in chat_msgs[:last_user_idx]:
        if role == "user":
            history.append(("human", text))
        elif role == "assistant":
            history.append(("ai", text))
        # tool 角色的历史跳过（agent 不需要重放 tool 结果）

    # 解析 provider
    provider = req.provider
    if not provider:
        # 也支持通过 model name 指定：ccvault-agent-claude -> claude
        if req.model.endswith("-claude"):
            provider = "claude"
        else:
            provider = "deepseek"

    # 选/建 agent
    try:
        agent = _get_agent(provider, req.temperature)
    except Exception as e:
        raise HTTPException(500, f"Agent 初始化失败: {e}")

    # 追加 system message（如果 request 里带了）—— 作为 system role 传递
    # 注意：我们的 agent 已有自己的 system prompt，用户额外的 system msg 前置作为上下文
    if system_msgs:
        prepend = "\n\n".join(system_msgs)
        question = f"(额外系统指示)\n{prepend}\n\n(用户问题)\n{question}"

    # 执行
    from .agent import run_once
    cid = f"chatcmpl-{uuid.uuid4().hex[:16]}"

    if not req.stream:
        # 非流式：同步跑完返回
        try:
            result = run_once(agent, question, history)
        except Exception as e:
            raise HTTPException(500, f"Agent 执行失败: {e}")

        answer = result.get("answer", "") or "(空回答)"
        return ChatCompletionResponse(
            id=cid,
            created=int(time.time()),
            model=req.model,
            choices=[Choice(message=Message(role="assistant", content=answer))],
        )

    # 流式：跑完后分块 SSE 推送（"伪流式"，LangGraph agent 本身不是 token-by-token）
    async def _stream() -> AsyncIterator[dict]:
        try:
            result = run_once(agent, question, history)
        except Exception as e:
            payload = {
                "id": cid, "object": "chat.completion.chunk", "created": int(time.time()),
                "model": req.model,
                "choices": [{"index": 0, "delta": {"content": f"[agent error] {e}"},
                             "finish_reason": "stop"}],
            }
            yield {"data": json.dumps(payload, ensure_ascii=False)}
            yield {"data": "[DONE]"}
            return

        answer = result.get("answer", "") or "(空回答)"

        # role delta
        first = {
            "id": cid, "object": "chat.completion.chunk", "created": int(time.time()),
            "model": req.model,
            "choices": [{"index": 0, "delta": {"role": "assistant"}, "finish_reason": None}],
        }
        yield {"data": json.dumps(first, ensure_ascii=False)}

        # 按字符分块推送（每 20 字一块模拟流式效果）
        CHUNK = 20
        for i in range(0, len(answer), CHUNK):
            chunk = answer[i:i + CHUNK]
            payload = {
                "id": cid, "object": "chat.completion.chunk", "created": int(time.time()),
                "model": req.model,
                "choices": [{"index": 0, "delta": {"content": chunk}, "finish_reason": None}],
            }
            yield {"data": json.dumps(payload, ensure_ascii=False)}

        # 结束
        done = {
            "id": cid, "object": "chat.completion.chunk", "created": int(time.time()),
            "model": req.model,
            "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
        }
        yield {"data": json.dumps(done, ensure_ascii=False)}
        yield {"data": "[DONE]"}

    return EventSourceResponse(_stream())


# ---------------------------------------------------------------------------
# 本地入口（给 _agent_server.py 调用）
# ---------------------------------------------------------------------------

def run(host: str = "127.0.0.1", port: int = 7777, reload: bool = False):
    import uvicorn
    if reload:
        # reload 模式需要 module:path 字符串
        uvicorn.run("agent.server:app", host=host, port=port, reload=True)
    else:
        uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run()
