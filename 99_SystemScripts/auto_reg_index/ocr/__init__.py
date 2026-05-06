"""OCR layer: routes files through pdfplumber → 百度云 → MinerU fallback."""
from .router import route_ocr, OCRResult, OCR_LAYER

__all__ = ["route_ocr", "OCRResult", "OCR_LAYER"]
