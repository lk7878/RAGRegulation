"""
Stage 1 · DeepSeek V3 结构化抽取

输入：state=ocr_done 的文件，读 .staging/{hash}/raw.md
输出：.staging/{hash}/extracted.md（YAML frontmatter + Markdown body）
状态：state → extracted / failed
"""
from __future__ import annotations

import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

sys.path.insert(0, str(Path(__file__).parent.parent))

from manifest import Manifest, FileRecord
from llm import DeepSeekClient
from llm.prompts import load_prompt

console = Console()

ROOT = Path(__file__).parent.parent
STAGING_DIR = ROOT / ".staging"

# Max input chars (~40k tokens) sent to DeepSeek per call. Longer files are chunked.
MAX_INPUT_CHARS = 120_000


def _staging_path(rec: FileRecord) -> Path:
    return STAGING_DIR / rec.content_hash[:2] / rec.content_hash


def _guess_reg_id_from_filename(rec: FileRecord) -> str:
    """从文件路径推断 reg_id 作为 prompt 的提示"""
    name = Path(rec.path).stem
    # 去除 (1)(2) 等副本标记
    for suf in ["(1)", "(2)", "(3)", "(4)", "(5)"]:
        name = name.replace(suf, "")
    # 常见的版本/修改单号模式：GB 4785-2019, ECE R48-06, FMVSS 208
    return name.strip()


def _guess_region_from_path(rec: FileRecord) -> Optional[str]:
    """从路径推断 region"""
    p = rec.path.lower()
    if "国内法规" in rec.path or "gb" in p:
        return "cn"
    if "ece" in p or "ece标准" in rec.path:
        return "ece"
    if "欧盟" in rec.path or "/eu/" in p:
        return "eu"
    if "fmvss" in p or "美国" in rec.path:
        return "us"
    if "日本" in rec.path:
        return "jp"
    if "韩国" in rec.path:
        return "kr"
    return None


def _parse_llm_output(text: str) -> tuple[dict, str]:
    """
    解析 LLM 输出为 (frontmatter_dict, markdown_body)，容忍多种格式：
      A. `---\\nyaml\\n---\\nbody`（标准 frontmatter）
      B. `key: value\\n...\\n<markdown body>`（无 --- 包裹）
      C. 前后加了 ```yaml / ```markdown code fence
      D. 前置 "Here is..." explanation 行
      E. Output 截断（YAML 中途截断或 body 不完整）
      F. YAML 后紧跟 ``` 反引号（LLM 误加 code fence）
      G. Body 使用 **bold** 而非 ## heading
    """
    # BOM 会让首行 key-match 失败，导致 reg_id 等字段被当作 "前置解释" 吃掉
    text = text.lstrip("\ufeff")
    text = text.strip()

    # 1) Strip outer code fences (only at very start/end of whole text)
    text = re.sub(r"^```(?:yaml|markdown|md)?\s*\n?", "", text)
    text = re.sub(r"\n?\s*```\s*$", "", text)
    text = text.strip()

    # 2) Strip any leading explanation lines before first YAML content
    lines = text.split("\n")
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if s == "---" or re.match(r"^[A-Za-z_][A-Za-z0-9_.-]*\s*:\s", s):
            start = i
            break
    text = "\n".join(lines[start:])

    # 3) Case A: --- ... --- ... body
    if text.startswith("---"):
        rest = text[3:].lstrip("\n")
        m = re.search(r"\n---\s*(\n|$)", rest)
        if m:
            yaml_str = rest[: m.start()]
            body = rest[m.end():].strip()
            fm = _safe_yaml_load(yaml_str)
            if fm:
                return fm, body
        fm = _safe_yaml_load(rest)
        if fm:
            return fm, ""

    # 4) Case B/G: incremental YAML boundary detection.
    #    Walk line by line, keep lines that look like YAML; stop at first body-ish line.
    yaml_str, body = _split_yaml_and_body(text)
    fm = _safe_yaml_load(yaml_str)
    if fm:
        return fm, body

    # 5) Total failure
    console.print("[yellow]_parse_llm_output: could not parse any YAML, returning empty frontmatter[/yellow]")
    return {}, text


# Pattern for a YAML key line: `key: value` or `key:` (multiline scalar start)
_YAML_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*\s*:(?:\s|$)")


def _split_yaml_and_body(text: str) -> tuple[str, str]:
    """Walk lines, keep every line that belongs to the YAML block. Stop at first body-like line.

    A line is considered "still in YAML" if it matches any of:
      - blank line (allowed inside YAML between keys)
      - starts with a YAML key: `name:` or `name: value`
      - starts with indentation (>= 2 spaces or a tab) — list items, nested dicts, continued scalars
      - starts with `- ` at col 0 — top-level list item
      - is `---` (YAML doc separator, also used as frontmatter close)
      - is a markdown code fence ```...``` — these sometimes appear inside YAML; skip them
    """
    lines = text.split("\n")
    yaml_end = len(lines)
    seen_mapping_key = False  # 若已出现 top-level `key: value`，则不允许再混入 top-level `- item`
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        # Blank lines: keep walking (could be between YAML keys)
        if not stripped:
            continue
        # Stray code fence: drop it from output but keep walking
        if stripped.startswith("```"):
            continue
        # --- separator: end of YAML block
        if stripped == "---":
            yaml_end = i
            break
        # YAML key line
        if _YAML_KEY_RE.match(stripped):
            seen_mapping_key = True
            continue
        # Indented continuation / list items
        if line.startswith(("  ", "\t")):
            continue
        # Top-level `- item`：只有在还没见过 mapping key 时才当 YAML list；
        # 否则（前面已经是 `reg_id: ...` 等 mapping）视为 markdown bullet → body
        if stripped.startswith("- ") and not seen_mapping_key:
            continue
        # Otherwise this line is body
        yaml_end = i
        break

    yaml_lines = [ln for ln in lines[:yaml_end] if not ln.lstrip().startswith("```")]
    yaml_str = "\n".join(yaml_lines).strip()

    body_lines = lines[yaml_end:]
    # Drop leading --- (frontmatter closing) if present
    while body_lines and body_lines[0].strip() in ("---", ""):
        body_lines.pop(0)
    body = "\n".join(body_lines).strip()
    return yaml_str, body


# =============================================================
# Schema normalization (canonicalize LLM's drifted field names/values)
# =============================================================
# LLM 喜欢用自己的命名（pub_date / release_date / issuer / enforce_date...）。
# 统一映射到 02_Schema/03_frontmatter_schema.md 里的规范字段名。
_FIELD_ALIAS: dict[str, str] = {
    # id / 标准号
    "id": "reg_id",
    "regulation_id": "reg_id",
    "standard_number": "reg_id",
    "standard_id": "reg_id",
    "document_id": "reg_id",
    "spec_id": "reg_id",
    # title
    "regulation_title": "title",
    "standard_title": "title",
    # 发布日期
    "release_date": "publication_date",
    "issue_date": "publication_date",
    "pub_date": "publication_date",
    "date_issued": "publication_date",
    "issued_date": "publication_date",
    # 实施日期
    "enforcement_date": "implementation_date_new_vehicle",
    "enforce_date": "implementation_date_new_vehicle",
    "imp_date": "implementation_date_new_vehicle",
    "implementation_date": "implementation_date_new_vehicle",
    "effective_date": "implementation_date_new_vehicle",
    "date_effective": "implementation_date_new_vehicle",
    "eff_date": "implementation_date_new_vehicle",
    # 归口单位
    "issuing_body": "standard_body",
    "issuing_authority": "standard_body",
    "issuer": "standard_body",
    "department": "standard_body",
    "issued_by": "standard_body",
    # 取代关系
    "previous_reg_id": "supersedes",
    "replaces": "supersedes",
    "replace": "supersedes",
    "replaced_standard": "supersedes",
    "superseded": "supersedes",
    "replacing_standard": "superseded_by",
    "replaced_by": "superseded_by",
    "succeeded_by": "superseded_by",
    # 修改单专用
    "amendment_number": "amendment_number",  # schema-aligned, keep
    "parent_standard": "parent_version",
    "modifies": "parent_version",
}

# type 值归一化
_TYPE_ALIAS: dict[str, str] = {
    "type/standard": "type/version",
    "type/national-standard": "type/version",
    "type/regulation-version": "type/version",
    "type/version": "type/version",
    "type/vehicle_approval": "type/version",
    "type/global_technical_regulation": "type/version",
    "type/technical_regulation": "type/version",
    "type/amendment": "type/amendment",
    "type/modification": "type/amendment",
    "type/corrigendum": "type/amendment",
    "type/erratum": "type/amendment",
    "type/regulation": "type/regulation",
}

# status 值归一化
_STATUS_ALIAS: dict[str, str] = {
    "现行": "active",
    "现行有效": "active",
    "有效": "active",
    "生效": "active",
    "已生效": "active",
    "active": "active",
    "valid": "active",
    "final": "active",
    "final text": "active",
    "in force": "active",
    "in-force": "active",
    "in_force": "active",
    "inforce": "active",
    "effective": "active",
    "current": "active",
    "published": "active",
    "retained": "active",
    "mandatory": "active",
    "已废止": "withdrawn",
    "废止": "withdrawn",
    "作废": "withdrawn",
    "withdrawn": "withdrawn",
    "repealed": "withdrawn",
    "obsolete": "withdrawn",
    "被取代": "superseded",
    "取代": "superseded",
    "superseded": "superseded",
    "replaced": "superseded",
    "草稿": "draft",
    "draft": "draft",
    "征求意见稿": "draft",
    "提案申请": "draft",
    "proposal": "draft",
    "修订中": "under_revision",
    "under revision": "under_revision",
    "under_revision": "under_revision",
    "under-revision": "under_revision",
    # 修订单类：corrigendum / erratum / amended 等应视为「已发布的修订单」→ active
    "amendment": "active",
    "amended": "active",
    "修正": "active",
    "corrigendum": "active",
    "erratum": "active",
    # LLM 错把 tag 填到 status
    "type/status/active": "active",
    "type/active": "active",
    # 未知显式值 → 保留 "unknown"（schema 允许）
    "unknown": "unknown",
    "未知": "unknown",
}


# ECE PDF stem 正则：带 H 后缀支持（R13H = Harmonized passenger cars braking 等变体）
# ECE 仅 R13H 确定存在，但为容纳未来新变体泛化为 H/h
_ECE_STEM_RE = re.compile(
    r"^R(\d{1,4})([Hh])?(?:r(\d+))?(?:(am|a)(\d+))?(?:c(\d+))?[a-z]?$",
    re.IGNORECASE,
)
# 带 ECE/UN/UNECE 前缀的 stem：'ECE R008r4e' / 'UN R094r4am1e' / 'UN R13H Rev4 Am4'
_PREFIXED_ECE_STEM_RE = re.compile(
    r"^(?:ECE|UN|UNECE)[-\s]?R(\d{1,4})([Hh])?(?:r(\d+))?(?:(am|a)(\d+))?(?:c(\d+))?[a-z]?$",
    re.IGNORECASE,
)


# 用于提取内嵌 stem 的正则（无 anchor，可出现在字符串中间）
_STEM_INLINE_RE = re.compile(
    r"\bR(\d{1,4})([Hh])?(?:r(\d+))?(?:(am|a)(\d+))?(?:c(\d+))?[a-z]?\b",
    re.IGNORECASE,
)


def _canonicalize_reg_id(reg_id: str) -> str:
    """把 LLM 可能漂移的 reg_id 格式归一化。

    规则：
      - `R094r4am1e` / `R088am1e` 等 ECE PDF stem → `ECE R94 Rev4 Am1` / `ECE R88 Am1`
      - `ECE R008r4e` / `UN R094r4am1e` 等带前缀 stem → `ECE R8 Rev4` / `ECE R94 Rev4 Am1`
      - `ECE R48r12am10e Rev12 Am10` 混合型 → `ECE R48 Rev12 Am10`（合并去重）
      - `ECE-R<n>` / `UNECE-R<n>` / `UN-R<n>` → `ECE R<n>` (破折号 → 空格)
      - `ECE-R<n>-am<k>` / `ECE R<n>-am<k>` → `ECE R<n> Am<k>` (amendment 后缀)
      - `ECE-R<n>-rev<k>` / `R<n>rev<k>` → `ECE R<n> Rev<k>`
      - 多空格合并为单空格
    """
    if not isinstance(reg_id, str):
        return reg_id
    s = reg_id.strip()
    # 先去掉中间或末尾的 `_\d+` 文件名副本标记（如 `R001r4e_1` → `R001r4e`，`R021r2e_1 Rev2` → `R021r2e Rev2`）
    s = re.sub(r"_\d+(?=\s|$)", "", s)
    # 预处理：`ECE R13-H` / `ECE-R13-H` / `UN R13-H` → 把 -H/-h 归一为紧贴的 H
    s = re.sub(r"(R\d{1,4})[-\s]+([Hh])\b", r"\1\2", s)
    # 带前缀的 ECE stem 优先（完整匹配）：'ECE R008r4e'、'UN R094r4am1e'、'UN R13H Rev4 Am4'
    m = _PREFIXED_ECE_STEM_RE.match(s)
    if m:
        num, h_suffix, rev, _, am, corr = m.groups()
        num_int = int(num)
        h = h_suffix.upper() if h_suffix else ""
        parts = [f"ECE R{num_int}{h}"]
        if rev:
            parts.append(f"Rev{int(rev)}")
        if am:
            parts.append(f"Am{int(am)}")
        if corr:
            parts.append(f"Corr{int(corr)}")
        return " ".join(parts)
    # ECE PDF stem 兜底（完整匹配）：R094r4am1e / R088am1e / R135e / R013Hr4am1e
    m = _ECE_STEM_RE.match(s)
    if m:
        num, h_suffix, rev, _, am, corr = m.groups()
        num_int = int(num)
        h = h_suffix.upper() if h_suffix else ""
        parts = [f"ECE R{num_int}{h}"]
        if rev:
            parts.append(f"Rev{int(rev)}")
        if am:
            parts.append(f"Am{int(am)}")
        if corr:
            parts.append(f"Corr{int(corr)}")
        return " ".join(parts)
    # 混合型：'ECE R48r12am10e Rev12 Am10' — 提取内嵌 stem，把它前面的前缀 + stem
    # 替换为 canonical 'ECE R<num>'；再加上后面已有的 Rev/Am/Corr 文字（去重）
    m = _STEM_INLINE_RE.search(s)
    if m and re.match(r"^(?:ECE|UN|UNECE)?[-\s]*R\d", s, re.IGNORECASE):
        full = m.group(0)
        # 只处理 stem 带后缀的情况（有 H / r\d / am\d / c\d / 结尾字母）
        if re.search(r"r\d|am\d|a\d|c\d|[a-z]$", full, re.IGNORECASE) and full.lower() != f"r{int(m.group(1))}":
            num, h_suffix, rev, _, am, corr = m.groups()
            num_int = int(num)
            h = h_suffix.upper() if h_suffix else ""
            # 构造 canonical 片段
            canon_parts = [f"ECE R{num_int}{h}"]
            if rev:
                canon_parts.append(f"Rev{int(rev)}")
            if am:
                canon_parts.append(f"Am{int(am)}")
            if corr:
                canon_parts.append(f"Corr{int(corr)}")
            canon = " ".join(canon_parts)
            # 把 'ECE/UN/UNECE [prefix-sep] R\d\d\d[H][stem junk]' 整体替换为 canon
            s_new = re.sub(
                r"^(?:ECE|UN|UNECE)?[-\s]*R\d{1,4}[Hh]?(?:r\d+)?(?:(?:am|a)\d+)?(?:c\d+)?[a-z]?",
                canon,
                s,
                count=1,
                flags=re.IGNORECASE,
            )
            # 去重：如果尾部重复了 Rev<n> / Am<n> / Corr<n>，保留一个
            for tok in re.findall(r"\b(Rev|Am|Corr)(\d+)\b", canon):
                patt = re.escape(tok[0] + tok[1])
                # 保留第一个，删除后续（整词）
                count = 0
                def _sub(match, _count=[0]):
                    _count[0] += 1
                    return "" if _count[0] > 1 else match.group(0)
                s_new = re.sub(rf"\b{patt}\b", _sub, s_new)
            s = re.sub(r"\s+", " ", s_new).strip()
            return s
    # UN/UNECE → ECE（保留 H 后缀）
    s = re.sub(r"^(?:UNECE|UN)[-\s]?R(\d+)([Hh])?", lambda m: f"ECE R{m.group(1)}{(m.group(2) or '').upper()}", s, flags=re.IGNORECASE)
    # ECE-R<n>[H] → ECE R<n>[H]
    s = re.sub(r"^ECE[-\s]?R(\d+)([Hh])?", lambda m: f"ECE R{m.group(1)}{(m.group(2) or '').upper()}", s, flags=re.IGNORECASE)
    # 剥离括号内容（只剥"含 Rev./Amend./Corr. 的版本注释括号"，保留 (EU) (2026) 等普通括号）
    s = re.sub(
        r"\s*[\(（][^）\)]*(?:Rev|Amend|Corr)\.?\s*\d+[^）\)]*[\)）]",
        "",
        s,
        flags=re.IGNORECASE,
    )
    # 后缀：am/amend/amendment N（前缀分隔符可为 空格/破折号/斜杠/逗号；数字前可为 空格/点/破折号） → Am<N>
    s = re.sub(r"[-\s/,]am(?:end(?:ment)?)?[-\s.]?(\d+)", r" Am\1", s, flags=re.IGNORECASE)
    # 后缀：rev/revision N → Rev<N>
    s = re.sub(r"[-\s/,]rev(?:ision)?[-\s.]?(\d+)", r" Rev\1", s, flags=re.IGNORECASE)
    # 后缀：corr/corrigendum N → Corr<N>
    s = re.sub(r"[-\s/,]corr(?:igendum)?[-\s.]?(\d+)", r" Corr\1", s, flags=re.IGNORECASE)
    # 清理伪 Rev<NNN>：如果 "ECE R<N> ... Rev<N>" 中 Rev 后数字 == R 法规号，视为 LLM 误抽取
    m_reg = re.match(r"^ECE R(\d+)", s)
    if m_reg:
        reg_num = m_reg.group(1)
        s = re.sub(rf"\s+Rev{reg_num}\b", "", s)
    # 后缀 token 去重（Rev4 Am2 Rev4 Am2 → Rev4 Am2）
    for token_type in ("Rev", "Am", "Corr"):
        positions = list(re.finditer(rf"\b{token_type}(\d+)\b", s))
        if len(positions) > 1:
            seen: set[str] = set()
            parts: list[str] = []
            last_end = 0
            for m in positions:
                tok = m.group(0)
                if tok in seen:
                    parts.append(s[last_end : m.start()])
                    last_end = m.end()
                else:
                    seen.add(tok)
            parts.append(s[last_end:])
            s = "".join(parts)
    # 合并多余空格
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Region 规范化（与 obsidian_writer._REGION_ALIASES 保持一致）
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


def _canonicalize_region(region) -> Optional[str]:
    if not region:
        return None
    key = str(region).strip().lower()
    return _REGION_ALIASES.get(key, _REGION_ALIASES.get(str(region).strip()))


def _normalize_frontmatter(fm: dict) -> dict:
    """把 LLM 输出的 frontmatter 归一化到 schema 标准字段名/值。

    规则：
      1. 把别名 key 改成标准 key（如 pub_date → publication_date）；
         对应的 _conf / _reason 后缀字段同步重命名。
      2. 归一化 type / status / region 值。
      3. 归一化 reg_id（ECE-R<n> → ECE R<n> 等）。
      4. wikilink 包装（supersedes / superseded_by / parent_version）。
      5. 修改单从 reg_id 推导 amendment_id / amendment_number / parent_version。
      6. 兜底补 tags（基于 type + region + status）。
    """
    if not isinstance(fm, dict):
        return fm
    out: dict = {}
    for k, v in fm.items():
        base_key = k
        suffix = ""
        for suf in ("_conf", "_reason"):
            if k.endswith(suf):
                base_key = k[: -len(suf)]
                suffix = suf
                break
        canonical_base = _FIELD_ALIAS.get(base_key, base_key)
        canonical_key = canonical_base + suffix
        if canonical_key in out and canonical_key != k:
            continue
        out[canonical_key] = v

    # 归一化 type
    if "type" in out and isinstance(out["type"], str):
        t = out["type"].strip()
        out["type"] = _TYPE_ALIAS.get(t, t)

    # 归一化 status（case-insensitive + 兜底关键字匹配）
    if "status" in out and isinstance(out["status"], str):
        s = out["status"].strip()
        canon = _STATUS_ALIAS.get(s) or _STATUS_ALIAS.get(s.lower())
        if not canon:
            # 兜底：含关键字判断
            low = s.lower()
            if any(kw in low for kw in ("corrigendum", "erratum", "勘误", "修正本", "修订", "amendment", "amend")):
                canon = "active"
            elif any(kw in s for kw in ("生效", "有效", "现行")):
                canon = "active"
        out["status"] = canon or s

    # 归一化 reg_id（ECE-R<n> → ECE R<n>, Am/Rev 后缀等）
    if "reg_id" in out and isinstance(out["reg_id"], str):
        out["reg_id"] = _canonicalize_reg_id(out["reg_id"])

    # 归一化 region（UN → ece, AU → au, 中文 → lowercase code）
    if "region" in out and out["region"]:
        canon_region = _canonicalize_region(out["region"])
        if canon_region:
            out["region"] = canon_region

    node_type = out.get("type", "")

    # 修改单：从 reg_id 推导 amendment_id / amendment_number / parent_version
    if node_type == "type/amendment":
        reg_id = out.get("reg_id")
        if isinstance(reg_id, str) and "/" in reg_id:
            # e.g. "GB 4785-2007/XG1-2009" → parent="GB 4785-2007", amendment="XG1-2009"
            parent, _, suffix_str = reg_id.partition("/")
            parent = parent.strip()
            out.setdefault("amendment_id", reg_id)
            out.setdefault("parent_version", f"[[{parent}]]")
            # Try to extract amendment_number from suffix
            m = re.search(r"XG\s*(\d+)|第\s*(\d+)\s*号", suffix_str)
            if m:
                num = m.group(1) or m.group(2)
                try:
                    out.setdefault("amendment_number", int(num))
                except ValueError:
                    pass

    # wikilink 包装（字符串类型且未包装的 wikilink 字段）
    for k in ("supersedes", "superseded_by", "parent_version", "parent_regulation"):
        v = out.get(k)
        if isinstance(v, str) and v and not v.lstrip().startswith("[["):
            out[k] = f"[[{v.strip()}]]"

    # tags 兜底
    tags = out.get("tags")
    if not isinstance(tags, list):
        tags = []
    existing = set(t for t in tags if isinstance(t, str))
    if node_type and node_type not in existing:
        tags.append(node_type)
    region = out.get("region")
    if isinstance(region, str) and region:
        reg_tag = f"reg/{region}"
        if reg_tag not in existing:
            tags.append(reg_tag)
    status = out.get("status")
    if isinstance(status, str) and status:
        status_tag_map = {
            "active": "status/active",
            "withdrawn": "status/withdrawn",
            "superseded": "status/superseded",
            "draft": "status/draft",
            "under_revision": "status/under-revision",
        }
        st_tag = status_tag_map.get(status)
        if st_tag and st_tag not in existing:
            tags.append(st_tag)
    if tags:
        out["tags"] = tags

    return out


# =============================================================
# Body continuation (handle output token truncation)
# =============================================================
_CONTINUATION_SYSTEM = """你是一位法规文档抽取工程师。
用户正在续写一份已经部分抽取好的 Markdown 文档。你之前的输出被 max_tokens 限制截断了。

任务：
  1. 查看【OCR 原文】和【已输出的尾部】
  2. 从【已输出的尾部】停止的地方开始，继续抽取【OCR 原文】中对应的下一段内容
  3. 保持相同的章节层级格式（## / ### / #### + 有序/无序列表）
  4. **只输出 Markdown 新内容**，不要 YAML frontmatter，不要 ``` 代码围栏
  5. 不要重复【已输出的尾部】中的任何句子；从断点直接续写
  6. 若已到原文末尾，输出 "<END>" 即可
"""

_CONTINUATION_USER = """【OCR 原文】:
<<<
{raw_markdown}
>>>

【已输出的尾部 2000 字】:
<<<
{body_tail}
>>>

请从断点继续抽取。只输出新的 Markdown 内容。"""


def _continue_body_extraction(
    client: "DeepSeekClient",
    *,
    raw_text: str,
    partial_body: str,
    reg_id: str,
    prompt_version: str,
    max_retries: int = 3,
) -> tuple[str, int, bool]:
    """若第一轮 extract output 被截断，多轮续写 body。
    Returns: (完整 body, 续写次数, 是否仍被截断)
    """
    body = partial_body
    passes = 0
    still_truncated = True

    for attempt in range(max_retries):
        tail = body[-2000:] if len(body) > 2000 else body
        try:
            resp = client.chat(
                system=_CONTINUATION_SYSTEM,
                user=_CONTINUATION_USER.format(
                    raw_markdown=raw_text,
                    body_tail=tail,
                ),
                max_tokens=8192,
                temperature=0.1,
                enable_cache=True,
            )
        except Exception as e:
            console.print(f"[yellow]续写 pass {attempt+1} 失败: {e}[/yellow]")
            break

        client.log_cost(
            stage="s1_extract_continue",
            response=resp,
            reg_id=reg_id,
            prompt_version=f"{prompt_version}+cont",
        )

        new_text = resp.content.strip()
        # 去掉续写响应里可能夹带的 YAML frontmatter / code fence
        new_text = re.sub(r"^---[\s\S]*?---\s*", "", new_text)
        new_text = re.sub(r"^```(?:markdown|md|yaml)?\s*\n?", "", new_text)
        new_text = re.sub(r"\n?\s*```\s*$", "", new_text)
        new_text = new_text.strip()

        passes += 1

        if not new_text or new_text.startswith("<END>") or new_text in ("END", "<END>"):
            still_truncated = False
            break

        body = body.rstrip() + "\n\n" + new_text

        if resp.finish_reason != "length" and resp.output_tokens < 8000:
            still_truncated = False
            break

    return body, passes, still_truncated


_TOP_KV_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_.-]*)\s*:\s*(.*?)\s*$")


def _quote_unsafe_values(s: str) -> str:
    """把 `key: value with : unquoted colons` 的行里 value 用双引号包起来。

    只处理 top-level（无缩进）的简单 scalar 行；list/dict/多行值/已引号值不碰。
    """
    out_lines = []
    for line in s.split("\n"):
        # 只处理无缩进、单行 key: value 形式
        if line and not line[0].isspace():
            m = _TOP_KV_RE.match(line)
            if m:
                key, value = m.group(1), m.group(2)
                if value and not value.startswith(("[", "{", "'", '"', "|", ">", "!", "&", "*", "-")) and ": " in value:
                    # 用双引号包裹；转义内部的 " 和 \
                    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
                    out_lines.append(f'{key}: "{escaped}"')
                    continue
        out_lines.append(line)
    return "\n".join(out_lines)


def _safe_yaml_load(s: str) -> dict:
    """Try yaml.safe_load. On error:
      1. 先尝试对 top-level scalar 值里的裸冒号加引号（LLM 常漏）。
      2. 失败则逐行丢弃末尾（截断修复），最多 20 次。
    """
    s = s.strip()
    if not s:
        return {}

    # 第一次直接解析
    try:
        result = yaml.safe_load(s)
        if isinstance(result, dict):
            return result
        return {}
    except yaml.YAMLError:
        pass

    # 第二次：尝试把不安全的 top-level value 加引号后再解析
    quoted = _quote_unsafe_values(s)
    if quoted != s:
        try:
            result = yaml.safe_load(quoted)
            if isinstance(result, dict):
                return result
        except yaml.YAMLError:
            pass
        s = quoted  # 后续截断恢复基于引号修复后的版本

    # 第三次：截断恢复
    for _ in range(20):
        if "\n" not in s:
            return {}
        s = s.rsplit("\n", 1)[0]
        try:
            result = yaml.safe_load(s)
            if isinstance(result, dict):
                return result
            return {}
        except yaml.YAMLError:
            continue
    return {}


def run_single(
    rec: FileRecord,
    mf: Manifest,
    client: DeepSeekClient,
    *,
    force: bool = False,
) -> bool:
    stage_dir = _staging_path(rec)
    raw = stage_dir / "raw.md"
    out = stage_dir / "extracted.md"

    if not raw.exists():
        rec.mark_failed(f"raw.md missing at {raw}")
        return False

    if out.exists() and not force and rec.state in {"extracted", "verified", "needs_review", "written"}:
        return True

    raw_text = raw.read_text(encoding="utf-8")

    # 超长 → 截断（Day 2 先粗暴处理；Day 3 遇到再实现分块）
    truncated = False
    if len(raw_text) > MAX_INPUT_CHARS:
        raw_text = raw_text[:MAX_INPUT_CHARS]
        truncated = True

    # 加载 prompt
    prompt = load_prompt("extract")

    user = prompt.render_user(
        reg_id=_guess_reg_id_from_filename(rec),
        source_pdf=str(Path(os.getenv("RAW_SOURCE_DIR", "")) / rec.path),
        region_hint=_guess_region_from_path(rec) or "unknown",
        page_count="unknown",
        raw_markdown=raw_text,
    )

    try:
        resp = client.chat(
            system=prompt.system,
            user=user,
            max_tokens=8192,
            temperature=0.1,
            enable_cache=True,
        )
    except Exception as e:
        rec.mark_failed(f"DeepSeek error: {e}")
        return False

    # 检测输出截断：DeepSeek 用 max_tokens 触顶时 finish_reason="length"
    output_truncated = (resp.finish_reason == "length") or (resp.output_tokens >= 8192)

    # 成本日志
    client.log_cost(
        stage="s1_extract",
        response=resp,
        reg_id=_guess_reg_id_from_filename(rec),
        prompt_version=prompt.version,
    )

    # 解析 + 归一化
    frontmatter, body = _parse_llm_output(resp.content)
    frontmatter = _normalize_frontmatter(frontmatter)

    # 若 output 截断，调用续写 pass 直到完成或达到上限
    continuation_passes = 0
    if output_truncated:
        body, continuation_passes, still_truncated = _continue_body_extraction(
            client=client,
            raw_text=raw_text,
            partial_body=body,
            reg_id=_guess_reg_id_from_filename(rec),
            prompt_version=prompt.version,
            max_retries=3,
        )
        if still_truncated:
            frontmatter["_truncated_output"] = True
            tags = frontmatter.get("tags") or []
            if isinstance(tags, list) and "status/needs-review" not in tags:
                tags.append("status/needs-review")
                frontmatter["tags"] = tags

    # 补字段（pipeline 已知的信息）
    if truncated:
        frontmatter.setdefault("_truncated_input", True)
    if continuation_passes > 0:
        frontmatter["_continuation_passes"] = continuation_passes
    frontmatter.setdefault("extracted_by", "deepseek-v3")
    frontmatter.setdefault("region", _guess_region_from_path(rec))
    frontmatter.setdefault("source_pdf", str(Path(os.getenv("RAW_SOURCE_DIR", "")) / rec.path))

    # 写回 staging
    out.write_text(
        "---\n" + yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False) + "---\n\n" + body,
        encoding="utf-8",
    )

    # 更新 manifest
    reg_id = frontmatter.get("reg_id") or _guess_reg_id_from_filename(rec)
    rec.reg_id = reg_id
    rec.region = frontmatter.get("region")
    rec.advance_to("extracted", note=f"{resp.input_tokens}→{resp.output_tokens} tok")
    return True


def run_batch(
    mf: Manifest,
    *,
    limit: Optional[int] = None,
    max_workers: int = 10,
    dry_run: bool = False,
) -> dict:
    ready = mf.files_in_state("ocr_done")
    if limit:
        ready = ready[:limit]

    if dry_run:
        total_chars = 0
        for rec in ready:
            raw = _staging_path(rec) / "raw.md"
            if raw.exists():
                total_chars += raw.stat().st_size
        est_input_tokens = total_chars // 3   # 中文粗算 3 字节/token
        est_output_tokens = est_input_tokens // 4
        est_cost = (
            est_input_tokens * 0.27 / 1_000_000
            + est_output_tokens * 1.10 / 1_000_000
        )
        console.print(f"[yellow]DRY-RUN[/yellow] {len(ready)} files")
        console.print(f"  est. input  = {est_input_tokens:,} tokens")
        console.print(f"  est. output = {est_output_tokens:,} tokens")
        console.print(f"  est. cost   ≈ ${est_cost:.2f} = ¥{est_cost*7.2:.0f}")
        return {"total": len(ready), "est_cost_usd": est_cost, "dry_run": True}

    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        console.print("[red]ERROR[/red] DEEPSEEK_API_KEY not set")
        return {"error": "no_api_key"}

    client = DeepSeekClient(api_key=api_key, base_url=os.getenv("DEEPSEEK_BASE_URL"))
    console.print(f"[cyan]Extract batch:[/cyan] {len(ready)} files, {max_workers} workers")

    stats = {"success": 0, "failed": 0}
    save_interval = 25
    processed = 0
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Extract", total=len(ready))
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {pool.submit(run_single, rec, mf, client): rec for rec in ready}
            for fut in as_completed(futures):
                rec = futures[fut]
                try:
                    ok = fut.result()
                    stats["success" if ok else "failed"] += 1
                except Exception as e:
                    rec.mark_failed(f"Unhandled: {e}")
                    stats["failed"] += 1
                progress.advance(task)
                # 每 50 份保存一次 manifest（避免中断丢进度）
                if (stats["success"] + stats["failed"]) % 50 == 0:
                    mf.save()

    mf.save()
    console.print(f"[green]Extract done:[/green] {stats}")
    return stats


if __name__ == "__main__":
    mf = Manifest.load_or_create()
    run_batch(mf)
