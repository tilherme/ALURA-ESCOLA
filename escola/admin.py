from django.contrib import admin
from escola.models import *

class Alunos(admin.ModelAdmin):
    list_display = ('id','name','rg','cpf','birth_date')
    list_display_links = ('id', 'name')
    search_fields =('name',)
    list_per_page = 20

class Courses(admin.ModelAdmin):
    list_display = ('id','code_course','descripition')
    list_display_links = ('id', 'code_course')
    search_fields =('code_course',)
    list_per_page = 20
class Registrations(admin.ModelAdmin):
    list_display = ('id','aluno','course')
    list_display_links = ('id', 'aluno')
    list_per_page = 20

admin.site.register(Aluno,Alunos)
admin.site.register(Course, Courses)
admin.site.register(Registration, Registrations)