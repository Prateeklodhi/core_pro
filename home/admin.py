from django.contrib import admin
from .models import Students
# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','address']
    list_filter = ['age']
    search_fields = ['name']
    