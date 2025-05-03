from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    StudentsRegSrtializer,
    TeacherRegSerializer,
    ModeratorRegSerializer
)

from .renderer import UserBaseJSONRenderer

class AbstractNewUserBase(APIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (UserBaseJSONRenderer, )
    serializer_class = ...

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentNewAPIView(AbstractNewUserBase):
    serializer_class = StudentsRegSrtializer


class TeacherNewAPIView(AbstractNewUserBase):
    serializer_class = TeacherRegSerializer


class ModeratorNewAPIView(AbstractNewUserBase):
    serializer_class = ModeratorRegSerializer
