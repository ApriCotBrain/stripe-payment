"""Views for endpoints of the "Orders" application."""

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import stripe

from orders.models import Order
from orders.utilities import calculate_total_amount, calculate_item_total_amount

stripe.api_key = settings.STRIPE_SECRET_API_KEY


def order_detail(request, order_id):
    """View function to display the details of the item."""
    order = get_object_or_404(Order, id=order_id)
    item_total_amounts = calculate_item_total_amount(order)
    total_amount = calculate_total_amount(order)
    STRIPE_PUBLIC_API_KEY = settings.STRIPE_PUBLIC_API_KEY

    context = {
        "order": order,
        "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY,
        "item_total_amount": item_total_amounts,
        "total_amount": total_amount,
    }
    return render(request, "order_detail.html", context)


def create_checkout_session(request, order_id):
    """URL request handler to create Session Id for paying for the selected item."""
    order = get_object_or_404(Order, id=order_id)

    line_items = []
    for order_item in order.order_to_items.all():
        item = order_item.item
        line_item = {
            "price_data": {
                "currency": "usd",
                "unit_amount": int(item.price * 100),
                "product_data": {
                    "name": item.name,
                    "description": item.description,
                },
            },
            "quantity": order_item.quantity,
        }
        line_items.append(line_item)

    try:
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        return JsonResponse({"session_id": session["id"]})
    except Exception as error:
        return JsonResponse({"error": str(error)})
