from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _

class ContatoForm(forms.Form):
    nome = forms.CharField(label=_("Nome"), max_length=50)
    email = forms.EmailField(label=_("Email"), max_length=50)
    subject = forms.CharField(label=_("Assunto"), max_length=50)
    message = forms.CharField(label=_("Escreva sua mensagem aqui"), widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        name = _("Nome")
        e_mail = _("Email")
        assunto = _("Assunto")
        mensagem = _("Mensagem")

        conteudo = f"{name}: {nome}\n{e_mail}: {email}\n{assunto}: {subject}\n{mensagem}: {message}"
        mail = EmailMessage(
            subject=nome,
            body=conteudo,
            from_email='contato@fusion.com.br', #Remetente
            to=['contato@fusion.com.br',], #Especifica o destinatário
            headers={'Reply-to': email}
        )
        mail.send()