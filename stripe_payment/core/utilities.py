"""Helper functions for the endpoints of 'stripe_payment' project."""

import stripe


def create_checkout_session(line_items):
    """Create a checkout session using Stripe API."""
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )
    return session["id"]
