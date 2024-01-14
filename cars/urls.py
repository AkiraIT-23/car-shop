from django.urls import path

from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryDetailAPIView,
    CarListAPIView,
    CarCreateAPIView,
    CarDetailAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/create/', CategoryCreateAPIView.as_view()),
    path('create/detail/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('', CarListAPIView.as_view()),
    path('create/', CarCreateAPIView.as_view()),
    path('<int:pk>/', CarDetailAPIView.as_view()),
]
