from django.contrib import admin

from .models import Category, Car, CarImage


admin.site.register(Category)
admin.site.register(Car)
admin.site.register(CarImage)
