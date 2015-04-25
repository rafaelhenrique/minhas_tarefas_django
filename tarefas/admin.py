from django.contrib.admin import site
from django.contrib.admin import ModelAdmin

from tarefas.models import Tarefa


class TarefaAdmin(ModelAdmin):
    # recebe um conjunto de strings, em geral campos do modelo
    # valores que vc vai conseguir acessar como um atributo
    list_display = ['nome', 'descricao', 'data_de_criacao',
                    'data_de_execucao', 'finalizado']

site.register(Tarefa, TarefaAdmin)
