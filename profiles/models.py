from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='media/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    summary = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        

class WorkExperince(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_experience')
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    currently_working = models.BooleanField(default=False, blank=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
    class Meta:
        verbose_name = "Work Experince"
        verbose_name_plural = "Work Experince"

    
class Education(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    graduation_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree}, {self.course} at {self.school}"
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    



