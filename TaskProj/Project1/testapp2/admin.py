from django.contrib import admin
from .models import Task1

# Register your models here.

class Task1Admin(admin.ModelAdmin):
    list_display = ['task_ref_no','instruction','file']

admin.site.register(Task1,Task1Admin)