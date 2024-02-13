from django.contrib import admin
from django.utils import
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner']
    list_display_links = ['id', 'name']
    list_filter = ['owner']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_done', 'deadline', 'project' 'owner', 'created_at']
    list_filter = ['is done', 'deadline', 'created_at']
    search_fields = ['name', 'description', 'project_name', 'owner_last_name']



admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)

# Register your models here.
