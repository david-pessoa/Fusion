from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    subject = forms.CharField(label="Assunto", max_length=50)
    message = forms.CharField(label="Escreva sua mensagem aqui", widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        conteudo = f"Nome: {nome}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}"
        mail = EmailMessage(
            nome=nome,
            body=conteudo,
            from_email='contato@fusion.com.br', #Remetente
            to=['contato@fusion.com.br',], #Especifica o destinatário
            headers={'Reply-to': email}
        )
        mail.send()