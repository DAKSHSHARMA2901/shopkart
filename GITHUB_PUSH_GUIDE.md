# GitHub Push Guide for ShopKart

## Step-by-Step Instructions

### 1. Create a GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the "+" icon in the top right
3. Select "New repository"
4. Fill in:
   - **Repository name**: `shopkart` (or your preferred name)
   - **Description**: "A modern e-commerce platform built with Django"
   - **Visibility**: Public or Private (your choice)
   - **DO NOT** initialize with README (we already have one)
5. Click "Create repository"

### 2. Initialize Git in Your Project (First Time Only)

Open PowerShell/Terminal in your project directory:

```powershell
cd "c:\Users\daksh\OneDrive\Desktop\phthon it vendant\miniproject sem 4\shoeskart"
```

Initialize Git:
```bash
git init
```

### 3. Configure Git (First Time Only)

Set your username and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### 4. Add Files to Git

Add all files to staging:
```bash
git add .
```

Check what will be committed:
```bash
git status
```

### 5. Commit Your Changes

Create your first commit:
```bash
git commit -m "Initial commit: ShopKart e-commerce platform with blue/yellow theme"
```

### 6. Connect to GitHub Repository

Add your GitHub repository as remote (replace `yourusername` with your GitHub username):
```bash
git remote add origin https://github.com/yourusername/shopkart.git
```

Verify the remote:
```bash
git remote -v
```

### 7. Push to GitHub

Push your code to GitHub:
```bash
git branch -M main
git push -u origin main
```

If prompted, enter your GitHub credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your password)

### 8. Create Personal Access Token (If Needed)

If GitHub asks for a password:

1. Go to GitHub → Settings → Developer settings
2. Click "Personal access tokens" → "Tokens (classic)"
3. Click "Generate new token" → "Generate new token (classic)"
4. Give it a name: "ShopKart Project"
5. Select expiration: 90 days or No expiration
6. Check these scopes:
   - ✅ `repo` (all)
   - ✅ `workflow`
7. Click "Generate token"
8. **COPY THE TOKEN** (you won't see it again!)
9. Use this token as your password when pushing

## Alternative: Using GitHub Desktop

If you prefer a GUI:

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and sign in
3. File → Add Local Repository
4. Select your project folder
5. Click "Publish repository"
6. Choose public/private and click "Publish"

## Subsequent Updates (After First Push)

When you make changes and want to push again:

```bash
# 1. Check what changed
git status

# 2. Add all changes
git add .

# 3. Commit with a descriptive message
git commit -m "Description of what you changed"

# 4. Push to GitHub
git push
```

## Common Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# View differences
git diff

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Pull latest changes from GitHub
git pull

# Clone repository (for teammates)
git clone https://github.com/yourusername/shopkart.git
```

## ⚠️ IMPORTANT: Before Pushing

### 1. Remove Sensitive Data

Make sure these are in `.gitignore`:
- ✅ `db.sqlite3` - Your database (contains user data)
- ✅ `*.pyc` - Python compiled files
- ✅ `__pycache__/` - Cache directories
- ✅ `.env` - Environment variables
- ✅ `venv/` - Virtual environment

### 2. Update Razorpay Keys

**NEVER push real Razorpay keys to GitHub!**

Before pushing:
1. Create a `secrets.py` file (add to .gitignore)
2. Move Razorpay keys there
3. Or use environment variables

Example:
```python
# In settings.py or views.py
import os
RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID', 'test_key')
RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET', 'test_secret')
```

### 3. Update README

Before pushing, update in README.md:
- Replace `yourusername` with your actual GitHub username
- Add screenshots if you want
- Update author information

## Files Already Set Up ✅

These files have been created for you:
- ✅ `.gitignore` - Ignores unnecessary files
- ✅ `README.md` - Project documentation
- ✅ `requirements.txt` - Python dependencies
- ✅ `BRANDING_UPDATE.md` - Branding documentation
- ✅ `DESIGN_UPDATES.md` - Design documentation

## Troubleshooting

### Problem: "fatal: not a git repository"
**Solution**: Run `git init` first

### Problem: "Permission denied"
**Solution**: Use Personal Access Token instead of password

### Problem: "remote origin already exists"
**Solution**: 
```bash
git remote remove origin
git remote add origin https://github.com/yourusername/shopkart.git
```

### Problem: Large file errors
**Solution**: Make sure media files are in `.gitignore`

### Problem: Merge conflicts
**Solution**: 
```bash
git pull --rebase origin main
# Resolve conflicts manually
git add .
git rebase --continue
git push
```

## Quick Command Summary

```bash
# First time setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/shopkart.git
git branch -M main
git push -u origin main

# Regular updates
git add .
git commit -m "Your message"
git push
```

## After Pushing

1. Visit your GitHub repository
2. Verify all files are there
3. Check that `.gitignore` worked (no `db.sqlite3`, `__pycache__`, etc.)
4. Update repository description and add topics
5. Add a nice README with screenshots
6. Consider adding a LICENSE file
7. Enable GitHub Pages if you want (for documentation)

## Sharing Your Project

Share your repository URL:
```
https://github.com/yourusername/shopkart
```

People can clone it with:
```bash
git clone https://github.com/yourusername/shopkart.git
```

---

**Need Help?**
- GitHub Docs: https://docs.github.com
- Git Documentation: https://git-scm.com/doc
- GitHub Learning Lab: https://lab.github.com

Good luck! 🚀
