# Quick Start Guide - ShoeKart 🚀

## Running the Project

1. **Start the development server:**
   ```powershell
   cd "c:\Users\daksh\OneDrive\Desktop\phthon it vendant\miniproject sem 4\shoeskart"
   python manage.py runserver
   ```

2. **Access the website:**
   - Homepage: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Admin Credentials
- Username: `admin`
- Password: (your set password)

## Key URLs

| Page | URL |
|------|-----|
| Homepage | http://127.0.0.1:8000/ |
| Sign In | http://127.0.0.1:8000/signin |
| Sign Up | http://127.0.0.1:8000/signup |
| Cart | http://127.0.0.1:8000/cart |
| Wishlist | http://127.0.0.1:8000/wishlist |
| Orders | http://127.0.0.1:8000/orders |
| Admin | http://127.0.0.1:8000/admin/ |

## Payment Testing

### Razorpay Test Cards
- Card Number: `4111 1111 1111 1111`
- CVV: Any 3 digits (e.g., `123`)
- Expiry: Any future date (e.g., `12/25`)
- Name: Any name

## Installed Dependencies

```
django==5.2.7
pillow
razorpay
```

## Project Structure

```
shoeskart/
├── app1/                  # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── admin.py          # Admin configuration
│   └── migrations/       # Database migrations
├── static/
│   ├── css/
│   │   └── style.css     # 🎨 NEW Enhanced CSS
│   ├── images/           # Static images
│   └── js/               # JavaScript files
├── templates/            # HTML templates
│   ├── base.html         # 🎨 Enhanced base template
│   ├── index.html        # 🎨 Redesigned homepage
│   ├── signin.html       # 🎨 New auth design
│   ├── signup.html       # 🎨 New auth design
│   ├── product_details.html  # 🎨 Enhanced product page
│   ├── payment.html      # 🎨 New payment design
│   └── ...
├── media/                # User uploaded files
└── shoeskart/            # Project settings
    └── settings.py
```

## Features

### 🛍️ Shopping Features
- Browse products by category
- Search products
- View product details
- Add to cart
- Add to wishlist
- Place orders
- Payment integration (Razorpay)
- Cash on Delivery option

### 🎨 Design Features
- Modern gradient UI
- Smooth animations
- Responsive design
- Icon integration (Font Awesome)
- Beautiful alerts (SweetAlert2)
- Hover effects
- Card-based layouts

### 👤 User Features
- User registration
- User login/logout
- Order history
- Address management
- Profile management

### 🔐 Admin Features
- Product management
- Category management
- Order management
- User management

## Browser Compatibility

✅ Chrome (Recommended)
✅ Firefox
✅ Edge
✅ Safari
⚠️ IE11 (Limited support)

## Tips

1. **Clear browser cache** after design updates (Ctrl+Shift+R)
2. **Use Chrome DevTools** to test responsiveness
3. **Check terminal** for any error messages
4. **Refresh payment page** if Razorpay doesn't load initially

## Common Issues & Solutions

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic` and refresh browser

### Issue: Images not displaying
**Solution:** Check if `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.py

### Issue: Payment gateway error
**Solution:** Verify Razorpay credentials in both views.py and payment.html match

### Issue: Database errors
**Solution:** Run migrations: `python manage.py migrate`

## Development Commands

```powershell
# Run server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Open Python shell
python manage.py shell
```

## Customization

### Change Color Scheme
Edit `static/css/style.css` - Look for `:root` variables at the top

### Modify Navigation
Edit `templates/base.html` - Find the `<nav>` section

### Update Homepage Layout
Edit `templates/index.html` - Modify the product grid

### Change Fonts
Add Google Fonts link in `base.html` and update CSS

## Support

For issues or questions:
1. Check the terminal for error messages
2. Review `DESIGN_UPDATES.md` for detailed changes
3. Check Django documentation
4. Review Razorpay integration docs

---

**Happy Shopping! 🎉**
