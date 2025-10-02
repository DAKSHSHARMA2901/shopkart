from django.shortcuts import render , redirect,get_object_or_404
from .models import Products,Categories,SubCategories,Cart,Address,Wishlist,Orders
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q
from django.http import HttpResponse
import razorpay


# Create your views here.
from django.db.models import Subquery, OuterRef

def index(request):
    # Fetch all subcategories
    subcategories = SubCategories.objects.all()
    
    # Initialize an empty list to store one product from each subcategory
    products_per_subcategory = []
    
    # Iterate through each subcategory
    for subcategory in subcategories:
        # Fetch one product from the current subcategory
        product = Products.objects.filter(subcategories=subcategory).first()
        # If a product is found for the subcategory, add it to the list
        if product:
            products_per_subcategory.append(product)
    
    return render(request, "index.html", {'products': products_per_subcategory})


def product_details(request,pid):
    products = Products.objects.get(id=pid)
    
    date = datetime.datetime.today().date() + datetime.timedelta(days=5)
    return render(request,"product_details.html",{'products':products,'date':date})

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
        if pass1 == pass2:
                try:
                    user = User.objects.create_user(username=email,first_name=fname,last_name=lname,email=email,password=pass1)
                    user.save()
                    return redirect('signin')
                except:
                    error = "User already exists"
                    return render(request,"signup.html",{'error':error})
        else:
            error = "password does not match!"
            return render(request,"signup.html",{'error':error})
            
    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user = authenticate(username = uname, password = pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            error = "Invalid Username or Password!"
            return render(request,"signin.html",{'error':error})
        
    return render(request,"signin.html")

def signout(request):
    logout(request)
    return redirect('index')
    

    
def about(request):
    return render(request,"about.html")

def search_product(request):
    url = request.GET.get('product')
    print("=============================================================================================="+url)
    
    # Simplified logic - try to get the subcategory and return products
    try:
        value = SubCategories.objects.get(name=url)
        products = Products.objects.filter(subcategories=value)
        return render(request, "search_results.html", {'products': products})
    except SubCategories.DoesNotExist:
        # If subcategory doesn't exist, return empty products list
        return render(request, "search_results.html", {'products': []})
    

def search_bar(request):
    var = request.GET.get('searchbar')
    categories = Categories.objects.filter(name__icontains=var)
    subcategories = SubCategories.objects.filter(name__icontains=var)

    # Extracting primary keys from queryset objects
    category_ids = categories.values_list('id', flat=True)
    subcategory_ids = subcategories.values_list('id', flat=True)

    # Get product names matching the search query, categories, or subcategories
    products = Products.objects.filter(
        Q(product_name__icontains=var) | 
        Q(subcategories__id__in=subcategory_ids) | 
        Q(categories__id__in=category_ids)
    )
    return render(request, "search_results.html",{'products': products})
    
    
def add_cart(request,pid):
    c = Wishlist.objects.filter(product = pid,user =  request.user)
    if c is not None:
        c.delete()
    product = Products.objects.get(id=pid)
    user = request.user if request.user.is_authenticated else None
    if user:
         cart_item , created = Cart.objects.get_or_create(product = product,user = user)
    else:
        return redirect('signin')
    
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1

    cart_item.save()

    return redirect('index')

def cart(request):
    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user = request.user)
    else:
        cart_item = Cart.objects.filter(user = None)

    context = {}
    context['items']= cart_item

    total_price = 0
    for x in cart_item:
        total_price += (x.product.price * x.quantity)

    context['total']=total_price

    length = len(cart_item)
    context['total_product']= length

    return render(request,"cart.html",context)
    
def updateqty(request,val,pid):
    user = request.user
    c = Cart.objects.filter(product = pid,user =  user)
    if val == 0:
         if c[0].quantity > 1:
            a = c[0].quantity-1
            c.update(quantity=a)
    else:
         a = c[0].quantity+1
         c.update(quantity=a)
         
    return redirect('cart')


def remove_product(request,pid):
    user = request.user
    c = Cart.objects.filter(product = pid,user =  user)
    c.delete()
    return redirect('cart')

def address(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            new_address = request.POST['address']
            new_pincode = request.POST['pincode']
            total_address = Address.objects.filter(user=request.user)
            if len(total_address) < 3:
                add_address = Address.objects.create(user=request.user, address=new_address, pincode=new_pincode)
                add_address.save()
                # Redirect after POST
                return redirect('address')  # Replace 'address_view' with the name of your view for displaying addresses
            else:
                address = Address.objects.filter(user=request.user)
                return render(request, "address.html", {'address': address})
        else:
            address = Address.objects.filter(user=request.user)
            return render(request, "address.html", {'address': address})
    else:
        # Handle unauthenticated users if needed
        return HttpResponse("Unauthorized", status=401)
    
def delete_address(request,pid):
    if request.user.is_authenticated:
        address =  Address.objects.filter(user=request.user,id=pid)
        address.delete()
        return redirect('address')

def update_address(request, pid):
    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user)
        update_address = get_object_or_404(Address, user=request.user, id=pid)
        if request.method == 'POST':
            # Update the address with the new data from the form
            update_address.address = request.POST.get('address')
            update_address.pincode = request.POST.get('pincode')
            update_address.save()
            # Redirect to the address view after updating
            return redirect('address')
        else:
            # Render the form with the existing address data for editing
            return render(request, 'address.html', {'update_address': update_address,'address':address})
    else:
        # Handle unauthenticated users if needed
        return HttpResponse("Unauthorized", status=401)

def wishlist(request):
    if request.user.is_authenticated:
        wishlist_item = Wishlist.objects.filter(user = request.user)
    else:
        wishlist_item = Wishlist.objects.filter(user = request.user)

    context = {}
    context['items']= wishlist_item
    return render(request,"wishlist.html",context)


def add_wishlist(request,pid):
    product = Products.objects.get(id=pid)
    user = request.user if request.user.is_authenticated else None
    if user:
         wishlist_item , created = Wishlist.objects.get_or_create(product = product,user = user)
    else:
        return redirect('signin')
    
    if not created:
        error="already added to wishlist"
    else:
        wishlist_item.save()
    return redirect('wishlist')


def remove_wishlist(request,pid):
    user = request.user
    c = Wishlist.objects.filter(product = pid,user =  user)
    c.delete()
    return redirect('wishlist')

def confirm_order(request,pid):
    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user = request.user)
        address = Address.objects.get(id=pid,user=request.user)
    else:
        cart_item = Cart.objects.filter(user = None)
        address = Address.objects.get(user=None)


    context = {}
    context['items']= cart_item
    context['address'] =address
    list= []
    total_price = 0
    for x in cart_item:
        total_price += (x.product.price * x.quantity)
        list.append(total_price)

    context['list']=list

    context['total']=total_price

    length = len(cart_item)
    context['total_product']= length

    return render(request,"confirm_order.html",context)

import random
def payment(request,pid):
    if request.user.is_authenticated:
        user = request.user
        address = Address.objects.get(user = user,id=pid)
        allcarts = Cart.objects.filter(user = user)
        oid = 0
        for x in allcarts:
            oid = random.randrange(1000,9999)
            date = datetime.datetime.today().date()
            Orders.objects.create(order_id = oid,product= x.product,user = x.user,quantity =x.quantity,order_date = date,address= address)
            x.delete()
        orders = Orders.objects.filter(user= user)

        total_price = 0
        for x in allcarts:
            total_price += (x.product.price * x.quantity)
        for x in orders:
            oid=x.order_id
        
        client = razorpay.Client(auth=("rzp_test_ROdO6CGivLBaVf", "hpwho4yrEQ4BW1B0mQBMDlt3"))

        data = { "amount": total_price*100, "currency": "INR", "receipt": str(oid) }
        payment = client.order.create(data=data)

        context = {}

        context['data'] = payment
        context['amount']=payment
        context['payment_status']= False
        return render(request,"payment.html",context)
    else:
        user = None
        return redirect('signin')

def orders(request):
     if request.user.is_authenticated:
        user = request.user
        allorders = Orders.objects.filter(user=user)
        
     return render(request,"orders.html",{'allorders':allorders})
    
    
             
    
        