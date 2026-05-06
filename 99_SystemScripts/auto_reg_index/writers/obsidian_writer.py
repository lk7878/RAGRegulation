"""
ObsidianWriter · 把 extracted.md 写进 01_Wiki/

关键逻辑：
1. 按 region 和 type 选择目标目录
2. 按命名规范生成文件名
3. 如果目标文件已含 `status/manually-edited` tag，不覆盖（跳过或生成 .conflict 文件）
4. 更新 manifest state = written
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Optional

import yaml
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent.parent))

from manifest import Manifest, FileRecord

console = Console()

ROOT = Path(__file__).parent.parent
STAGING_DIR = ROOT / ".staging"
WIKI_ROOT = Path(os.getenv("WIKI_OUTPUT_DIR", "D:/CcVault/01_Wiki"))


# =============================================================
# Path resolution
# =============================================================
_REG_ID_KEYS = [
    "reg_id", "regulation_id", "standard_number", "standard_id",
    "id", "document_id", "spec_id",
]
_TITLE_KEYS = ["title_short", "title", "regulation_title", "standard_title"]
_AMENDMENT_KEYS = ["amendment_id", "amendment_number", "amendment"]

# Region canonicalisation: LLM 经常返回中文或其他变体，统一到标准代码
# 与 stages.s1_extract._REGION_ALIASES 保持一致
_REGION_ALIASES = {
    "中国": "cn", "中华人民共和国": "cn", "cn": "cn", "china": "cn", "gb": "cn",
    "美国": "us", "美利坚合众国": "us", "us": "us", "usa": "us",
    "欧盟": "eu", "欧洲联盟": "eu", "eu": "eu",
    "联合国欧洲经济委员会": "ece", "ece": "ece", "unece": "ece", "un": "ece",
    "日本": "jp", "jp": "jp", "japan": "jp",
    "韩国": "kr", "大韩民国": "kr", "kr": "kr", "korea": "kr",
    "印度": "in", "in": "in", "india": "in",
    "巴西": "br", "br": "br", "brazil": "br",
    "智利": "cl", "cl": "cl", "chile": "cl",
    "澳大利亚": "au", "au": "au", "australia": "au",
    "南非": "za", "za": "za",
    "印度尼西亚": "id", "id": "id", "indonesia": "id",
    "马来西亚": "my", "my": "my", "malaysia": "my",
    "泰国": "th", "th": "th", "thailand": "th",
    "越南": "vn", "vn": "vn", "vietnam": "vn",
    "沙特阿拉伯": "sa", "sa": "sa", "saudi arabia": "sa",
    "东盟": "asean", "asean": "asean",
    "海合会": "gcc", "gcc": "gcc", "gso": "gcc",
    "俄罗斯": "ru-eaeu", "欧亚经济联盟": "ru-eaeu", "ru-eaeu": "ru-eaeu",
    "ru": "ru-eaeu", "eaeu": "ru-eaeu", "ea": "ru-eaeu",
}


def _canonical_region(raw: Optional[str]) -> Optional[str]:
    if not raw:
        return None
    key = str(raw).strip().lower()
    return _REGION_ALIASES.get(key, _REGION_ALIASES.get(str(raw).strip(), None))


def _first_nonempty(fm: dict, keys: list[str]) -> Optional[str]:
    """From a dict, return the first non-empty string value for any of the given keys.
    Skips obviously-bad values like source-file UUIDs or raw ECE filename stems."""
    for k in keys:
        v = fm.get(k)
        if v and isinstance(v, str) and v.strip():
            val = v.strip()
            # Skip values that look like "<something>_upload_<uuid>"
            if re.search(r"_upload_[0-9a-f-]{20,}", val, re.IGNORECASE):
                continue
            # Skip raw ECE filename stems like "R094r4am1e" / "R048r12am10e" / "R013Hr4am1e"
            # (they contain lowercase 'r' + digits; a proper reg_id would be "ECE R94" / "ECE R13H")
            if re.fullmatch(r"R\d{2,4}[Hh]?r\d+(?:am\d+)?[a-z]?", val):
                continue
            return val
    return None


# Patterns to derive canonical regulation IDs from file paths
# 支持 H 后缀：R013Hr4am1e.pdf → "ECE R13H"
_ECE_FILENAME_RE = re.compile(r"R(\d{2,4})([Hh])?(?:r(\d+))?(?:am(\d+))?(?:[a-z])?\.pdf", re.IGNORECASE)


def _derive_canonical_reg_id(rec: Optional["FileRecord"]) -> Optional[str]:
    """从文件路径/名称提取规范 reg_id（ECE R94 / ECE R13H / GB 4785-2007 等），当 LLM 输出不可用时兜底。"""
    if not rec:
        return None
    name = Path(rec.path).name
    # ECE: R094r4am1e.pdf → "ECE R94"；R013Hr4am1e.pdf → "ECE R13H"（上层 _canonicalize_reg_id 会再加 Rev/Am 后缀）
    m = _ECE_FILENAME_RE.search(name)
    if m:
        num = int(m.group(1))
        h = (m.group(2) or "").upper()
        return f"ECE R{num}{h}"
    # GB with year: GB 4785-2019 / 4785-2019-gb
    m = re.search(r"(GB\s*)?(\d{4,5})-(\d{4})", name, re.IGNORECASE)
    if m:
        return f"GB {m.group(2)}-{m.group(3)}"
    # FMVSS / KMVSS
    m = re.search(r"(FMVSS|KMVSS)\s*(\d{2,4})", name, re.IGNORECASE)
    if m:
        return f"{m.group(1).upper()} {m.group(2)}"
    return None


def _derive_amendment_suffix(rec: Optional["FileRecord"]) -> Optional[str]:
    """从文件名提取修改单后缀：ECE 'Rev4 Am1' / 'Rev2 Corr2' / 中文 '第 N 号修改单'

    处理的 ECE PDF 命名模式（后缀顺序可变）：
      - R094r4am1e    → Rev4 Am1
      - R094r4e       → Rev4
      - R094am1e      → Am1
      - R094r2c2e     → Rev2 Corr2
      - R094c1e       → Corr1
      - R094r1a1e     → Rev1 Am1 (`a` = amendment 简写)
      - R094a1e       → Am1
    """
    if not rec:
        return None
    name = Path(rec.path).stem
    # 中文优先（避免 ECE regex 误伤）
    m = re.search(r"(第\s*\d+\s*号修改单|XG\d+(?:-\d+)?)", rec.path)
    if m:
        return m.group(1)

    # ECE: R<num>[H]{r<rev>}{am<am>|a<am>|c<corr>}e
    m = re.match(
        r"^R(\d{1,4})([Hh])?(?:r(\d+))?(?:(am|a)(\d+))?(?:c(\d+))?[a-z]?",
        name,
        re.IGNORECASE,
    )
    if m:
        _num, _h, rev, _, am, corr = m.groups()
        parts: list[str] = []
        if rev:
            parts.append(f"Rev{rev}")
        if am:
            parts.append(f"Am{am}")
        if corr:
            parts.append(f"Corr{corr}")
        if parts:
            return " ".join(parts)
    return None


def _infer_type(frontmatter: dict, rec: Optional["FileRecord"] = None) -> str:
    """确定 note 的 type。
    规则（PDF 源的文件不会是 type/regulation —— 那是后续综合的主条目）：
      - path/文件名 含 '修改单'/'amendment' 或 ECE `am\\d+` → type/amendment
      - 其他 PDF → type/version
      - 非 PDF（或无 rec）且 LLM 声明了 type → 尊重 LLM
    """
    declared = frontmatter.get("type") or frontmatter.get("node_type")
    declared = declared if (isinstance(declared, str) and declared.startswith("type/")) else None

    path_hay = " ".join(
        str(v) for v in [
            frontmatter.get("amendment"),
            frontmatter.get("amendment_id"),
            frontmatter.get("document_type"),
            frontmatter.get("regulation_type"),
            rec.path if rec else "",
        ] if v
    ).lower()

    # ECE amendment pattern: R<num>r<rev>am<amnum>e (e.g. R094r4am1e)
    is_ece_amendment = bool(re.search(r"r\d{1,3}(?:r\d+)?am\d+e\b", path_hay))
    is_cn_amendment = any(kw in path_hay for kw in ["修改单", "amendment", "xg1", "xg2", "xg3"])

    if is_ece_amendment or is_cn_amendment:
        return "type/amendment"

    # PDF-sourced notes are always versions (not main regulation entries)
    if rec and rec.path.lower().endswith(".pdf"):
        return "type/version"

    # 非 PDF 或无 rec：尊重 LLM 声明
    if declared in {"type/regulation", "type/version", "type/amendment",
                    "type/test-method", "type/dummy", "type/injury-metric",
                    "type/vehicle-class", "type/topic"}:
        return declared
    return "type/version"


def _target_dir_for(frontmatter: dict, rec: Optional["FileRecord"] = None) -> Path:
    """Decide target dir based on type + region"""
    node_type = _infer_type(frontmatter, rec)
    region = (
        _canonical_region(frontmatter.get("region"))
        or _canonical_region(rec.region if rec else None)
        or "cn"
    )

    if node_type in {"type/regulation", "type/version", "type/amendment"}:
        return WIKI_ROOT / "regulations" / region
    if node_type == "type/test-method":
        return WIKI_ROOT / "test-methods"
    if node_type == "type/dummy":
        return WIKI_ROOT / "dummies"
    if node_type == "type/injury-metric":
        return WIKI_ROOT / "injury-metrics"
    if node_type == "type/vehicle-class":
        return WIKI_ROOT / "vehicle-classes"
    if node_type == "type/topic":
        return WIKI_ROOT / "topics"
    return WIKI_ROOT / "regulations" / region


def _filename_for(frontmatter: dict, rec: Optional["FileRecord"] = None) -> str:
    """生成文件名。支持多种字段名；缺字段时用 rec.path 兜底保证唯一性。"""
    node_type = _infer_type(frontmatter, rec)

    # 先从 frontmatter 挑 reg_id / title
    reg_id = _first_nonempty(frontmatter, _REG_ID_KEYS)
    title = _first_nonempty(frontmatter, _TITLE_KEYS)

    # 兜底：从 rec.path 推规范 reg_id（ECE "UN R94" / "GB 4785-2007" / FMVSS 等）
    if not reg_id:
        reg_id = _derive_canonical_reg_id(rec)
    if not reg_id and rec:
        stem = Path(rec.path).stem
        stem = re.sub(r"_upload_[0-9a-f\-]+$", "", stem)
        reg_id = stem.strip() or "UNKNOWN"
    if not reg_id:
        reg_id = "UNKNOWN"

    if node_type == "type/regulation":
        # 主条目用 reg_id + title_short（若短）。过长 title 不入文件名（避免 255 字符上限）
        title_short = frontmatter.get("title_short")
        if isinstance(title_short, str) and 0 < len(title_short) <= 30:
            name = f"{reg_id} {title_short}".strip()
        else:
            name = reg_id
        return f"{_sanitize_filename(name)}.md"

    if node_type == "type/version":
        return f"{_sanitize_filename(reg_id)}.md"

    if node_type == "type/amendment":
        amendment_id = _first_nonempty(frontmatter, _AMENDMENT_KEYS)
        suffix = _derive_amendment_suffix(rec)
        if amendment_id and not re.fullmatch(r"R\d{2,4}r\d+am\d+[a-z]?", amendment_id):
            # 有 LLM 给的有效 amendment_id，组合
            name = f"{reg_id} {amendment_id}" if reg_id not in amendment_id else amendment_id
        elif suffix:
            name = f"{reg_id} {suffix}"
        else:
            name = reg_id
        return f"{_sanitize_filename(name)}.md"

    if node_type in {"type/test-method", "type/dummy", "type/injury-metric"}:
        key = node_type.split("/")[-1].replace("-", "_") + "_id"
        id_val = frontmatter.get(key) or reg_id
        last = id_val.split("/")[-1] if "/" in id_val else id_val
        return f"{_sanitize_filename(last)}.md"

    if node_type == "type/vehicle-class":
        class_id = frontmatter.get("class_id") or reg_id
        return f"{_sanitize_filename(class_id)}.md"

    if node_type == "type/topic":
        topic_id = frontmatter.get("topic_id", "topic/unknown")
        if title:
            return f"{_sanitize_filename(title)}.md"
        return f"{_sanitize_filename(topic_id.replace('/', '_'))}.md"

    # 最终 fallback
    return f"{_sanitize_filename(reg_id)}.md"


def _sanitize_filename(name: str, *, max_len: int = 100) -> str:
    """移除 Windows 文件名非法字符 + 规整空白 + 截断超长名（默认 100 chars）。
    Windows 非法: \\ / : * ? " < > |
    把 / \\ : 替换成空格（保留可读性），其它非法字符直接删。"""
    s = re.sub(r'[\\/:]+', " ", name)
    s = re.sub(r'[*?"<>|]+', "", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > max_len:
        s = s[:max_len].rstrip()
    return s or "UNKNOWN"


# =============================================================
# Safety checks
# =============================================================
def _is_manually_edited(path: Path) -> bool:
    """检查目标文件是否已被手动编辑"""
    if not path.exists():
        return False
    try:
        content = path.read_text(encoding="utf-8")
        # 简单匹配 tags: 下的 status/manually-edited
        return "status/manually-edited" in content
    except Exception:
        return False


# =============================================================
# Main write
# =============================================================
def write_note(rec: FileRecord, mf: Manifest, *, force_overwrite: bool = False) -> Optional[Path]:
    """把一份 extracted.md 写入 01_Wiki"""
    stage_dir = STAGING_DIR / rec.content_hash[:2] / rec.content_hash
    extracted = stage_dir / "extracted.md"
    if not extracted.exists():
        rec.mark_failed(f"extracted.md missing at {extracted}")
        return None

    content = extracted.read_text(encoding="utf-8")
    parts = content.split("---", 2)
    if len(parts) < 3:
        rec.mark_failed("extracted.md has no frontmatter")
        return None
    _, yaml_str, body = parts
    try:
        frontmatter = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError as e:
        rec.mark_failed(f"YAML parse error: {e}")
        return None

    # Normalize field names / enum values (in case extracted.md was produced
    # by an older pipeline version without normalization applied)
    try:
        from stages.s1_extract import _normalize_frontmatter
        frontmatter = _normalize_frontmatter(frontmatter)
    except Exception:
        pass  # Normalization best-effort; pass-through on any error

    # 让 frontmatter 的 type 与 _infer_type 的结果一致（LLM 可能误判）
    inferred_type = _infer_type(frontmatter, rec)
    if inferred_type and frontmatter.get("type") != inferred_type:
        frontmatter["type"] = inferred_type
        # Update tags to match
        tags = frontmatter.get("tags") or []
        if isinstance(tags, list):
            tags = [t for t in tags if not (isinstance(t, str) and t.startswith("type/"))]
            tags.insert(0, inferred_type)
            frontmatter["tags"] = tags

    # 若 reg_id 是文件名原样（如 "R094r4am1e"），换成规范 ID（"UN R94"）
    current_reg_id = frontmatter.get("reg_id")
    if isinstance(current_reg_id, str) and re.fullmatch(r"R\d{2,4}r\d+(?:am\d+)?[a-z]?", current_reg_id.strip()):
        canonical = _derive_canonical_reg_id(rec)
        if canonical:
            frontmatter["reg_id"] = canonical

    target_dir = _target_dir_for(frontmatter, rec)
    target_dir.mkdir(parents=True, exist_ok=True)
    filename = _filename_for(frontmatter, rec)
    target = target_dir / filename

    # 用归一化后的 frontmatter 重新序列化，保证 01_Wiki 输出 schema-compliant
    normalized_content = (
        "---\n"
        + yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
        + "---\n\n"
        + body.lstrip()
    )

    # 防止覆盖人工精修
    if _is_manually_edited(target) and not force_overwrite:
        conflict = target.with_suffix(".conflict.md")
        conflict.write_text(normalized_content, encoding="utf-8")
        rec.advance_to(
            "written",
            note=f"target manually-edited; saved as {conflict.name}",
        )
        return conflict

    # 碰撞保护：目标存在，但它的 source_pdf 和当前 rec 不同，说明不同的源 PDF
    # 产生了相同文件名（writer 的 _filename_for + _derive_amendment_suffix 没能区分）。
    # 加 _dup<N> 后缀确保不同源不覆盖。
    if target.exists() and not force_overwrite:
        try:
            existing = target.read_text(encoding="utf-8")
            ex_end = existing.find("\n---", 4) if existing.startswith("---") else -1
            existing_fm = yaml.safe_load(existing[4:ex_end]) if ex_end > 0 else {}
            existing_src = (existing_fm or {}).get("source_pdf") or (existing_fm or {}).get("source_file")
            current_src = frontmatter.get("source_pdf") or frontmatter.get("source_file")
            same_source = (
                isinstance(existing_src, str)
                and isinstance(current_src, str)
                and existing_src.replace("\\", "/") == current_src.replace("\\", "/")
            )
        except Exception:
            same_source = False

        if not same_source:
            # 寻找可用的 _dupN 后缀
            stem = target.stem
            suffix = target.suffix
            for i in range(1, 50):
                alt = target.with_name(f"{stem}_dup{i}{suffix}")
                if not alt.exists():
                    target = alt
                    break

    target.write_text(normalized_content, encoding="utf-8")
    rec.advance_to("written", note=str(target.relative_to(WIKI_ROOT)))
    return target


def run_batch(mf: Manifest, *, limit: Optional[int] = None) -> dict:
    """把所有 state 为 verified / extracted 的 note 写入 wiki"""
    # extracted 或 verified 都可以写；needs_review 也写（只是标了 tag）
    eligible_states = {"extracted", "verified", "needs_review"}
    pending = [rec for rec in mf.records.values() if rec.state in eligible_states]
    if limit:
        pending = pending[:limit]

    stats = {"written": 0, "conflict": 0, "failed": 0}
    for rec in pending:
        try:
            target = write_note(rec, mf)
            if target is None:
                stats["failed"] += 1
            elif target.name.endswith(".conflict.md"):
                stats["conflict"] += 1
            else:
                stats["written"] += 1
        except Exception as e:
            rec.mark_failed(f"write error: {e}")
            stats["failed"] += 1

    mf.save()
    console.print(f"[green]Write done:[/green] {stats}")
    return stats


if __name__ == "__main__":
    mf = Manifest.load_or_create()
    run_batch(mf)
