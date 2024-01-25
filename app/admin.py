from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "due_date", "status"]

admin.site.register(Task, TaskAdmin)
