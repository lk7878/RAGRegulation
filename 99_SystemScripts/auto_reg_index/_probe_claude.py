"""探测 Claude 代理支持的模型 + 测试 opus-4-6."""
import os
import json
import httpx
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)

BASE = os.getenv("ANTHROPIC_BASE_URL").rstrip("/")
KEY = os.getenv("ANTHROPIC_API_KEY")

print(f"Base: {BASE}")
print(f"Key tail: ...{KEY[-8:]}")

# Try models endpoint
url = BASE + "/v1/models"
for auth_style in [
    ("x-api-key header", {"x-api-key": KEY, "anthropic-version": "2023-06-01"}),
    ("Bearer token", {"Authorization": f"Bearer {KEY}", "anthropic-version": "2023-06-01"}),
]:
    label, headers = auth_style
    try:
        r = httpx.get(url, headers=headers, timeout=15)
        print(f"\n[{label}] status={r.status_code}")
        try:
            data = r.json()
            if "data" in data:
                print(f"  models count: {len(data['data'])}")
                for m in data["data"][:30]:
                    print(f"    {m.get('id')}")
            else:
                print(f"  body: {json.dumps(data, ensure_ascii=False)[:400]}")
        except Exception:
            print(f"  text: {r.text[:400]}")
    except Exception as e:
        print(f"  err: {e}")

# Try direct call with various model names
print("\n--- Model candidates via /v1/messages ---")
candidates = [
    "claude-opus-4-6",
    "claude-opus-4-5",
    "claude-opus-4",
    "claude-opus-4-20250514",
    "claude-3-opus-latest",
    "claude-3-opus-20240229",
    "claude-sonnet-4-5",
    "claude-sonnet-4",
    "claude-3-5-sonnet-latest",
    "claude-3-5-sonnet-20241022",
    "claude-3-7-sonnet-latest",
    "claude-3-7-sonnet-20250219",
    "claude-haiku-4-5",
    "claude-3-5-haiku-latest",
]
from anthropic import Anthropic

c = Anthropic(api_key=KEY, base_url=BASE)
for m in candidates:
    try:
        resp = c.messages.create(
            model=m,
            max_tokens=6,
            messages=[{"role": "user", "content": "OK"}],
        )
        content = "".join(b.text for b in resp.content if hasattr(b, "text"))
        print(f"  OK  {m:45} -> {content!r}  in={resp.usage.input_tokens} out={resp.usage.output_tokens}")
    except Exception as e:
        msg = str(e)[:200]
        if "model_not_found" in msg:
            print(f"  NA  {m}")
        else:
            print(f"  ERR {m}: {msg}")
