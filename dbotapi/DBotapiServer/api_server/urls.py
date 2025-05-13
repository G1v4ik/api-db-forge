from django.urls import path, include

from .views import (
    RegistrationAPIView, 
    LoginAPIView,
    UserRetrieveUpdateAPIView    
)


app_name = 'api_server'

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/update/', UserRetrieveUpdateAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    
]

urlpatterns_driving_school = [
    path('driving-school/', include('driving_school.urls')),
]

urlpatterns_academy = [
    path('academy/', include('academy.urls')),
]

urlpatterns += urlpatterns_driving_school
urlpatterns += urlpatterns_academy
