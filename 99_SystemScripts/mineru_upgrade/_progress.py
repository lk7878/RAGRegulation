"""Quick progress check."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

state = json.loads(Path(r"D:\CcVault\99_SystemScripts\mineru_upgrade\_mineru_state.json").read_text(encoding="utf-8"))
today = date.today().isoformat()
done_today = [h for h, info in state["done"].items() if info.get("date") == today]
failed_today = [h for h, info in state["failed"].items() if info.get("date") == today]
total_done = len(state["done"])

print(f"累计完成: {total_done} / 1444 ({total_done * 100 // 1444}%)")
print(f"今日新增完成: {len(done_today)}")
print(f"今日失败: {len(failed_today)}")
print(f"今日消耗页数: {state['daily_pages_used'].get(today, 0)}")
print(f"剩余未跑: {1444 - total_done}")

# 最近 10 条
recent = sorted(
    [(info.get("date", ""), info.get("pages", 0), info.get("reg_id", ""))
     for info in state["done"].values()],
    reverse=True,
)[:10]
print("\n最近 10 条完成:")
for d, p, rid in recent:
    print(f"  {d}  {p:>3}p  {rid}")
