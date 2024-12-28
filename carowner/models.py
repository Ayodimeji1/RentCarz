from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Owner(models.Model):
    phone_number = models.BigIntegerField()
    address = models.TextField()   
    picture = models.ImageField(upload_to='owner_img', default=False)

    # def __str__(self):
    #     return self.user.username
