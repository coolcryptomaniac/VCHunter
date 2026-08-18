# VC Hunter — GitHub-only edition

A shareable investor discovery + pitching app that runs entirely on **GitHub Pages + static JSON + GitHub Actions**.

## What you get
- 10,000 investor profiles in a browser-searchable index.
- India / US / Global / Rest-of-world views.
- Company URL + idea intake and local fit ranking.
- Dedicated Roamwise investor room.
- One-click pitch generation, `mailto:` for verified public professional emails, and official pitch-route links.
- Team mode for Mohit, Febin, Adarsh and Deepanshi.
- Browser-local shortlists and pitch history; exportable as JSON.
- GitHub Issues for verified data corrections and outreach outcomes.
- GitHub Actions for validation, index rebuild and Pages deployment.

## Zero-infrastructure design
GitHub Pages is static. It cannot safely write arbitrary browser data back to the repository without credentials, and **you should never put a GitHub token in frontend JavaScript**.

So this repo uses:
1. **Static public data** in `docs/data/`.
2. **Local browser state** for each team member's shortlist/pitches.
3. **Export JSON** for portable activity.
4. **GitHub Issues / PRs** for verified shared updates.
5. **GitHub Actions** as the only backend-like compute layer.

## Deploy in ~2 minutes
1. Create a new GitHub repository.
2. Upload everything in this folder (or push with git).
3. Open **Settings → Pages** and choose **GitHub Actions** as the source.
4. The included `pages.yml` deploys `docs/`.
5. Share the resulting Pages URL with Febin, Adarsh and Deepanshi.

### Git commands
```bash
git init
git add .
git commit -m "Launch VC Hunter"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

## Adding / updating investors
Do not hand-edit `docs/data/search-index.json`.

- Put licensed/manual raw imports in `data/raw/`.
- Add curated current facts to `data/curated/` with source URLs and `verified_at`.
- Run `python scripts/build.py`.
- Commit generated `docs/data/*`.

## Data/compliance policy
Use only data you can lawfully reuse:
- official VC/fund websites;
- approved APIs;
- licensed exports;
- publicly posted professional contact details;
- team-verified research.

**LinkedIn:** use link-outs or approved API access. Do not scrape login-gated profiles, private emails, or private phone numbers.

**LLMs:** use them to summarize already-sourced public information, not as the primary source. Every factual enrichment should keep its source URL and verification date.

## Optional LLM enrichment in GitHub Actions
You can add repo secrets such as `OPENAI_API_KEY` or another provider and write a scheduled workflow that summarizes official pages. Keep the API key only in GitHub Secrets. The browser app never receives it.

## Team sharing
Each person's browser keeps a separate activity record. Use **Export my activity** to generate a JSON file. Shared/final facts should be submitted through the included GitHub issue templates or committed via PR.
