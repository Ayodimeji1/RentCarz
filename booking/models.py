from django.db import models
from car.models import Car
from django.contrib.auth.models import User


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id}: {self.user.username} - {self.car.model}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['car', 'start_date', 'end_date'], name='unique_booking_per_car')
        ]


