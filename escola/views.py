from termios import VSTART
from django.shortcuts import render
from rest_framework import viewsets,generics
from escola.models import *
from .serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class RegistrationAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class RegistrationAlunoOneCouse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = AlunoRegistrationOneCourseSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)