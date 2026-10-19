"""The shopping basket — more of this in Guide 11."""

from decimal import Decimal

from .models import Product

CART_SESSION_KEY = "cart"

def get_cart(request):
    """Return the raw dictionary of {product_id: quantity}."""
    return request.session.get(CART_SESSION_KEY, {})

def cart_count(request):
     """Total number of things in the basket."""
     return sum(get_cart(request).values())