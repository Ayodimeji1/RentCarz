from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    pictures = models.ImageField()

    def __str__(self):
        return self.model+self.brand


# class Brand(models.Model):
#     name = models.CharField(max_length=100)

    
