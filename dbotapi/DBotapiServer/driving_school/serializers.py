from rest_framework import serializers

from .models import Teacher, Student, Moderators


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
    

    mode = serializers.CharField(max_length=15, read_only=True)


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
