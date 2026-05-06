"""
_split_eu_2018_858_llm.py — 用 Opus 拆分 (EU) 2018 858_dup1 (多法规汇编) 成多个独立 note

策略：
  1. 把 _dup1 整个 body 给 Opus（~42K chars ≈ 14K tokens）
  2. Opus 输出 JSON 数组：每个主 reg_id 一份 (reg_id / type / title / scope / body_md / weight)
  3. 过滤 weight>=5 的（避免无意义碎片）+ reg_id 不能与已有 vault 冲突
  4. 写入 01_Wiki/regulations/eu/<reg_id>.md
  5. 原 _dup1 移到 trash_dups/2026-04-25/

成本预估：~$0.40 一次（input 14K + output ~10K）
"""
from __future__ import annotations
import json
import os
import re
import shutil
import sys
import time
from datetime import date
from pathlib import Path

import httpx
import yaml
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(r"D:\CcVault\99_SystemScripts\auto_reg_index\.env", override=True)

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
EU_DIR = WIKI / "eu"
DUP1_PATH = EU_DIR / "(EU) 2018 858_dup1.md"
TRASH_DIR = Path(r"D:\CcVault\05_Audit\trash_dups\2026-04-25")
LOG_PATH = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.stage3\split_eu_2018_858.json")

API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
OPUS_MODEL = os.environ.get("CLAUDE_OPUS_MODEL", "claude-opus-4-6").strip()

HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

SYSTEM_PROMPT = """你是欧盟汽车法规知识库专家。用户给你一份混乱的中文文档，FM 标记 reg_id=(EU) 2018/858，但实际含 30+ 不同 EU 法规内容。
你的任务：识别其中 5-8 个**最显著**的法规（content depth 最大者），为每个生成独立 note 内容。

⭐ 法规权重 (weight) 标准：
- 10：文档主体内容，可单独成为完整 note（>2000 字相关内容）
- 7-9：有专门的章节描述但不及主体（500-2000 字）
- 5-6：有具体条款被引用（200-500 字）
- 1-4：仅 1-2 处提及（不要拆分）

⭐ 输出格式（只输出 JSON 数组，不要其他文字）:
[
  {
    "reg_id": "(EU) 2019/2144",                  // 标准格式：(EU) 年份/号
    "type": "regulation",                          // regulation | directive | version | amendment
    "title": "<简洁中文标题，复述法规主题>",
    "scope": "<2-3 句中文简介，说明该法规适用范围>",
    "body_md": "<从原文档抽取相关段落，按层级整理为 markdown，可加 ## 小标题>",
    "publication_date": "YYYY-MM-DD" | null,      // 若原文有提及
    "status": "active" | "superseded" | "unknown",
    "weight": 1-10,                                // 上述权重
    "supersedes": ["(EU) ..."] | [],               // 若该法规取代了其他法规
    "references_other": ["(EU) ..."]               // 该法规交叉引用的其他法规
  },
  ...
]

⭐ 硬性要求:
- reg_id 必须从原文档实际出现的法规中提取，不要凭空添加
- 只提取 weight >= 5 的法规（不要拆分 weight 1-4 的零星引用）
- body_md 必须从原文档抽取，可适度合并段落但不要凭空创造
- 不要包含原文档中关于 (EU) 2018/858 框架法规本身的介绍（保留给 canonical）
- 输出必须是合法 JSON 数组（外层 [...]），无 markdown 围栏，无注释
- 中文标题、scope 用中文，body_md 保持原文档语言（多数为中文）
"""


def call_opus(body_text: str, client: httpx.Client) -> tuple[list, dict]:
    user_msg = (
        f"以下是需要拆分的 _dup1 文档 body（{len(body_text)} 字符）：\n\n"
        f"```markdown\n{body_text}\n```\n\n"
        f"按 SYSTEM 指示提取 5-8 个最显著的法规，输出 JSON 数组。"
    )
    last_err = ""
    for attempt in range(5):
        try:
            r = client.post(
                BASE_URL + "/v1/messages",
                headers=HEADERS,
                json={
                    "model": OPUS_MODEL,
                    "max_tokens": 16000,
                    "system": SYSTEM_PROMPT,
                    "messages": [{"role": "user", "content": user_msg}],
                },
                timeout=300,
            )
            if r.status_code == 429:
                wait = 30 * (attempt + 1)  # 30s / 60s / 90s / ...
                print(f"  [429] 限流，等 {wait}s 后重试 (attempt {attempt+1}/5)")
                time.sleep(wait)
                last_err = "429"
                continue
            r.raise_for_status()
            j = r.json()
            txt = "".join(c.get("text", "") for c in j.get("content", []))
            usage = j.get("usage", {})
            # 抽 JSON 数组
            m = re.search(r"\[\s*\{[\s\S]*\}\s*\]", txt)
            if not m:
                last_err = f"no JSON array in reply: {txt[:200]}"
                time.sleep(5)
                continue
            arr = json.loads(m.group(0))
            return arr, usage
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            wait = 5 * (2 ** attempt)
            print(f"  [{type(e).__name__}] {e}, 等 {wait}s 重试")
            time.sleep(wait)
    raise RuntimeError(f"Opus failed: {last_err}")


def safe_filename(reg_id: str) -> str:
    """(EU) 2019/2144 → '(EU) 2019 2144.md'  (复合 vault 已有命名风格)"""
    s = reg_id.replace("/", " ").strip()
    return f"{s}.md"


def render_note(item: dict) -> str:
    today = date.today().isoformat()
    fm = {
        "reg_id": item["reg_id"],
        "region": "eu",
        "type": f"type/{item.get('type', 'regulation')}",
        "title": item.get("title") or "",
        "scope": item.get("scope") or "",
        "publication_date": item.get("publication_date"),
        "status": item.get("status", "unknown"),
        "language": "zh",  # body 是中文 (从原文档继承)
        "source_pdf": "国外法规\\1.欧盟\\（欧标）欧洲联盟汽车技术指令.pdf",
        "supersedes": item.get("supersedes", []),
        "tags": [f"region/eu", f"topic/regulation"],
        # 标记来源
        "_split_source": "(EU) 2018/858_dup1",
        "_split_at": today,
        "_split_method": "stage3_llm_opus",
        "_split_weight": item.get("weight"),
    }
    fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    body = item.get("body_md", "").strip()
    return f"---\n{fm_str}---\n\n{body}\n"


def main() -> int:
    if not DUP1_PATH.exists():
        print(f"[ERROR] _dup1 不存在: {DUP1_PATH}")
        return 1

    txt = DUP1_PATH.read_text(encoding="utf-8")
    mo = FM_RE.match(txt)
    body = txt[mo.end():] if mo else txt
    print(f"_dup1 body 长度: {len(body)} 字符")

    print(f"\n调用 Opus ({OPUS_MODEL})...")
    with httpx.Client() as client:
        items, usage = call_opus(body, client)
    print(f"Opus 返回 {len(items)} 个 reg_id 提案")
    print(f"Token usage: input={usage.get('input_tokens',0)} output={usage.get('output_tokens',0)}")

    # 估算成本
    in_t = usage.get("input_tokens", 0)
    out_t = usage.get("output_tokens", 0)
    cost = in_t / 1e6 * 5.0 + out_t / 1e6 * 25.0
    print(f"预计成本: ${cost:.3f}")

    # 写日志
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(
        json.dumps({"items": items, "usage": usage, "cost_usd": cost},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n=== Opus 提案预览 ===")
    for it in items:
        rid = it.get("reg_id", "?")
        title = (it.get("title") or "")[:50]
        weight = it.get("weight", "?")
        body_len = len(it.get("body_md", ""))
        print(f"  · {rid:<25}  weight={weight}  body={body_len:>6}  {title}")

    # 过滤 + 校验
    valid = []
    for it in items:
        rid = (it.get("reg_id") or "").strip()
        if not re.match(r"\(EU\)\s*\d{4}/\d+", rid):
            print(f"  ✗ 跳过 {rid}: reg_id 格式不符")
            continue
        if it.get("weight", 0) < 5:
            print(f"  ✗ 跳过 {rid}: weight={it.get('weight')} < 5")
            continue
        if not it.get("body_md", "").strip():
            print(f"  ✗ 跳过 {rid}: body 为空")
            continue
        # 检查 vault 里是否已有该 reg_id
        target = EU_DIR / safe_filename(rid)
        if target.exists():
            print(f"  ✗ 跳过 {rid}: 文件已存在 {target.name}")
            continue
        valid.append(it)

    print(f"\n通过校验的 reg_id: {len(valid)}")
    if not valid:
        print("[ABORT] 无有效拆分项")
        return 1

    print(f"\n=== 即将写入的 note ===")
    for it in valid:
        target = EU_DIR / safe_filename(it["reg_id"])
        body_len = len(it.get("body_md", ""))
        print(f"  → {target.name}  body={body_len}")

    print(f"\n[DRY-RUN] 已生成日志 {LOG_PATH}")
    print(f"如果 OK，运行 'python _split_eu_2018_858_llm.py --apply' 写入")
    if "--apply" not in sys.argv:
        return 0

    # 实际写入
    written = []
    for it in valid:
        target = EU_DIR / safe_filename(it["reg_id"])
        target.write_text(render_note(it), encoding="utf-8")
        written.append(target.name)
        print(f"  ✓ {target.name}")

    # 移动 _dup1 到 trash
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    trash_target = TRASH_DIR / DUP1_PATH.name
    shutil.move(str(DUP1_PATH), str(trash_target))
    print(f"\n[DONE] 写入 {len(written)} 个新 note · _dup1 已移到 {trash_target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
