from django.db import models

# Create your models here.
from django.db import models

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    nome_coordenador = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria_curso = models.IntegerField()
    email = models.EmailField()
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=100)
