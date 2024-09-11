from django.db import models
from django.conf import settings

# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     release_date = models.DateField()
#     genre = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usa settings.AUTH_USER_MODEL
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.movie}'