from django.shortcuts import render, redirect
from  product.forms import *
from product.models import *

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('add_category')

    else:
        form = CategoryForm()        

    return render(request,'add_category.html',{'form':form})

# add product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('dashboard_product_lists')

    else:
        form=ProductForm()
    return render(request,'add_product.html',{'form':form})

# Getting Products

def products(request):
    product_lists = Product.objects.all()
    return render(request,'dashboard_product_lists.html',{'products':product_lists})