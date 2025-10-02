# ShopKart Deployment Guide 🚀

This guide will help you deploy ShopKart to various hosting platforms.

## Table of Contents
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Deploy to Render](#deploy-to-render-recommended)
3. [Deploy to Railway](#deploy-to-railway)
4. [Deploy to Heroku](#deploy-to-heroku)
5. [Deploy to PythonAnywhere](#deploy-to-pythonanywhere)
6. [Post-Deployment Steps](#post-deployment-steps)
7. [Troubleshooting](#troubleshooting)

---

## Pre-Deployment Checklist

Before deploying, make sure you have:

✅ All files committed to GitHub
✅ `.env` file with environment variables (DON'T commit this!)
✅ `requirements.txt` with all dependencies
✅ `Procfile` created
✅ `runtime.txt` specifying Python version
✅ Static files configured in settings.py

### Commit Your Latest Changes

```bash
git add .
git commit -m "Prepare for deployment: Add production configs"
git push origin main
```

---

## Deploy to Render (Recommended) 🌟

Render offers free hosting for web services with PostgreSQL database.

### Steps:

1. **Sign up at [render.com](https://render.com)**

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `DAKSHSHARMA2901/shopkart`
   - Render will detect it's a Python app

3. **Configure the Service**
   - **Name**: `shopkart`
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: Leave empty (or `.` if required)
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```
     gunicorn shoeskart.wsgi:application
     ```
   - **Plan**: Select "Free"

4. **Add Environment Variables**
   - Click "Environment" tab
   - Add these variables:
   
   ```
   SECRET_KEY=django-insecure-in0#!u0$^@_1nu_qg68z+o_+m-o&v4p=ubla%^oa*kk0v42w=m
   DEBUG=False
   ALLOWED_HOSTS=shopkart.onrender.com,www.shopkart.onrender.com
   RAZORPAY_KEY_ID=rzp_test_ROdO6CGivLBaVf
   RAZORPAY_KEY_SECRET=hpwho4yrEQ4BW1B0mQBMDlt3
   PYTHON_VERSION=3.13.7
   ```
   
   **⚠️ IMPORTANT**: Generate a new SECRET_KEY for production! Use this Python command:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Create PostgreSQL Database (Optional but Recommended)**
   - Click "New +" → "PostgreSQL"
   - **Name**: `shopkart-db`
   - **Plan**: "Free"
   - After creation, copy the "Internal Database URL"
   - Add to your Web Service environment variables:
     ```
     DATABASE_URL=<paste-internal-database-url-here>
     ```

6. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy your app
   - Wait for build to complete (5-10 minutes)

7. **Run Database Migrations**
   - After first deployment, go to "Shell" tab
   - Run:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py collectstatic --noinput
     ```

8. **Your site will be live at**: `https://shopkart.onrender.com`

---

## Deploy to Railway 🚂

Railway offers $5 free credit per month.

### Steps:

1. **Sign up at [railway.app](https://railway.app)**

2. **Create New Project**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select `DAKSHSHARMA2901/shopkart`

3. **Add Environment Variables**
   - Click on your service → "Variables" tab
   - Add:
   ```
   SECRET_KEY=<your-new-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=${{ RAILWAY_PUBLIC_DOMAIN }}
   RAZORPAY_KEY_ID=rzp_test_ROdO6CGivLBaVf
   RAZORPAY_KEY_SECRET=hpwho4yrEQ4BW1B0mQBMDlt3
   ```

4. **Add PostgreSQL Database**
   - Click "New" → "Database" → "Add PostgreSQL"
   - Railway will automatically set DATABASE_URL

5. **Configure Settings**
   - Railway auto-detects Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn shoeskart.wsgi:application`

6. **Generate Domain**
   - Click "Settings" → "Generate Domain"
   - Your site will be at: `https://shopkart-production-xxxx.up.railway.app`

7. **Run Migrations**
   - Click service → "Shell" or "Deployments" → "View Logs"
   - Use Railway CLI or wait for first deployment, then:
   ```bash
   railway run python manage.py migrate
   railway run python manage.py createsuperuser
   railway run python manage.py collectstatic --noinput
   ```

---

## Deploy to Heroku ☁️

Heroku requires credit card for verification (no charges on free tier).

### Steps:

1. **Install Heroku CLI**
   ```bash
   # Windows (using Chocolatey)
   choco install heroku-cli
   
   # Or download installer from heroku.com/install
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create shopkart-app
   ```

4. **Add PostgreSQL Database**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=<your-new-secret-key>
   heroku config:set DEBUG=False
   heroku config:set RAZORPAY_KEY_ID=rzp_test_ROdO6CGivLBaVf
   heroku config:set RAZORPAY_KEY_SECRET=hpwho4yrEQ4BW1B0mQBMDlt3
   ```

6. **Update ALLOWED_HOSTS**
   ```bash
   heroku config:set ALLOWED_HOSTS=shopkart-app.herokuapp.com
   ```

7. **Deploy**
   ```bash
   git push heroku main
   ```

8. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   heroku run python manage.py collectstatic --noinput
   ```

9. **Open Your App**
   ```bash
   heroku open
   ```

---

## Deploy to PythonAnywhere 🐍

Great for beginners, free tier available.

### Steps:

1. **Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)**
   - Choose "Beginner" account (free)

2. **Open Bash Console**
   - Dashboard → "Bash" console

3. **Clone Repository**
   ```bash
   git clone https://github.com/DAKSHSHARMA2901/shopkart.git
   cd shopkart
   ```

4. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 shopkart-env
   pip install -r requirements.txt
   ```

5. **Configure Web App**
   - Dashboard → "Web" tab → "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - **Source code**: `/home/yourusername/shopkart`
   - **Working directory**: `/home/yourusername/shopkart`
   - **Virtualenv**: `/home/yourusername/.virtualenvs/shopkart-env`

6. **Edit WSGI Configuration**
   - Click "WSGI configuration file" link
   - Replace content with:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/shopkart'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'shoeskart.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

7. **Set Environment Variables**
   - Web tab → "Environment variables" section
   - Add variables (same as above)

8. **Configure Static Files**
   - Web tab → "Static files" section
   - URL: `/static/` → Directory: `/home/yourusername/shopkart/staticfiles`
   - URL: `/media/` → Directory: `/home/yourusername/shopkart/media`

9. **Run Migrations**
   - In Bash console:
   ```bash
   cd shopkart
   workon shopkart-env
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic --noinput
   ```

10. **Reload Web App**
    - Green "Reload" button on Web tab
    - Visit: `http://yourusername.pythonanywhere.com`

---

## Post-Deployment Steps

After deploying to any platform:

### 1. **Upload Products & Data**
   - Visit `https://your-domain.com/admin`
   - Login with superuser credentials
   - Add products, categories, subcategories

### 2. **Test Payment Integration**
   - Make a test purchase
   - Verify Razorpay integration works

### 3. **Update Razorpay Settings**
   - If using production keys, update environment variables
   - Test with live credentials

### 4. **Configure Custom Domain (Optional)**
   - Most platforms allow custom domains
   - Follow their specific documentation

### 5. **Set Up Media File Storage (For Production)**
   - Consider using AWS S3, Cloudinary, or similar
   - Update settings.py with storage backend

### 6. **Enable HTTPS**
   - Most platforms provide free SSL
   - Ensure SECURE_SSL_REDIRECT in settings.py

---

## Troubleshooting

### Issue: Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic --noinput
```

Check STATIC_ROOT in settings.py and whitenoise configuration.

### Issue: Database Connection Error

**Solution:**
- Verify DATABASE_URL environment variable is set
- Run migrations: `python manage.py migrate`
- Check database credentials

### Issue: 500 Internal Server Error

**Solution:**
1. Check logs (varies by platform):
   - **Render**: Logs tab in dashboard
   - **Railway**: Deployments → View Logs
   - **Heroku**: `heroku logs --tail`
   - **PythonAnywhere**: Error log in Web tab

2. Common causes:
   - DEBUG=True (should be False in production)
   - Missing environment variables
   - Database not migrated
   - Static files not collected

### Issue: ALLOWED_HOSTS Error

**Solution:**
Add your domain to ALLOWED_HOSTS environment variable:
```
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Issue: Media Files Not Showing

**Solution:**
For production, configure cloud storage (AWS S3, Cloudinary):

1. Install django-storages: `pip install django-storages boto3`
2. Add to requirements.txt
3. Configure in settings.py:
```python
if not DEBUG:
    # AWS S3 Configuration
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
```

---

## Important Notes

⚠️ **Security Reminders:**
1. Never commit `.env` file to GitHub
2. Generate a new SECRET_KEY for production
3. Set DEBUG=False in production
4. Use HTTPS for all production sites
5. Keep Razorpay credentials secure

📊 **Database:**
- SQLite works for development, but use PostgreSQL for production
- Most platforms offer free PostgreSQL databases
- Remember to run migrations on production database

📁 **Media Files:**
- Consider cloud storage (AWS S3, Cloudinary) for product images
- Local media/ folder won't persist on some platforms (Heroku, Render)

---

## Need Help?

- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **Heroku Docs**: https://devcenter.heroku.com
- **PythonAnywhere**: https://help.pythonanywhere.com

---

**Good luck with your deployment! 🎉**

For issues specific to ShopKart, check the main README.md or create an issue on GitHub.
