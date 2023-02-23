from rest_framework import generics

from .models import Curso
from .serializers import CursoSerializer


# GET - Listar todos os cursos
class ListarTodosCursosAPIVIew(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# GET - Pegar apenas um Curso
class ListarUmCursoAPIView(generics.RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# POST - Adicionar Curso
class AdicionarCursoAPIView(generics.CreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# GET e PUT - Atualizar Curso
class AtualizarCurso(generics.RetrieveUpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Get e Delete - Deletar Curso
class DeletarCurso(generics.RetrieveDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
