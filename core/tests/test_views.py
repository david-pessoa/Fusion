from django.test import TestCase
from django.test import Client #Serve como cliente para executar métodos HTTP
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'subject': 'Um assunto qualquer',
            'message': 'Uma mensagem qualquer'
        }
        self.cliente = Client()
    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Felicidades Jéssica',
            'assunto': 'Meu assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)