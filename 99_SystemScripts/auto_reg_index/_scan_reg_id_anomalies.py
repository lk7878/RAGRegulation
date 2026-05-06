"""一次性扫描脚本 - 找出 vault 中所有 reg_id 命名异常，分类汇总。

分类：
  A. OCR 残留：reg_id 长得像 UN 文件名 stem（R013Hr4am1e / R013r8am5e）
  B. 重复：同一 reg_id 存在多条 note
  C. H 家族 reg_id 与 title 矛盾：reg_id 无 H 但 title 说 "passenger cars"
  D. 异名前缀：UN R... / UNECE R... / R...-H 等非标准命名
  E. 点号 / 空格异常：ECE R13 Rev.8 / ECE R-13
  F. 数字零前缀：ECE R008 / ECE R094（应该是 R8 / R94）
  G. reg_id 与文件内容不符（title 指向别的法规）

用法：
    python _scan_reg_id_anomalies.py
    python _scan_reg_id_anomalies.py --category A    # 只看某一类
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

VAULT = Path("D:/CcVault")
WIKI = VAULT / "01_Wiki" / "regulations"


# ---------------------------------------------------------------------------
# 异常检测规则
# ---------------------------------------------------------------------------

# A. OCR 残留：像 UN 文件名 stem 的 reg_id
RE_OCR_STEM = re.compile(r"^R\d{2,4}[Hh]?(?:r\d+)?(?:am\d+)?[a-z]?$", re.IGNORECASE)

# D.1 异名前缀：UN R / UNECE R / UN-R
RE_UN_PREFIX = re.compile(r"^(?:UN|UNECE)[-\s]?R\d", re.IGNORECASE)
# D.2 破折号分隔 H：R13-H
RE_DASH_H = re.compile(r"^(?:ECE\s+)?R\d+[-\s]+H\b", re.IGNORECASE)

# E. 点号 / 空格异常
RE_WEIRD_DOT = re.compile(r"Rev\.\s*\d|R-\d|R\s+\d+\s+-\s+\d+", re.IGNORECASE)

# F. 数字零前缀
RE_LEADING_ZERO = re.compile(r"^ECE\s+R0\d", re.IGNORECASE)

# C. H 家族矛盾：title 含 "passenger cars" 但 reg_id 无 H
RE_TITLE_PASSENGER = re.compile(r"passenger\s+cars|乘用车", re.IGNORECASE)


# ---------------------------------------------------------------------------
# FM 解析
# ---------------------------------------------------------------------------

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_note(path: Path) -> tuple[dict, str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}, ""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, m.group(2)


# ---------------------------------------------------------------------------
# 扫描
# ---------------------------------------------------------------------------

def scan(filter_category: str | None = None) -> None:
    notes: list[dict] = []
    print(f"[scan] 扫描 {WIKI}...", file=sys.stderr)
    for p in WIKI.rglob("*.md"):
        fm, _ = parse_note(p)
        if not fm:
            continue
        notes.append({
            "path": str(p),
            "reg_id": str(fm.get("reg_id") or ""),
            "title": str(fm.get("title") or ""),
            "title_en": str(fm.get("title_en") or ""),
            "region": str(fm.get("region") or ""),
            "confidence": str(fm.get("cross_check_overall_confidence") or ""),
        })

    print(f"[scan] 共 {len(notes)} 条 notes", file=sys.stderr)

    # 分类检测
    results: dict[str, list[dict]] = defaultdict(list)

    # A. OCR 残留
    for n in notes:
        if RE_OCR_STEM.match(n["reg_id"]):
            results["A_OCR_stem"].append(n)

    # B. 重复 reg_id
    by_regid: dict[str, list[dict]] = defaultdict(list)
    for n in notes:
        if n["reg_id"]:
            by_regid[n["reg_id"]].append(n)
    for rid, items in by_regid.items():
        if len(items) > 1:
            results["B_duplicate"].extend(items)

    # C. reg_id 无 H 但 title 说 passenger cars（R13/R13H 混淆类）
    for n in notes:
        rid = n["reg_id"]
        title = n["title"] + " " + n["title_en"]
        # 只对 ECE R13/R90/R123/R140 等可能有 H 变体的数字法规检查
        m = re.match(r"^ECE\s+R(\d+)(?![H\d])", rid, re.IGNORECASE)
        if m and RE_TITLE_PASSENGER.search(title):
            # ECE R13 无 H 后缀，但 title 说 passenger cars → 疑似应为 R13H
            num = int(m.group(1))
            # 只对已知/可能的 H 变体告警
            if num in (13, 90, 123, 140):
                results["C_H_mismatch"].append(n)

    # D. 异名前缀
    for n in notes:
        rid = n["reg_id"]
        if RE_UN_PREFIX.match(rid) or RE_DASH_H.match(rid):
            results["D_alias_prefix"].append(n)

    # E. 点号 / 空格异常
    for n in notes:
        if RE_WEIRD_DOT.search(n["reg_id"]):
            results["E_weird_char"].append(n)

    # F. 数字零前缀
    for n in notes:
        if RE_LEADING_ZERO.match(n["reg_id"]):
            results["F_leading_zero"].append(n)

    # 输出
    categories = {
        "A_OCR_stem":       "A. OCR 残留（长得像 UN 文件名 stem）",
        "B_duplicate":      "B. 重复 reg_id（同一 reg_id ≥2 条 notes）",
        "C_H_mismatch":     "C. R13/R90 等无 H 后缀但 title 说乘用车（疑似应为 R13H/R90H）",
        "D_alias_prefix":   "D. 异名前缀（UN R / UN-R / R13-H 等）",
        "E_weird_char":     "E. 点号/破折号异常（Rev.8 / R-13）",
        "F_leading_zero":   "F. 数字零前缀（ECE R008 应为 ECE R8）",
    }

    print()
    print("=" * 80)
    print(f"{'类别':<55} {'命中':>6}")
    print("-" * 80)
    for key, label in categories.items():
        cnt = len(results.get(key, []))
        mark = "  <-- " if cnt > 0 else ""
        print(f"{label:<55} {cnt:>6}{mark}")
    print()

    if filter_category:
        # 只打印指定类别
        key = next((k for k in categories if k.startswith(filter_category.upper())), None)
        if not key:
            print(f"[error] 未知类别: {filter_category}")
            return
        _print_category(key, categories[key], results.get(key, []))
    else:
        for key, label in categories.items():
            items = results.get(key, [])
            if items:
                _print_category(key, label, items, preview=12)


def _print_category(key: str, label: str, items: list[dict], preview: int = 0) -> None:
    print(f"\n{'=' * 80}")
    print(f"## {label}")
    print(f"命中数: {len(items)}")
    print("-" * 80)

    # B 类按 reg_id 分组
    if key == "B_duplicate":
        by_rid: dict[str, list[dict]] = defaultdict(list)
        for n in items:
            by_rid[n["reg_id"]].append(n)
        for rid in sorted(by_rid.keys())[: preview or len(by_rid)]:
            group = by_rid[rid]
            print(f"\n  reg_id = {rid!r} ({len(group)} 条):")
            for n in group:
                title = (n["title"] or n["title_en"])[:45]
                print(f"    [{n['confidence']:<7}] {title}")
                print(f"      path: {n['path']}")
        return

    # 其他类按顺序打
    limit = preview if preview > 0 else len(items)
    for n in items[:limit]:
        title = (n["title"] or n["title_en"])[:50]
        print(f"  reg_id={n['reg_id']!r}  region={n['region']}  conf={n['confidence']}")
        print(f"    title: {title}")
        print(f"    path : {n['path']}")
    if preview and len(items) > preview:
        print(f"  ... and {len(items) - preview} more")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", "-c", help="只看某一类（A/B/C/D/E/F）")
    args = ap.parse_args()
    scan(filter_category=args.category)
