from django.urls import path
from . import views


urlpatterns = [
    path('sayhello/', views.sayhello, name='sayhello'),
]