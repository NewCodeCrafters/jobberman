from django.contrib import admin
from .models import  Profiles

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'contact_email', 'contact_phone')
    search_fields = ('user__first_name', 'user__last_name', 'location')


# @admin.register(WorkExperience)
# class WorkExperienceAdmin(admin.ModelAdmin):
#     list_display = ('user', 'job_title', 'company', 'start_date', 'end_date')
#     search_fields = ('user', 'job_title', 'company', 'description')

# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'degree', 'course', 'school', 'graduation_date')
#     search_fields = ('user','degree', 'course', 'school')

