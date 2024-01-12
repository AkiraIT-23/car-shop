from rest_framework import generics, status, response

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
