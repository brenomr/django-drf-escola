from django.db.models import query
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, ListaMatriculasAlunoSerializer, ListarAlunosMatriculadosSerializer, MatriculaSerializer

class AlunosViewset(viewsets.ModelViewSet):
  """Exibir alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CursosViewset(viewsets.ModelViewSet):
  """Exibir cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class MatriculasViewset(viewsets.ModelViewSet):
  """Exibir matrículas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaMatriculasAlunoViewset(generics.ListAPIView):
  """Exibir as matrículas por aluno"""
  serializer_class = ListaMatriculasAlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset

class ListaAlunosMatriculadosViewset(generics.ListAPIView):
  """Listar alunos em um determinado curso"""
  serializer_class = ListarAlunosMatriculadosSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset