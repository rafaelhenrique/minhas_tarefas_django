from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField


class Tarefa(Model):
    # verbose name serve para os labels do formulario
    # ajuda tambem na traducao, depois para fazer um de para das palavras
    nome = CharField(max_length=100, verbose_name='nome')
    descricao = TextField(verbose_name='descrição')
    # auto_now_add quando criar o objeto usa a data/hora atual
    # auto_now quando criar/atualizar o objeto usa a data/hora atual
    data_de_criacao = DateTimeField(auto_now_add=True,
                                    verbose_name='data de criação')
    # blank = aceita o campo em branco
    # null = aceita que no banco de dados ele pode ter valor null
    data_de_execucao = DateTimeField(verbose_name='data de execução',
                                     blank=True, null=True)
    finalizado = BooleanField(default=False, verbose_name='finalizado')

    class Meta:
        ordering = ['-data_de_criacao']
        # esses verbose servem para traducao
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'
