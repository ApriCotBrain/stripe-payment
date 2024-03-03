"""Helper functions for the endpoints of 'Orders' application."""

from decimal import Decimal

from orders.models import Order


def calculate_total_amount(order: Order) -> Decimal:
    """Calculate the total amount of the order."""
    total_amount = 0

    for order_item in order.order_to_items.all():
        total_amount += order_item.item.price * order_item.quantity

    return total_amount


def get_unique_order_items(order: Order) -> list:
    """Returns unique order items."""
    unique_order_items = []

    for order_item in order.order_to_items.all():
        total_item_amount = order_item.quantity * order_item.item.price
        existing_item_index = None

        for index, item in enumerate(unique_order_items):
            if item["item"].id == order_item.item.id:
                existing_item_index = index
                break

        if existing_item_index is not None:
            existing_item = unique_order_items[existing_item_index]
            existing_item["quantity"] += order_item.quantity
            existing_item["total_item_amount"] += total_item_amount
        else:
            unique_order_items.append(
                {
                    "item": order_item.item,
                    "quantity": order_item.quantity,
                    "price": order_item.item.price,
                    "total_item_amount": total_item_amount,
                }
            )

    return unique_order_items


def get_line_items_for_create_order_checkout_session(order: Order) -> list:
    """Returns a list of line_items for creating a checkout session."""
    line_items_dict = {}

    for order_item in order.order_to_items.all():
        order_item_id = f"{order_item.item.id}"

        if order_item_id in line_items_dict:
            line_items_dict[order_item_id]["quantity"] += order_item.quantity
        else:
            line_items_dict[order_item_id] = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(order_item.item.price * 100),
                    "product_data": {
                        "name": order_item.item.name,
                        "description": order_item.item.description,
                    },
                },
                "quantity": order_item.quantity,
            }

    return list(line_items_dict.values())
