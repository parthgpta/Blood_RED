from django.db import models
from django.conf import settings


# Create your models here.


class Person(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    blood_grp = models.CharField(max_length=1)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    bio = models.TextField()
    

    def __str__(self):
        return self.email
    
