from django.contrib import admin
from projects.models import Project

# Register your models here.
@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ["name", "description", "id"]
