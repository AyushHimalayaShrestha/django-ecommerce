from django.shortcuts import render
from . models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.



def products(request):
    product_lists =Product.objects.all().order_by('-id')
    item={
        "products":product_lists
    }
    return  render(request, 'product/productlists.html',item)

def product_details(request,product_id):
    product = Product.objects.get(id =product_id)

    data={
       'product':product

    }
    return render(request,'product/product_details.html',data)

# cart list
@login_required(login_url='login_view')
def cart_lists(request):
    return render(request,'cart/cart.html')
