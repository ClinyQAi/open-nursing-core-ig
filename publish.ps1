# Publish Script for Open Nursing Core IG
# Safely updates GitHub Pages (docs/) while preserving CNAME an using .nojekyll

Write-Host "Starting Publication Process..." -ForegroundColor Cyan

# 1. Clean docs directory (but keep it existence)
Write-Host "Cleaning docs/ directory..."
if (Test-Path "docs") {
    Remove-Item "docs\*" -Recurse -Force
}
else {
    New-Item -ItemType Directory -Force -Path "docs"
}

# 2. Copy build output
Write-Host "Copying new build from output/..."
Copy-Item "output\*" "docs\" -Recurse -Force

# 3. Restore CNAME (CRITICAL for custom domain)
Write-Host "Restoring CNAME..."
if (Test-Path "CNAME") {
    Copy-Item "CNAME" "docs\CNAME" -Force
    Write-Host "SUCCESS: CNAME preserved." -ForegroundColor Green
}
else {
    Write-Error "ERROR: ROOT CNAME FILE MISSING! Custom domain will fail."
    exit 1
}

# 4. Create .nojekyll (CRITICAL for FHIR IGs)
Write-Host "Creating .nojekyll..."
New-Item -Path "docs\.nojekyll" -ItemType File -Force | Out-Null

# 5. Git Operations
Write-Host "Committing to GitHub..."
git add docs/
git commit -m "Deploy: Update site content, preserve CNAME, add .nojekyll"
git push

Write-Host ""
Write-Host "Published successfully!" -ForegroundColor Green
Write-Host "Site should be live at: https://opennursingcoreig.com/"
