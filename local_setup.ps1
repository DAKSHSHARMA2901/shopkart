# ShopKart - Local Development Setup

# 1. Create .env file (copy from .env.example)
Copy-Item .env.example .env

Write-Host "✅ Created .env file. Please edit it with your actual values!" -ForegroundColor Green
Write-Host ""

# 2. Install production dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

# 3. Update .env for local development
Write-Host ""
Write-Host "⚙️  For LOCAL development, make sure .env has:" -ForegroundColor Yellow
Write-Host "   DEBUG=True" -ForegroundColor Yellow
Write-Host "   ALLOWED_HOSTS=127.0.0.1,localhost" -ForegroundColor Yellow
Write-Host ""

# 4. Run migrations
Write-Host "🗄️  Running migrations..." -ForegroundColor Cyan
python manage.py migrate

# 5. Create superuser (optional)
Write-Host ""
$createSuperuser = Read-Host "Create superuser? (y/n)"
if ($createSuperuser -eq "y") {
    python manage.py createsuperuser
}

# 6. Collect static files
Write-Host ""
Write-Host "📁 Collecting static files..." -ForegroundColor Cyan
python manage.py collectstatic --noinput

Write-Host ""
Write-Host "✨ Setup complete! Run 'python manage.py runserver' to start the development server." -ForegroundColor Green
Write-Host "🌐 Visit: http://127.0.0.1:8000" -ForegroundColor Cyan
