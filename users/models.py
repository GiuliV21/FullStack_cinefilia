from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    pass




# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     profile_name = models.CharField(max_length=100, blank=True)  # Agrega este campo
#     profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.profile_name} ({self.user.username})'