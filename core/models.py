import uuid
from django.db import models
from stdimage.models import StdImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename): #   Cria um nome único para a foto do usuário
    ext = filename.split('.')[-1]
    return f'{uuid.uuid4()}.{ext}'

class Base(models.Model):
    data = models.DateField(_("Data de criação"), auto_now_add= True) #Define que a data será igual APENAS a data de criação do objeto
    modificado = models.DateField(_("Data da última atualização"), auto_now= True)  #auto_now = True muda a data sempre que o objeto é atualizado no banco de dados
    ativo = models.BooleanField(_("Ativo?"), default= True)

    class Meta:
        abstract = True

CHOICES = (
    ('lni-cog', _('Engrenagem')),
    ('lni-stats-up', _('Gráfico')),
    ('lni-users', _('Usuários')),
    ('lni-layers', _('Design')),
    ('lni-mobile', _('Mobile')),
    ('lni-rocket', _('Foguete')),
    ('lni-leaf', _('Folha')),
    ('lni-laptop-phone', _('Dispositivos')),
    ('lni-package', _('Pacote')),
    ('lni-drop', _('Gota')),
    ('lni-star', _('Estrela')),
    ('lni-star-filled', _('Estrela Cheia')),
    ('lni-star-half', _('Estrela Vazia'))
)

def get_max_length():
    return max(len(choice[0]) for choice in CHOICES)


class Servico(Base):
    # ('Nome salvo banco de dados', 'Nome exibido no django admin')
    icone = models.CharField(_("ícone"), max_length=get_max_length(), choices=CHOICES)
    servico = models.CharField("Nome do Serviço", max_length=100)
    descricao = models.TextField(_("Descrição"), max_length=500)

    class Meta: #Dá um nome para o modelo
        verbose_name = _("Serviço")
        verbose_name_plural = _("Serviços")
    
    def __str__(self): #Nomeia o objeto da tabela
        return self.servico

class Cargo(Base):
    cargo = models.CharField(_("Cargo"), max_length=50)

    class Meta:
        verbose_name = _("Cargo")
        verbose_name_plural = _("Cargos")
    
    def __str__(self):
        return self.cargo

class Funcionario(Base):
    foto = StdImageField(_("Foto do funcionário"), upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField(_("Nome"), max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    descricao = models.TextField(_("Descrição"), max_length=700)
    facebook = models.CharField("Facebook", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")

    class Meta:
        verbose_name = _("Funcionário")
        verbose_name_plural = _("Funcionários")
    
    def __str__(self):
        return self.nome

class Feature(Base):
    icone = models.CharField(_("ícone"), max_length=get_max_length(), choices=CHOICES)
    nome = models.CharField(_("Nome"), max_length=50)
    descricao = models.TextField(_("Descrição"), max_length=100)

    class Meta: 
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
    
    def __str__(self):
        return self.nome

class Plano(Base):
    icone = models.CharField(_("ícone"), max_length=get_max_length(), choices=CHOICES)
    nome = models.CharField(_("Nome"), max_length=20)
    preco = models.DecimalField(_("Preço"), decimal_places=2, max_digits=10)
    numero_usuarios = models.DecimalField(_("Número máximo de usuários"), decimal_places=0, max_digits=6)
    numero_usuarios_ilimitado = models.BooleanField(_("Número de usuários ilimitado?"), default=False)
    armazenamento = models.DecimalField(_("Limite máximo de armazenamento (GB)"), decimal_places=0, max_digits=4)
    armazenamento_ilimitado = models.BooleanField(_("Armazenamento ilimitado?"), default=False)
    suporte = models.CharField(_("Tipo de suporte"))
    atualizacoes = models.CharField(_("Atualizações"), max_length=50, default=_("Lifetime updates"))

    class Meta:
        verbose_name = _('Plano')
        verbose_name_plural = _('Planos')
    
    def __str__(self):
        return self.nome

class Depoimento(Base):
    foto = StdImageField(_("Foto do cliente"), upload_to=get_file_path, variations={'thumb':{'width': 75, 'height': 75, 'crop': True}})
    nome = models.CharField(_("Nome"), max_length=70)
    profissao = models.CharField(_("Profissão"), max_length=70)
    estrelas = models.DecimalField(_("Número de estrelas"), decimal_places=0, max_digits=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    descricao = models.TextField(_("Descrição"), max_length=500, default="Praesent cursus nulla non arcu tempor, ut egestas elit tempus. In ac ex fermentum, gravida felis nec, tincidunt ligula.")

    class Meta:
        verbose_name = _('Depoimento')
        verbose_name_plural = _('Depoimentos')
    
    def __str__(self):
        return self.nome