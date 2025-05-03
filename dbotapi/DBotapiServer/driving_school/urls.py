from django.urls import path

from .views import (
    StudentNewAPIView,
    TeacherNewAPIView,
    ModeratorNewAPIView
)


app_name = 'driving_school'

urlpatterns = [
    path('new/students/', StudentNewAPIView.as_view()),
    path('new/teachers/', TeacherNewAPIView.as_view()),
    path('new/moderators/', ModeratorNewAPIView.as_view()),
    
]
