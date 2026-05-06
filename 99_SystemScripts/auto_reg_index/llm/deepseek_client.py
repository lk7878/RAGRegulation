"""
DeepSeek V3 client

使用 OpenAI-compatible API (via openai python SDK)
定价：
    input cache miss  : $0.27 / M tokens
    input cache hit   : $0.07 / M tokens
    output            : $1.10 / M tokens
"""
from __future__ import annotations

from typing import Optional

import httpx
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from .base import LLMClient, LLMResponse


class DeepSeekClient(LLMClient):
    provider = "deepseek"
    default_model = "deepseek-chat"

    # Pricing per 1M tokens
    PRICE_INPUT_MISS_USD = 0.27
    PRICE_INPUT_HIT_USD = 0.07
    PRICE_OUTPUT_USD = 1.10

    def __init__(self, api_key: str, base_url: Optional[str] = None, timeout: float = 300.0):
        super().__init__(api_key, base_url or "https://api.deepseek.com/v1")
        # 大陆网络对 HTTP/2 + keepalive 连接发大 POST 时常被中间设备 reset，
        # 导致 [SSL: UNEXPECTED_EOF_WHILE_READING]。强制 HTTP/1.1 + 不复用连接可避免。
        self._http = httpx.Client(
            timeout=httpx.Timeout(timeout, connect=30.0),
            http2=False,
            transport=httpx.HTTPTransport(retries=2, http2=False),
            limits=httpx.Limits(max_connections=10, max_keepalive_connections=0),
        )
        self._client = OpenAI(
            api_key=api_key,
            base_url=self.base_url,
            http_client=self._http,
            max_retries=0,  # 由 tenacity 统一管理 retry
        )

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=2, min=2, max=60),
        retry=retry_if_exception_type((httpx.HTTPError, httpx.NetworkError, OSError)),
        reraise=True,
    )
    def chat(
        self,
        system: str,
        user: str,
        *,
        model: Optional[str] = None,
        max_tokens: int = 8192,
        temperature: float = 0.1,
        enable_cache: bool = True,   # DeepSeek 原生支持，默认开
    ) -> LLMResponse:
        model = model or self.default_model
        response = self._client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            stream=False,
        )
        choice = response.choices[0]
        usage = response.usage
        # DeepSeek 的 cached tokens 在 usage.prompt_cache_hit_tokens
        cached = getattr(usage, "prompt_cache_hit_tokens", 0) or 0

        return LLMResponse(
            content=choice.message.content or "",
            model=model,
            input_tokens=usage.prompt_tokens,
            output_tokens=usage.completion_tokens,
            cached_tokens=cached,
            finish_reason=choice.finish_reason or "stop",
            raw_response=response.model_dump() if hasattr(response, "model_dump") else None,
        )

    def submit_batch(
        self,
        requests: list[dict],
        *,
        model: Optional[str] = None,
    ) -> str:
        """DeepSeek 不支持原生 batch API。我们用 concurrency 模拟。
        这里返回一个 fake batch_id；由 caller 用 asyncio + semaphore 做并发。"""
        raise NotImplementedError(
            "DeepSeek has no native batch API. "
            "Use stages.runner.run_concurrent() instead."
        )

    def fetch_batch(self, batch_id: str) -> Optional[list[LLMResponse]]:
        raise NotImplementedError("DeepSeek has no batch API.")

    # ---------- Cost ----------
    def calculate_cost_usd(
        self,
        input_tokens: int,
        output_tokens: int,
        cached_tokens: int = 0,
        model: Optional[str] = None,
    ) -> float:
        miss_tokens = max(input_tokens - cached_tokens, 0)
        input_cost = (
            (miss_tokens * self.PRICE_INPUT_MISS_USD / 1_000_000)
            + (cached_tokens * self.PRICE_INPUT_HIT_USD / 1_000_000)
        )
        output_cost = output_tokens * self.PRICE_OUTPUT_USD / 1_000_000
        return round(input_cost + output_cost, 6)
