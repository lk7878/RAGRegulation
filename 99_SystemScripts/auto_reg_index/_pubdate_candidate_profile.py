"""诊断 P1.4 候选 — 97 条缺 publication_date 的 notes 里，实际 body 有日期线索的有多少？"""
from pathlib import Path
import re, yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
FM_RE = re.compile(r"^---\s*\n([\s\S]*?)\n---\s*\n")

# 检测 body 里的"发布/实施"日期关键词
DATE_SIGNAL_RE = re.compile(
    r"(\d{4}[-/年]\s?\d{1,2}[-/月]\s?\d{1,2}|"           # 2018-03-15 / 2018 年 3 月 15 日
    r"\d{1,2}\s?(January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{4}|"  # 15 March 2018
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s?\d{1,2},?\s?\d{4}|"  # March 15, 2018
    r"(发布|实施|施行|生效|issued|published|effective|entry\s+into\s+force)[^\n]{0,30}\d{4})",
    re.IGNORECASE,
)


def main():
    buckets = {
        "empty_body (<200 chars)": 0,
        "very_short (200-1000)": 0,
        "short_no_date_signal (1000-3000 无日期关键词)": 0,
        "has_date_signal (body 有日期关键词)": 0,
    }
    date_signal_samples = []
    region_counts = {}
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
        v = fm.get("publication_date")
        is_missing = (v is None or str(v).strip().lower() in ("", "unknown", "none", "null", "n/a"))
        if not is_missing:
            continue
        body = txt[m.end():]
        body_len = len(body)
        region = fm.get("region", "?")
        region_counts[region] = region_counts.get(region, 0) + 1

        if body_len < 200:
            buckets["empty_body (<200 chars)"] += 1
        elif body_len < 1000:
            buckets["very_short (200-1000)"] += 1
        else:
            # 看前 3000 字符有没有日期关键词
            head = body[:3000]
            m2 = DATE_SIGNAL_RE.search(head)
            if m2:
                buckets["has_date_signal (body 有日期关键词)"] += 1
                if len(date_signal_samples) < 10:
                    date_signal_samples.append({
                        "reg_id": fm.get("reg_id", p.stem),
                        "region": region,
                        "body_len": body_len,
                        "match": m2.group(0)[:60],
                    })
            else:
                buckets["short_no_date_signal (1000-3000 无日期关键词)"] += 1

    print("=== 缺 publication_date 的 97 条候选分布 ===\n")
    print("按 body 状态:")
    for k, v in buckets.items():
        print(f"  {k:<55}: {v}")
    total_with_signal = buckets["has_date_signal (body 有日期关键词)"]
    total = sum(buckets.values())
    print(f"\n总计 {total} 条，其中 body 含日期关键词 {total_with_signal} 条（{total_with_signal*100//max(total,1)}% 可能可修）")
    print("\n按 region 分布:")
    for r, n in sorted(region_counts.items(), key=lambda x: -x[1]):
        print(f"  {r:<10}: {n}")
    print("\n含日期关键词的样本（前 10 条）:")
    for s in date_signal_samples:
        print(f"  [{s['region']}] {s['reg_id']:<30} body={s['body_len']:>6}  signal={s['match']!r}")


if __name__ == "__main__":
    main()
