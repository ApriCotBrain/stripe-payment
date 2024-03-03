"""Admin site settings of the 'Orders' application."""

from django.contrib import admin
from django.contrib.auth.models import Group

from orders.models import Order


class OrderItemInline(admin.TabularInline):
    """Settings for presenting items in 'Order' model."""

    model = Order.items.through


@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    """Settings for presenting 'Order' model on the admin site."""

    list_display = ("id",)
    search_fields = ("id",)
    inlines = (OrderItemInline,)


admin.site.unregister(Group)
