from django.urls import path

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
