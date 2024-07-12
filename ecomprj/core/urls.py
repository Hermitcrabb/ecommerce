from django.urls import path
from  core.views import category,products_list,contact,shop,checkout,index,category_items

app_name = "core"

urlpatterns = [
    path("", index, name = "index"),    
    path("checkout/", checkout, name= "checkout"),
    path("contact/", contact, name= "contact"),
    path("shop/", shop, name= "shop"),
    path("products/<str:pid>/", products_list, name= "products"),
    path("category/",category,name="category"),
    path("category_items/<str:cid>/",category_items,name="category_items"),

]