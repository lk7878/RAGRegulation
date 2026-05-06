"""LangGraph ReAct Agent 装配。

提供两个入口：
  - build_agent(provider='deepseek'|'claude') -> Runnable
  - run_once(agent, question, history=[]) -> dict  （单次问答）

消息历史用 list[(role, content)] 简单表示，role ∈ {human, ai, system}。
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, Optional

from dotenv import load_dotenv

# 加载 auto_reg_index/.env
_ENV_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(_ENV_PATH, override=True)


SYSTEM_PROMPT = """\
你是 CcVault 汽车法规知识库的 AI 助手。你的任务是**基于工具返回的真实数据**回答用户问题。

=== 知识库背景 ===
- CcVault 是一个包含 ~1429 条汽车法规 notes 的 Obsidian vault
- 区域覆盖：cn (GB/GB·T 约 460 条) / ece (UN ECE 959 条) / eu / us / jp / kr / iso / sae
- 37 个人工 topic 主题（brakes / lighting_signaling / ev_battery_safety 等）
- 33 个 GraphRAG 社区（Louvain 自动聚类 + LLM 综述）
- 62 条跨区等价映射

=== 工具使用原则 ===
1. **永远先调用至少一个 tool 再回答**，除非是闲聊或确认指令
2. **统计类问题**（"多少条""哪些最多"）→ describe_vault / count_regulations / stats_by_field
3. **检索类问题**（找某条法规）→ search_regulations_bm25
4. **领域全景问题**（"XX 领域的整体格局"）→ search_communities_graphrag
5. **版本演化**（"XX 最新是哪版"）→ get_supersession_chain
6. **跨区对标**（"XX 对应国外的什么"）→ get_equivalence
7. **深入读某条**（已知 reg_id）→ read_regulation
8. **审计类**（"哪些需要复核"）→ list_needs_review

=== 回答规范 ===
- 回答用中文
- 引用具体 reg_id（如 "GB 4785-2019"），不要编造
- 如果 tool 返回 "[not found]" 或 "No results"，诚实告知用户
- 不要在回答中直接复述工具返回的全部文本，要提炼结论
- 复杂问题可以串联多个 tool（比如先 search_regulations_bm25 找到 reg_id，再 get_supersession_chain）
- 回答结尾可以引用 reg_id 列表作为"依据"（类似学术论文参考文献）
"""


def build_model(
    provider: Literal["deepseek", "claude"] = "deepseek",
    temperature: float = 0,
):
    """构造 LangChain ChatModel。"""
    if provider == "deepseek":
        from langchain_openai import ChatOpenAI
        api_key = os.getenv("DEEPSEEK_API_KEY", "")
        base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        if not api_key:
            raise RuntimeError("DEEPSEEK_API_KEY 未在 auto_reg_index/.env 中设置")
        return ChatOpenAI(
            model="deepseek-chat",
            api_key=api_key,
            base_url=base_url,
            temperature=temperature,
        )

    if provider == "claude":
        try:
            from langchain_anthropic import ChatAnthropic
        except ImportError:
            raise RuntimeError(
                "需要安装 langchain-anthropic: "
                ".venv/Scripts/python.exe -m pip install langchain-anthropic"
            )
        api_key = os.getenv("ANTHROPIC_API_KEY", "")
        base_url = os.getenv("ANTHROPIC_BASE_URL")  # 可选
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY 未在 auto_reg_index/.env 中设置")
        kwargs = {
            "model": "claude-sonnet-4-20250514",
            "api_key": api_key,
            "temperature": temperature,
        }
        if base_url:
            kwargs["base_url"] = base_url
        return ChatAnthropic(**kwargs)

    raise ValueError(f"Unknown provider: {provider}")


def build_agent(
    provider: Literal["deepseek", "claude"] = "deepseek",
    temperature: float = 0,
):
    """构建 ReAct agent。返回 Runnable。"""
    from langchain.agents import create_agent
    from .tools import ALL_TOOLS

    model = build_model(provider, temperature)
    agent = create_agent(
        model=model,
        tools=ALL_TOOLS,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent


def run_once(
    agent,
    question: str,
    history: Optional[list[tuple[str, str]]] = None,
) -> dict:
    """单次问答。history 是 (role, content) 列表，role ∈ human / ai。

    返回 dict 含：answer / tool_calls（调用轨迹） / raw_messages。
    """
    history = history or []
    messages = list(history) + [("human", question)]

    result = agent.invoke({"messages": messages})
    all_msgs = result.get("messages", [])

    # 抽取 tool_calls（用于 verbose 调试）
    tool_calls = []
    for m in all_msgs:
        role = getattr(m, "type", None) or m.__class__.__name__.lower()
        # AIMessage 里可能带 tool_calls
        tc = getattr(m, "tool_calls", None)
        if tc:
            for call in tc:
                tool_calls.append({
                    "name": call.get("name"),
                    "args": call.get("args"),
                })

    # 最后一条 AIMessage 即答案
    final = all_msgs[-1] if all_msgs else None
    answer = getattr(final, "content", "") if final else ""

    return {
        "answer": answer,
        "tool_calls": tool_calls,
        "raw_messages": all_msgs,
    }
