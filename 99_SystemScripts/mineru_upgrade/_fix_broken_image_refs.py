"""
_fix_broken_image_refs.py — 修复 _clean_ocr_typesetting.py 误压缩的 _mineru_assets 路径

副作用诊断：
  - 清理脚本把 8+ 连续下划线 `_` 当排版残留压缩为 3 个 `_`
  - 但 `_mineru_assets/<safe_reg_id>/...` 里 safe_reg_id 含正常的多下划线（reg_id 中文字符 → `_`）
  - 例如 `3.2024______________` → `3.2024___`（破坏）

修复策略：
  1. 扫每个 note 里所有 ![...](../_mineru_assets/<dir>/<file>) 引用
  2. 检查 dir 是否真存在；若不存在，从 disk 实际 _mineru_assets/ 目录列表里找前缀匹配最长的真目录
  3. 替换路径
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(r"D:\CcVault")
ASSETS = VAULT / "01_Wiki" / "regulations" / "_mineru_assets"

# 真实存在的目录列表
real_dirs = sorted([d.name for d in ASSETS.iterdir() if d.is_dir()])
real_dirs_set = set(real_dirs)

IMG_REF_RE = re.compile(r"\.\./_mineru_assets/([^/\s\)]+)/([^/\s\)\"]+)")


def find_real_dir(broken: str) -> str | None:
    """根据被压缩的目录名（如 '3.2024___'），从 real_dirs 里找前缀匹配最长的"""
    if broken in real_dirs_set:
        return broken  # 不需修
    # 找以 broken[:-3] 开头的真目录（去掉末尾 ___ 后做前缀匹配）
    if broken.endswith("___"):
        prefix = broken[:-3]
        candidates = [d for d in real_dirs if d.startswith(prefix) and d != broken]
        if candidates:
            # 返回最长的（避免误匹配）
            return max(candidates, key=len)
    # 完全 ___ → 找含 ___ 的目录（不靠谱，跳过）
    return None


def fix_one(p: Path, dry_run: bool) -> dict:
    result = {"file": str(p.relative_to(VAULT)), "fixed": 0, "unfixable": 0}
    txt = p.read_text(encoding="utf-8", errors="replace")
    fix_map: dict[str, str] = {}
    unfixable: list[str] = []

    for m in IMG_REF_RE.finditer(txt):
        broken_dir = m.group(1)
        if broken_dir in real_dirs_set:
            continue  # 路径正确
        real = find_real_dir(broken_dir)
        if real and real != broken_dir:
            fix_map[broken_dir] = real
        else:
            unfixable.append(broken_dir)

    if not fix_map:
        result["unfixable"] = len(set(unfixable))
        return result

    new_txt = txt
    for broken, real in fix_map.items():
        new_txt = new_txt.replace(
            f"../_mineru_assets/{broken}/",
            f"../_mineru_assets/{real}/",
        )

    result["fixed"] = sum(1 for line in new_txt.split("\n") if False) + len(fix_map)
    result["unfixable"] = len(set(unfixable))

    if not dry_run and new_txt != txt:
        p.write_text(new_txt, encoding="utf-8")

    return result


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"\n{'='*72}")
    print(f"  扫描 _mineru_assets 被破坏的图像引用")
    print(f"{'='*72}")
    print(f"  实际 _mineru_assets/ 目录: {len(real_dirs)} 个")

    fixed_files = 0
    total_fixes = 0
    total_unfixable = 0
    for p in (VAULT / "01_Wiki" / "regulations").rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if "_mineru_assets" not in txt:
            continue
        r = fix_one(p, args.dry_run)
        if r["fixed"] > 0:
            fixed_files += 1
            total_fixes += r["fixed"]
            print(f"  ✓ {r['file']:<60}  {r['fixed']} 个目录修复")
        if r["unfixable"] > 0:
            total_unfixable += r["unfixable"]
            print(f"  ⚠ {r['file']}: {r['unfixable']} 个不可修（找不到对应真目录）")

    print(f"\n  修复 {total_fixes} 个引用 / {fixed_files} 个文件")
    print(f"  不可修: {total_unfixable}")
    if args.dry_run:
        print(f"  [DRY-RUN] 未写入")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
