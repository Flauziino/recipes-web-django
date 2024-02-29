from django import forms
from django.contrib.auth.models import User
from utils.placeholder import add_placeholder


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuário')
        add_placeholder(self.fields['email'], 'Ex: John@email.com')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')

    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Sua senha'
        }),
        error_messages={
            'required': 'O campo não pode estar vazio'
        },
        help_text=(
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        )
    )
    password2 = forms.CharField(
        label='Repita sua senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'email', 'password'
        ]

        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório'
            },
            'first_name': {
                'required': 'Este campo é obrigatório'
            },
            'email': {
                'required': 'Este campo é obrigatório'
            },
            'password': {
                'required': 'Este campo é obrigatório'
            },
        }
