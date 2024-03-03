"""Helper functions for the endpoints of 'Orders' application."""


def calculate_total_amount(order):
    """Calculate the total amount of the order."""
    total_amount = 0

    for order_item in order.order_to_items.all():
        total_amount += order_item.item.price * order_item.quantity

    return total_amount


def calculate_item_total_amount(order):
    """Calculate the total amount for each item."""
    item_total_amount = {}

    for order_item in order.order_to_items.all():
        total_price = order_item.item.price * order_item.quantity
        item_total_amount[order_item.id] = total_price

    return item_total_amount
