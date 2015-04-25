from django.conf.urls import patterns, url

from tarefas.views import Home
from tarefas.views import TarefasView

urlpatterns = patterns(
    '',
    # as_view envelopa a class dentro de uma funcao
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tarefas/$', TarefasView.as_view(), name='tarefas'),
)
