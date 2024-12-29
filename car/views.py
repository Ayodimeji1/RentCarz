from .models import Car, CarAvailability
from .serializers import CarSerializer, CarAvailabilitySerializer
from rest_framework.viewsets import ModelViewSet # type: ignore
# from rest_framework.filters import SearchFilter, OrderingFilter


# class CarAvailabiltyViewSet(ModelViewSet):
#     queryset = CarAvailability.objects.all()
#     serializer_class = CarAvailabilitySerializer
class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category']
    # search_fields = ['name', 'description']
    # ordering_fields = ['price', 'created_at']
 



