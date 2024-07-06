from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product,Category,Seller,CartOrderItems,CartOrder,wishlist,Address,ProductImages,ProductReview

def index(request):
    product = Product.objects.all()

    context = {
        "products":product

    }
    return render(request, 'core/index.html', context)

