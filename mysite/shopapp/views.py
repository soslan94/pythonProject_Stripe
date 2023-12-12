from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, TemplateView, CreateView
from django.conf import settings
import stripe

from .models import Item


class ItemListView(ListView):
    """
    Create a list of items
    """
    template_name = 'shopapp/items-list.html'
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.all()


class ItemDetailsView(DetailView):
    """
    Create a page with detail information about item with checkout button
    """
    template_name = 'shopapp/item-detail.html'
    queryset = Item.objects.all()
    context_object_name = 'item'


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(View):
    """
    Create a Stripe checkout session
    """

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(item.price),
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },

                    },
                    "quantity": 1,
                }
            ],
            metadata={"product_id": Item.id},
            mode="payment",
            success_url='http://127.0.0.1:8000/shopapp/success/',
            cancel_url='http://127.0.0.1:8000/shopapp/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "shopapp/success.html"


class CancelView(TemplateView):
    template_name = "shopapp/cancel.html"


