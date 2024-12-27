from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename): #   Cria um nome único para a foto do usuário
    ext = filename.split('.')[-1]
    return f'{uuid.uuid4()}.{ext}'

class Base(models.Model):
    data = models.DateField("Data de criação", auto_now_add= True) #Define que a data será igual APENAS a data de criação do objeto
    modificado = models.DateField("Data da última atualização", auto_now= True)  #auto_now = True muda a data sempre que o objeto é atualizado no banco de dados
    ativo = models.BooleanField("Ativo?", default= True)

    class Meta:
        abstract = True

class Icones:
    CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-leaf', 'Folha'),
        ('lni-laptop-phone', 'Dispositivos'),
    )

class Servico(Base):
    # ('Nome salvo banco de dados', 'Nome exibido no django admin')
    icone = models.CharField("ícone", max_length=16, choices=Icones.CHOICES)
    servico = models.CharField("Nome do Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=500)

    class Meta: #Dá um nome para o modelo
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    
    def __str__(self): #Nomeia o objeto da tabela
        return self.servico

class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=50)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
    
    def __str__(self):
        return self.cargo

class Funcionario(Base):
    foto = StdImageField("Foto do funcionário", upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField("Nome", max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    descricao = models.TextField("Descrição", max_length=700)
    facebook = models.CharField("Facebook", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
    
    def __str__(self):
        return self.nome

class Feature(Base):
    icone = models.CharField("Ícone", max_length=16, choices=Icones.CHOICES)
    nome = models.CharField("Nome", max_length=50)
    descricao = models.TextField("Descrição", max_length=100)

    class Meta: 
        verbose_name = "Feature"
        verbose_name_plural = "Features"
    
    def __str__(self):
        return self.nome