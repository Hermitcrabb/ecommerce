from core.models import Product,Category,CartOrderItems,CartOrder,wishlist,Address,ProductImages,ProductReview




def default(request):
    categories = Category.objects.all()
    return {
        'categories':categories,
    }