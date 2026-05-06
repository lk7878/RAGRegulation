"""CcVault ReAct Agent 层。

将现有脚本（_semantic_search, _graphrag_search, _build_graph 等）封装为
LangChain @tool，给 LLM 装上自主检索 + 统计 + 审计能力。

入口：
    python _agent_chat.py "vault 里有多少条中国法规"
    python _agent_chat.py              # REPL 对话模式
"""
