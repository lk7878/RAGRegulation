"""P1.3 分诊：75 条低置信度 notes 按 body 可用性分类，估算 Opus 命中率。"""
from pathlib import Path
import re, yaml
from collections import Counter

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

def main():
    low_notes = []
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
        conf = (fm.get("cross_check_overall_confidence") or "").lower()
        if conf != "low":
            continue
        body = txt[m.end():]
        low_notes.append({
            "path": p,
            "reg_id": fm.get("reg_id", p.stem),
            "region": fm.get("region", "?"),
            "topic": fm.get("topic", "?"),
            "body_len": len(body),
            "flags_count": len(fm.get("cross_check_flags") or []),
            "extracted_by": fm.get("extracted_by", "?"),
            "has_recheck": bool(fm.get("recheck_at") or fm.get("low_conf_rechecked")),
        })

    print(f"=== 低置信度 notes 总数: {len(low_notes)} ===\n")

    # 按 body 长度桶
    buckets = Counter()
    for n in low_notes:
        bl = n["body_len"]
        if bl < 300:
            b = "A. (<300)           空/几乎空"
        elif bl < 1500:
            b = "B. (300-1500)       很短，OCR 可能失败"
        elif bl < 4000:
            b = "C. (1500-4000)      中等，Opus 可能帮上忙"
        else:
            b = "D. (>=4000)         body 充足，Opus 大概率能改善"
        buckets[b] += 1
    print("按 body 长度分布:")
    for k in sorted(buckets):
        print(f"  {k:<45}: {buckets[k]}")

    # 按 region
    print("\n按 region:")
    reg_cnt = Counter(n["region"] for n in low_notes)
    for r, c in reg_cnt.most_common():
        print(f"  {r:<12}: {c}")

    # 按 topic
    print("\n按 topic (top 10):")
    top_cnt = Counter(n["topic"] for n in low_notes)
    for t, c in top_cnt.most_common(10):
        print(f"  {t:<30}: {c}")

    # 已经 recheck 过的
    has_recheck = sum(1 for n in low_notes if n["has_recheck"])
    print(f"\n已经 P1.3 Phase 2b（DeepSeek recheck）跑过的: {has_recheck}")

    # 可修候选：body >= 1500，未曾 recheck
    candidates = [n for n in low_notes if n["body_len"] >= 1500 and not n["has_recheck"]]
    print(f"\n=== Opus 真值得跑的候选: {len(candidates)} 条 ===")
    print("(body>=1500 且未经过 DeepSeek recheck)")

    # 按长度降序列前 15
    candidates.sort(key=lambda x: -x["body_len"])
    print("\nTop 15 候选:")
    for n in candidates[:15]:
        print(f"  [{n['region']:<5}] {n['reg_id']:<35} body={n['body_len']:>5} flags={n['flags_count']}")


if __name__ == "__main__":
    main()
