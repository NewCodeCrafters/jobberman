from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workExperiences')
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    currently_working = models.BooleanField(default=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    graduation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree}, {self.course} at {self.school}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)

    work_experiences = models.ManyToManyField(WorkExperience, blank=True)
    educations = models.ManyToManyField(Education, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
