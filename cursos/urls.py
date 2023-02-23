from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (AvaliacaoAPIView, AvaliacaoViewSet, AvaliacoesAPIView,
                    CursoAPIView, CursosAPIView, CursoViewSet)
from .viewsEstudos import (AdicionarCursoAPIView, AtualizarCurso, DeletarCurso,
                           ListarTodosCursosAPIVIew, ListarUmCursoAPIView)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    #### API V1  ####
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    # Todas as Avaliações dentro do curso
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacoes'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    

    #### API V2  ####




    #### MEu aprendizado ####
    path('estudoscurso/', ListarTodosCursosAPIVIew.as_view(), name='listarCursos'),
    path('estudosAdicionarcurso/', AdicionarCursoAPIView.as_view(), name='adicionarCurso'),
    path('estudoscurso/<int:pk>/', ListarUmCursoAPIView.as_view(), name='lerCurso'),
    path('estudoscurso/atualizar/<int:pk>/', AtualizarCurso.as_view(), name='atualizarCurso'),
    path('estudoscurso/deletar/<int:pk>/', DeletarCurso.as_view(), name='deletarCurso'),
]