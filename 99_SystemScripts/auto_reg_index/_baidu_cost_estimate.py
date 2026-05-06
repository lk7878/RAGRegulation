"""估算全量跑 Baidu OCR 的成本（不调 API，仅计页数）。"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pypdfium2 as pdfium

MF_PATH = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
RAW_ROOT = Path(r"D:\CcVault\00_Raw\标准库")


def count_pages(pdf_path: Path) -> int:
    try:
        doc = pdfium.PdfDocument(str(pdf_path))
        n = len(doc)
        doc.close()
        return n
    except Exception:
        return 0


def main() -> int:
    data = json.loads(MF_PATH.read_text(encoding="utf-8"))
    failed = [(h, r) for h, r in data["records"].items() if r.get("state") == "failed"]

    total_pages = 0
    per_file: list[tuple[int, str]] = []
    for h, r in failed:
        path = r.get("path", "")
        pdf = RAW_ROOT / path
        if not pdf.exists():
            continue
        n = count_pages(pdf)
        total_pages += n
        per_file.append((n, path))

    per_file.sort(reverse=True)
    print(f"Failed PDFs: {len(failed)}")
    print(f"Total pages: {total_pages}")
    print(f"Est. cost (¥0.007/page): ¥{total_pages * 0.007:.2f}  (~${total_pages * 0.007 / 7:.2f})")
    print(f"Daily free quota: first 1000 pages free/day\n")

    print("Top 10 by page count:")
    for n, p in per_file[:10]:
        print(f"  {n:5} pages  {p[:70]}")

    print(f"\nSmall PDFs (<=30 pages) count: {sum(1 for n, _ in per_file if 0 < n <= 30)}")
    print(f"Medium (31-100 pages):           {sum(1 for n, _ in per_file if 31 <= n <= 100)}")
    print(f"Large (>100 pages):              {sum(1 for n, _ in per_file if n > 100)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
