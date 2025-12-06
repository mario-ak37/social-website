from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Action


# Register your models here.
@admin.register(Action)
class ActionAdmin(ModelAdmin):
    list_display = ["user", "verb", "target", "created"]
    list_filter = ["created"]
    search_fields = ["verb"]
    
