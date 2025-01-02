from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated] 
