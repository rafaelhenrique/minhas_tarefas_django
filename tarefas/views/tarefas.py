# view mais basica usada para criar as nossas views
from django.views.generic import View
# Converter o template para que o browser consiga renderizar
from django.shortcuts import render_to_response
from django.shortcuts import redirect
# Usado pra nao perder dado de context e talz
# transferencia de uma requisicao pra outra
from django.template.context import RequestContext

from tarefas.models import Tarefa
from tarefas.forms import FormNovoUsuario
from tarefas.forms import FormTarefa


class Home(View):
    template_name = 'tarefas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        # Este objects eh a instancia de um manager que executa as funcoes
        # de acesso ao banco
        self.context['counter'] = Tarefa.objects.filter(
            finalizado=False).count()
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))


class CriaUsuario(View):
    template_name = 'tarefas/cria_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormNovoUsuario()
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

    # O post http eh direcionado a este metodo atraves do as_view que
    # estamos usando no urls.py
    def post(self, request, *args, **kwargs):
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        self.context['form'] = form
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))


class AdicionaTarefa(View):
    template_name = 'tarefas/cria_tarefa.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormTarefa()
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = FormTarefa(request.POST)
        if form.is_valid():
            tarefa = form.save()
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('/')
        self.context['form'] = form
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

__all__ = [
    "Home",
    "CriaUsuario",
    "AdicionaTarefa",
]
