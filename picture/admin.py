from django.contrib import admin
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'name',
        'uploader',
        'image', 
        'date_upload'
    ]

admin.site.register(Picture, PictureAdmin)
