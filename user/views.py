from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated] 
