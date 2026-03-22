from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director = models.CharField(max_length=255)
    awards = models.CharField(max_length=255, blank=True, null=True)
    imdb_votes = models.IntegerField()
    imdb_id = models.CharField(max_length=255)
    imdb_rating = models.FloatField()
    poster_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    personal_rating = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length = 255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.movie}"

