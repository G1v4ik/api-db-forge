from rest_framework import status, serializers
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import models

from .renderer import AcademyJSONRenderer

from .serializers import (
    StudentSerializer, 
    CertificateSerializer,
    CoursesSerializer,
    EducationalMaterialsSerializer,
    GetCertificateSerializer,
    GetCoursesSerializer,
    GetEducationalMaterialsSetializer,
    GetStudentSerializer
)

class AbstractAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (AcademyJSONRenderer, )
    serializer_class: serializers.ModelSerializer.__class__ = ...
    get_serializer_class: serializers.ModelSerializer.__class__ = ...


    def post(self, request):
        _post = request.data.get('data', {})
        serializer = self.serializer_class(
            data=_post
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    
    def get(self, request, *args, **kwargs):
        pk_model = kwargs.get('pk', None)
        

        if pk_model is not None:
            data_model = self._model.objects.get(pk=pk_model)
            serializer = self.get_serializer_class(
                data=self.get_serializer_class(data_model).data
            )
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        else:
            data_model = self._model.objects.all()
            serializer = self.get_serializer_class(
                
                data=self.get_serializer_class(
                    data_model, 
                    many=True).data, 
                
                many=True
            )
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
            

class StudentAPIView(AbstractAPIView):
    serializer_class = StudentSerializer
    get_serializer_class = StudentSerializer
    _model: models.Model = serializer_class.Meta.model


class CertificateAPIView(AbstractAPIView):
    serializer_class = CertificateSerializer
    get_serializer_class = GetCertificateSerializer
    _model: models.Model = serializer_class.Meta.model


class CoursesAPIView(AbstractAPIView):
    serializer_class = CoursesSerializer
    get_serializer_class = GetCoursesSerializer
    _model: models.Model = serializer_class.Meta.model


class EducationalMaterialsAPIView(AbstractAPIView):
    serializer_class = EducationalMaterialsSerializer
    get_serializer_class = GetEducationalMaterialsSetializer
    _model: models.Model = serializer_class.Meta.model