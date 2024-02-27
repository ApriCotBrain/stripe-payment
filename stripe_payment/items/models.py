"""Database settings of the 'Items' application."""

from django.db import models

from core.items.field_limits import FIELD_LIMITS_ITEMS_APP

class Item(models.Model):
    "Model Item."

    name = models.CharField(
        "name",
        help_text="Items's name",
        max_length=FIELD_LIMITS_ITEMS_APP["ITEM_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "An item with this name already exists.",
        },
    )
    description = models.CharField(
        "description",
        help_text="Item's description",
        max_length=FIELD_LIMITS_ITEMS_APP["ITEM_DESCRIPTION_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "An Item with this description already exists.",
        },
    )
    price = models.DecimalField(
        "price",
        help_text = "Item's price",
        max_digits=FIELD_LIMITS_ITEMS_APP["ITEM_PRICE_MAX_DIGITS"],
        decimal_places=FIELD_LIMITS_ITEMS_APP["ITEM_PRICE_MAX_DECIMAL_PLACES"],
    )

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return self.name
