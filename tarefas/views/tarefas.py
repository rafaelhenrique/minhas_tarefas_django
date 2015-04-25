# view mais basica usada para criar as nossas views
from django.views.generic import View

# Converter o template para que o browser consiga renderizar
from django.shortcuts import render_to_response
# Usado pra nao perder dado de context e talz
# transferencia de uma requisicao pra outra
from django.template.context import RequestContext


class Home(View):
    template_name = 'tarefas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

__all__ = [
    "Home",
]
