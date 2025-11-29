from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ["id", "title", "slug", "image", "created"]
    list_filter = ["created"]
