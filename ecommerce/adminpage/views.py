from django.shortcuts import render, redirect
from  product.forms import *
from product.models import *
from django.contrib import messages
from users.auth import admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    return render(request,'dashboard/main.html')

@admin_only
@login_required
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
@admin_only
@login_required
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
@admin_only
@login_required
def products(request):
    product_lists = Product.objects.all()
    return render(request,'dashboard_product_lists.html',{'products':product_lists})

# getting category
@admin_only
@login_required
def category(request):
    category_lists = Category.objects.all()
    return render(request,'dashboard_category_lists.html',{'categories':category_lists})

# update product
@admin_only
@login_required
def update_product(request, product_id):
    instance = Product.objects.get(id = product_id)
    if request.method =='POST':
        form =ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Product updated successfully!")
            return redirect('dashboard_product_lists')
        else:
            messages.error(request,"Error,Something went wrong!")

    else:
        form =ProductForm(instance=instance)

    return render(request,'update_product.html',{'form':form})

# delete product
@admin_only
@login_required
def delete_product(request, product_id):
    product=Product.objects.get(id = product_id)
    product.delete()
    messages.success(request,'Product deleted successfully!')
    return redirect('dashboard_product_lists')

# update category
@admin_only
@login_required
def update_category(request, category_id):
    instance= Category.objects.get(id=category_id)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Category updated successfully!')
            return redirect('dashboard_category_lists')
        else:
            messages.error(request,"Error,Something went wrong!")
            
    else:
        form=CategoryForm(instance=instance)
    return render(request,'update_category.html',{'form':form})

# delete category
@admin_only
@login_required
def delete_category(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.success(request,'Category deleted successfully!')
    return redirect('dashboard_category_lists')
