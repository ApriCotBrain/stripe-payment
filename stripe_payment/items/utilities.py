"""Helper functions for the endpoints of 'Items' application."""

from items.models import Item


def get_line_items_for_create_item_checkout_session(item: Item) -> list:
    """Returns a list of line_items for creating a checkout session."""
    return [
        {
            "price_data": {
                "currency": "usd",
                "unit_amount": int(item.price * 100),
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
            },
            "quantity": 1,
        }
    ]
