#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then echo "Usage: ./deploy.sh https://github.com/YOUR-USERNAME/YOUR-REPO.git"; exit 1; fi
git init
git add .
git commit -m "Launch VC Hunter"
git branch -M main
git remote add origin "$1"
git push -u origin main
echo "Now set GitHub Settings -> Pages -> Source: GitHub Actions"
