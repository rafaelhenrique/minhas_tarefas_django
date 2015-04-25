from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView

from tarefas.models import Tarefa


class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_de_criacao'


class TarefaDetail(DetailView):
    model = Tarefa

# Cria uma lista com nome das coisas que vc quer disponibilizar
__all__ = [
    'TarefasView',
    'TarefaDetail',
]
