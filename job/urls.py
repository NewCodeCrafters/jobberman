from django.urls import path

from . import views

urlpatterns = [
    path("post-job/", views.PostJobView.as_view()),
    path("add-skill/", views.AddSkillView.as_view()),
]
