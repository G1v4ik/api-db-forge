from rest_framework import serializers

from .models import (
    EducationalMaterials,
    Student,
    Certificate,
    Courses
)

class GetBaseSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField()
    class Meta:
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'telegram_id',
            'name',
            'surname',
            'email'
        ]

class CertificateSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='get_pk', read_only=True)
    class Meta:
        model = Certificate
        fields = [
            'pk',
            'id_student',
            'id_courses',
            'url'
            ] 

class CoursesSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='get_pk', read_only=True)
    class Meta:
        model = Courses
        fields = [
            "pk",
            "title",
        ]


class EducationalMaterialsSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='get_pk', read_only=True)
    class Meta:
        model = EducationalMaterials
        fields = [
            "pk",
            "id_courses",
            "url",
        ]

class GetStudentSerializer(GetBaseSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class GetCoursesSerializer(GetBaseSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class GetCertificateSerializer(GetBaseSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"

class GetEducationalMaterialsSetializer(GetBaseSerializer):
    class Meta:
        model = EducationalMaterials
        fields = "__all__"