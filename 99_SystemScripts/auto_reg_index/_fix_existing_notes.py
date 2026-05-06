"""
后处理脚本：修复 01_Wiki/regulations 下已写入的 notes。

做两件事：
  1. 检测 "double frontmatter"（body 开头有 `reg_id:` 等 YAML 行）
     → 重新解析 body，合并到外层 frontmatter，剥离 body 中的 YAML 前缀。
  2. 规范化 reg_id（ECE-R100 → ECE R100 等），
     若 reg_id 变化则重命名文件。

用法：python _fix_existing_notes.py [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from stages.s1_extract import (
    _canonicalize_reg_id,
    _canonicalize_region,
    _parse_llm_output,
    _normalize_frontmatter,
    _STATUS_ALIAS,
    _TYPE_ALIAS,
)
from writers.obsidian_writer import _sanitize_filename, _derive_amendment_suffix

WIKI_ROOT = Path(r"D:\CcVault\01_Wiki\regulations")


def _safe_filename(name: str) -> str:
    """复用 obsidian_writer 的 sanitization 规则，保证一致性。"""
    return _sanitize_filename(name)


def _read_note(path: Path) -> tuple[dict, str]:
    """读取一个 .md note，返回 (frontmatter, body)。"""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    rest = text[3:].lstrip("\n")
    end = rest.find("\n---")
    if end < 0:
        return {}, text
    yaml_str = rest[:end]
    body = rest[end + 4:].lstrip("\n")
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def _write_note(path: Path, fm: dict, body: str) -> None:
    yaml_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    path.write_text(
        "---\n" + yaml_str + "---\n\n" + body.strip() + "\n",
        encoding="utf-8",
    )


def _body_is_yaml(body: str) -> bool:
    """如果 body 前几行长得像 YAML frontmatter（有 reg_id: 或其他典型字段），则判定需修复。

    常见形态：
      A. body 直接以 `reg_id: xxx` 开头
      B. body 以 `---` 包裹的 YAML（双 frontmatter）
      C. body 前几行有 title/status/scope 等典型 schema 字段
    """
    head = "\n".join(body.splitlines()[:8]).strip()
    if not head:
        return False
    # A / B：明显带 reg_id 的 YAML
    stripped = head.lstrip("-").lstrip()
    for prefix in ("reg_id:", "regulation_id:", "standard_id:"):
        if stripped.startswith(prefix):
            return True
    return False


def _fix_note(path: Path, *, dry_run: bool) -> dict:
    """修复单个 note，返回 {changed: [...], renamed_to: Path|None}"""
    changes = []
    fm, body = _read_note(path)

    # 1) body-wrapped YAML 修复
    if _body_is_yaml(body):
        inner_fm, inner_body = _parse_llm_output(body)
        if inner_fm:
            inner_fm = _normalize_frontmatter(inner_fm)
            # 合并：inner_fm 优先（它含 reg_id、title、scope 等真内容），
            # 外层 fm 提供 source_pdf / extracted_by 等元信息
            merged = {**fm, **inner_fm}
            # 但保留外层的 tags（已合并过 type + region）
            if "tags" in fm and "tags" not in inner_fm:
                merged["tags"] = fm["tags"]
            fm = merged
            body = inner_body
            changes.append("merged_double_fm")

    # 2) reg_id 规范化
    old_reg_id = fm.get("reg_id")
    if isinstance(old_reg_id, str):
        new_reg_id = _canonicalize_reg_id(old_reg_id)
        if new_reg_id != old_reg_id:
            fm["reg_id"] = new_reg_id
            changes.append(f"reg_id: {old_reg_id!r} → {new_reg_id!r}")

    # 2.5) region 规范化（UN/AU/BR/ZA 等大写 → lowercase, UN → ece）
    old_region = fm.get("region")
    if old_region:
        new_region = _canonicalize_region(old_region)
        if new_region and new_region != old_region:
            fm["region"] = new_region
            changes.append(f"region: {old_region!r} → {new_region!r}")
            # tags 里的 reg/<region> 也同步更新
            tags = fm.get("tags") or []
            if isinstance(tags, list):
                fm["tags"] = [
                    f"reg/{new_region}" if t == f"reg/{old_region}" else t
                    for t in tags
                ]

    # 2.7) status 规范化（'现行有效' / 'in_force' / 'amendment' 等 → active）
    old_status = fm.get("status")
    if isinstance(old_status, str):
        s_strip = old_status.strip()
        if not s_strip:
            # 空字符串 → 删除字段（避免 schema 校验歧义）
            fm.pop("status", None)
            changes.append(f"status: '' → <removed>")
            canon_status = None
            old_status = None
        else:
            canon_status = _STATUS_ALIAS.get(s_strip) or _STATUS_ALIAS.get(s_strip.lower())
        if old_status is not None and not canon_status:
            low = s_strip.lower()
            if any(kw in low for kw in ("corrigendum", "erratum", "勘误", "修正本", "修订", "amendment", "amend")):
                canon_status = "active"
            elif any(kw in s_strip for kw in ("生效", "有效", "现行")):
                canon_status = "active"
        if canon_status and canon_status != old_status:
            fm["status"] = canon_status
            changes.append(f"status: {old_status!r} → {canon_status!r}")
            # tags 同步
            tags = fm.get("tags") or []
            if isinstance(tags, list):
                status_tag_map = {
                    "active": "status/active",
                    "withdrawn": "status/withdrawn",
                    "superseded": "status/superseded",
                    "draft": "status/draft",
                    "under_revision": "status/under-revision",
                }
                new_tag = status_tag_map.get(canon_status)
                if new_tag and new_tag not in tags:
                    # 移除旧 status/* tag
                    tags = [t for t in tags if not (isinstance(t, str) and t.startswith("status/"))]
                    tags.append(new_tag)
                    fm["tags"] = tags

    # 2.8) type 规范化
    old_type = fm.get("type")
    if isinstance(old_type, str):
        canon_type = _TYPE_ALIAS.get(old_type.strip())
        if canon_type and canon_type != old_type:
            fm["type"] = canon_type
            changes.append(f"type: {old_type!r} → {canon_type!r}")
            # tags 同步 type/* 前缀
            tags = fm.get("tags") or []
            if isinstance(tags, list):
                tags = [t for t in tags if not (isinstance(t, str) and t.startswith("type/"))]
                tags.insert(0, canon_type)
                fm["tags"] = tags

    # 2.9) reg_id 兜底（从文件名推导，若为空）
    import re as _re
    if not fm.get("reg_id"):
        # 从 path.stem 反推（已经是 canonical filename）
        stem = path.stem
        # 去掉 _dupN 后缀
        stem = _re.sub(r"_dup\d*$", "", stem)
        if stem:
            fm["reg_id"] = stem
            changes.append(f"reg_id_filled: {stem!r}")

    # 2.95) 若 reg_id 不含 Am/Rev/Corr 后缀但 source_file 暗示是修订单，推导并追加
    rid = fm.get("reg_id")
    if isinstance(rid, str) and rid.strip():
        has_am_rev = _re.search(r"\b(Am|Rev|Corr|XG|第\s*\d+\s*号修改单)", rid, _re.IGNORECASE)
        if not has_am_rev:
            src = fm.get("source_pdf") or fm.get("source_file") or ""
            if isinstance(src, str) and src:
                # 构造 shim 模拟 FileRecord
                class _ShimRec:
                    def __init__(self, p): self.path = p
                suffix = _derive_amendment_suffix(_ShimRec(src))
                if suffix:
                    new_rid = f"{rid} {suffix}".strip()
                    fm["reg_id"] = new_rid
                    changes.append(f"reg_id: {rid!r} → {new_rid!r} (amendment suffix from source)")
                    # 若原 type/version，但 suffix 含 Am/Corr（实质是修订单）→ 自动升级为 type/amendment
                    if fm.get("type") == "type/version" and _re.search(r"(Am|Corr)\d", suffix):
                        fm["type"] = "type/amendment"
                        tags = fm.get("tags") or []
                        if isinstance(tags, list):
                            tags = [t for t in tags if not (isinstance(t, str) and t.startswith("type/"))]
                            tags.insert(0, "type/amendment")
                            fm["tags"] = tags
                        changes.append("type: 'type/version' → 'type/amendment' (inferred from source suffix)")

    # 3) 文件重命名（若 reg_id 变化或当前名显然不规范）
    new_name = None
    current_stem = path.stem
    reg_id = fm.get("reg_id")
    if isinstance(reg_id, str) and reg_id.strip():
        expected_stem = _safe_filename(reg_id)
        if expected_stem != current_stem:
            # 也对现文件名先做一次 canonicalize，排除 UN vs ECE 前缀差异
            current_canon = _safe_filename(_canonicalize_reg_id(current_stem))
            # 保护：若现文件名（canonicalize 后）startswith expected_stem，说明只是多了描述后缀，保留。
            # 例：UN R048 Rev12 Am2 → canon → ECE R048 Rev12 Am2，startswith "ECE R048" → 保留
            if (
                current_canon.startswith(expected_stem)
                and len(current_canon) > len(expected_stem) + 2
            ):
                # 只需 canonicalize 前缀（UN → ECE），不需要换掉整个描述
                if current_canon != current_stem:
                    new_name = current_canon + ".md"
                # 否则完全保留
            else:
                new_name = expected_stem + ".md"

    # 4) 目录归位：FM.region 与所在文件夹不一致时移到正确目录
    new_dir = None
    fm_region = fm.get("region")
    cur_dir_name = path.parent.name
    if isinstance(fm_region, str) and fm_region and fm_region != cur_dir_name:
        proper_dir = path.parent.parent / fm_region
        if proper_dir.exists() or not proper_dir.parent.name.startswith("."):
            new_dir = proper_dir
            changes.append(f"move_dir: {cur_dir_name}/ → {fm_region}/")

    # 若没改动，返回
    if not changes and not new_name and not new_dir:
        return {"changed": [], "renamed_to": None}

    # 执行
    target_path = path
    target_parent = new_dir or path.parent
    target_name = new_name or path.name
    if new_dir or new_name:
        target_parent.mkdir(parents=True, exist_ok=True)
        candidate = target_parent / target_name
        # 避免覆盖已有文件（同名碰撞时加 _dupN 后缀）
        if candidate.exists() and candidate.resolve() != path.resolve():
            stem = Path(target_name).stem
            suf = Path(target_name).suffix
            for i in range(1, 50):
                alt = target_parent / f"{stem}_dup{i}{suf}"
                if not alt.exists():
                    candidate = alt
                    break
        target_path = candidate
        if target_path != path:
            if new_name and not new_dir:
                changes.append(f"rename: {path.name} → {target_path.name}")
            # 移动/重命名都在下面统一执行

    if not dry_run:
        _write_note(path, fm, body)
        if target_path != path:
            path.rename(target_path)

    return {"changed": changes, "renamed_to": target_path if target_path != path else None}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    all_md = list(WIKI_ROOT.glob("**/*.md"))
    print(f"Scanning {len(all_md)} notes under {WIKI_ROOT}...")

    n_double = 0
    n_renamed = 0
    n_moved = 0
    n_reg_id_changed = 0
    n_reg_id_filled = 0
    n_region_changed = 0
    n_status_changed = 0
    n_type_changed = 0
    samples_double = []
    samples_renamed = []
    samples_moved = []
    samples_region = []
    samples_status = []
    samples_type = []

    for path in all_md:
        try:
            r = _fix_note(path, dry_run=args.dry_run)
        except Exception as e:
            print(f"[red]Error on {path.name}: {e}")
            continue
        for c in r["changed"]:
            if c == "merged_double_fm":
                n_double += 1
                if len(samples_double) < 10:
                    samples_double.append(path.name)
            elif c.startswith("reg_id:"):
                n_reg_id_changed += 1
            elif c.startswith("reg_id_filled:"):
                n_reg_id_filled += 1
            elif c.startswith("region:"):
                n_region_changed += 1
                if len(samples_region) < 5:
                    samples_region.append(c)
            elif c.startswith("status:"):
                n_status_changed += 1
                if len(samples_status) < 5:
                    samples_status.append(c)
            elif c.startswith("type:"):
                n_type_changed += 1
                if len(samples_type) < 5:
                    samples_type.append(c)
            elif c.startswith("rename:"):
                n_renamed += 1
                if len(samples_renamed) < 10:
                    samples_renamed.append(c.split(": ", 1)[1])
            elif c.startswith("move_dir:"):
                n_moved += 1
                if len(samples_moved) < 10:
                    samples_moved.append(f"{path.name}: {c}")

    print(f"\n{'[DRY-RUN] ' if args.dry_run else ''}Fixes applied:")
    print(f"  - double_fm merged:     {n_double}")
    print(f"  - reg_id canonicalized: {n_reg_id_changed}")
    print(f"  - reg_id filled (from filename): {n_reg_id_filled}")
    print(f"  - region canonicalized: {n_region_changed}")
    print(f"  - status canonicalized: {n_status_changed}")
    print(f"  - type canonicalized:   {n_type_changed}")
    print(f"  - files renamed:        {n_renamed}")
    print(f"  - files moved (region): {n_moved}")

    if samples_moved:
        print("\n  move_dir samples:")
        for s in samples_moved:
            print(f"    - {s}")
    if samples_double:
        print("\n  double_fm samples:")
        for s in samples_double:
            print(f"    - {s}")
    if samples_status:
        print("\n  status samples:")
        for s in samples_status:
            print(f"    - {s}")
    if samples_type:
        print("\n  type samples:")
        for s in samples_type:
            print(f"    - {s}")
    if samples_region:
        print("\n  region samples:")
        for s in samples_region:
            print(f"    - {s}")
    if samples_renamed:
        print("\n  rename samples:")
        for s in samples_renamed:
            print(f"    - {s}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
