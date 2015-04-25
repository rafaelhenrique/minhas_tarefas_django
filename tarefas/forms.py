from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class FormNovoUsuario(Form):
    nome_de_usuario = CharField()
    nome = CharField(required=False)
    email = EmailField(required=False)
    senha = CharField(widget=PasswordInput)
    repeticao_senha = CharField(widget=PasswordInput)

    def save(self):
        params = {
            'username': self.cleaned_data['nome_de_usuario'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['senha']
        }
        if self.cleaned_data['nome']:
            params['first_name'] = self.cleaned_data['nome']
        User.objects.create_user(**params)

    # Esse metodo tem que ter o nome clean_<campo>
    # eh um metodo de validacao de campos do Django
    def clean_repeticao_senha(self):
        senha1 = self.cleaned_data['senha']
        senha2 = self.cleaned_data['repeticao_senha']

        if senha1 != senha2:
            raise ValidationError("As senhas digitadas não conferem")
        return senha1
