from django.db import models

from django.utils.text import slugify

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class WorkType(models.TextChoices):
    hybrid = "Hybrid"
    remote = "Remote"
    onsite = "On site"

class JobType(models.TextChoices):
    fulltime = "Fulltime"
    contract = "Contract"
    intenship = "intenship"
    parttime = "Par time"


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Skills") # verbose
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.title 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, verbose_name="Job Title")
    slug = models.SlugField(max_length=100, blank=True)
    company = models.CharField(max_length=60, verbose_name="Company Name")
    work_type = models.CharField(max_length=20, choices=WorkType.choices)
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    description = models.TextField(help_text="Company Description, Role Description, Qualifications")
    skills = models.ManyToManyField(Skill)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self) -> str:
        return self.title 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

