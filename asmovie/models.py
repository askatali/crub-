from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    genre = models.CharField(max_length=10)
    production_year = models.IntegerField(default=4)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name}'



