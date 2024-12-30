from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    pictures = models.ImageField()

    def __str__(self):
        return self.model+self.brand


class CarAvailability(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="availability")
    date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    class Meta: 
        unique_together = ('car', 'date')
        verbose_name = 'Car Availability'
        verbose_name_plural = 'Car Availabilities'

    def __str__(self):
        return f"{self.car.name} - {self.date.strftime('%Y-%m-%d %H:%M:%S')} - {'Available' if self.is_available else 'Unavailable'}"

    
