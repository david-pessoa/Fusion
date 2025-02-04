import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
    
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test__str__(self):
        self.assertEqual(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')
    
    def test__str__(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')
    
    def test__str__(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)

class FeatureTestCase(TestCase):
    def setUp(self):
        self.feature = mommy.make('Feature')
    
    def test__str__(self):
        self.assertEqual(str(self.feature), self.feature.nome)

class PlanoTestCase(TestCase):
    def setUp(self):
        self.plano = mommy.make('Plano', #Às vezes o mommy pode dar erro, então é melhor criar a instância explicitamente nesses casos
                                nome='Plano Piloto',
                                icone='lni-laptop-phone',
                                preco=20.88,
                                numero_usuarios=3,
                                numero_usuarios_ilimitado=False,
                                armazenamento=40,
                                armazenamento_ilimitado=False,
                                suporte='Suportado',
                                atualizacoes='Lifetime updates'
                                )
    
    def test__str__(self):
        self.assertEqual(str(self.plano), self.plano.nome)

class DepoimentoTestCase(TestCase):
    def setUp(self):
        self.depoimento = mommy.make('Depoimento')
    
    def test__str__(self):
        self.assertEqual(str(self.depoimento), self.depoimento.nome)