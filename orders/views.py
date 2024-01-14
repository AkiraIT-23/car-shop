from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Order
from .serializers import OrderSerializer, CreatingOrderSerializer, HistoryOrderSerializer
from .permissions import IsOrderAuthorOrAdmin


class OrderAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreatingOrderSerializer
    permission_classes = [IsAuthenticated]


class MyOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOrderAuthorOrAdmin]
    pagination_class = OrderAPIListPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AllOrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    pagination_class = OrderAPIListPagination


class OrderHistoryAPIView(ListAPIView):
    serializer_class = HistoryOrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = OrderAPIListPagination

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
