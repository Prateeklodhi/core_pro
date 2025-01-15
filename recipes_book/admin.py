from django.contrib import admin
from .models import Recipe
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name','description','created']
    list_filter = ['created']
    search_fields = ['name','description']