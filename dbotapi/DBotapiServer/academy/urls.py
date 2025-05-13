from django.urls import path

from .views import (
    StudentAPIView,
    CoursesAPIView,
    CertificateAPIView,
    EducationalMaterialsAPIView
)

urlpatterns = [
    path('students/', StudentAPIView.as_view()),
    path('students/<int:pk>/', StudentAPIView.as_view()),
    
    path('courses/', CoursesAPIView.as_view()),
    path('courses/<int:pk>/', CoursesAPIView.as_view()),

    path('certificates/', CertificateAPIView.as_view()),
    path('certificates/<int:pk>/', CertificateAPIView.as_view()),
    

    path('educationalmaterials/', EducationalMaterialsAPIView.as_view()),
    path('educationalmaterials/<int:pk>/', EducationalMaterialsAPIView.as_view()),
]
