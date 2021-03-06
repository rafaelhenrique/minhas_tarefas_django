from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tarefas.models import Tarefa


class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_de_criacao'

    # O com o super eu chamo o get da classe mãe, portanto eu mudo o queryset
    # depois chamo o get original da classe mãe
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        self.queryset = Tarefa.objects.filter(usuario=request.user.id)
        return super().get(request, *args, **kwargs)


class TarefaDetail(DetailView):
    model = Tarefa

# Cria uma lista com nome das coisas que vc quer disponibilizar
__all__ = [
    'TarefasView',
    'TarefaDetail',
]
