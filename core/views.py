from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Funcionario, Servico

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        context['servicos'] = Servico.objects.all()
        return context

