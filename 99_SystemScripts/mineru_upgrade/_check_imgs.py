"""Check content_list for empty img_path bug."""
import json, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

d = Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\outputs\e9754fafd4ab5c5f")
cl = list(d.glob("*_content_list.json"))[0]
data = json.loads(cl.read_text(encoding="utf-8"))
imgs = [x for x in data if x.get("type") == "image"]
print(f"共 {len(imgs)} 个 image 条目")
for i, img in enumerate(imgs[:5]):
    print(f"  [{i}] img_path={img.get('img_path', '')!r}  page={img.get('page_idx')}")
empty = [x for x in imgs if not x.get("img_path")]
print(f"\n空 img_path 条目: {len(empty)}")
