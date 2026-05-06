"""
Stage 3 准备：从所有 notes 的 FM 中提取 equivalent_to 字段。

输出：
- .stage3/raw_equivalences.json — 每条 note 的 equivalent_to 清单（含原始结构）
- .stage3/equivalence_candidates.json — 去重/规整后的映射候选表
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
OUT_DIR = ROOT / ".stage3"
OUT_DIR.mkdir(exist_ok=True)
WIKI = Path(r"D:\CcVault\01_Wiki\regulations")


def strip_version(reg_id: str) -> str:
    """简化 reg_id 到 "家族级别"，便于归并。
    - 'GB 4785-2019' -> 'GB 4785'
    - 'ECE R48 Rev6 Am1' -> 'ECE R48'
    - 'GB/T 17692-2024' -> 'GB/T 17692'
    """
    s = (reg_id or "").strip()
    # 去 -YYYY 年份后缀
    s = re.sub(r"-(19|20)\d{2}(/XG\d+-\d{4})?$", "", s)
    # 去 Rev/Am/Corr
    s = re.sub(r"\s+(Rev\.?\d+|Am\.?\d+|Corr\.?\d+|Amendment\s*\d+).*$", "", s, flags=re.IGNORECASE)
    # 去 " Rev.N/Amend.M" 形式
    s = re.sub(r"\s*\(Rev\.?\d+[^)]*\)\s*$", "", s)
    return s.strip()


def normalize_ref(ref: str) -> str:
    """normalize equivalent_to.ref 到可比对形式。"""
    if not ref:
        return ""
    s = str(ref).strip()
    # "UN R48" -> "ECE R48"
    s = re.sub(r"^UN\s+R(\d)", r"ECE R\1", s)
    s = re.sub(r"^UN\s+ECE\s+R", "ECE R", s)
    # ECE R48:2015 / ECE R48-2015 -> ECE R48
    s = re.sub(r":\s*(19|20)\d{2}", "", s)
    s = strip_version(s)
    return s


def main() -> int:
    raw_eq = []
    edges_counter = defaultdict(lambda: {"count": 0, "relations": defaultdict(int), "sources": []})

    for p in WIKI.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if not txt.startswith("---"):
            continue
        end = txt.find("\n---", 4)
        if end < 0:
            continue
        try:
            fm = yaml.safe_load(txt[4:end]) or {}
        except yaml.YAMLError:
            continue

        reg_id = fm.get("reg_id") or ""
        region = fm.get("region") or ""
        eq = fm.get("equivalent_to")
        if not eq:
            continue

        if isinstance(eq, dict):
            eq_list = [eq]
        elif isinstance(eq, list):
            eq_list = [e for e in eq if isinstance(e, dict)]
        else:
            continue

        src_family = strip_version(reg_id)

        for item in eq_list:
            ref = item.get("ref")
            relation = str(item.get("relation") or "").strip().lower()
            if not ref:
                continue
            ref_norm = normalize_ref(ref)
            if not ref_norm or ref_norm == src_family:
                continue
            raw_eq.append({
                "src_reg_id": reg_id,
                "src_family": src_family,
                "src_region": region,
                "target_ref": ref,
                "target_ref_norm": ref_norm,
                "relation": relation,
                "version": item.get("version"),
                "note_path": str(p),
            })

            # 无向边 key：按字母序两端
            a, b = sorted([src_family, ref_norm])
            key = f"{a}||{b}"
            edges_counter[key]["count"] += 1
            edges_counter[key]["relations"][relation or "unknown"] += 1
            if len(edges_counter[key]["sources"]) < 3:
                edges_counter[key]["sources"].append({
                    "reg_id": reg_id,
                    "relation": relation,
                    "version": str(item.get("version") or ""),
                })

    # 序列化
    (OUT_DIR / "raw_equivalences.json").write_text(
        json.dumps(raw_eq, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    edges_clean = {}
    for k, v in edges_counter.items():
        edges_clean[k] = {
            "count": v["count"],
            "relations": dict(v["relations"]),
            "sources": v["sources"],
        }
    (OUT_DIR / "equivalence_candidates.json").write_text(
        json.dumps(edges_clean, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(f"Raw equivalence claims: {len(raw_eq)}")
    print(f"Unique (family-level) edges: {len(edges_clean)}")

    # 前 20 条最多引用的边
    top = sorted(edges_clean.items(), key=lambda x: -x[1]["count"])[:20]
    print("\nTop 20 most-referenced equivalence edges:")
    for k, v in top:
        rels = "/".join(f"{r}x{c}" for r, c in v["relations"].items())
        print(f"  {k:50} count={v['count']:3d}  relations={rels}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
