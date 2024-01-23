from django.contrib import admin
from asmovie.models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'movie_age', 'time')
    list_display_links = list_display


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
