from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display =[
        "task",
        "description",
        "priority",
        "done",
        "updated_at",
        "created_at"
    ]

admin.site.register(Todo, TodoAdmin)