# todo_app/admin.py
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'predmet', 'ocekavane', 'done', 'created']
    list_filter = ['done', 'deleted', 'predmet', 'created']
    search_fields = ['text', 'poznamka']
    list_editable = ['done']
    date_hierarchy = 'created'