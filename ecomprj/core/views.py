from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from core.models import Product,Category,CartOrderItems,CartOrder,wishlist,Address,ProductImages,ProductReview

def index(request):
    
    products = Product.objects.filter(product_status="published",featured=True)

    context = {
        "products":products

    }
    return render(request, 'core/index.html', context)

def shop(request):
    products = Product.objects.all().order_by("-id")
    
 
    context = {
        
        "products":products,
    }
    return render(request,'core/shop.html', context)

def category(request):
    category = Category.objects.all() 

    context = {
        "category": category,
    }
    return render(request,'core/category.html', context)

def category_items(request, cid):
    categorys = Category.objects.get(cid=cid)  # Using singular 'category' for clarity
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "categorys": categorys,
        "products": products,
    }

    return render(request, 'core/category_items.html', context)

def checkout(request):
    return render(request, 'core/checkout.html')

def contact(request):
    return render(request, 'core/contact.html')

def products_list(request,pid):
    products = get_object_or_404(Product,pid=pid)
    p_image = products.p_images.all()
    context = {
        "product": products,
        "p_image": p_image,
    }
    return render(request, 'core/products.html', context)