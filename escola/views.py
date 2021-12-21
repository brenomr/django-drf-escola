from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

class AlunosViewset(viewsets.ModelViewSet):
  """Exibir alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursosViewset(viewsets.ModelViewSet):
  """Exibir cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer