from django.views.generic import ArchiveIndexView

from tarefas.models import Tarefa


class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_de_criacao'

# Cria uma lista com nome das coisas que vc quer disponibilizar
__all__ = [
    'TarefasView',
]
