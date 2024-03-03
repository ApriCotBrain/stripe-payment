"""Views for endpoints of the "Orders" application."""

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import stripe

from core.utilities import create_checkout_session
from orders.models import Order
from orders.utilities import (
    calculate_total_amount,
    get_line_items_for_create_order_checkout_session,
    get_unique_order_items,
)

stripe.api_key = settings.STRIPE_SECRET_API_KEY


def order_detail(request, order_id):
    """View function to display the details of the item."""
    order = get_object_or_404(Order, id=order_id)
    unique_order_items = get_unique_order_items(order)
    total_amount = calculate_total_amount(order)
    STRIPE_PUBLIC_API_KEY = settings.STRIPE_PUBLIC_API_KEY

    context = {
        "order": order,
        "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY,
        "unique_order_items": unique_order_items,
        "total_amount": total_amount,
        "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY,
    }

    return render(request, "order_detail.html", context)


def create_order_checkout_session(request, order_id):
    """URL request handler to create Session Id for paying for the selected item."""
    order = get_object_or_404(Order, id=order_id)
    line_items = get_line_items_for_create_order_checkout_session(order)
    try:
        session_id = create_checkout_session(line_items)
        return JsonResponse({"session_id": session_id})
    except Exception as error:
        return JsonResponse({"error": str(error)})
