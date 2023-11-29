from django.contrib import admin
from .models import TodoItemModel

@admin.register(TodoItemModel)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'completed')
    list_filter = ('priority', 'completed')
    search_fields = ('title', 'description')
    list_editable = ('completed',)

