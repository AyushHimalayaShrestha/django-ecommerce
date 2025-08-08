from django.db import models

# Create your models here.

class Category(models.Model):
    category_name= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.category_name

class Product(models.Model):
    product_name= models.CharField(max_length=100, null=True)
    product_price=models.IntegerField(null=True)
    description=models.TextField(null=True)
    quantity=models.IntegerField(null=True)
    image= models.URLField(null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.product_name

