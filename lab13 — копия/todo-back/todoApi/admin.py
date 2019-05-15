from django.contrib import admin
from todoApi.models import TaskList, Task

# Register your models here.

admin.site.register(Task)

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by',)