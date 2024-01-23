from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.title}'


class Movie(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movie', blank=True)
    production_year = models.IntegerField(default=4)
    movie_age = models.IntegerField(default=18)
    time = models.IntegerField(default=58)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name}'



