"""
_resolve_dedupe_conflicts_llm.py — Claude Opus 审阅 16 组 dedupe conflicts，输出处理建议报告

审计报告 P0.2：
- `_dedupe_notes.py` 已把易判的 13 条 _dup 文件扔到 trash
- 16 组 "conflict"（loser body >= 1.5x canonical）需要人工决定
- 这 16 组常见情况：loser 可能是**更完整的版本**或**不同语言版本**，不一定是噪声

本脚本不会直接移动/删除任何文件。只产出：
  `05_Audit/dedupe_resolution_proposal_2026-04-21.md`
用户 review 后再决定是否执行

每组送给 Opus：
  - 两份 FM（全量）
  - 两份 body 开头各 2500 字（控制 token）
  - body 总长度 / confidence

Opus 返回决策 JSON：
  {
    "decision": "keep_canonical | replace_with_dup | keep_both_as_separate | merge | needs_human",
    "reason": "...",
    "diff_summary": "2-3 句话差异",
    "suggested_rename_for_dup": null | "ECE R108 (EN).md",
    "risk": "low | medium | high"
  }
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import httpx
import yaml
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(r"D:\CcVault\99_SystemScripts\auto_reg_index\.env", override=True)

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
AUDIT_DIR = Path(r"D:\CcVault\05_Audit")
CONFLICT_MD = AUDIT_DIR / "dedupe_conflicts_2026-04-21.md"
OUT_MD = AUDIT_DIR / "dedupe_resolution_proposal_2026-04-21.md"

API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
OPUS_MODEL = os.environ.get("CLAUDE_OPUS_MODEL", "claude-opus-4-6").strip()

HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

VALID_DECISIONS = {
    "keep_canonical",        # _dup 扔 trash（默认）
    "replace_with_dup",      # canonical 扔 trash，_dup 顶上
    "keep_both_as_separate", # _dup 重命名保留为独立 note
    "merge",                 # 合并 body/FM 到 canonical
    "needs_human",           # Opus 也拿不准
}
VALID_RISK = {"low", "medium", "high"}

SYSTEM_PROMPT = """你是汽车法规知识库的去重决策专家。
用户有两份 note 文件，它们 reg_id 相同但内容不同，需要你决定如何处理。

⭐ 决策类别（5 选 1）:
- **keep_canonical**: canonical 已足够好，_dup 是它的低质量重复（OCR 更差 / 内容更短 / 无新信息）→ _dup 扔 trash
- **replace_with_dup**: _dup 严格更好（内容更全 / confidence 更高 / 结构更清晰），canonical 可替换
- **keep_both_as_separate**: ⚠️ 常见！两份其实是**不同语言版本**（中译 vs 英文原版）或**不同 PDF 来源**（不同机构转写），都有价值 → _dup 重命名为独立 note 保留
- **merge**: 两份内容互补，建议合并 body 到 canonical（_dup 扔 trash）
- **needs_human**: 情况复杂（冲突信息 / 版本模糊），不敢自动判

⭐ 判定线索:
- 两份 title 一份中文一份英文 → 大概率 keep_both_as_separate
- 两份 source_file 不同 PDF → 先看内容是否互补
- 一份 body 明显是另一份的 OCR 残缺版 → keep_canonical
- _dup body 长度是 canonical 的 3x+ 且包含 canonical 没有的条款 → 倾向 replace_with_dup 或 merge
- confidence 差距悬殊（medium vs high，一份有很多 cross_check_flags 说"原文未提及"）→ 偏向选 confidence 高的那份

⭐ 输出格式（只输出 JSON，不要 markdown）:
{
  "decision": "<上述 5 选 1>",
  "reason": "<50-150 字的判定理由，说明为什么选这个决策>",
  "diff_summary": "<50-100 字客观描述两份的核心差异>",
  "suggested_rename_for_dup": <string or null>,   // 仅 keep_both_as_separate 时必填，如 "ECE R108 (EN).md"
  "risk": "<low | medium | high>"   // 决策的风险：high=容易出错，low=非常确定
}

⭐ 硬性要求:
- 基于我给你的 FM + body 片段客观判断，不要猜测
- 若信息不足 → needs_human，reason 说清需要什么信息
- 不要输出 decision 以外的字段命名
- reason/diff_summary 不要用引号转义
"""


def read_note(p: Path) -> tuple[dict, str, str]:
    """返回 (fm_dict, body_full, body_head)"""
    txt = p.read_text(encoding="utf-8", errors="replace")
    if not txt.startswith("---"):
        return {}, "", ""
    end = txt.find("\n---", 4)
    if end < 0:
        return {}, "", ""
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        fm = {}
    body = txt[end + 4:]
    return fm, body, body[:2500]


def parse_conflicts_md(md_path: Path) -> list[dict]:
    """解析 dedupe_conflicts_2026-04-21.md，提取每组 (canonical_path, dup_path)。"""
    text = md_path.read_text(encoding="utf-8")
    groups = []
    # 按 ## 标题拆
    sections = re.split(r"\n## `([^`]+)`\n", text)
    # sections: [header, reg_id1, block1, reg_id2, block2, ...]
    for i in range(1, len(sections), 2):
        reg_id = sections[i].strip()
        block = sections[i + 1]
        canonical_line = re.search(r"Winner 候选:\s*`([^`]+)`", block)
        loser_lines = re.findall(r"Loser 候选:\s*`([^`]+)`.*?—\s*(.*?)(?:\n|$)", block)
        if not canonical_line or not loser_lines:
            continue
        canonical_rel = canonical_line.group(1).replace("\\", "/")
        for loser_rel, meta in loser_lines:
            loser_rel = loser_rel.replace("\\", "/")
            canonical_p = WIKI / canonical_rel
            loser_p = WIKI / loser_rel
            if not canonical_p.exists() or not loser_p.exists():
                continue
            groups.append({
                "reg_id": reg_id,
                "canonical": canonical_p,
                "dup": loser_p,
                "meta": meta.strip(),
            })
    return groups


def call_opus(
    reg_id: str,
    canonical_fm: dict,
    canonical_body_head: str,
    canonical_body_len: int,
    dup_fm: dict,
    dup_body_head: str,
    dup_body_len: int,
    *,
    client: httpx.Client,
    max_retries: int = 3,
) -> tuple[dict, dict]:
    def fm_str(fm: dict) -> str:
        # 只保留关键字段减少 token
        keys = ["reg_id", "title", "region", "type", "status", "publication_date",
                "version", "source_file", "extracted_by",
                "cross_check_overall_confidence", "scope"]
        out = {k: fm.get(k) for k in keys if fm.get(k) is not None}
        return yaml.safe_dump(out, allow_unicode=True, sort_keys=False)

    user = (
        f"reg_id: {reg_id}\n\n"
        f"=== A: CANONICAL ===\n"
        f"文件: {canonical_fm.get('source_file', '?')}\n"
        f"body 总长度: {canonical_body_len}\n"
        f"FM 关键字段:\n{fm_str(canonical_fm)}\n"
        f"body 前 2500 字:\n---\n{canonical_body_head}\n---\n\n"
        f"=== B: DUP (候选替换 / 保留 / 合并) ===\n"
        f"文件: {dup_fm.get('source_file', '?')}\n"
        f"body 总长度: {dup_body_len}\n"
        f"FM 关键字段:\n{fm_str(dup_fm)}\n"
        f"body 前 2500 字:\n---\n{dup_body_head}\n---\n\n"
        f"请按 schema 输出 JSON。"
    )
    payload = {
        "model": OPUS_MODEL,
        "max_tokens": 800,
        "temperature": 0,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user}],
    }
    last_err = None
    for attempt in range(max_retries):
        try:
            r = client.post(f"{BASE_URL}/v1/messages", json=payload, timeout=120)
            if r.status_code != 200:
                last_err = f"HTTP {r.status_code}: {r.text[:200]}"
                time.sleep(2 ** attempt)
                continue
            j = r.json()
            txt = "".join(c.get("text", "") for c in j.get("content", []))
            usage = j.get("usage", {})
            m = re.search(r"\{[\s\S]*\}", txt)
            if not m:
                last_err = "no JSON in reply"
                continue
            data = json.loads(m.group(0))
            return data, usage
        except Exception as e:
            last_err = str(e)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Opus failed: {last_err}")


def validate(data: dict) -> dict | None:
    d = (data.get("decision") or "").strip()
    if d not in VALID_DECISIONS:
        return None
    risk = (data.get("risk") or "medium").strip().lower()
    if risk not in VALID_RISK:
        risk = "medium"
    out = {
        "decision": d,
        "reason": (data.get("reason") or "").strip(),
        "diff_summary": (data.get("diff_summary") or "").strip(),
        "suggested_rename_for_dup": data.get("suggested_rename_for_dup") or None,
        "risk": risk,
    }
    # keep_both_as_separate 必须有 rename 建议
    if d == "keep_both_as_separate" and not out["suggested_rename_for_dup"]:
        # 缺失 rename → 降级 needs_human
        out["decision"] = "needs_human"
        out["reason"] += "\n（Opus 说 keep_both 但未给 rename，降级 needs_human）"
    return out


def process_group(group: dict, client: httpx.Client) -> dict:
    canonical_fm, canonical_body, canonical_head = read_note(group["canonical"])
    dup_fm, dup_body, dup_head = read_note(group["dup"])
    try:
        raw, usage = call_opus(
            group["reg_id"],
            canonical_fm, canonical_head, len(canonical_body),
            dup_fm, dup_head, len(dup_body),
            client=client,
        )
    except Exception as e:
        return {**group, "status": "api_error", "err": str(e)}
    v = validate(raw)
    if not v:
        return {**group, "status": "bad_output", "raw": raw, "usage": usage}
    return {
        **group,
        "status": "ok",
        "canonical_body_len": len(canonical_body),
        "dup_body_len": len(dup_body),
        "canonical_conf": canonical_fm.get("cross_check_overall_confidence"),
        "dup_conf": dup_fm.get("cross_check_overall_confidence"),
        **v,
        "usage": usage,
    }


DECISION_LABELS = {
    "keep_canonical": "🗑️ 删 _dup（canonical 足够）",
    "replace_with_dup": "🔄 _dup 替换 canonical",
    "keep_both_as_separate": "📑 两份都留（_dup 重命名）",
    "merge": "🔀 合并 _dup 到 canonical",
    "needs_human": "❓ 需要人工判断",
}
RISK_ICONS = {"low": "🟢", "medium": "🟡", "high": "🔴"}


def render_report(results: list[dict], total_cost: float) -> str:
    today = date.today().isoformat()
    # 按 decision 分组
    by_decision: dict[str, list] = {}
    for r in results:
        d = r.get("decision", "error")
        by_decision.setdefault(d, []).append(r)

    lines = [
        "---",
        "type: audit_report",
        f"created: {today}",
        "category: dedupe_resolution_proposal",
        "severity: medium",
        "status: needs_human_confirm",
        "tags: [audit/dedupe, audit/proposal, audit/llm_review]",
        "---",
        "",
        "# Dedupe 冲突处理建议（Claude Opus 审阅）",
        "",
        f"> 从 `dedupe_conflicts_2026-04-21.md` 的 {len(results)} 组冲突里，Opus 4.6 逐组审阅两份 FM + body 给出处理建议。",
        f"> **本报告不执行任何动作**，仅供人工快速决策。成本 ${total_cost:.2f}。",
        "",
        "## 决策汇总",
        "",
        "| 决策 | 组数 | 说明 |",
        "| --- | ---: | --- |",
    ]
    for d in ["keep_canonical", "replace_with_dup", "keep_both_as_separate", "merge", "needs_human"]:
        cnt = len(by_decision.get(d, []))
        lines.append(f"| {DECISION_LABELS[d]} | {cnt} | |")
    err_cnt = sum(1 for r in results if r.get("status") != "ok")
    if err_cnt:
        lines.append(f"| ⚠️ API error / bad output | {err_cnt} | 需重跑 |")
    lines.append("")

    lines.append("## 操作说明")
    lines.append("")
    lines.append("1. 逐条读 Opus 的 reason + diff_summary")
    lines.append("2. 同意 → 按 decision 执行（手工或写脚本）")
    lines.append("3. 不同意 → 标注后交给人工流程（`/process_audits`）")
    lines.append("")

    # 按决策展开
    for d in ["keep_canonical", "replace_with_dup", "keep_both_as_separate", "merge", "needs_human"]:
        items = by_decision.get(d, [])
        if not items:
            continue
        lines.append(f"## {DECISION_LABELS[d]}  · {len(items)} 组")
        lines.append("")
        for r in items:
            risk_icon = RISK_ICONS.get(r.get("risk", "medium"), "🟡")
            lines.append(f"### `{r['reg_id']}` {risk_icon}")
            lines.append("")
            lines.append(f"- **canonical**：`{r['canonical'].relative_to(WIKI)}` "
                         f"(body={r.get('canonical_body_len','?')}, conf={r.get('canonical_conf','?')})")
            lines.append(f"- **dup**：`{r['dup'].relative_to(WIKI)}` "
                         f"(body={r.get('dup_body_len','?')}, conf={r.get('dup_conf','?')})")
            lines.append(f"- **判定**：{DECISION_LABELS[d]} · 风险 {r.get('risk')}")
            lines.append(f"- **差异摘要**：{r.get('diff_summary', '')}")
            lines.append(f"- **理由**：{r.get('reason', '')}")
            if d == "keep_both_as_separate" and r.get("suggested_rename_for_dup"):
                lines.append(f"- **建议重命名**：`{r['suggested_rename_for_dup']}`")
            lines.append("")

    # 错误
    errors = [r for r in results if r.get("status") != "ok"]
    if errors:
        lines.append("## ⚠️ 处理异常")
        lines.append("")
        for r in errors:
            lines.append(f"- `{r['reg_id']}`: status={r.get('status')}, err={r.get('err', '?')[:200]}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*由 `_resolve_dedupe_conflicts_llm.py` 生成 · {today} · 模型: {OPUS_MODEL}*")

    return "\n".join(lines)


def main() -> int:
    groups = parse_conflicts_md(CONFLICT_MD)
    print(f"解析到 {len(groups)} 组 conflicts")
    print("-" * 60)
    print(f"模式: 生成报告（不执行任何写操作）")
    print(f"model: {OPUS_MODEL}")
    print("-" * 60)

    results = []
    total_in = total_out = 0
    with httpx.Client(headers=HEADERS, timeout=120) as client:
        with ThreadPoolExecutor(max_workers=3) as ex:
            futs = {ex.submit(process_group, g, client): g for g in groups}
            for i, fut in enumerate(as_completed(futs), 1):
                g = futs[fut]
                try:
                    r = fut.result()
                except Exception as e:
                    r = {**g, "status": "exception", "err": str(e)}
                results.append(r)
                u = r.get("usage") or {}
                total_in += u.get("input_tokens") or 0
                total_out += u.get("output_tokens") or 0
                d = r.get("decision") or r.get("status")
                risk = r.get("risk", "?")
                print(f"[{i:>2}/{len(groups)}] {r['reg_id']:<25} decision={d:<25} risk={risk}")

    total_cost = total_in * 15 / 1e6 + total_out * 75 / 1e6
    print("-" * 60)
    print(f"Token: input={total_in:,} output={total_out:,}")
    print(f"成本: ${total_cost:.2f}")

    # 写报告
    OUT_MD.write_text(render_report(results, total_cost), encoding="utf-8")
    print(f"\n报告已写入: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
