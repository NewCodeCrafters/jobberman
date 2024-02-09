from django.urls import path

from . import views

urlpatterns = [
    path('available-jobs', views.AvailableJobs.as_view()),
    path("post-job/", views.PostJobView.as_view()),
    path("add-skill/", views.AddSkillView.as_view()),
    path("update-job/", views.GetUpdateJobView.as_view()),
]
