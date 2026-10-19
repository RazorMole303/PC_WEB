from django.urls import path

from . import views

# The name= on each path is how we refer to a URL from a template, so we never
# hard-code addresses in our HTML.

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.product_list, name="product_list"),
]