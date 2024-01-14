from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Order
from .serializers import OrderSerializer, CreatingOrderSerializer, HistoryOrderSerializer
from .permissions import IsOrderAuthorOrAdmin


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreatingOrderSerializer
    permission_classes = [IsAuthenticated]


class MyOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOrderAuthorOrAdmin]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AllOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class OrderHistoryAPIView(ListAPIView):
    serializer_class = HistoryOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
