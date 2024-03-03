"""Template filters for the 'Orders' application."""

from django import template

register = template.Library()


@register.filter
def get_item_total_amount(item_total_amounts, order_item_id):
    """Retrieve the total amount for a the item from the item_totals dictionary."""
    return item_total_amounts.get(order_item_id)
