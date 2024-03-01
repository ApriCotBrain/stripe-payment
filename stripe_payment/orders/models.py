"""Database settings of the 'Orders' application."""

from django.db import models

from core.orders.constants import CONSTANTS_ORDERS_APP
from items.models import Item


class Order(models.Model):
    """Model Order."""

    items = models.ManyToManyField(
        Item,
        verbose_name="items",
        help_text="Order items.",
        related_name="orders",
        through="OrderToItem",
    )

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(self.id)


class OrderToItem(models.Model):
    """Model OrderToItem. Linking model for products added to the order."""

    order = models.ForeignKey(
        Order,
        verbose_name="order",
        help_text="The order in which the item is.",
        on_delete=models.PROTECT,
        related_name="order_to_items",
    )
    item = models.ForeignKey(
        Item,
        verbose_name="item",
        help_text="The item that is in the order.",
        on_delete=models.PROTECT,
        related_name="order_to_items",
    )
    quantity = models.IntegerField(
        "quantity",
        help_text="The quantity of the product in the order",
        default=CONSTANTS_ORDERS_APP["ORDER_QUANTITY_DEFAULT_VALUE"],
    )

    class Meta:
        verbose_name = "order to item"
        verbose_name_plural = "order to items"

    def __str__(self):
        return f"{self.item} {self.quantity}"
