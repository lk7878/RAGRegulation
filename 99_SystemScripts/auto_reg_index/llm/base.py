"""
LLM Client · 统一抽象层

所有 pipeline 代码都通过这层调用 LLM，不直接 import anthropic/openai。
好处：
- 统一错误处理 + 重试
- 统一成本记录
- 未来换模型只改这一层
"""
from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent.parent
COST_LOG_PATH = ROOT / "logs" / "cost_log.jsonl"


# =============================================================
# Data classes
# =============================================================
@dataclass
class LLMResponse:
    """所有 LLM 客户端的标准返回"""
    content: str                           # 完整回复文本
    model: str
    input_tokens: int
    output_tokens: int
    cached_tokens: int = 0
    finish_reason: str = "stop"
    raw_response: Optional[dict] = None    # 原始 API 响应（debug 用）


@dataclass
class CostRecord:
    """成本日志单条记录"""
    ts: str
    stage: str                              # s1_extract / s2_cross_check / ...
    provider: str                           # deepseek / anthropic
    model: str
    reg_id: Optional[str]
    input_tokens: int
    output_tokens: int
    cached_tokens: int
    cost_usd: float
    prompt_version: str = "unknown"

    def write(self):
        COST_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with COST_LOG_PATH.open("a", encoding="utf-8") as f:
            from dataclasses import asdict
            f.write(json.dumps(asdict(self), ensure_ascii=False) + "\n")


# =============================================================
# Base client
# =============================================================
class LLMClient(ABC):
    """所有 LLM 客户端的接口"""

    provider: str = "unknown"
    default_model: str = "unknown"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url

    @abstractmethod
    def chat(
        self,
        system: str,
        user: str,
        *,
        model: Optional[str] = None,
        max_tokens: int = 8192,
        temperature: float = 0.1,
        enable_cache: bool = False,
    ) -> LLMResponse:
        """同步单次 chat。"""
        ...

    @abstractmethod
    def submit_batch(
        self,
        requests: list[dict],
        *,
        model: Optional[str] = None,
    ) -> str:
        """提交 batch API 任务。返回 batch_id。"""
        ...

    @abstractmethod
    def fetch_batch(self, batch_id: str) -> Optional[list[LLMResponse]]:
        """拉取 batch 结果。None = 还没完成。"""
        ...

    # ---------- Cost calculator (subclass 覆盖) ----------
    def calculate_cost_usd(
        self,
        input_tokens: int,
        output_tokens: int,
        cached_tokens: int = 0,
        model: Optional[str] = None,
    ) -> float:
        """默认实现：按 provider pricing 计算。子类覆盖。"""
        raise NotImplementedError

    # ---------- Logging helper ----------
    def log_cost(
        self,
        stage: str,
        response: LLMResponse,
        reg_id: Optional[str] = None,
        prompt_version: str = "unknown",
    ):
        cost = self.calculate_cost_usd(
            response.input_tokens,
            response.output_tokens,
            response.cached_tokens,
            response.model,
        )
        record = CostRecord(
            ts=datetime.now(timezone.utc).isoformat(),
            stage=stage,
            provider=self.provider,
            model=response.model,
            reg_id=reg_id,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            cached_tokens=response.cached_tokens,
            cost_usd=cost,
            prompt_version=prompt_version,
        )
        record.write()
        return cost
