from django.contrib import admin

# Register your models here.

from .models import Job, Skill


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'work_type','job_type', 'description','skills']
    list_display_links = list_display[:1]
    search_fields = ['title']
    list_filter = ['company', 'description']


admin.site.register(Job)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = list_display[:1]


admin.site.register(Skill)
