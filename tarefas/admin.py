from django.contrib.admin import site
from django.contrib.admin import ModelAdmin

from tarefas.models import Tarefa


class TarefaAdmin(ModelAdmin):
    # recebe um conjunto de strings, em geral campos do modelo
    # valores que vc vai conseguir acessar como um atributo
    list_display = ['nome', 'descricao', 'data_de_criacao',
                    'data_de_execucao', 'finalizado']
    # nao mostrar esse campo
    # exclude = ['data_de_execucao']

    # exibir somente esses campos no form
    fields = ['nome', 'descricao', 'finalizado']

    # quais campos serao editaveis na lista geral
    list_editable = ['finalizado']

site.register(Tarefa, TarefaAdmin)
