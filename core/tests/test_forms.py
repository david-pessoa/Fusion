from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.subject = 'Um assunto qualquer'
        self.message = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'subject': self.subject,
            'message': self.message
        }

        self.form = ContatoForm(data=self.dados)  #ContatoForm(rquest.POST)
    
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)