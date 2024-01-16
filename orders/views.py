from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Order
from .serializers import OrderSerializer, CreatingOrderSerializer, HistoryOrderSerializer
from .permissions import IsOrderAuthorOrAdmin
from generics.pagination import CustomAPIListPagination


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreatingOrderSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class MyOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOrderAuthorOrAdmin]
    pagination_class = CustomAPIListPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        return self.queryset.filter(user=self.request.user)


class AllOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomAPIListPagination


class OrderHistoryAPIView(ListAPIView):
    serializer_class = HistoryOrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomAPIListPagination

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
