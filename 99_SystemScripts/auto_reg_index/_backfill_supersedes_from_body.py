"""
_backfill_supersedes_from_body.py

从 notes 的 body 中识别"本标准代替 GB XXXX-YYYY" / "Supersedes ECE R13" 等模式，
回填到 FM 的 supersedes 字段。处理完后建议再跑 _build_supersession_chain.py 建双向链。

修复 审计报告 P0.1 — cn/ 62 条 GB 标准 body 有"代替"但 FM supersedes 缺失。

用法：
    python _backfill_supersedes_from_body.py --dry-run              # 看预测
    python _backfill_supersedes_from_body.py --only cn --dry-run    # 只看中文
    python _backfill_supersedes_from_body.py                        # 正式跑
    python _backfill_supersedes_from_body.py --mark-superseded-status  # 同时把前置版本 status 改为 superseded
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")

# ---------- 正则：中文标准"代替"模式 ----------
CN_PATTERNS = [
    # 本标准代替 GB 4785-2007 / 本标准代替GB/T 18099—2013 / 本标准代替 GB/T 18408—2001
    re.compile(r"本标准代替\s*(GB(?:/T)?\s*\d+(?:\.\d+)?[-—–]\d{2,4})"),
    # 代替《XXX》(GB XXXX-YYYY) — 带书名号 + 括号
    re.compile(r"代替\s*《[^》]+》\s*\(\s*(GB(?:/T)?\s*\d+(?:\.\d+)?[-—–]\d{2,4})\s*\)"),
    # 代替 GB XXXX-YYYY（不在"本标准"之前但有明确代替）— 放末尾优先级低
    re.compile(r"(?:替代|代替)\s*(GB(?:/T)?\s*\d+(?:\.\d+)?[-—–]\d{2,4})"),
]

# ---------- 正则：英文 ECE 代替模式 ----------
EN_PATTERNS = [
    re.compile(
        r"[Ss]upersedes?\s+(ECE R\d+[A-Z]?(?:\s*Rev\s*\d+)?(?:\s*Am\s*\d+)?)"
    ),
    re.compile(
        r"[Rr]eplaces?\s+(ECE R\d+[A-Z]?(?:\s*Rev\s*\d+)?(?:\s*Am\s*\d+)?)"
    ),
]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")


# ---------- reg_id 归一化 ----------
def canonicalize_reg_id(s: str) -> str:
    """规范化 reg_id 格式。"""
    s = s.strip()
    # 剥离中/英文括号及其内容（通常是注释说明，如"(部分代替，非金属罐体部分)"）
    s = re.sub(r"[\(（][^）\)]*[\)）]", "", s).strip()
    # em dash / en dash / full-width hyphen -> ASCII hyphen
    s = s.replace("—", "-").replace("–", "-").replace("－", "-")
    # GB4785 -> GB 4785, GB/T18099 -> GB/T 18099
    s = re.sub(r"(GB(?:/T)?)\s*(\d)", r"\1 \2", s, count=1)
    # ECE R13 Rev 4 -> ECE R13 Rev4 (去 Rev/Am 后空格)
    s = re.sub(r"(Rev|Am)\s+(\d)", r"\1\2", s)
    # 多空格合一
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_fm_body(txt: str):
    """把 md 文本拆成 (fm_dict, fm_raw, body)."""
    if not txt.startswith("---"):
        return None, None, txt
    end = txt.find("\n---", 4)
    if end < 0:
        return None, None, txt
    try:
        fm = yaml.safe_load(txt[4:end]) or {}
    except yaml.YAMLError:
        return None, None, txt
    body = txt[end + 4 :]
    return fm, txt[4:end], body


def find_candidates(body: str, patterns) -> list[str]:
    found = []
    for pat in patterns:
        for m in pat.finditer(body):
            found.append(m.group(1))
    return found


def parse_existing_supersedes(v) -> list[str]:
    """抽取已有 supersedes 列表，返回规范化 reg_id 列表。"""
    if not v:
        return []
    out = []

    def _extract(s: str) -> list[str]:
        """先剥 wikilink 再按逗号/分号拆分（防畸形 wikilink 内含多 reg_id）。"""
        m = WIKILINK_RE.findall(s)
        raw = [a.strip() for a in m] if m else [s]
        results = []
        for item in raw:
            # 拆分前先移除括号及其内容（防括号内 `，` 被误拆）
            cleaned = re.sub(r"[\(（][^）\)]*[\)）]?", "", item)
            parts = re.split(r"[,，、;；]\s*", cleaned)
            results.extend([p.strip() for p in parts if p.strip()])
        return results

    if isinstance(v, str):
        out = _extract(v)
    elif isinstance(v, list):
        for x in v:
            if isinstance(x, str):
                out.extend(_extract(x))
            elif isinstance(x, dict):
                ref = x.get("ref") or x.get("reg_id")
                if ref:
                    out.append(str(ref).strip())
    return [canonicalize_reg_id(s) for s in out if s]


def dedupe(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def self_reference_check(new_regs: list[str], self_reg: str) -> list[str]:
    """过滤掉自引用（note 的 reg_id == 其 supersedes 中的一项）。"""
    if not self_reg:
        return new_regs
    return [r for r in new_regs if r != self_reg]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="不修改文件，只输出预测")
    ap.add_argument(
        "--only",
        choices=["cn", "ece", "all"],
        default="all",
        help="只处理某个 region 子集",
    )
    ap.add_argument("--verbose", action="store_true", help="详细打印每条预测")
    args = ap.parse_args()

    scanned = 0
    with_matches = 0
    total_add = 0
    files_updated = 0
    predictions: list[dict] = []

    for p in WIKI.rglob("*.md"):
        region = p.parent.name
        if args.only == "cn" and region != "cn":
            continue
        if args.only == "ece" and region != "ece":
            continue

        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm, _fm_raw, body = extract_fm_body(txt)
        if fm is None:
            continue
        scanned += 1

        if region == "cn":
            patterns = CN_PATTERNS
        elif region in ("ece", "eu", "intl", "asean"):
            patterns = EN_PATTERNS
        else:
            # 其他 region（us/jp/kr/au 等）也尝试英文
            patterns = EN_PATTERNS

        raw = find_candidates(body, patterns)
        if not raw:
            continue
        with_matches += 1

        candidates = dedupe([canonicalize_reg_id(x) for x in raw])
        existing = parse_existing_supersedes(fm.get("supersedes"))
        existing_set = set(existing)
        self_reg = canonicalize_reg_id((fm.get("reg_id") or "").strip())
        to_add = [c for c in candidates if c not in existing_set and c != self_reg]

        if not to_add:
            continue

        total_add += len(to_add)
        pred = {
            "file": str(p.relative_to(WIKI)),
            "region": region,
            "reg_id": self_reg,
            "existing": existing,
            "add": to_add,
        }
        predictions.append(pred)

        if args.dry_run:
            continue

        # 写回 FM
        combined = existing + to_add
        wikilinks = [f"[[{x}]]" for x in combined]
        fm["supersedes"] = wikilinks if len(wikilinks) > 1 else wikilinks[0]

        new_fm_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
        new_content = "---\n" + new_fm_yaml + "---" + body
        p.write_text(new_content, encoding="utf-8")
        files_updated += 1

    # ---------- 输出 ----------
    print(f"Scanned files            : {scanned}")
    print(f"Files with body matches  : {with_matches}")
    print(f"Files needing backfill   : {len(predictions)}")
    print(f"Total reg_ids to add     : {total_add}")
    if not args.dry_run:
        print(f"Files actually updated   : {files_updated}")

    # 预览预测
    if args.verbose or args.dry_run:
        print("\n=== All Predictions ===")
        for pred in predictions:
            print(
                f"  [{pred['region']}] {pred['reg_id']:<22} "
                f"existing={pred['existing']} "
                f"add={pred['add']}"
            )

    if args.dry_run:
        print("\n[DRY RUN] No files written.")
        print("Re-run without --dry-run to apply.")

    print("\nNext steps:")
    print("  python _build_supersession_chain.py   # 重建双向链")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
