"""Admin site settings of the 'Items' application."""

from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Settings for presenting 'Item' model on the admin site."""

    list_display = (
        "id",
        "name",
        "description",
        "price",
    )
    search_fields = ("name",)
