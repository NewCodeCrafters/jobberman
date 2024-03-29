from rest_framework import serializers
from .models import Job, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("__all__")


class JobSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(slug_field='slug', queryset=Skill.objects.all(), many=True)
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Job
        fields = ("title", 'slug', "company", "work_type", "job_type", "description", "skills", 'is_available')
        
