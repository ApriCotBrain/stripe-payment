"""URLs configuration of the 'Items' application v1."""

from django.urls import path

from items.views import create_item_checkout_session, item_detail

urlpatterns = [
    path("item/<int:item_id>/", item_detail, name="item_detail"),
    path(
        "buy/item/<int:item_id>/",
        create_item_checkout_session,
        name="create_checkout_session",
    ),
]
