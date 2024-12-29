"""
URL configuration for rentcarz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from car import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', views.CarViewSet, basename='cars')
router.register('car_availability', views.CarViewSet, basename='car_availability')
router.register('booking', views.CarViewSet, basename='bookings')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + debug_toolbar_urls()
