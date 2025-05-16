from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujrat', 'Gujrat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhan', 'Jharkhan'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Maharashtra', 'Maharashtra'),
        ('Madhaya Pradesh', 'Madhaya Pradesh'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Tripura', 'Tripura'),
        ('Telangana', 'Telangana'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman & Nicobar (UT)', 'Andaman & Nicobar (UT)'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra & Nagar Haveli and Daman & Diu (UT)', 'Dadra & Nagar Haveli and Daman & Diu (UT)'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Ladakh', 'Ladakh'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),                
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, blank=True, null=True)

    
    def __str__(self):
        return str(self.user)


CATEGORY_CHOICES = (
    ('Camera', 'Camera'),
    ('Men', 'Men'),
    ('Women' , 'Women'),
    ('Goggle', 'Goggles'),
    ('Shoes', 'Shoes'),
    ('Mobile', 'Mobiles'),
    ('Watch', 'Watches'),
    ('Bag', 'Bags'),
)

class Product(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=200,blank=True)
    product_name = models.CharField(max_length=200)
    discount_price = models.FloatField()
    selling_price = models.FloatField()
    discription = models.TextField()
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product_name)


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete = models.CASCADE)  
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)


STATUS_CHOICES =(
    ('Accepted' , 'Accepted'),
    ('On The Way' , 'On The Way'),
    ('Delivered' , 'Delivered'),
    ('Canceled' , 'Canceled'),
)

class Ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    house_no = models.TextField()
    road_name = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Ordered_placed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.user)   

class Wishlist(models.Model):
    user = models.ForeignKey(Customer, on_delete = models.CASCADE)  
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    user = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to="picture")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return str(self.user)
