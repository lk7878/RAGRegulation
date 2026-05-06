"""
OCR 分层路由

策略（节约成本）：
  1. pdfplumber 尝试（免费，快）
     - 若每页文本 >= min_text_per_page_chars → 成功
     - 否则视为扫描件
  2. 百度云 OCR （¥0.007/页，云端）
     - 处理扫描件
  3. MinerU CPU （免费，慢）
     - 处理复杂表格或百度置信度低的
"""
from __future__ import annotations

import enum
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


class OCR_LAYER(enum.Enum):
    PDFPLUMBER = "pdfplumber"
    BAIDU = "baidu"
    MINERU = "mineru"
    FAILED = "failed"


@dataclass
class OCRResult:
    """OCR 层统一返回"""
    success: bool
    layer_used: OCR_LAYER
    markdown: str                          # 输出的 markdown 文本
    page_count: int = 0
    warnings: list[str] = field(default_factory=list)
    cost_cny: float = 0.0                  # 仅百度云有成本


def route_ocr(
    pdf_path: Path,
    *,
    min_text_per_page_chars: int = 50,
    enable_baidu: bool = True,
    enable_mineru: bool = True,
    force_layer: Optional[OCR_LAYER] = None,
) -> OCRResult:
    """
    对一份 PDF 做 OCR。按层级路由，返回第一个成功的结果。

    Args:
        pdf_path: PDF 绝对路径
        min_text_per_page_chars: pdfplumber 判定"有文本"的阈值
        enable_baidu: 是否启用百度云层
        enable_mineru: 是否启用 MinerU 层
        force_layer: 强制走某一层（测试用）
    """
    # -------- 强制指定层 --------
    if force_layer:
        return _run_layer(force_layer, pdf_path)

    # -------- Layer 1: pdfplumber --------
    from . import pdfplumber_extractor
    result = pdfplumber_extractor.extract(
        pdf_path,
        min_text_per_page_chars=min_text_per_page_chars,
    )
    if result.success:
        return result

    # -------- Layer 2: 百度云 OCR --------
    if enable_baidu:
        try:
            from . import baidu_ocr
            result = baidu_ocr.extract(pdf_path)
            if result.success:
                return result
        except ImportError:
            result.warnings.append("baidu-aip not installed")
        except Exception as e:
            result.warnings.append(f"baidu_ocr failed: {e}")

    # -------- Layer 3: MinerU --------
    if enable_mineru:
        try:
            from . import mineru_extractor
            result = mineru_extractor.extract(pdf_path)
            if result.success:
                return result
        except ImportError:
            result.warnings.append("mineru not installed")
        except Exception as e:
            result.warnings.append(f"mineru failed: {e}")

    # 三层全失败
    return OCRResult(
        success=False,
        layer_used=OCR_LAYER.FAILED,
        markdown="",
        warnings=result.warnings + ["All OCR layers failed"],
    )


def _run_layer(layer: OCR_LAYER, pdf_path: Path) -> OCRResult:
    """Force 某一层"""
    if layer == OCR_LAYER.PDFPLUMBER:
        from . import pdfplumber_extractor
        return pdfplumber_extractor.extract(pdf_path, min_text_per_page_chars=0)
    if layer == OCR_LAYER.BAIDU:
        from . import baidu_ocr
        return baidu_ocr.extract(pdf_path)
    if layer == OCR_LAYER.MINERU:
        from . import mineru_extractor
        return mineru_extractor.extract(pdf_path)
    raise ValueError(f"Unknown layer: {layer}")
