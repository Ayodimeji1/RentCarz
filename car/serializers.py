from rest_framework import serializers
from .models import Car, CarAvailability



class CarAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAvailability
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    availability = CarAvailabilitySerializer(many=True, read_only=True)  # Nested serialization
    class Meta:
        model = Car
        fields = "__all__"
       


 