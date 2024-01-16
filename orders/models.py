from django.db import models
from django.contrib.auth import get_user_model

from cars.models import Car

User = get_user_model()


class Order(models.Model):
    quantity = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sold = models.BooleanField(blank=True, null=True, default=None)
