"""
URL configuration for shoeskart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('product_details/<int:pid>',views.product_details,name="product_details"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('about',views.about,name="about"),
    path('search_product',views.search_product,name="search_product"),
    path('search_bar',views.search_bar,name="search_bar"),
    path('add_cart/<int:pid>',views.add_cart,name="add_cart"),
    path('cart',views.cart,name="cart"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('add_wishlist/<int:pid>',views.add_wishlist,name="add_wishlist"),
    path('remove_wishlist/<int:pid>',views.remove_wishlist,name="remove_wishlist"),
    path('updateqty/<int:val>/<int:pid>',views.updateqty,name="updateqty"),
    path('remove_product/<int:pid>',views.remove_product,name="remove_product"),
    path('address',views.address,name="address"),
    path('delete_address/<int:pid>',views.delete_address,name="delete_address"),
    path('update_address/<int:pid>',views.update_address,name="update_address"),
    path('confirm_order/<int:pid>',views.confirm_order,name="confirm_order"),
    path('payment/<int:pid>',views.payment,name="payment"),
    path('orders',views.orders,name="orders"),
    
   


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)