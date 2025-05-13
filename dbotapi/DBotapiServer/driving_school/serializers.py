from rest_framework import serializers

from .models import Teacher, Student, Moderators
from .models import (
    GroupTheory, 
    Driving,
    TimeWork,
    Groups
    )

#abstract classes
class UserBaseRegSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'telegram_id',
            'name',
            'surname',
            'phone',
            'email',
            'berth_day',
            'mode'
            ]


class GetUserBaseSerializer(serializers.ModelSerializer):
    mode = serializers.CharField(max_length=15)
    pk = serializers.IntegerField()
    class Meta:
        
        fields = [
            'telegram_id',
            'name',
            'surname',
            'phone',
            'email',
            'berth_day',
            'mode'
            ]


class GroupTheoryBaseSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField()
    class Meta:
        fields = [
            'id_grouptheory',
            'telegram_id_teacher',
            'name_group',
            'time_lesson',
            'theory_studied',
            'date_exam_theory'
        ]


class DrivingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id_driving',
            'telegram_id_student',
            'telegram_id_teacher',
            'datetime_driving',
            'errors'
        ]


class TimeWorkBaseSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField()
    class Meta:
        fields = [
            'id_timework',
            'work_begin',
            'work_end'
        ]


class GroupsBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id_group',
            'telegram_id_student',
            'id_grouptheory'
        ]


### get info serializer
class StudentSerializer(GetUserBaseSerializer):
    GetUserBaseSerializer.Meta.model = Student


class TeacherSerializer(GetUserBaseSerializer):
    GetUserBaseSerializer.Meta.model = Teacher


class ModeratorSerializer(GetUserBaseSerializer):
    GetUserBaseSerializer.Meta.model = Moderators



### Registration Serializer
class StudentsRegSrtializer(UserBaseRegSerializer):

    class Meta:
        model = Student
        fields = UserBaseRegSerializer.Meta.fields


class TeacherRegSerializer(UserBaseRegSerializer):

    class Meta:
        model = Teacher
        fields = UserBaseRegSerializer.Meta.fields


class ModeratorRegSerializer(UserBaseRegSerializer):

    class Meta:
        model = Moderators
        fields = UserBaseRegSerializer.Meta.fields


#to do serializers
class GroupTheorySerializer(GroupTheoryBaseSerializer):
    GroupTheoryBaseSerializer.Meta.model = GroupTheory

    
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = [
            'id_group',
            'telegram_id_student',
            'id_grouptheory'
        ]


class DrivingSerializer(DrivingBaseSerializer):
    DrivingBaseSerializer.Meta.model = Driving


class TimeWorkSerializer(TimeWorkBaseSerializer):
    TimeWorkBaseSerializer.Meta.model = TimeWork
