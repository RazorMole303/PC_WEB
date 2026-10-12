from django.shortcuts import render


def home(request):
    """The landing page."""
    shop_name = "ByteBarn"
    return render(request, "shop/home.html", {"shop_name": shop_name})