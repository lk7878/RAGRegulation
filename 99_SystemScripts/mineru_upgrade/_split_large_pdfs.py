"""
_split_large_pdfs.py — Phase 1：把 8 条超页 PDF 拆成 ≤180p 的块

输入：`@D:\CcVault\05_Audit\2026-04-23_oversized_pdfs.md` 里的 TARGETS
输出：`_split_work/<reg_id>__partN.pdf`（N 从 1 起），每块 ≤ CHUNK_SIZE 页

设计：
  - CHUNK_SIZE=180（保守留 20p 缓冲，应对 MinerU 计页可能略多于 pypdf）
  - reg_id 中的 `/` `(` `)` 转成 `_`，避免文件名冲突
  - 失败的 PDF 单独记录，不影响其他 PDF 的拆分
  - 写一个 `_split_manifest.json`，记录每个 part 的元数据（reg_id / 原 PDF / 起止页 / 输出文件名）
    Phase 2 上传时用这个 manifest 关联 reg_id

用法：
    python _split_large_pdfs.py            # 跑全部
    python _split_large_pdfs.py --dry-run  # 只列页数，不写文件
    python _split_large_pdfs.py --reg-id "ECE R83"  # 只拆一条

输出目录结构：
    _split_work/
      ECE_R37_Rev8__part1.pdf  (180p)
      ECE_R37_Rev8__part2.pdf  (37p)
      ...
      _split_manifest.json
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import pypdf

ROOT = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade")
RAW = Path(r"D:\CcVault\00_Raw\标准库")
WORK = ROOT / "_split_work"
MANIFEST_PATH = WORK / "_split_manifest.json"

CHUNK_SIZE = 180  # 留 20 页缓冲（MinerU 200 硬限制）

# 11 条超页 PDF 清单（与 audit 文件保持一致 · 第 9-11 条为 2026-04-25 daily_batch 新发现）
TARGETS: list[tuple[str, str]] = [
    ("ECE R37 Rev8",        r"国外法规\ECE标准\标准法规-UNECE\0~40\37\R037r8e.pdf"),
    ("ECE R96 Rev3",        r"国外法规\ECE标准\标准法规-UNECE\81~120\96\R096r3e.pdf"),
    ("ECE R96 Rev3 Am2",    r"国外法规\ECE标准\标准法规-UNECE\81~120\96\R096r3am2e.pdf"),
    ("ECE R49 Rev6",        r"国外法规\ECE标准\标准法规-UNECE\41～80\49\R049r6e.pdf"),
    ("GB 18352.6-2016",     r"国内法规\国内标准\GB 18352.6-2016_upload_1b653a88-219a-412e-acb3-923dd4f1af30.pdf"),
    ("ECE R154 Rev1",       r"国外法规\ECE标准\标准法规-UNECE\121~160\154\R154r1e.pdf"),
    ("ECE R13 Rev8",        r"国外法规\ECE标准\标准法规-UNECE\0~40\13\R013r8e.pdf"),
    ("ECE R83",             r"国外法规\ECE标准\11.ECE法规（中文）\法规83号\83.pdf"),
    # 第 2 批：2026-04-25 daily_batch 新发现的超页 PDF
    ("ECE R110 Rev6",       r"国外法规\ECE标准\标准法规-UNECE\81~120\110\R110r6e.pdf"),
    ("ECE R83 Rev5",        r"国外法规\ECE标准\标准法规-UNECE\81~120\83\R083r5e.pdf"),
    ("3.2024版国际主流《汽车标准法规目录》", r"国外法规\3.2024版国际主流《汽车标准法规目录》.pdf"),
    # 第 3 批：2026-04-25 第二轮 daily_batch 又发现的超页 PDF
    ("汽车标准法规目录（2026）", r"国内法规\汽车标准法规目录（2026）.pdf"),
    ("ECE R154 Rev2 Am1",     r"国外法规\ECE标准\标准法规-UNECE\121~160\154\R154r2am1e.pdf"),
]


def safe_name(reg_id: str) -> str:
    """文件名安全化：/、(、)、空格、《、》 都转 _"""
    s = re.sub(r"[\\/\(\)\s《》【】]+", "_", reg_id).strip("_")
    return s


def split_one(reg_id: str, rel_path: str, dry_run: bool) -> dict:
    """拆一个 PDF，返回 dict 记录拆分结果"""
    src = RAW / rel_path
    result = {
        "reg_id": reg_id,
        "src_path": rel_path,
        "src_pages": 0,
        "src_size_kb": 0,
        "parts": [],   # [{idx, file, pages, page_range}]
        "status": "",
        "err": "",
    }

    if not src.exists():
        result["status"] = "src_not_found"
        result["err"] = f"PDF 不存在: {src}"
        return result

    result["src_size_kb"] = round(src.stat().st_size / 1024, 1)

    try:
        reader = pypdf.PdfReader(str(src))
        n = len(reader.pages)
        result["src_pages"] = n
    except Exception as e:
        result["status"] = "read_error"
        result["err"] = f"{type(e).__name__}: {e}"
        return result

    if n <= CHUNK_SIZE:
        result["status"] = "no_split_needed"
        result["err"] = f"页数 {n} ≤ {CHUNK_SIZE}，无需拆分"
        return result

    # 拆分
    base = safe_name(reg_id)
    n_parts = (n + CHUNK_SIZE - 1) // CHUNK_SIZE
    for i in range(n_parts):
        start = i * CHUNK_SIZE
        end = min(start + CHUNK_SIZE, n)
        out_name = f"{base}__part{i+1}.pdf"
        out_path = WORK / out_name
        part_pages = end - start

        if not dry_run:
            writer = pypdf.PdfWriter()
            for p in range(start, end):
                writer.add_page(reader.pages[p])
            with out_path.open("wb") as f:
                writer.write(f)

        result["parts"].append({
            "idx": i + 1,
            "file": out_name,
            "pages": part_pages,
            "page_range": [start + 1, end],   # 1-indexed 显示
            "size_kb": round(out_path.stat().st_size / 1024, 1) if (not dry_run and out_path.exists()) else None,
        })

    result["status"] = "split_ok" if not dry_run else "split_planned"
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只读 PDF 列页数，不写文件")
    ap.add_argument("--reg-id", help="只处理指定 reg_id（如 'ECE R83'）")
    args = ap.parse_args()

    if not args.dry_run:
        WORK.mkdir(parents=True, exist_ok=True)

    targets = TARGETS
    if args.reg_id:
        targets = [(rid, p) for rid, p in TARGETS if rid == args.reg_id]
        if not targets:
            print(f"[ERROR] reg_id={args.reg_id} 不在清单中")
            return 1

    print(f"\n{'='*72}")
    print(f"  超页 PDF 拆分 · CHUNK_SIZE={CHUNK_SIZE}p  ·  目标 {len(targets)} PDF")
    print(f"  {'[DRY-RUN]' if args.dry_run else '[REAL]'}  输出: {WORK}")
    print(f"{'='*72}\n")

    results = []
    total_parts = 0
    total_pages = 0

    for reg_id, rel in targets:
        print(f"▶ {reg_id}")
        print(f"  src: {rel}")
        r = split_one(reg_id, rel, args.dry_run)
        results.append(r)

        if r["status"] == "src_not_found":
            print(f"  ✗ 源文件不存在")
            continue
        if r["status"] == "read_error":
            print(f"  ✗ 读取失败: {r['err']}")
            continue

        print(f"  src: {r['src_pages']}p, {r['src_size_kb']} KB")
        if r["status"] == "no_split_needed":
            print(f"  · 无需拆分（{r['src_pages']}p ≤ {CHUNK_SIZE}p）")
            continue

        for part in r["parts"]:
            size_str = f", {part['size_kb']} KB" if part.get("size_kb") else ""
            print(f"    [part{part['idx']}] {part['pages']:>4}p  "
                  f"页码 {part['page_range'][0]}-{part['page_range'][1]}  "
                  f"→ {part['file']}{size_str}")
            total_parts += 1
            total_pages += part["pages"]
        print()

    # 写 manifest
    if not args.dry_run and results:
        manifest = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "chunk_size": CHUNK_SIZE,
            "total_parts": total_parts,
            "total_pages": total_pages,
            "results": results,
        }
        MANIFEST_PATH.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"\n[OK] manifest 写入: {MANIFEST_PATH}")

    print(f"\n{'='*72}")
    print(f"  拆分汇总")
    print(f"{'='*72}")
    succeeded = [r for r in results if r["status"] == "split_ok"]
    planned = [r for r in results if r["status"] == "split_planned"]
    skipped = [r for r in results if r["status"] in ("no_split_needed",)]
    failed = [r for r in results if r["status"] in ("src_not_found", "read_error")]
    print(f"  拆分成功 PDF: {len(succeeded) + len(planned)}")
    print(f"  无需拆分:    {len(skipped)}")
    print(f"  失败:        {len(failed)}")
    print(f"  生成 parts:  {total_parts}")
    print(f"  总页数:      {total_pages}")
    if failed:
        print(f"\n  失败明细:")
        for r in failed:
            print(f"    · {r['reg_id']}: {r['err']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
