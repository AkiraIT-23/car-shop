from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=255)
    birthdate = models.IntegerField()
    price = models.IntegerField()
    model = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars')

