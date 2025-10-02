from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategories(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    desc =  models.TextField(max_length=799)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategories = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to="product_images")
    objects = models.Manager()

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])

    def __str__(self):
        return self.address


class Wishlist(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Orders(models.Model):
    order_id=models.IntegerField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    
