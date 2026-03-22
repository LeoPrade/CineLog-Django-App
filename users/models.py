from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    bio = models.CharField(max_length = 255, blank=True, null=True)
    favorite_genre = models.CharField(max_length = 255, blank=True, null=True)
    favorite_movie = models.CharField(max_length = 255, blank=True, null=True)
    favorite_actor = models.CharField(max_length = 255, blank=True, null=True)
    favorite_director = models.CharField(max_length = 255, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)