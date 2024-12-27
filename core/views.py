from math import ceil
from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Feature, Funcionario, Servico

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        features =  list(Feature.objects.all())
        print(features)
        midpoint = ceil(len(features) / 2)

        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        context['servicos'] = Servico.objects.order_by('?').all()
        
        context['features_left'] = features[:midpoint]
        context['features_right'] = features[midpoint:]
        return context
    
    #Falta alterar o HTML