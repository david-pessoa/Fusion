from math import ceil
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from core.forms import ContatoForm
from core.models import Feature, Funcionario, Servico, Plano, Depoimento

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    succes_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        features =  list(Feature.objects.all())
        midpoint = ceil(len(features) / 2)

        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        context['servicos'] = Servico.objects.order_by('?').all()
        
        context['features_left'] = features[:midpoint]
        context['features_right'] = features[midpoint:]

        context['planos'] = Plano.objects.all()
        context['depoimentos'] = Depoimento.objects.all()
        context['range_five'] = range(1, 6)
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "Formulário enviado com sucesso")
        return super(IndexView, self).form_valid(self, form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Não foi possível enviar o formulário. Verifique os dados e tente novamente")
        return super(IndexView, self).form_invalid(self, form, *args, **kwargs)


