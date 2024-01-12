from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import Category, Car, CarImage

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarImageSerializer(ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'


class CarSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'title', 'birthdate', 'price', 'model', 'category', 'author', 'images',
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        files = request.FILES.getlist("images")
        validated_data["author"] = request.user
        car = Car.objects.create(**validated_data)
        for image in files:
            CarImage.objects.create(
                car=car,
                image=image
            )
        return car

    def update(self, instance, validated_data):
        request = self.context.get("request")
        files = request.FILES.getlist("images")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        if files:
            CarImage.objects.filter(car=instance).delete()
            for image in files:
                CarImage.objects.create(
                    car=instance,
                    image=image
                )
        return instance

