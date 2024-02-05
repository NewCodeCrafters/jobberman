from django.db import models

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

    def __str__(self) -> str:
        return self.title 

# str

class Job(models.Model):
    title = models.CharField(max_length=60, verbose_name="Job Title")
    company = models.CharField(max_length=60, verbose_name="Company Name")
    work_type = models.CharField(max_length=20, choices=WorkType.choices)
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    description = models.TextField(help_text="Company Description, Role Description, Qualifications")
    skills = models.ManyToManyField(Skill)
    
    def __str__(self) -> str:
        return self.title 

