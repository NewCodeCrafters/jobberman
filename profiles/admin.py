from django.contrib import admin
from .models import Education, Profiles, WorkExperince


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "location", "contact_email", "contact_phone"]
    list_display_links = list_display
    list_filter = ["user"]
    
    
@admin.register(WorkExperince)
class WorkExperinceAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "job_title", "company", ]
    list_display_links = list_display
    list_filter = ["user_profile"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "degree", "course", "school" ]
    list_display_links = list_display[:2]
    list_filter = ["user_profile"]
