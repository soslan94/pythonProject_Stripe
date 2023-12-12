from django.urls import path

from .views import ItemListView, ItemDetailsView, CreateStripeCheckoutSessionView, SuccessView, CancelView


app_name = 'shopapp'


urlpatterns = [
     path('items-list/', ItemListView.as_view(), name='items-list'),
     path('items-list/<int:pk>/', ItemDetailsView.as_view(), name='item_detail'),
     path('create-checkout-session/<int:pk>/', CreateStripeCheckoutSessionView.as_view(),
          name='create-checkout-session'),
     path('success/', SuccessView.as_view(), name='success'),
     path('cancel/', CancelView.as_view(), name='cancel'),
]
