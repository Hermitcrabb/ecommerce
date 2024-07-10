from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product,Category,CartOrderItems,CartOrder,wishlist,Address,ProductImages,ProductReview

def index(request):
    #product = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published",featured=True)

    context = {
        "products":products

    }
    return render(request, 'core/index.html', context)

def shop(request):
    products = Product.objects.all().order_by("-id")
    Categories = Category.objects.all()
 
    context = {
        "categories":Categories,
        "products":products,
    }
    return render(request,'core/shop.html', context)

def category(request,cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status = "published", category=category)

    context = {
        "category":category,
        "products":products,
    }
    return render(request,'core/category.html',context)

def checkout(request):
    return render(request,'core/checkout.html')

def contact(request):
    return render(request,'core/contact.html')

def single_product_details(request):
    return render(request,'core/single-product-details.html')