from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.db.models import ForeignKey

from django.contrib.auth.models import User


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

    # todas as relacoes do django sao bi-direcionais
    # related_name serve para que consiga fazer a query de user para tarefa

    # Se nao colocar related_name ele escreve um related_name:
    # FK - <atributo>_set
    # N to N - <atributo>s
    # 1 to 1 - <atributo>
    usuario = ForeignKey(User, verbose_name='usuário', related_name='tarefas',
                         blank=True, null=True)

    class Meta:
        ordering = ['-data_de_criacao']
        # esses verbose servem para traducao
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'

    def __str__(self):
        return self.nome
