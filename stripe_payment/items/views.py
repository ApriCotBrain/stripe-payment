"""Views for endpoints of the "Items" application."""

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import stripe

from items.models import Item

stripe.api_key = settings.STRIPE_SECRET_API_KEY


def item_detail(request, item_id):
    """View function to display the details of the item."""
    item = Item.objects.get(id=item_id)
    STRIPE_PUBLIC_API_KEY = settings.STRIPE_PUBLIC_API_KEY
    return render(
        request,
        "item_detail.html",
        {"item": item, "STRIPE_PUBLIC_API_KEY": STRIPE_PUBLIC_API_KEY},
    )


def create_checkout_session(request, item_id):
    """URL request handler to create Session Id tfor paying for the selected item."""
    item = get_object_or_404(Item, id=item_id)

    try:
        session = stripe.checkout.Session.create(
            line_items=[
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
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        return JsonResponse({"session_id": session["id"]})
    except Exception as error:
        return JsonResponse({"error": str(error)})
