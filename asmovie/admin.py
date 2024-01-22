from django.contrib import admin
from asmovie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display

