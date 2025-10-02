# ShopKart - E-Commerce Platform

![ShopKart](static/images/logoo.png)

A modern, full-featured e-commerce platform built with Django, featuring a beautiful blue and yellow color scheme.

## 🌟 Features

### User Features
- 🛍️ **Product Browsing**: Browse products by categories (Footwear, Upperwear, Bottomwear, Accessories)
- 🔍 **Advanced Search**: Search products by name, category, or subcategory
- 🛒 **Shopping Cart**: Add products to cart with quantity management
- ❤️ **Wishlist**: Save favorite products for later
- 📦 **Order Management**: Track your orders and order history
- 💳 **Multiple Payment Options**: Razorpay integration + Cash on Delivery
- 🔐 **User Authentication**: Secure signup/signin system
- 📱 **Responsive Design**: Works perfectly on mobile, tablet, and desktop

### Admin Features
- 📊 **Product Management**: Add, edit, delete products
- 📂 **Category Management**: Manage categories and subcategories
- 👥 **User Management**: View and manage users
- 📋 **Order Management**: Track and manage orders

## 🎨 Design Features

- Modern blue and yellow gradient theme
- Smooth animations and transitions
- Custom scrollbar
- Hover effects on product cards
- Professional UI/UX design
- Font Awesome icons integration
- Google Fonts (Inter)

## 🛠️ Technology Stack

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5.3.3, HTML5, CSS3, JavaScript
- **Database**: SQLite3 (Development)
- **Payment Gateway**: Razorpay
- **Image Processing**: Pillow
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)

## 📋 Prerequisites

- Python 3.13.7 or higher
- pip (Python package manager)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DAKSHSHARMA2901/shopkart.git
cd shopkart
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django==5.2.7
pip install pillow
pip install razorpay
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
shoeskart/
├── app1/                       # Main application
│   ├── migrations/            # Database migrations
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── admin.py               # Admin configuration
│   └── apps.py                # App configuration
├── shoeskart/                  # Project configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI configuration
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Homepage
│   ├── signin.html            # Sign in page
│   ├── signup.html            # Sign up page
│   ├── search_results.html    # Search results
│   ├── product_details.html   # Product details
│   ├── cart.html              # Shopping cart
│   ├── wishlist.html          # Wishlist
│   ├── orders.html            # Orders page
│   ├── payment.html           # Payment page
│   └── address.html           # Address management
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/                    # JavaScript files
│   └── images/                # Static images
├── media/                      # User uploaded files
│   └── product_images/        # Product images
├── db.sqlite3                  # Database file
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies (create this)
```

## 🔑 Configuration

### Razorpay Setup

1. Sign up at [Razorpay](https://razorpay.com/)
2. Get your API keys (Key ID and Key Secret)
3. Update in `app1/views.py` (line 362):
   ```python
   client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET"))
   ```
4. Update in `templates/payment.html` (line 54):
   ```javascript
   "key": "YOUR_KEY_ID",
   ```

### Email Configuration (Optional)

Update in `shoeskart/settings.py` if you want to enable email features:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## 👨‍💼 Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

**Admin Features:**
- Manage Products
- Manage Categories & Subcategories
- View Orders
- Manage Users
- View Cart & Wishlist items

## 🎯 Usage

### For Users
1. **Browse Products**: Visit homepage to see featured products
2. **Search**: Use search bar to find specific products
3. **Filter by Category**: Click on category dropdowns
4. **Add to Cart**: Click cart icon on product cards
5. **Wishlist**: Click heart icon to save favorites
6. **Checkout**: Go to cart and proceed to payment
7. **Payment**: Choose Razorpay or Cash on Delivery

### For Admin
1. Login to admin panel
2. Add categories and subcategories
3. Add products with images
4. Manage orders
5. View user information

## 🎨 Color Scheme

- **Primary Blue**: `#1e3a8a`
- **Secondary Yellow**: `#fbbf24`
- **Accent Blue**: `#60a5fa`
- **Success Green**: `#11998e`
- **Danger Red**: `#e74c3c`

## 📱 Responsive Breakpoints

- **Mobile**: < 576px
- **Tablet**: 576px - 768px
- **Desktop**: 768px - 992px
- **Large Desktop**: > 992px

## 🔒 Security Features

- CSRF protection enabled
- Secure password hashing
- Session management
- SQL injection protection (Django ORM)
- XSS protection

## 🐛 Known Issues

- None currently reported

## 📝 To-Do / Future Enhancements

- [ ] Add product reviews and ratings
- [ ] Implement email notifications
- [ ] Add order tracking system
- [ ] Implement coupon/discount codes
- [ ] Add product comparison feature
- [ ] Implement social media login
- [ ] Add live chat support
- [ ] Multi-language support
- [ ] Export orders to PDF
- [ ] Advanced analytics dashboard

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Daksh Sharma** - *Initial work* - [DAKSHSHARMA2901](https://github.com/DAKSHSHARMA2901)

## 🙏 Acknowledgments

- Bootstrap for the frontend framework
- Font Awesome for icons
- Google Fonts for typography
- Razorpay for payment integration
- Django community for the amazing framework

## 📞 Contact

- **Email**: shopkart@gmail.com
- **Phone**: +91 546335323
- **Address**: Buildings Alyssa, Begonia & Clove Embassy Tech Village, Outer Ring Road, Thakur Village, Mumbai, 401107, Maharashtra, India

## 📸 Screenshots

### Homepage
Beautiful product showcase with gradient hero section

### Search Results
Advanced search with category filtering

### Product Details
Detailed product information with add to cart

### Shopping Cart
Manage cart items and quantities

### Payment
Secure payment with Razorpay integration

---

**Made with ❤️ by ShopKart Team**

## 🚀 Deployment

ShopKart is ready for production deployment! We've configured it for easy deployment to various platforms.

### Quick Deploy Options:

#### 🌟 **Render** (Recommended - Free Tier Available)
- One-click deploy from GitHub
- Free PostgreSQL database included
- Automatic SSL certificates
- [See detailed guide](DEPLOYMENT_GUIDE.md#deploy-to-render-recommended)

#### 🚂 **Railway** ($5 free credit/month)
- Auto-detects Django
- Free PostgreSQL
- Custom domains
- [See detailed guide](DEPLOYMENT_GUIDE.md#deploy-to-railway)

#### ☁️ **Heroku** (Credit card required for verification)
- Industry standard
- Add-ons ecosystem
- CLI tools
- [See detailed guide](DEPLOYMENT_GUIDE.md#deploy-to-heroku)

#### 🐍 **PythonAnywhere** (Free tier available)
- Great for beginners
- Easy manual setup
- Built-in MySQL
- [See detailed guide](DEPLOYMENT_GUIDE.md#deploy-to-pythonanywhere)

### Production Configuration Included:

✅ `Procfile` - Web server configuration  
✅ `runtime.txt` - Python version specification  
✅ `requirements.txt` - All dependencies including production packages  
✅ WhiteNoise - Static file serving  
✅ Environment variables - Secure configuration with `.env`  
✅ Database URL - PostgreSQL support via dj-database-url  

### Quick Production Setup:

1. **Install production dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   # Copy example and edit
   copy .env.example .env
   ```

3. **Configure for production:**
   - Set `DEBUG=False`
   - Update `ALLOWED_HOSTS`
   - Generate new `SECRET_KEY`
   - Set up PostgreSQL (recommended)

4. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### 📖 Full Deployment Instructions

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete step-by-step instructions for each platform.

### ⚠️ Important Production Notes:

- **Never commit `.env` file** - It contains sensitive data
- **Generate new SECRET_KEY** - Don't use development key in production
- **Use PostgreSQL** - SQLite not recommended for production
- **Configure media storage** - Use AWS S3 or Cloudinary for images
- **Enable HTTPS** - Most platforms provide free SSL

For troubleshooting and advanced configuration, refer to the [Deployment Guide](DEPLOYMENT_GUIDE.md).

---

*Last Updated: October 2, 2025*
