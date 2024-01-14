from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Order


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car', 'user']


class HistoryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car']


class CreatingOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car', 'user']
