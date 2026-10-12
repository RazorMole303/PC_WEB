from django.shortcuts import render

# --- Pages anybody can see ----------------------------------------------------


def home(request):
    """The landing page."""
    return render(request, "shop/home.html")