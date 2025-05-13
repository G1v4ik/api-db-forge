from django.urls import path

from .views import (
    StudentAPIView,
    TeacherAPIView,
    ModeratorAPIView,
    GetInfoStudent,
    GetInfoTeacher,
    GetInfoModerator,
    GetAllStudent,
    GetAllTeacher,
    GetAllModerator,
    DrivingAPIView,
    TimeWorkAPIView
)

from .views import (
    GroupTheoryAPIView,
    GroupsAPIView
)


app_name = 'driving_school'

urlpatterns = [
    path('new/students/', StudentAPIView.as_view()),
    path('new/teachers/', TeacherAPIView.as_view()),
    path('new/moderators/', ModeratorAPIView.as_view()),
    
    path ('info/students/', GetAllStudent.as_view()),
    path ('info/teachers/', GetAllTeacher.as_view()),
    path ('info/moderators/', GetAllModerator.as_view()),

    path('info/students/<int:telegram_id>/', GetInfoStudent.as_view()),
    path('info/teachers/<int:telegram_id>/', GetInfoTeacher.as_view()),
    path('info/moderators/<int:telegram_id>/', GetInfoModerator.as_view()),

    path('groupstheories/', GroupTheoryAPIView.as_view()),

    path('groups/', GroupsAPIView.as_view()),
    path('groups/students/<int:telegram_id_student>/', GroupsAPIView.as_view()),
    path('groups/groupstheories/<int:id_grouptheory>/', GroupsAPIView.as_view()),
    path('groups/<int:id_group>/', GroupsAPIView.as_view()),

    path('driving/', DrivingAPIView.as_view()),
    path('driving/<int:id_driving>/', DrivingAPIView.as_view()),
    path('driving/students/<int:telegram_id_student>/', DrivingAPIView.as_view()),
    path('driving/teachers/<int:telegram_id_teacher>/', DrivingAPIView.as_view()),

    path('timeworks/', TimeWorkAPIView.as_view()),
]
