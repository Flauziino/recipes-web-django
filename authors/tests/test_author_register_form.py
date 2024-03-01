from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from django.urls import reverse

from authors.forms import RegisterForm

from parameterized import parameterized


class AuthorRegisterFormTest(TestCase):
    def test_first_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['first_name'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Ex.: John', placeholder
        )

    def test_last_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['last_name'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Ex.: Doe', placeholder
        )

    def test_email_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['email'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Ex: John@email.com', placeholder
        )

    def test_username_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['username'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Seu nome de usuário', placeholder
        )

    def test_password_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['password'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Sua senha', placeholder
        )

    def test_password2_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form['password2'].field.widget.attrs['placeholder']
        self.assertEqual(
            'Confirme sua senha', placeholder
        )

    @parameterized.expand([
        ('password', (
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
            )
         ),
        ('username', (
            'Obrigatório. 150 caracteres ou menos.'
            ' Letras, números e @/./+/-/_ apenas.'
            )
         ),
    ])
    def test_field_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('first_name', 'Primeiro nome'),
        ('last_name', 'Último nome'),
        ('username', 'Usuário'),
        ('email', 'Endereço de email'),
        ('password', 'Senha'),
        ('password2', 'Confirme sua senha'),
    ])
    def test_fields_labels(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)


class AuthorRegisterIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'email': 'emailuser@email.com',
            'password': 'Str0123456b',
            'password2': 'Str0123456b',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Este campo é obrigatóiro'),
        # ('last_name', 'Este campo é obrigatório'),
        # ('email', 'Este campo é obrigatório'),
        # ('password', 'Este campo é obrigatório'),
        # ('password2', 'Este campo é obrigatório'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ' '
        url = reverse('authors:create')
        response = self.client.post(
            url, data=self.form_data, follow=True
        )
        self.assertIn(
            msg, response.content.decode('utf-8')
        )
