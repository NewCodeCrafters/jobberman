from rest_framework import serializers
from .models import Job, Skill




class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("title", "company", "work_type", "job_type", "description", "skills")
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("__all__")