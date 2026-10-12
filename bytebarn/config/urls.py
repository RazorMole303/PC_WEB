from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # The admin site, at /admin/
    path("admin/", admin.site.urls),

    # Everything else belongs to the shop app, so / goes straight there.
    path("", include("shop.urls")),
]