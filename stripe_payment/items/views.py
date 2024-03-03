"""Views for endpoints of the "Items" application."""

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import stripe

from core.utilities import create_checkout_session
from items.models import Item
from items.utilities import get_line_items_for_create_item_checkout_session

stripe.api_key = settings.STRIPE_SECRET_API_KEY


def item_detail(request, item_id):
    """View function to display the details of the item."""
    item = get_object_or_404(Item, id=item_id)
    STRIPE_PUBLIC_API_KEY = settings.STRIPE_PUBLIC_API_KEY
    return render(
        request,
        "item_detail.html",
        {"item": item, "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY},
    )


def create_item_checkout_session(request, item_id):
    """URL request handler to create Session Id for paying for the selected item."""
    item = get_object_or_404(Item, id=item_id)
    line_items = get_line_items_for_create_item_checkout_session(item)
    try:
        session_id = create_checkout_session(line_items)
        return JsonResponse({"session_id": session_id})
    except Exception as error:
        return JsonResponse({"error": str(error)})
