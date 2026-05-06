"""
_priority_selector.py — 从 manifest + CcVault notes 里决定今天该重跑哪些 PDF

优先级（高 → 低）：
  P1. 28 条 body<1500 的 data-floor notes（P1.3 修不了的）
  P2. 35 条仍为 low confidence（Opus 判 keep 的那 6 条 + 28 条 data floor 里的）
  P3. body 无日期线索但被 P1.4 判了 no_date 的
  P4. ECE amendments 含 "Annex" 和表格标记的（嵌套表格多）
  P5. GB 制动 / 碰撞 / 排放类（嵌套表格密集）
  P6. 其余常规文档

按 content_hash 关联 manifest.path → 00_Raw 目录下的实际 PDF 文件
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
RAW_ROOT = Path(r"D:\CcVault\00_Raw\标准库")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")

FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")


@dataclass
class PdfCandidate:
    content_hash: str
    pdf_path: Path           # 绝对路径
    reg_id: str | None
    region: str | None
    priority: int            # 1 = 最高
    reason: str              # 为什么被挑
    note_path: Path | None   # 对应的 CcVault note（若有）
    body_len: int            # 当前 body 长度
    has_tables_or_formulas_hint: bool  # body 是否暗示有表格/公式
    size_mb: float


# body 里可能出现"表 N"、"Annex"、"公式 N"、"Table" 等的关键词
TABLE_HINT_RE = re.compile(r"(表\s*\d+|Table\s+\d+|Annex|附录|Appendix|公式|Formula)", re.IGNORECASE)


def load_manifest() -> dict[str, dict]:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return m["records"]


def scan_notes_metadata() -> dict[str, dict]:
    """扫 CcVault 所有 notes，按 content_hash（_ocr_hash）或 source_pdf 回查。"""
    notes_by_hash: dict[str, dict] = {}
    notes_by_pdf_path: dict[str, dict] = {}
    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        m = FM_RE.match(txt)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        body = txt[m.end():]
        info = {
            "note_path": p,
            "body_len": len(body),
            "body_head": body[:3000],
            "conf": (fm.get("cross_check_overall_confidence") or "").lower(),
            "pub_date": fm.get("publication_date"),
            "reg_id": fm.get("reg_id"),
            "region": fm.get("region"),
            "source_pdf": fm.get("source_pdf") or fm.get("source_file"),
            "has_tables_or_formulas_hint": bool(TABLE_HINT_RE.search(body[:3000])),
        }
        # content_hash 字段 CcVault 没存过；用 source_pdf 回查 manifest
        sp = info["source_pdf"]
        if sp:
            # normalize slashes
            sp_norm = str(sp).replace("\\", "/")
            notes_by_pdf_path[sp_norm] = info
    return notes_by_pdf_path


def build_candidates() -> list[PdfCandidate]:
    records = load_manifest()
    notes_by_path = scan_notes_metadata()
    candidates: list[PdfCandidate] = []

    for chash, rec in records.items():
        if rec.get("state") != "written":
            continue
        raw_rel = rec.get("path")
        if not raw_rel or not raw_rel.lower().endswith(".pdf"):
            continue
        pdf_abs = RAW_ROOT / raw_rel.replace("/", "\\")
        if not pdf_abs.exists():
            # 备用查找
            pdf_abs = RAW_ROOT / raw_rel
            if not pdf_abs.exists():
                continue

        note_info = notes_by_path.get(raw_rel.replace("\\", "/"))
        body_len = note_info.get("body_len", 0) if note_info else 0
        has_hint = note_info.get("has_tables_or_formulas_hint", False) if note_info else False
        conf = note_info.get("conf") if note_info else None
        has_pub = bool(note_info and note_info.get("pub_date"))
        reg_id = rec.get("reg_id") or (note_info or {}).get("reg_id")
        region = rec.get("region") or (note_info or {}).get("region")

        # 分级
        priority, reason = _assign_priority(body_len, conf, has_pub, has_hint, reg_id, region, pdf_abs)

        candidates.append(PdfCandidate(
            content_hash=chash,
            pdf_path=pdf_abs,
            reg_id=reg_id,
            region=region,
            priority=priority,
            reason=reason,
            note_path=note_info.get("note_path") if note_info else None,
            body_len=body_len,
            has_tables_or_formulas_hint=has_hint,
            size_mb=pdf_abs.stat().st_size / 1024 / 1024 if pdf_abs.exists() else 0.0,
        ))

    candidates.sort(key=lambda c: (c.priority, -c.body_len))
    return candidates


def _assign_priority(body_len: int, conf: str | None, has_pub: bool,
                     has_hint: bool, reg_id: str | None, region: str | None,
                     pdf_path: Path) -> tuple[int, str]:
    # P1: data floor（body < 1500 的 notes，Opus 救不了）
    if body_len and body_len < 1500:
        return 1, f"data_floor (body={body_len})"
    # P2: 仍 low conf
    if conf == "low":
        return 2, f"low_conf (body={body_len})"
    # P3: 缺 pubdate 且非 overview
    if not has_pub and reg_id and not any(x in reg_id.upper() for x in ("OVERVIEW", "3CV", "FMVSS", "ADR")):
        return 3, "missing_pubdate"
    # P4: body 含表格/公式关键词且是 amendment/附录类
    if has_hint:
        return 4, "tables/formulas_hint"
    # P5: 大概率含表格的领域（制动 / 碰撞 / 排放）
    if reg_id:
        rid = reg_id.upper()
        if any(kw in rid for kw in ["R13", "R94", "R95", "R137", "GB 13094", "GB 21670",
                                     "GB 7258", "GB 18352", "GB 14248"]):
            return 5, "dense_table_domain"
    # P6: 默认
    return 6, "default"


def filter_by_page_budget(candidates: list[PdfCandidate],
                          target_pages: int,
                          already_done: set[str],
                          pages_per_mb: float = 30.0) -> list[PdfCandidate]:
    """按 content_hash 跳过已做的，粗估页数累加到预算为止。"""
    picked: list[PdfCandidate] = []
    used_pages = 0
    for c in candidates:
        if c.content_hash in already_done:
            continue
        est_pages = max(1, int(c.size_mb * pages_per_mb))
        if used_pages + est_pages > target_pages and picked:
            break
        picked.append(c)
        used_pages += est_pages
    return picked


if __name__ == "__main__":
    cands = build_candidates()
    from collections import Counter
    cnt = Counter(c.priority for c in cands)
    print(f"总候选: {len(cands)}")
    print(f"优先级分布: {dict(sorted(cnt.items()))}")
    print("\nTop 15 最高优先级:")
    for c in cands[:15]:
        print(f"  P{c.priority} [{c.reason:<28}] {c.reg_id or '?':<30} "
              f"body={c.body_len:>6} size={c.size_mb:.1f}MB  {c.pdf_path.name}")
