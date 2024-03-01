from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.placeholder import add_placeholder
from utils.strong_password import strong_password


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
        ),
        validators=[strong_password]
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha'
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

    # # Apenas um exemplo de validação de campo para ficar salvo
    # def clean_password(self):
    #     data = self.cleaned_data.get('password')

    #     if 'atencao' in data:
    #         raise ValidationError(
    #             'Não digite "atencao" no campo: Senha',
    #             code='invalid',
    #             params={'value': '"atencao"'}
    #         )

    # validaçao generalista
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError(
                {
                    'password': 'As duas senhas precisam ser iguais!',
                    'password2': 'As duas senhas precisam ser iguais!'
                }
            )
