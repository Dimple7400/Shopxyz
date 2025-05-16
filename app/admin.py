from django.contrib import admin
from .models import (Customer, Product, Cart, Ordered, Ordered_placed, Wishlist, Profile)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user' ,'locality', 'city','zipcode', 'state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_name', 'selling_price', 'discription', 'brand', 'image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

@admin.register(Ordered)
class Ordered(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'house_no', 'road_name', 'city', 'state', 'zip_code']

@admin.register(Ordered_placed)
class Ordered_placed(admin.ModelAdmin):
    list_display = ['user','customer', 'product', 'cart', 'quantity', 'ordered_date', 'status']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'picture', 'name', 'phone', 'gender', 'birth_date', 'city', 'state', 'zip_code']

