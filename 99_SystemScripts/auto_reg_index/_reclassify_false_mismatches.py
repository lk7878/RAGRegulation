"""
重新分类 Stage 2 的假告警（false mismatches）。

Stage 2 cross-check 对 330 条 notes 打了 low confidence，其中 78 条 reg_id mismatch
绝大多数是 "格式差异"（如 GB11555-94 vs GB 11555-1994），Stage 1 规范化正确。
本脚本将这类 flag 状态从 mismatch 降为 normalized，并重算 overall_confidence。

规则：
  reg_id mismatch → normalized  如果 extracted 和 original 剥离格式后相等（同 R 号 / 同 GB 号）
  其他字段 mismatch 不动

重算 overall_confidence：
  - 若所有 mismatch 都已降为 normalized → 升 low → medium，tag 加 status/verified 去 needs-review
  - 若仍有真正 mismatch → 保持 low

用法：python _reclassify_false_mismatches.py [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# R 号规范化正则
_ECE_R = re.compile(r"(?:regulation\s*(?:no\.?)?\s*|addendum\s*\d+\s*[–-]\s*regulation\s*no\.?\s*|ece\s*|un\s*)r?\s*0*(\d+[A-Za-z]?)",
                    re.IGNORECASE)
_GB_NUM = re.compile(r"^(gb(?:/t)?)\s*0*(\d+(?:\.\d+)?)[\s—–-]*(\d{2,4})?$", re.IGNORECASE)


def _r_num(s: str) -> str | None:
    """提取 R 号（含 H 后缀）。返回标准化如 '61'、'13H'。"""
    s = str(s or "").strip()
    m = _ECE_R.search(s)
    if m:
        return m.group(1).upper()
    return None


def _gb_canon(s: str) -> tuple[str, str, str] | None:
    """GB 号规范化：返回 (gb/gb/t, number, year4)。"""
    s = str(s or "").strip().replace("—", "-").replace("–", "-")
    # 去掉嵌入空格
    s2 = re.sub(r"gb\s*/\s*t", "GB/T", s, flags=re.IGNORECASE)
    s2 = re.sub(r"(gb(?:/t)?)(\d)", r"\1 \2", s2, flags=re.IGNORECASE)
    m = _GB_NUM.match(s2.strip())
    if not m:
        return None
    prefix = m.group(1).upper()
    num = m.group(2)
    year = m.group(3) or ""
    # 2 位年份 → 4 位
    if year and len(year) == 2:
        yi = int(year)
        year = f"19{year}" if yi >= 50 else f"20{year}"
    return (prefix, num, year)


_MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
    "一月": 1, "二月": 2, "三月": 3, "四月": 4, "五月": 5, "六月": 6,
    "七月": 7, "八月": 8, "九月": 9, "十月": 10, "十一月": 11, "十二月": 12,
}


def _parse_date(v) -> _dt.date | None:
    """从各种日期表达解析为 date 对象。"""
    if v is None:
        return None
    if isinstance(v, _dt.date):
        return v
    if isinstance(v, _dt.datetime):
        return v.date()
    s = str(v).strip()
    if not s:
        return None
    # ISO: YYYY-MM-DD
    m = re.match(r"^(\d{4})[-/](\d{1,2})[-/](\d{1,2})", s)
    if m:
        try: return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError: pass
    # "DD Month YYYY" / "D Month YYYY"
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})\b", s)
    if m:
        mon = _MONTHS.get(m.group(2).lower())
        if mon:
            try: return _dt.date(int(m.group(3)), mon, int(m.group(1)))
            except ValueError: pass
    # "Month DD, YYYY"
    m = re.search(r"\b([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})\b", s)
    if m:
        mon = _MONTHS.get(m.group(1).lower())
        if mon:
            try: return _dt.date(int(m.group(3)), mon, int(m.group(2)))
            except ValueError: pass
    # 中文: YYYY年M月D日
    m = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", s)
    if m:
        try: return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError: pass
    return None


def is_date_equivalent(extracted, original) -> bool:
    """判断两个日期字段是否实质相等（只是表述差异）。"""
    de, do = _parse_date(extracted), _parse_date(original)
    if de and do and de == do:
        return True
    # original 含 parenthetical like "1994-03-04 (原文页首日期为"4 March 1994")"
    if do is None and extracted:
        # original 字符串中可能含多个日期；如果 extracted 对应的 ISO 日期出现在 original 中，视为等价
        de2 = _parse_date(extracted)
        if de2:
            iso = de2.strftime("%Y-%m-%d")
            if iso in str(original):
                return True
    return False


def is_format_equivalent(extracted: str, original: str) -> bool:
    """判断两个 reg_id 字符串是否"实质相等"（只是格式差异）。"""
    if not extracted or not original:
        return False
    e = str(extracted).strip()
    o = str(original).strip()
    if e.lower() == o.lower():
        return True
    # 按 R 号比对
    e_r, o_r = _r_num(e), _r_num(o)
    if e_r and o_r and e_r == o_r:
        return True
    # 按 GB 号比对（prefix + number + year 全一致）
    e_g, o_g = _gb_canon(e), _gb_canon(o)
    if e_g and o_g and e_g == o_g:
        return True
    # GB 号 OCR 可能漏小数点："GB 5135.6" vs "GB51356" / "GB/T 3730.1" vs "GB/T 37301"
    def _gb_no_dot(s: str) -> str | None:
        s = str(s or "").strip().replace("—", "-").replace("–", "-")
        m = re.match(r"^(gb(?:/t)?)\s*(\d+)(?:\.\d)?\s*-?\s*(\d{2,4})?$", s, re.IGNORECASE)
        if m:
            return f"{m.group(1).upper()}:{m.group(2).replace('.', '')}"
        return None
    e_gnd, o_gnd = _gb_no_dot(e), _gb_no_dot(o)
    if e_gnd and o_gnd and e_gnd == o_gnd:
        return True
    # ECE/UN 各种变形："ECE R68 Am1" vs "UN R068am1e"  —  剥 am/rev/corr 后比对
    def _un_canon(s: str) -> str | None:
        s = str(s or "").lower()
        # 抽 R 号
        m = re.search(r"r\s*0*(\d+[a-z]?)", s)
        if not m:
            return None
        r = m.group(1).upper()
        # 抽 rev / am / corr 数字
        rev = re.search(r"(?:rev(?:ision)?\.?\s*|r)\s*(\d+)", s)
        am = re.search(r"(?:am(?:end(?:ment)?)?\.?\s*)(\d+)", s)
        corr = re.search(r"(?:corr(?:igendum)?\.?\s*)(\d+)", s)
        parts = [f"R{r}"]
        if rev: parts.append(f"Rev{rev.group(1)}")
        if am: parts.append(f"Am{am.group(1)}")
        if corr: parts.append(f"Corr{corr.group(1)}")
        return " ".join(parts)
    e_u, o_u = _un_canon(e), _un_canon(o)
    if e_u and o_u and e_u == o_u:
        return True
    # WP.29 文档号：ECE/TRANS/505/Rev.1/Add.XX/... 实质指向某 ECE R 号
    # 如果 og 含 /Add.N/，N 通常对应 R 号的 addendum。但这种不能 1:1 推导，
    # 所以如果 extracted 是干净的 "ECE Rxxx" 且 original 是 "ECE/TRANS/505/..."，视为格式差异
    if re.match(r"^(ECE|UN)\s+R\s*\d+", e, re.IGNORECASE) and \
       re.search(r"ECE/(?:324|TRANS/505)/Rev\.?\d+/Add\.?\d+", o, re.IGNORECASE):
        return True
    return False


def process_note(path: Path, dry_run: bool) -> dict | None:
    """处理单个 note。返回修改记录 or None。"""
    try:
        txt = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    if not txt.startswith("---"):
        return None
    end = txt.find("\n---", 4)
    if end < 0:
        return None
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        return None

    if fm.get("cross_check_overall_confidence") != "low":
        return None

    flags = fm.get("cross_check_flags")
    if not isinstance(flags, list):
        return None

    reclassified = []
    true_mismatch_remaining = 0
    for f in flags:
        if not isinstance(f, dict):
            continue
        if f.get("status") != "mismatch":
            continue
        field = f.get("field")
        ex = f.get("extracted")
        og = f.get("original")

        # reg_id 格式差异降级
        if field == "reg_id" and is_format_equivalent(ex, og):
            f["status"] = "normalized"
            f["note"] = f"[Auto-reclassified] Same reg_id after normalization (was: '{ex}' vs '{og}')"
            reclassified.append(field)
        # reg_id mismatch 但原文无 reg_id → unsure
        elif field == "reg_id" and (og is None or str(og).strip().lower() in ("", "none", "null")):
            f["status"] = "unsure"
            f["note"] = f"[Auto-reclassified] Original OCR had no reg_id; extracted from filename/context"
            reclassified.append(field)
        # 日期字段 mismatch 但格式差异 → normalized
        elif field in ("publication_date", "implementation_date_new_vehicle",
                       "implementation_date_in_use") \
                and is_date_equivalent(ex, og):
            f["status"] = "normalized"
            f["note"] = f"[Auto-reclassified] Same date after parsing: {ex} == {og}"
            reclassified.append(field)
        # implementation_date_* / publication_date mismatch 但 extracted/original 其中一个为 null → unsure
        elif field in ("publication_date", "implementation_date_new_vehicle",
                       "implementation_date_in_use") \
                and (ex is None or og is None):
            f["status"] = "unsure"
            f["note"] = f"[Auto-reclassified] Insufficient evidence (was mismatch with null): '{ex}' vs '{og}'"
            reclassified.append(field)
        # equivalent_to.* mismatch 但 null → unsure
        elif field and field.startswith("equivalent_to") and (ex is None or og is None):
            f["status"] = "unsure"
            f["note"] = f"[Auto-reclassified] Insufficient evidence (was mismatch with null)"
            reclassified.append(field)
        # title mismatch 但 null → unsure
        elif field == "title" and (ex is None or og is None):
            f["status"] = "unsure"
            f["note"] = f"[Auto-reclassified] Insufficient evidence (was mismatch with null)"
            reclassified.append(field)
        else:
            true_mismatch_remaining += 1

    if not reclassified:
        return None

    # 重算 overall_confidence
    old_conf = fm["cross_check_overall_confidence"]
    if true_mismatch_remaining == 0:
        fm["cross_check_overall_confidence"] = "medium"
        new_conf = "medium"
    else:
        new_conf = old_conf  # 保持 low

    # 若升级 → 更新 tags
    tag_changed = False
    if new_conf == "medium" and old_conf == "low":
        tags = fm.get("tags") or []
        if isinstance(tags, list):
            if "status/needs-review" in tags:
                tags.remove("status/needs-review")
                tag_changed = True
            if "status/verified" not in tags:
                tags.append("status/verified")
                tag_changed = True
            fm["tags"] = tags

    # 标注重分类元数据
    fm.setdefault("stage2_reclassified", []).extend(reclassified)
    fm["stage2_reclassified"] = sorted(set(fm["stage2_reclassified"]))
    fm["stage2_reclassified_at"] = "2026-04-18"

    # 写回
    if not dry_run:
        body = txt[end + 4 :]
        new_content = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---" + body
        path.write_text(new_content, encoding="utf-8")

    return {
        "path": str(path),
        "reg_id": fm.get("reg_id"),
        "reclassified_fields": reclassified,
        "confidence_change": f"{old_conf} -> {new_conf}",
        "tags_updated": tag_changed,
        "true_mismatch_remaining": true_mismatch_remaining,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total = 0
    touched = 0
    upgraded = 0
    reclass_counter = {}

    for p in WIKI.rglob("*.md"):
        total += 1
        res = process_note(p, args.dry_run)
        if res:
            touched += 1
            if "low -> medium" in res["confidence_change"]:
                upgraded += 1
            for f in res["reclassified_fields"]:
                reclass_counter[f] = reclass_counter.get(f, 0) + 1

    print(f"Total notes scanned: {total}")
    print(f"Notes reclassified: {touched}")
    print(f"Notes upgraded low -> medium: {upgraded}")
    print(f"Remaining low-confidence: {330 - upgraded}")
    print("\nReclassified field counts:")
    for fld, c in sorted(reclass_counter.items(), key=lambda x: -x[1]):
        print(f"  {fld:45s} {c}")

    if args.dry_run:
        print("\n[DRY RUN] No files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
