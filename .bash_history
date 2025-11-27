# 1. Go to Project
if [ -d "open-nursing-core-ig" ]; then cd open-nursing-core-ig; fi
# 2. Move Secrets to a Safe Temporary Location (Outside the Git folder)
echo "🛡️  Moving Secrets to Safety..."
mv chroma_db_fons ../temp_db_safe
mv fons_knowledge_base ../temp_pdfs_safe
mv .env ../temp_env_safe
# 3. Destroy the Git History (This removes all record of the DB ever existing)
echo "🧹 Scrubbing History..."
rm -rf .git
# 4. Re-Initialize Git (Start Fresh)
git init
git branch -M main
# 5. Create the Shield (.gitignore)
# This tells Git: "Even if these files exist, IGNORE them."
echo ".env" > .gitignore
echo "chroma_db_fons/" >> .gitignore
echo "fons_knowledge_base/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
# 6. Add the Code (But NOT the secrets, because they are moved away)
git add .
git commit -m "initial commit: Open Nursing Core IG (Open Source Code Only)"
# 7. Force Push to GitHub
# (You might need to authenticate again if prompted)
git remote add origin https://github.com/ClinyQAi/open-nursing-core-ig.git
git push -u --force origin main
# 8. Restore Secrets (Bring them back so your App still works!)
echo "🔙 Restoring Secrets to App..."
mv ../temp_db_safe chroma_db_fons
mv ../temp_pdfs_safe fons_knowledge_base
mv ../temp_env_safe .env
echo "✅ REPO IS NOW CLEAN. Safe to make Public."
# 1. Go to Project
if [ -d "open-nursing-core-ig" ]; then cd open-nursing-core-ig; fi
# 2. CONFIGURE GIT IDENTITY (Fixes the fatal error)
git config --global user.email "lincoln@clinyqai.com"
git config --global user.name "Lincoln Gombedza"
# 3. Move Secrets to Safety (Only if they exist)
echo "🛡️  Backing up Secrets..."
if [ -d "chroma_db_fons" ]; then mv chroma_db_fons ../temp_db_safe; fi
if [ -d "fons_knowledge_base" ]; then mv fons_knowledge_base ../temp_pdfs_safe; fi
if [ -f ".env" ]; then mv .env ../temp_env_safe; fi
# 4. Scrub History
echo "🧹 Scrubbing Git History..."
rm -rf .git
# 5. Re-Initialize
git init
git branch -M main
# 6. Create Shield (.gitignore)
echo ".env" > .gitignore
echo "chroma_db_fons/" >> .gitignore
echo "fons_knowledge_base/" >> .gitignore
echo "__pycache__/" >> .gitignore
# 7. Commit Code (Without the Secrets)
git add .
git commit -m "initial commit: Open Nursing Core IG (Code Only - Data is Proprietary)"
# 8. Force Push (Overwrites the public history)
# Note: You may need to re-authenticate if prompted
git remote add origin https://github.com/ClinyQAi/open-nursing-core-ig.git
git push -u --force origin main
# 9. Restore Secrets (Bring them back for your App)
echo "🔙 Restoring Secrets..."
if [ -d "../temp_db_safe" ]; then mv ../temp_db_safe chroma_db_fons; fi
if [ -d "../temp_pdfs_safe" ]; then mv ../temp_pdfs_safe fons_knowledge_base; fi
if [ -f "../temp_env_safe" ]; then mv ../temp_env_safe .env; fi
echo "✅ SUCCESS. Repository is scrubbed. You can now make it Public."
