"""ping Opus + Sonnet 看 API 是否健康"""
import os, httpx, sys
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(r"D:\CcVault\99_SystemScripts\auto_reg_index\.env", override=True)
API_KEY = os.environ["ANTHROPIC_API_KEY"]
BASE_URL = os.environ["ANTHROPIC_BASE_URL"].rstrip("/")
HEADERS = {"x-api-key": API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"}

for model in ["claude-opus-4-6", "claude-sonnet-4-6"]:
    try:
        with httpx.Client() as c:
            r = c.post(BASE_URL + "/v1/messages", headers=HEADERS, json={
                "model": model, "max_tokens": 50,
                "messages": [{"role": "user", "content": "回复 OK"}]
            }, timeout=30)
        print(f"{model}: status={r.status_code}")
        if r.status_code != 200:
            print(f"  body={r.text[:300]}")
        else:
            j = r.json()
            txt = j.get("content", [{}])[0].get("text", "")
            print(f"  reply={txt[:60]!r}")
            print(f"  usage={j.get('usage')}")
    except Exception as e:
        print(f"{model}: ERROR {e}")
