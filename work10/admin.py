# work10/admin.py
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'status', 'due_date', 'created_at')
    list_filter = ('status','created_by')
    search_fields = ('title','description','created_by__username')
