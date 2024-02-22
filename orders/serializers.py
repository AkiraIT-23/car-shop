from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Order, Car


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car', 'user', 'sold']


class HistoryOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car', 'sold']


class CreatingOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = ['id', 'quantity', 'car', 'user']


class BuySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    car_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    sold = serializers.BooleanField(default=None)

    def update(self, instance, validated_data):
        car = Car.objects.get(id=instance.id)
        car.quantity -= instance.quantity
        car.save()
        instance.sold = True
        instance.save()
        return instance
