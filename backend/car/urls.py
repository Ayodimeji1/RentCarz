from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
]
