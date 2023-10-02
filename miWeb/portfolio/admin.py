from django.contrib import admin
from .models import Skill, Category, Project

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )

class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
