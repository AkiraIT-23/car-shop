from django.urls import path

from .views import CategoryAPIView, CategoryDetailAPIView, CarAPIView, CarDetailAPIView


urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('create/categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('', CarAPIView.as_view()),
    path('<int:pk>/', CarDetailAPIView.as_view()),
]
