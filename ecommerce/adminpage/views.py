from django.shortcuts import render, redirect
from  product.forms import *

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('add_category')

    else:
        form = CategoryForm()        

    return render(request,'add_category.html',{'form':form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('add_product')

    else:
        form=ProductForm()
    return render(request,'add_product.html',{'form':form})