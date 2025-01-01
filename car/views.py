from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
# from rest_framework.filters import SearchFilter, OrderingFilter


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category']
    # search_fields = ['name', 'description']
    # ordering_fields = ['price', 'created_at']
 
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Car.objects.all()
    serializer_class= CarSerializer
