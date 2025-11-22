from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]
