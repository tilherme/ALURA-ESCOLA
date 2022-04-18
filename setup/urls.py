
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from escola.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos',AlunoViewSet)
router.register('courses',CourseViewSet)
router.register('matriculas',RegistrationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('aluno/<int:pk>/matricula/', RegistrationAluno.as_view()),
    path('curso/<int:pk>/matricula/', RegistrationAlunoOneCouse.as_view())
   
]
