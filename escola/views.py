from rest_framework import generics, serializers, viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer

class AlunosViewset(viewsets.ModelViewSet):
  """Exibir alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursosViewset(viewsets.ModelViewSet):
  """Exibir cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class MatriculasViewset(viewsets.ModelViewSet):
  """Exibir matrículas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

class ListaMatriculasAlunoViewset(generics.ListAPIView):
  """Exibir as matrículas por aluno"""
  serializer_class = ListaMatriculasAlunoSerializer

  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset