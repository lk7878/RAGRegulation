"""列出所有 >200 页超限失败样本 + 找对应 PDF 路径和实际页数。"""
from __future__ import annotations
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

STATE = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_state.json")
MANIFEST = Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json")
RAW = Path(r"D:\CcVault\00_Raw\标准库")

s = json.loads(STATE.read_text(encoding="utf-8"))
m = json.loads(MANIFEST.read_text(encoding="utf-8"))
records = m["records"]  # content_hash → record

oversized = [(h, info) for h, info in s["failed"].items() if "200 pages" in info.get("err", "")]

print(f"共 {len(oversized)} 条 >200 页失败样本:\n")
for i, (h, info) in enumerate(oversized, 1):
    print(f"[{i}] reg_id  : {info['reg_id']}")
    print(f"    hash    : {h}")
    rec = records.get(h)
    if rec:
        pdf_rel = rec.get("path", "")
        pdf_abs = RAW / pdf_rel if pdf_rel else None
        print(f"    pdf     : {pdf_rel}")
        if pdf_abs and pdf_abs.exists():
            size_mb = pdf_abs.stat().st_size / (1024 * 1024)
            print(f"    size    : {size_mb:.1f} MB")
            # 用 pypdf 读页数（如有）
            try:
                import pypdf
                reader = pypdf.PdfReader(str(pdf_abs))
                n_pages = len(reader.pages)
                print(f"    pages   : {n_pages}")
            except ImportError:
                print(f"    pages   : (装 pypdf 可读)")
            except Exception as e:
                print(f"    pages   : (读失败: {type(e).__name__})")
        else:
            print(f"    size    : (文件不存在)")
    else:
        print(f"    pdf     : (manifest 无记录)")
    print(f"    reg 链接: [[{info['reg_id']}]]")
    print()
