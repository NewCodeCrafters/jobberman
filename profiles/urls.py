from django.urls import path

from . import views

urlpatterns = [
    path('update-profile/', views.UpdateProfileView.as_view()),

]
