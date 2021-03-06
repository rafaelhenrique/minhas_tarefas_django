from django.conf.urls import patterns, url

from tarefas.views import Home
from tarefas.views import TarefasView
from tarefas.views import TarefaDetail
from tarefas.views import CriaUsuario
from tarefas.views import AdicionaTarefa

urlpatterns = patterns(
    '',
    # as_view envelopa a class dentro de uma funcao
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tarefas/$', TarefasView.as_view(), name='tarefas'),
    url(r'^tarefas/(?P<pk>\d+)/$',
        TarefaDetail.as_view(),
        name='tarefas_detail'),
    url(r'^criar_usuario/$',
        CriaUsuario.as_view(),
        name='criar_usuario'),
    url(r'^criar_tarefa/$',
        AdicionaTarefa.as_view(),
        name='criar_tarefa'),
)
