# Generated by Django 4.2.6 on 2024-01-30 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workExperiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profiles',
            name='educations',
            field=models.ManyToManyField(blank=True, to='profiles.education'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profiles',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, to='profiles.workexperience'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL),
        ),
    ]
