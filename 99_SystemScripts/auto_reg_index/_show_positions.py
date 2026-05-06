import json
from pathlib import Path
mf = json.loads(Path(r"D:\CcVault\99_SystemScripts\auto_reg_index\manifest.json").read_text(encoding="utf-8"))
all_recs = [(h, r) for h, r in mf["records"].items()]
# 仍为 failed 的 + 已 ocr_done 的（被最新 retry 转过的）
orig_failed = [(h, r) for h, r in all_recs if r.get("state") in ("failed", "ocr_done")]
# 恢复原顺序：按 size 升序（同 retry 脚本用的）
orig_failed.sort(key=lambda x: x[1].get("size_bytes", 0) or 0)
print(f"originally-failed + now-processed total: {len(orig_failed)}")
# positions 113-125 (0-index 112-124)
for i in range(110, min(len(orig_failed), 126)):
    r = orig_failed[i][1]
    sz = (r.get("size_bytes") or 0) // 1024
    state = r.get("state")
    path = str(r.get("path", ""))[:70]
    print(f"  #{i+1:3}  {sz:7}KB  state={state:10}  {path}")
