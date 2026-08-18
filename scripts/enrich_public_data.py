"""GitHub Actions enrichment scaffold.

Only fetch sources you are allowed to reuse. Preferred inputs are official VC pages, approved APIs, or licensed exports.
Never scrape login-gated LinkedIn/OpenVC/Crunchbase pages or guess private contacts.

Write verified facts to data/curated/ with source_url and verified_at, then rebuild the public index.
"""
from datetime import datetime, timezone
print('No-op enrichment scaffold:', datetime.now(timezone.utc).isoformat())
print('Add explicitly permitted source adapters here.')
