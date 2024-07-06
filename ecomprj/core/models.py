from django.db import models
from django.contrib import admin
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
 





STATUS_CHOICE = (
        ("process", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
)

STATUS = (
        ("draft", "Draft"),
        ("disabled", "Disabled"),
        ("rejected", "Rejected"),
        ("in_review", "In Review"),
        ("published", "Published"),
)

RATING = (
        ("1", "★☆☆☆☆"),
        ("2", "★★☆☆☆"),
        ("3", "★★★☆☆"),
        ("4", "★★★★☆"),
        ("5", "★★★★★"),
)


def user_directory_path(instance, filename):
        return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
   cid = models.UUIDField(unique=True, max_length=30)
   title= models.CharField(max_length=100, default="Shopify")
   image = models.ImageField(upload_to="categoryAdmin/",default="User.jpg")

class Meta:
        verbose_name_plural = "Categories" 

def category_image(self):
        return mark_safe('<img scr="%s" width="50" height="50" />' % (self.image.url))
    
def __str__(self):
        return self.title
class Tags(models.Model):
        pass
        
    
class Seller(models.Model):
        sid = models.UUIDField(unique=True, max_length=30)
        
        title= models.CharField(max_length=100, default="Seller Name")
        image = models.ImageField(upload_to=user_directory_path, default="Seller.jpg")
        description = models.TextField(null=True, blank=True, default= "This is the Seller")
        
        address = models.CharField(max_length=100, default="Street Name.")
        contact = models.CharField(max_length=100,default="+977 number" )
        Chat_resp_time = models.CharField(max_length=100, default="100")
        Ship_on_time = models.CharField(max_length=100, default="100")
        authentic_rating = models.CharField(max_length=100, default="100")
        days_return = models.CharField(max_length=100, default="100")
        warrenty_period = models.CharField(max_length=100, default="100")


user = models.ForeignKey(User, on_delete=models.CASCADE)


class Meta:
        verbose_name_plural = "Seller" 

def seller_image(self):
        return mark_safe('<img scr="%s" width="50" height="50" />' % (self.image.url))
    
def __str__(self):
        return self.title

class Product(models.Model):
        pid = models.UUIDField(unique=True,max_length=30)
        
        user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
        
        title= models.CharField(max_length=100, default="Title")
        image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
        description = models.TextField(null=True, blank=True, default= "This is the product")
         
        price = models.DecimalField(max_digits=10, decimal_places=2, default="1200")
        old_price = models.DecimalField(max_digits=10, decimal_places=2, default="1000")

        specifications = models.TextField(null=True, blank=True, default= "")
        #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL,null=True)

        product_status = models.CharField(choices=STATUS,max_length=10, default="in_review")

        status = models.BooleanField(default=True)
        in_stock = models.BooleanField(default=True)
        featured = models.BooleanField(default=False)
        digital = models.BooleanField(default=False)
        
        sku = ShortUUIDField(unique=True, max_length=10)

        date = models.DateTimeField(auto_now_add=True)
        update = models.DateTimeField(null=True, blank=True)
    
    
        class Meta:
            verbose_name_plural = "Products" 

        def product_image(self):
            return mark_safe('<img scr="%s" width="50" height="50" />' % (self.image.url))
    
        def __str__(self):
            return self.title
        
        def get_percentage(self):
               new_price = (self.price / self.old_price) * 100
               return new_price
        
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"


###############Cart,Order,Address################

class CartOrder(models.Model):
       user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
       price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1200")
       paid_status = models.BooleanField(default=True)
       order_date = models.DateTimeField(auto_now_add=True)
       product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

       class Meta:
            verbose_name_plural = "Cart Order"

class CartOrderItems(models.Model):
       order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
       invoice_no = models.CharField(max_length=200)
       product_status = models.CharField( max_length=30)
       item = models.CharField(max_length=200)
       image = models.CharField(max_length=200)
       qty = models.IntegerField(default=0)
       price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1200")
       total = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1200")

       class Meta:
            verbose_name_plural = "Cart Order Items"

       def order_img(self):
               return mark_safe('<img scr="%s" width="50" height="50" />' % (self.image))
       


#########product review,wishlist,address #######################


class ProductReview(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
        review = models.TextField()
        rating = models.IntegerField(choices=RATING, default=None )
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = "Product Review"
        
        def __str__(self):
               return self.product.title
        
        def get_rating(self):
               return self.rating
        

class wishlist(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
        product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = "wishlists"
        
        def __str__(self):
               return self.product.title
        
class Address(models.Model):
       user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
       address = models.CharField(max_length=100, null=True)
       status = models.BooleanField(default=False)

       class Meta:
            verbose_name_plural = "Address"