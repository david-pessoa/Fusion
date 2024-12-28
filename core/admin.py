from django.contrib import admin
from .models import Servico, Cargo, Funcionario, Feature, Plano, Depoimento

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'servico', 'icone', 'ativo', 'modificado')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cargo', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'cargo', 'ativo', 'modificado')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'icone', 'ativo', 'modificado')

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'preco', 'numero_usuarios_ilimitado', 'armazenamento_ilimitado', 'icone', 'ativo', 'modificado')

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nome', 'profissao', 'estrelas', 'ativo', 'modificado')

