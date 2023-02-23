from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Avaliacao, Curso
from .permissions import EhSuperUser
from .serializers import AvaliacaoSerializer, CursoSerializer

####################
#      API V1      #
####################

# Listar cursos e adicionar
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
# Listar apenas 1 curso, Atualizar o curos, deletar o curso
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id = self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    









####################
#      API V2      #
####################

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None): # avaliacoes é também a url
        self.paginnation_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)


        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)


# Usa Todos
"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

# Usa o que você quiser, caso não queira deletar, deletar...
class AvaliacaoViewSet(
            mixins.ListModelMixin, 
            mixins.CreateModelMixin, 
            mixins.RetrieveModelMixin, 
            mixins.UpdateModelMixin, 
            #mixins.DestroyModelMixin, 
            viewsets.GenericViewSet):
    
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

