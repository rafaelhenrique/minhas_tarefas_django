from django.conf.urls import patterns, include, url

from tarefas.views import Home

urlpatterns = patterns(
    '',
    # as_view envelopa a class dentro de uma funcao
    url(r'^$', Home.as_view(), name='home')
)
