from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'docs/data/search-index.json'
data=json.loads(p.read_text())
assert isinstance(data,list) and len(data)>=10000, 'Expected at least 10,000 investors'
seen=set()
for row in data:
    assert row.get('investor_name'), 'Missing investor_name'
    key=(row.get('snapshot_rank'),row.get('investor_name'))
    assert key not in seen, f'Duplicate investor key: {key}'
    seen.add(key)
print(f'Validated {len(data):,} investors')
