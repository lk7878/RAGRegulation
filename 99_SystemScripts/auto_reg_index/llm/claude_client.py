"""
Claude client (Sonnet 4.6 / Opus 4.7)

支持：
- 同步 chat (stages.s3_equivalence 调少量对，用同步)
- Batch API (stages.s2/s4/s5 大量请求用 batch，50% 折扣)
- Prompt Caching (system prompt + few-shot 模板缓存，30-40% 节省)

定价 (2026-04 官方):
    Opus 4.7 :  input $5 / M,  output $25 / M
    Sonnet 4.6: input $3 / M,  output $15 / M
    Cache write: 1.25x input price
    Cache read:  0.10x input price (90% off)
    Batch API: 所有价格 × 0.5
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Optional

from anthropic import Anthropic
from tenacity import retry, stop_after_attempt, wait_exponential

from .base import LLMClient, LLMResponse


PRICING_USD_PER_MILLION = {
    # model              : (input, output, cache_write, cache_read)
    "claude-opus-4-7":    (5.00, 25.00, 6.25, 0.50),
    "claude-opus-4-6":    (5.00, 25.00, 6.25, 0.50),
    "claude-sonnet-4-6":  (3.00, 15.00, 3.75, 0.30),
    "claude-sonnet-4-5":  (3.00, 15.00, 3.75, 0.30),
}

BATCH_DISCOUNT = 0.5


class ClaudeClient(LLMClient):
    provider = "anthropic"
    default_model = "claude-sonnet-4-6"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        super().__init__(api_key, base_url)
        kwargs = {"api_key": api_key}
        if base_url:
            kwargs["base_url"] = base_url
        self._client = Anthropic(**kwargs)

    # =========================================================
    # Sync chat
    # =========================================================
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=2, max=30),
    )
    def chat(
        self,
        system: str,
        user: str,
        *,
        model: Optional[str] = None,
        max_tokens: int = 8192,
        temperature: float = 0.1,
        enable_cache: bool = True,
    ) -> LLMResponse:
        model = model or self.default_model

        # 构造 system，支持 prompt caching
        system_blocks = [{"type": "text", "text": system}]
        if enable_cache and len(system) > 1024:
            # 只对够长的 system prompt 做 cache（cache write 有最小长度要求）
            system_blocks[0]["cache_control"] = {"type": "ephemeral"}

        response = self._client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_blocks,
            messages=[{"role": "user", "content": user}],
        )
        usage = response.usage

        content = ""
        for block in response.content:
            if hasattr(block, "text"):
                content += block.text

        cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
        cache_write = getattr(usage, "cache_creation_input_tokens", 0) or 0

        return LLMResponse(
            content=content,
            model=model,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            cached_tokens=cache_read,
            finish_reason=response.stop_reason or "stop",
            raw_response={
                "id": response.id,
                "cache_write_tokens": cache_write,
                "cache_read_tokens": cache_read,
            },
        )

    # =========================================================
    # Batch API
    # =========================================================
    def submit_batch(
        self,
        requests: list[dict],
        *,
        model: Optional[str] = None,
    ) -> str:
        """
        提交 batch。每个 request 的格式：
            {"custom_id": "...", "system": "...", "user": "...",
             "max_tokens": 8192, "temperature": 0.1}
        """
        model = model or self.default_model
        batch_requests = []
        for req in requests:
            system_blocks = [{"type": "text", "text": req["system"]}]
            if len(req["system"]) > 1024:
                system_blocks[0]["cache_control"] = {"type": "ephemeral"}

            batch_requests.append({
                "custom_id": req["custom_id"],
                "params": {
                    "model": model,
                    "max_tokens": req.get("max_tokens", 8192),
                    "temperature": req.get("temperature", 0.1),
                    "system": system_blocks,
                    "messages": [{"role": "user", "content": req["user"]}],
                },
            })

        batch = self._client.messages.batches.create(requests=batch_requests)
        return batch.id

    def fetch_batch(self, batch_id: str) -> Optional[list[LLMResponse]]:
        """拉 batch 结果。None = 还在跑。"""
        batch = self._client.messages.batches.retrieve(batch_id)
        if batch.processing_status != "ended":
            return None

        results = []
        for item in self._client.messages.batches.results(batch_id):
            res = item.result
            if res.type != "succeeded":
                # 失败的也占位，上游判断
                results.append(LLMResponse(
                    content="",
                    model=batch.model if hasattr(batch, "model") else "unknown",
                    input_tokens=0,
                    output_tokens=0,
                    finish_reason=f"batch_{res.type}",
                    raw_response={"custom_id": item.custom_id, "error": str(res)},
                ))
                continue

            msg = res.message
            content = "".join(b.text for b in msg.content if hasattr(b, "text"))
            usage = msg.usage
            cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0

            results.append(LLMResponse(
                content=content,
                model=msg.model,
                input_tokens=usage.input_tokens,
                output_tokens=usage.output_tokens,
                cached_tokens=cache_read,
                finish_reason=msg.stop_reason or "stop",
                raw_response={"custom_id": item.custom_id},
            ))
        return results

    def wait_for_batch(
        self,
        batch_id: str,
        *,
        poll_interval_seconds: int = 60,
        max_wait_hours: int = 24,
    ) -> list[LLMResponse]:
        """阻塞等待 batch 完成。"""
        deadline = time.time() + max_wait_hours * 3600
        while time.time() < deadline:
            results = self.fetch_batch(batch_id)
            if results is not None:
                return results
            time.sleep(poll_interval_seconds)
        raise TimeoutError(f"Batch {batch_id} did not finish within {max_wait_hours}h")

    # =========================================================
    # Cost
    # =========================================================
    def calculate_cost_usd(
        self,
        input_tokens: int,
        output_tokens: int,
        cached_tokens: int = 0,
        model: Optional[str] = None,
        is_batch: bool = False,
        cache_write_tokens: int = 0,
    ) -> float:
        model = model or self.default_model
        if model not in PRICING_USD_PER_MILLION:
            # 未知模型，用 sonnet 默认价兜底
            model = "claude-sonnet-4-6"

        p_in, p_out, p_cw, p_cr = PRICING_USD_PER_MILLION[model]

        # 普通 input = 总 input - cache 读 - cache 写
        fresh_input = max(input_tokens - cached_tokens - cache_write_tokens, 0)

        cost = (
            fresh_input * p_in / 1_000_000
            + cached_tokens * p_cr / 1_000_000
            + cache_write_tokens * p_cw / 1_000_000
            + output_tokens * p_out / 1_000_000
        )
        if is_batch:
            cost *= BATCH_DISCOUNT
        return round(cost, 6)
