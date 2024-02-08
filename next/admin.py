from django.contrib import admin
from next.models import Gmail

@admin.register(Gmail)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    list_display_links = list_display

