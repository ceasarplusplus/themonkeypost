from django.urls import path, include
from .views import checkout, order_completed, paystack, checkout, order_completed

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('payment/paystack/<pk>', paystack, name='paystack'),
    path('order_completed/', order_completed, name='order_completed'),
]