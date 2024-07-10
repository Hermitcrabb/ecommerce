from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),    
    path("checkout/", views.checkout, name= "checkout"),
    path("contact/", views.contact, name= "contact"),
    path("shop/", views.shop, name= "shop"),
    path("single_product_details/", views.single_product_details, name= "single_product_details"),
    path("category/<cid>/",views.category,name="category")

]