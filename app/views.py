from django.shortcuts import render,redirect, get_object_or_404
from .models import (Customer, Product, Cart, Ordered, Ordered_placed, Wishlist, Profile)
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from django.db.models import Count
from django.contrib.auth import logout

def home(request):
    all_product = Product.objects.all().order_by('-id')[:8]
    context = {
        'all_product' : all_product
    }
    return render(request, "index.html",context)

def contact(request):
    return render(request, 'contact.html')
    
class CategoryView(View):
    def get(self,request,val):
       product = Product.objects.filter(category=val)
       brand = Product.objects.filter(category=val).values('brand')
       return render(request, 'category.html',locals())

class CategoryBrand(View):
    def get(self,request,val):
       product = Product.objects.filter(brand=val)
       brand = Product.objects.filter(category=product[0].category).values('brand')
       return render(request, 'category.html',locals())

def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains = q)
    context ={
        'q' : q,
        'data' :data
    }
    return render(request, 'search.html', context)

class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form' : form})

    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation! Registered Successfully')
            form.save()
            return redirect("login")
        return render(request, 'registration.html', {'form' : form})

def profile(request):
    data = Profile.objects.filter(user=request.user)
    context = {
        'data' : data
    }
    return render(request, 'profile.html', context)

def profile_info(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect('home')
    if request.method ==  'POST':
        user = request.user
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        record = Profile(user=user, name=name, phone=phone, gender=gender, birth_date=birth_date, city=city, state=state, zip_code=zipcode)
        record.save()
        return redirect('home')
        
    data = Profile.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'profile_info.html',context)

def profile_update(request,id):
    if request.method ==  'POST':
        user = request.user
        picture = request.FILES.get('picture')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        record = Profile(user=user, id=id,picture=picture, name=name, phone=phone, gender=gender, birth_date=birth_date, city=city, state=state, zip_code=zip_code)
        record.save()
        return redirect('profile')
    data = Profile.objects.get(pk=id)
    context = {
        'data' : data
    }
    return render(request, 'profile_update.html', context)

def productdetails(request,id):
    pro_details = Product.objects.get(pk=id)
    context = {
        'pro_details' : pro_details
    }
    return render(request, 'product_details.html',context)

def discount(request):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(request, 'discount.html', context)

def addtocart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to add items to your cart.")
        return redirect('/login/')

    product = get_object_or_404(Product, pk=product_id)
    customer, created = Customer.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = Cart.objects.get_or_create(user=customer, product=product)

    # If the product is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    
    return redirect('cart')

def cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to view your cart.")
        return redirect('/login/')

    customer = Customer.objects.get(user=request.user)
    carts = Cart.objects.filter(user=customer)
    total_price = 0  
    total_quantity=0
    for i in carts:
        total_price += i.product.discount_price * i.quantity
        total_quantity += i.quantity
    context = {
        'carts': carts,
        'total': total_price,
        'quantity': total_quantity
    }
    return render(request, 'carts.html', context)

def addCartDelete(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart = Cart.objects.filter(user = customer,pk=id)
    cart.delete()   
    return redirect('cart')

def add_wishlist(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    customer, created = Customer.objects.get_or_create(user=request.user)

    wish_item, created = Wishlist.objects.get_or_create(user=customer, product=product)
    wish_item.save()
    return redirect('wishlist')

def wishlist(request):
    customer = Customer.objects.get(user=request.user)
    wishlist = Wishlist.objects.filter(user=customer)
    context = {
        'wishlist' : wishlist
    }
    return render(request, 'wishlist.html', context)

def delete_wishlist(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    wishlist = Wishlist.objects.filter(user = customer,pk=id)
    wishlist.delete() 
    return redirect('wishlist')

def checkout(request):
    delivery_address = Ordered.objects.all()
    customer = Customer.objects.get(user=request.user)
    carts = Cart.objects.filter(user=customer)
    total_price = 0  
    total_quantity=0
    for i in carts:
        total_price += i.product.discount_price * i.quantity
        total_quantity += i.quantity
    context = {
        'd_address' : delivery_address,
        'total': total_price,
        'quantity': total_quantity
    }
    return render(request, 'checkout.html', context)

def delivery_address(request):
    if request.method == 'POST':
       user = request.user
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       house_no = request.POST.get('house_no')
       road_name = request.POST.get('road_name')
       city = request.POST.get('city')
       state = request.POST.get('state')
       zip_code = request.POST.get('zip_code')
       record = Ordered(user=user,name=name, phone=phone, house_no=house_no, road_name=road_name, city=city, state=state, zip_code=zip_code)
       record.save()
       return redirect('checkout') 
    return render(request, 'delivery_address.html')

def update_address(request,id):
    if request.method == 'POST':
       user = request.user
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       house_no = request.POST.get('house_no')
       road_name = request.POST.get('road_name')
       city = request.POST.get('city')
       state = request.POST.get('state')
       zip_code = request.POST.get('zip_code')
       record = Ordered(user=user, id=id, name=name, phone=phone, house_no=house_no, road_name=road_name, city=city, state=state, zip_code=zip_code)
       record.save()
       return redirect('checkout') 
    data = Ordered.objects.get(pk=id)
    return render(request, 'update_address.html',{'data':data})

def logoutview(request):
    logout(request)
    return redirect(home)

def orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Ordered_placed.objects.filter(customer=customer).order_by('-ordered_date')
    return render(request, 'orders.html', {'orders': orders})

def place_order(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = Cart.objects.filter(user=customer)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart')

    for item in cart_items:
        Ordered_placed.objects.create(
            customer=customer,
            product=item.product,
            cart=item,
            quantity=item.quantity,
        )

    cart_items.delete()
    messages.success(request, "✅ Your order has been placed successfully!")
    return redirect('orders')

def payment(request):
    customer = Customer.objects.get(user=request.user)
    carts = Cart.objects.filter(user=customer)
    total_price = 0  
    total_quantity=0
    for i in carts:
        total_price += i.product.discount_price * i.quantity
        total_quantity += i.quantity
    context = {
        'total': total_price,
        'quantity': total_quantity
    }
    return render(request, 'payment.html', context)

def product(request):
    all_product = Product.objects.all()
    context = {
        'all_product': all_product
    }
    return render(request, 'product.html',context)

def order_success(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = Cart.objects.filter(user=customer)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart')

    for item in cart_items:
        Ordered_placed.objects.create(
            customer=customer,
            product=item.product,
            cart=item,
            quantity=item.quantity,
        )
    cart_items.delete()
    return render(request, 'order_success.html')
