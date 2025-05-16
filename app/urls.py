from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('categorybrand/<val>', views.CategoryBrand.as_view(), name="categorybrand"),
    path('search/', views.search, name='search'), 
    path('registration/',views.RegistrationView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/',views.logoutview, name='logout'), 
    path('profile/', views.profile, name='profile'),
    path('profile_info/', views.profile_info, name='profile_info'),
    path('profile_update/<int:id>', views.profile_update, name='profile_update'),
    path('productdetails/<int:id>', views.productdetails, name='productdetails'),
    path('discount/',views.discount, name='discount'),
    path('addtocart/<int:product_id>',views.addtocart, name='addtocart'),
    path('cart/',views.cart, name='cart'),
    path('delete/<int:id>', views.addCartDelete, name='addcartdelete'),
    path('checkout/', views.checkout, name='checkout'),
    path('delivery_address/',views.delivery_address, name='delivery_address'),
    path('update_address/<int:id>',views.update_address, name='update_address'),
    path('orders/', views.orders, name='orders'),
    path('place_order/', views.place_order, name='place_order'),
    path('payment/', views.payment, name='payment'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:product_id>', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:id>', views.delete_wishlist, name='delete_wishlist'),
    path('product/', views.product, name='product'),
    path('order_success/', views.order_success, name='order_success'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)