"""
Prompt 加载器

从 prompts/ 下的 .md 文件读取 SYSTEM + USER TEMPLATE。
Prompt 文件格式（见 prompts/extract.md）：

    ## SYSTEM

    ```
    <system prompt 原文>
    ```

    ## USER TEMPLATE

    ```
    <user template，含 {placeholder}>
    ```
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


@dataclass
class PromptSpec:
    name: str
    system: str
    user_template: str
    version: str = "unknown"

    def render_user(self, **kwargs) -> str:
        """Fill {placeholder} in user_template"""
        return self.user_template.format(**kwargs)


@lru_cache(maxsize=32)
def load_prompt(name: str) -> PromptSpec:
    """
    Load prompt by name (without .md suffix).
    name='extract' → prompts/extract.md
    """
    path = PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {path}")

    content = path.read_text(encoding="utf-8")

    system = _extract_fenced_block(content, header="## SYSTEM")
    user = _extract_fenced_block(content, header="## USER TEMPLATE")

    if not system or not user:
        raise ValueError(
            f"Prompt {name} must have '## SYSTEM' and '## USER TEMPLATE' "
            f"sections each containing a fenced code block."
        )

    # Extract version from any YAML frontmatter or a "prompt_version:" line
    version = _extract_version(content)

    return PromptSpec(
        name=name,
        system=system,
        user_template=user,
        version=version,
    )


def _extract_fenced_block(content: str, *, header: str) -> str:
    """Find `header` then the next ``` block after it."""
    header_idx = content.find(header)
    if header_idx == -1:
        return ""
    # Find the next ``` after header
    fence_open = content.find("```", header_idx)
    if fence_open == -1:
        return ""
    # Skip the fence line
    nl = content.find("\n", fence_open)
    fence_close = content.find("```", nl + 1)
    if fence_close == -1:
        return ""
    return content[nl + 1:fence_close].strip()


def _extract_version(content: str) -> str:
    m = re.search(r"prompt_version:\s*[\"']?([\d.]+)[\"']?", content)
    if m:
        return m.group(1)
    # Also look for "version: 0.1" on its own line (Day 1 schema style)
    m = re.search(r"^version:\s*[\"']?([\d.]+)[\"']?\s*$", content, re.MULTILINE)
    if m:
        return m.group(1)
    return "unknown"
