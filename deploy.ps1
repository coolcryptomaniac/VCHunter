param([Parameter(Mandatory=$true)][string]$RepoUrl)
git init
git add .
git commit -m "Launch VC Hunter"
git branch -M main
git remote add origin $RepoUrl
git push -u origin main
Write-Host "Now set GitHub Settings -> Pages -> Source: GitHub Actions"
