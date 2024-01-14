from django.urls import path

from .views import MyOrderListAPIView, OrderCreateAPIView, AllOrderListAPIView, OrderHistoryAPIView


urlpatterns = [
    path('my-orders/', MyOrderListAPIView.as_view()),
    path('create-order/', OrderCreateAPIView.as_view()),
    path('all-orders/', AllOrderListAPIView.as_view()),
    path('order-history/', OrderHistoryAPIView.as_view()),
]
