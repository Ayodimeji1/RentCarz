from rest_framework import serializers
from .models import Booking



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model =Booking 
        fields = "__all__"


    def validate(self, data):
        # Validate that end_date is after start_date
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        
        # Check for overlapping bookings for the same car
        overlapping_bookings = Booking.objects.filter(
            car=data['car'],
            start_date__lt=data['end_date'],
            end_date__gt=data['start_date'],
        )
        if overlapping_bookings.exists():
            raise serializers.ValidationError("This car is already booked for the selected dates.")
        
        return data



