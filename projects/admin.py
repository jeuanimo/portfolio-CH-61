from django.contrib import admin
from .models import Project, Skill

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    search_fields = ('name', 'description')
    list_filter = ('year',)
    ordering = ('-year',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
