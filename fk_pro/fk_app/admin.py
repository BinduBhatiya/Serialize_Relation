from django.contrib import admin
from .models import Singre,Song
# Register your models here.

class SingreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Singre,SingreAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singre', 'duration']

admin.site.register(Song,SongAdmin)

