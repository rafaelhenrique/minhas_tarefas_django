from django.contrib.admin import site
from tarefas.models import Tarefa

site.register(Tarefa)
