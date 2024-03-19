from django.test import TestCase
from django.contrib.auth.models import User

from authors.models import Profile


class AuthorsProfileTest(TestCase):

    def test_profile_model_returns_author_username(self):
        # criando o autor passando um username
        author = User.objects.create(
            first_name='hehe',
            last_name='what',
            username='profile_test'
        )

        # limpando o banco de dados do profile para nao dar unique contrait
        # nos testes
        Profile.objects.all().delete()

        # passando o author pra dentro do model
        model = Profile.objects.create(author=author)

        # verificando se o metodo __str__ contem o author.username
        self.assertEqual(
            str(model), author.username
        )
