from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Category
class Category(models.Model):
    category_name= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.category_name

# Product
class Product(models.Model):
    product_name= models.CharField(max_length=100, null=True)
    product_price=models.IntegerField(null=True)
    description=models.TextField(null=True)
    quantity=models.IntegerField(null=True)
    image= models.FileField(upload_to="products/", blank=True, null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.product_name
    

# Cart




class Cart(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   product= models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity= models.PositiveIntegerField()
   created_at= models.DateTimeField(auto_now_add=True)
   updated_at =models.DateTimeField(auto_now=True)

# order
class Order(models.Model):
   PAYMENT_METHOD =(
      ("Cash On Delivery","Cash On Delivery"),
      ("Esewa","Esewa"),
      ("Khalti","Khalti")
   )

   user =models.ForeignKey(User, on_delete=models.CASCADE)
   product= models.ForeignKey(Product,on_delete=models.CASCADE)
   totalPrice= models.IntegerField()
   payment_method= models.CharField(choices=PAYMENT_METHOD)
   payment_status= models.CharField(default="pending")
   email=models.EmailField()
   contact_no = models.CharField()
   address = models.CharField(max_length=150)
   created_at= models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


