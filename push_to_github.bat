@echo off
echo ==========================================
echo ShopKart - GitHub Push Script
echo ==========================================
echo.

cd "c:\Users\daksh\OneDrive\Desktop\phthon it vendant\miniproject sem 4\shoeskart"

echo Step 1: Initializing Git repository...
git init

echo.
echo Step 2: Configuring Git user...
git config user.name "DAKSHSHARMA2901"
git config user.email "dakshsharma737@gmail.com"

echo.
echo Step 3: Adding all files...
git add .

echo.
echo Step 4: Creating first commit...
git commit -m "Initial commit: ShopKart e-commerce platform with blue/yellow theme"

echo.
echo Step 5: Adding remote repository...
git remote add origin https://github.com/DAKSHSHARMA2901/shopkart.git

echo.
echo Step 6: Setting main branch...
git branch -M main

echo.
echo Step 7: Pushing to GitHub...
echo NOTE: You will be asked for credentials:
echo Username: DAKSHSHARMA2901
echo Password: Use your Personal Access Token (NOT your password)
echo.
git push -u origin main

echo.
echo ==========================================
echo Push Complete!
echo ==========================================
echo Your repository is now at:
echo https://github.com/DAKSHSHARMA2901/shopkart
echo.
pause
