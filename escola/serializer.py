from rest_framework import serializers
from .models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class ListRegistrationSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.descripition')
    periodo = serializers.SerializerMethodField()

    def get_periodo(self,obj):
        return obj.get_periodo_display()
    class Meta:
        model = Registration
        fields =['course','periodo']

class AlunoRegistrationOneCourseSerializer(serializers.ModelSerializer):
     aluno_name = serializers.ReadOnlyField(source='aluno.name')
     class Meta:
         model = Registration
         fields =['aluno_name']