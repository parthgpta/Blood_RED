from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length =30 ,blank=False)
    blood_group = models.CharField(max_length=1 , blank=False)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    about_me = models.TextField()

    @receiver(post_save ,sender=User)
    def update_user_profile(sender , instance , created , **kwargs):
        if created:
            profile.objects.create(user=instance)
        instance.profile.save()
    
    


class Person(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    blood_grp = models.CharField(max_length=1)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    #bio = models.TextField()
    
    

    def __str__(self):
        return self.email
    
