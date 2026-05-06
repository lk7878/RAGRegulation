"""内容级 QC：随机抽样 notes，打印 FM 核心字段 + 源 OCR 开头摘要，供手动比对。"""
import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

import yaml

WIKI = Path(r"D:\CcVault\01_Wiki\regulations")
STAGING = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\.staging")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")


def load_manifest() -> dict:
    """加载 manifest.json，返回 content_hash → rec 映射。"""
    if not MANIFEST.exists():
        return {}
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = data.get("records") if isinstance(data, dict) else data
    if isinstance(records, dict):
        return records  # 已是 hash → rec
    out = {}
    for r in records or []:
        if isinstance(r, dict):
            h = r.get("content_hash") or r.get("hash")
            if h:
                out[h] = r
    return out


def find_source_ocr(fm: dict, manifest_map: dict) -> str | None:
    """从 FM 的 source_pdf 找对应的 .staging/<hash>/raw.md。"""
    source_pdf = fm.get("source_pdf") or fm.get("source_file")
    if not source_pdf:
        return None
    source_norm = str(source_pdf).replace("\\", "/").lstrip("/")
    # 匹配 manifest 记录
    for h, rec in manifest_map.items():
        p = str(rec.get("path") or "").replace("\\", "/").lstrip("/")
        if p == source_norm or p.endswith(source_norm) or source_norm.endswith(p):
            # 2-char sharded：.staging/<prefix>/<hash>/raw.md
            staging_dir = STAGING / h[:2] / h
            raw = staging_dir / "raw.md"
            if raw.exists():
                return raw.read_text(encoding="utf-8", errors="replace")
            # fallback: non-sharded layout
            raw_alt = STAGING / h / "raw.md"
            if raw_alt.exists():
                return raw_alt.read_text(encoding="utf-8", errors="replace")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10, help="每区抽样数")
    ap.add_argument("--regions", nargs="+", default=["cn", "ece"], help="抽样区域")
    ap.add_argument("--show-ocr", type=int, default=500, help="显示源 OCR 字符数（0 关闭）")
    args = ap.parse_args()

    random.seed(42)
    manifest_map = load_manifest()

    samples: list[Path] = []
    for r in args.regions:
        d = WIKI / r
        if not d.exists():
            continue
        files = [f for f in d.glob("*.md") if not f.name.startswith(".")]
        if not files:
            continue
        picked = random.sample(files, min(args.n, len(files)))
        samples.extend(picked)

    schema_fields = ["reg_id", "title", "type", "region", "status", "publication_date", "standard_body"]
    cov = Counter()

    for p in samples:
        txt = p.read_text(encoding="utf-8")
        end = txt.find("\n---", 4)
        fm = yaml.safe_load(txt[4:end]) if end > 0 else {}
        fm = fm or {}
        print(f"\n=== {p.parent.name}/{p.name} ===")
        for k in schema_fields:
            v = fm.get(k)
            vs = repr(v) if v else "—"
            if len(vs) > 80:
                vs = vs[:77] + "...'"
            print(f"  {k:18}: {vs}")
            if v:
                cov[k] += 1
        # 源 OCR 摘要
        if args.show_ocr > 0:
            ocr = find_source_ocr(fm, manifest_map)
            if ocr:
                # 跳过前导空行，取前 N 字
                snippet = ocr.strip()[: args.show_ocr]
                print(f"\n  SOURCE OCR (first {args.show_ocr} chars):")
                for line in snippet.split("\n")[:15]:
                    print(f"  > {line[:140]}")
            else:
                print(f"  SOURCE OCR: [not found]")

    print(f"\n=== Coverage ({len(samples)} sampled) ===")
    for f in schema_fields:
        pct = 100 * cov[f] // len(samples) if samples else 0
        print(f"  {f:20}: {cov[f]}/{len(samples)} ({pct}%)")


if __name__ == "__main__":
    sys.exit(main() or 0)
