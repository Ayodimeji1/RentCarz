from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer' ,'Customer'),
        ('owner', 'Owner')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ROLE_CHOICES = [
        ('customer' ,'Customer'),
        ('owner', 'Owner')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')    
    # address = models.CharField(max_length=255, blank=True)
    phone_number = models.IntegerField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True) 

    def __str__(self):
        return self.user.username
