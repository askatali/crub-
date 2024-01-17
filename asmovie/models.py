from django.db import models


class Movie(models.Model):
    country = models.CharField(max_length=15)
    genre = models.CharField(max_length=10)


