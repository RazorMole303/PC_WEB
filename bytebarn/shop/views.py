from django.contrib import messages
from django.shortcuts import render


def home(request):
    """The landing page."""
    messages.success(request, "Hello from Django!")
    return render(request, "shop/home.html")

def test_page(request):
    """A throwaway page, here to prove base.html is being reused."""
    return render(request, "shop/test_page.html")