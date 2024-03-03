"""URLs configuration of the 'Orders' application v1."""

from django.urls import path

from orders.views import create_order_checkout_session, order_detail

urlpatterns = [
    path("order/<int:order_id>/", order_detail, name="order_detail"),
    path(
        "buy/order/<int:order_id>/",
        create_order_checkout_session,
        name="create_order_checkout_session",
    ),
]
