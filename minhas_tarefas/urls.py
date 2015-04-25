from django.conf.urls import patterns, include, url
from django.contrib import admin
import tarefas.urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'minhas_tarefas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Pergunta... se um babaca coloca um alias no apache para a app... por ex:
    # http://ip/aplicacao/
    # como ficaria essa treta aqui?

    # O match eh sequencial se coloco o vazio antes do admin ele nunca vai
    # cair no admin pois o match vazio casa com tudo sempre
    # se tenho varios app tenho que separar em varias divisoes senao nunca
    # vai cair no segundo se colocar tudo vazio
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(tarefas.urls)),
)
