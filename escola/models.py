from django.db import models

# Create your models here.
class Aluno(models.Model):
    name = models.CharField(max_length=40)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I','Intermediary'),
        ('A','Advanced')
    )
    code_course = models.CharField(max_length=10)
    descripition = models.CharField(max_length=100)
    levek = models.CharField(max_length=1, choices=LEVEL,blank=False,null=False, default='B')

    def __str__(self):
        return self.descripition

class Registration(models.Model):
    PERDIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('M','Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERDIODO,blank=False, null=False,default='M') 