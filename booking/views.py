from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookingSerializer
from .models import Booking


# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Allow admins to see all bookings, but regular users see only their own
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
