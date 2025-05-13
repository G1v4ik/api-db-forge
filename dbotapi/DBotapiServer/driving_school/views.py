from rest_framework import status, serializers
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    StudentsRegSrtializer,
    TeacherRegSerializer,
    ModeratorRegSerializer,
    StudentSerializer,
    TeacherSerializer,
    ModeratorSerializer,
    GroupTheorySerializer,
    GroupsSerializer,
    DrivingSerializer,
    TimeWorkSerializer
)

from .renderer import UserBaseJSONRenderer

from .models import (
    Student,
    Teacher,
    Moderators,
    GroupTheory,
    TimeWork,
    Groups,
    Driving
)

from django.db import models


class AbstractUserMethodsAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (UserBaseJSONRenderer, )
    serializer_class:serializers.ModelSerializer = ...
    


class AbstractUserBase(AbstractUserMethodsAPIView):
    def patch(self, request):
        user = request.data.get('user', {})
        _model:models.Model = self.serializer_class.Meta.model
        get_user_model = _model.objects.get(telegram_id=user['telegram_id'])
        serializer = self.serializer_class(
            get_user_model, data=user, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        _model:models.Model = self.serializer_class.Meta.model
        
        try:
            _checker = _model.objects.get(telegram_id=user['telegram_id'])
            raise ValidationError(
                f'The user exists {_checker}',
                )
        
        except _model.DoesNotExist:
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentAPIView(AbstractUserBase):
    serializer_class = StudentsRegSrtializer


class TeacherAPIView(AbstractUserBase):
    serializer_class = TeacherRegSerializer


class ModeratorAPIView(AbstractUserBase):
    serializer_class = ModeratorRegSerializer


class GetInfoStudent(AbstractUserMethodsAPIView):
    serializer_class = StudentSerializer
    

    def get(self, request, *args, **kwargs):
        
        telegram_id = kwargs.get('telegram_id', None)

        info_user = Student.objects.get(telegram_id=telegram_id)
        serializer = self.serializer_class(data=StudentSerializer(info_user).data)
        serializer.is_valid(raise_exception=True)

        
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetInfoTeacher(AbstractUserMethodsAPIView):
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        
        telegram_id = kwargs.get('telegram_id', None)

        info_user = Teacher.objects.get(telegram_id=telegram_id)
        serializer = self.serializer_class(data=TeacherSerializer(info_user).data)
        serializer.is_valid(raise_exception=True)

        
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetInfoModerator(AbstractUserMethodsAPIView):
    serializer_class = ModeratorSerializer

    def get(self, request, *args, **kwargs):

        telegram_id = kwargs.get('telegram_id', None)

        if telegram_id is None:
            raise 'telegram_id is None, LoL'

        info_user = Moderators.objects.get(telegram_id=telegram_id)
        serializer = self.serializer_class(data=ModeratorSerializer(info_user).data)
        serializer.is_valid(raise_exception=True)

        
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllStudent(AbstractUserMethodsAPIView):
    serializer_class = StudentSerializer

    def get(self, request):

        info_users = Student.objects.all()
        serializer = self.serializer_class(
            data=StudentSerializer(info_users, many=True).data, many=True
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllTeacher(AbstractUserMethodsAPIView):
    serializer_class = TeacherSerializer
    def get(self, request):

        info_users = Teacher.objects.all()
        serializer = self.serializer_class(
            data=TeacherSerializer(info_users, many=True).data, many=True
        )
        
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllModerator(AbstractUserMethodsAPIView):
    serializer_class = ModeratorSerializer
    def get(self, request):

        info_users = Moderators.objects.all()
        serializer = self.serializer_class(
            data=ModeratorSerializer(info_users, many=True).data, many=True
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupTheoryAPIView(AbstractUserMethodsAPIView):
    serializer_class = GroupTheorySerializer

    def patch(self, request):
        grouptheory = request.data.get('grouptheory', {})
        _model = GroupTheory.objects.get(id_grouptheory=grouptheory['id_grouptheory'])
        serializer = self.serializer_class(
            _model, data=grouptheory, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        _grouptheory = request.data.get('grouptheory', {})

        try:
            Teacher.objects.get(telegram_id=_grouptheory['telegram_id_teacher'])

        except Teacher.DoesNotExist:
            raise ValidationError("Teacher Does Not Exist")
        

        serializer = self.serializer_class(data=_grouptheory)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        
        _model = GroupTheory.objects.all()
        serializer = self.serializer_class(
            data=GroupTheorySerializer(_model, many=True).data, many=True
            )
        
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class GroupsAPIView(AbstractUserMethodsAPIView):
    serializer_class = GroupsSerializer

    def patch(self, request):
        groups = request.data.get('groups', {})
        _model = Groups.objects.get(id_group=groups['id_group'])
        serializer = self.serializer_class(
            _model, data=groups, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        
        json_new_group = request.data.get('groups', {})

        serializer = self.serializer_class(data=json_new_group)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def get_group(self, model):
        return Response(GroupsSerializer(model).data, status=status.HTTP_200_OK)


    def get(self, request, *args, **kwargs):
        
        id_group = kwargs.get('id_group')
        telegram_id_student = kwargs.get('telegram_id_student')
        id_grouptheory = kwargs.get('id_grouptheory')

        if id_group is not None:
            _model = Groups.objects.get(id_group=id_group)
            return self.get_group(_model)


        elif telegram_id_student is not None:
            _model = Groups.objects.get(telegram_id_student=telegram_id_student)
            return self.get_group(_model)
    

        elif id_grouptheory is not None:
            _model = Groups.objects.get(id_grouptheory=id_grouptheory)
            return self.get_group(_model)


        else:
            _model = Groups.objects.all()

            if len(_model) == 0:
                raise ValidationError("Haven`t objects")

            serializer = GroupsSerializer(_model, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class DrivingAPIView(AbstractUserMethodsAPIView):
    serializer_class = DrivingSerializer

    def patch(self, request):
        driving = request.data.get('driving', {})
        _model = Driving.objects.get(id_driving=driving['id_driving'])
        serializer = self.serializer_class(
            _model, data=driving, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_driving = request.data.get('driving', None)
        serializer = self.serializer_class(data=request_driving)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_201_CREATED)
    

    def get_driving(self, model):
        return Response(DrivingSerializer(model).data,
                        status=status.HTTP_200_OK)


    def get(self, request, *args, **kwargs):
        id_driving = kwargs.get('id_driving', None)
        tg_student = kwargs.get('telegram_id_student', None)
        tg_teacher = kwargs.get('telegram_id_teacher', None)
        
        if id_driving is not None:
            _model = Driving.objects.get(id_driving=id_driving)
            return self.get_driving(_model)
        

        elif tg_student is not None:
            _model = Driving.objects.get(telegram_id_student=tg_student)
            return self.get_driving(_model)
        

        elif tg_teacher is not None:
            _model = Driving.objects.get(telegram_id_teacher=tg_teacher)
            return self.get_driving(_model)
        

        else:
            _model = Driving.objects.all()
            serializer = DrivingSerializer(_model, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class TimeWorkAPIView(AbstractUserMethodsAPIView):
    serializer_class = TimeWorkSerializer

    def post(self, request):
        timework = request.data.get('timework', None)
        serializer = self.serializer_class(
            data=timework
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        _model = TimeWork.objects.all()
        serializer = TimeWorkSerializer(_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request):
        timework = request.data.get('timework', {})
        _model = TimeWork.objects.get(id_timework=timework['id_timework'])
        serializer = self.serializer_class(
            _model, data=timework, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)