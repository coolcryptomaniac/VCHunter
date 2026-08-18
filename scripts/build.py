from pathlib import Path
import pandas as pd, json
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/'data/raw/investors-historical.csv'
df=pd.read_csv(src).fillna('')
cols=['snapshot_rank','investor_name','country_code','region','city','observed_investments','unique_portfolio_companies','observed_stages','observed_sectors','portfolio_examples','first_observed_investment','last_observed_investment','data_confidence']
for c in cols:
    if c not in df.columns: df[c]=''
(ROOT/'docs/data/search-index.json').write_text(json.dumps(df[cols].to_dict('records'),ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(f'Built search index: {len(df):,} investors')
