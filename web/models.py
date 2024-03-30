from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.TextField()
    overview = models.TextField()
    genres = models.JSONField(default=list)  # Use JSONField to store the genres as a list
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.FloatField()

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    watched = models.JSONField(default=list)

    def __str__(self):
        return self.first_name
