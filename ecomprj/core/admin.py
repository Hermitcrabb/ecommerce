from django.contrib import admin
from core.models import Product,Category,CartOrderItems,CartOrder,wishlist,Address,ProductImages,ProductReview



# Register your models here.



class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('pid','user','title','image','price','category','featured','product_status')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cid','title','image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user','price','paid_status','order_date','product_status')

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('invoice_no','order','image','qty','price','product_status','total')

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','review','rating')

class wishlistAdmin(admin.ModelAdmin):
    list_display = ('user','product','date')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','address','status')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(wishlist,wishlistAdmin)
admin.site.register(Address,AddressAdmin)

