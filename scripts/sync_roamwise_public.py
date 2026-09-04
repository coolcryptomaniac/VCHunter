#!/usr/bin/env python3
"""Refresh public-only Roamwise facts for the unlisted founder workspace.

No private metrics, secrets, API keys or fundraising notes are fetched or committed.
"""
from __future__ import annotations
import json, re, urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://www.roamwise.co.in/"
OUT = Path("docs/data/roamwise_live.json")

req = urllib.request.Request(URL, headers={"User-Agent": "VCHunter-RoamwiseSync/1.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    html = r.read().decode("utf-8", "replace")
text = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", html, flags=re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)

old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}

def grab(pattern: str, default):
    m = re.search(pattern, text, re.I)
    return m.group(1) if m else default

countries = grab(r"(195\+)\s*Countries", old.get("public_metrics",{}).get("countries","195+"))
version = grab(r"Roam\s*Wise\s*Pro\s*(v[0-9.]+)", old.get("public_version",""))
india_price = grab(r"India\s*[—-]\s*(₹[0-9]+).*?one-time", old.get("public_metrics",{}).get("india_pro_price","₹100 one-time"))
global_price = grab(r"Worldwide\s*[—-]\s*(\$[0-9.]+).*?once", old.get("public_metrics",{}).get("global_pro_price","$4.99 one-time"))

data = old or {}
data.update({
    "company": "Roamwise",
    "url": URL,
    "snapshot_date": datetime.now(timezone.utc).date().isoformat(),
    "synced_at_utc": datetime.now(timezone.utc).isoformat(),
    "public_version": version,
    "public_only": True,
    "source": URL,
})
data.setdefault("public_metrics", {})
data["public_metrics"].update({
    "countries": countries,
    "max_itinerary_days": 14 if "14-day" in text else data["public_metrics"].get("max_itinerary_days",14),
    "currencies": 10 if re.search(r"\b10\s+Currencies\b", text, re.I) else data["public_metrics"].get("currencies",10),
    "crowd_months": 12 if re.search(r"\b12\s+Crowd months\b", text, re.I) else data["public_metrics"].get("crowd_months",12),
    "india_pro_price": india_price + " one-time" if "one-time" not in india_price.lower() else india_price,
    "global_pro_price": global_price + " one-time" if "one-time" not in global_price.lower() else global_price,
})
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Refreshed {OUT} from {URL}")
