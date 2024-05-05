from django.contrib import admin
from .models import Categories, SubCategories, Products,Cart,Address,Wishlist,Orders

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(SubCategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    list_display=["name","categories"]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","price","subcategories","categories","desc","image"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=["product","quantity","user"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=["user","address","pincode"]



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=["product","user"]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=["order_id","product","user","quantity","order_date","address","payment_status"]