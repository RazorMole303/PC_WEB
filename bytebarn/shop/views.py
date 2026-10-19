from django.contrib import messages
from django.shortcuts import render
from .models import Product

def home(request):
    """The landing page. Shows a handful of featured products."""
    products = Product.objects.filter(featured=True, stock__gt=0)
    return render(request, "shop/home.html", {"products": products})

def product_list(request):
    """The shop window: every product, with filters."""
    products = Product.objects.filter(stock__gt=0)

    # These come from the query string, e.g. /shop/?category=gpu&q=radeon
    selected_category = request.GET.get("category", "")
    query = request.GET.get("q", "").strip()

    if selected_category:
        products = products.filter(category=selected_category)
    if query:
        products = products.filter(name__icontains=query)

    context = {
        "products": products,
        "categories": Product.CATEGORY_CHOICES,
        "selected_category": selected_category,
        "query": query,
    }
    return render(request, "shop/product_list.html", context)



def test_page(request):
    """A throwaway page, here to prove base.html is being reused."""
    return render(request, "shop/test_page.html")