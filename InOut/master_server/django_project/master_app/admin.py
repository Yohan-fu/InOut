from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company", "site", "entry_time", "exit_time")
    list_filter = ("site",)
