"""URL configuration of the 'stripe_payment' application."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("items.urls")),
    path("admin/", admin.site.urls),
]
