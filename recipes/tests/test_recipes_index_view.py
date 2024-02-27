from django.urls import reverse, resolve
from recipes import views
from .test_recipes_base import RecipeTestBase


class RecipeIndexTest(RecipeTestBase):

    # tests da view index
    def test_recipes_index_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:index'
            )
        )
        self.assertIs(view.func, views.index)

    # teste do status code(index.view)
    def test_recipes_index_view_returns_statuscode_200_OK(self):
        response = self.client.get(
            reverse(
                'recipes:index'
            )
        )

        self.assertEqual(response.status_code, 200)

    # teste do template(index.view)
    def test_recipes_index_view_loads_correct_template(self):
        response = self.client.get(
            reverse(
                'recipes:index'
            )
        )

        self.assertTemplateUsed(
            response, 'recipes/index.html'
            )

    # teste se no template renderizado pela view index tem:
    # "No momento não tem-se receitas" caso nao tenha receita na pagina
    def test_recipes_index_views_template_shows_no_momento_não_tem_se_receitas(self):  # noqa: E501
        response = self.client.get(
            reverse(
                'recipes:index'
            )
        )

        self.assertIn(
            'No momento não tem-se receitas',
            response.content.decode('utf-8'))

    def test_recipes_index_template_loads_recipes(self):
        # criando a receita para o teste
        self.make_recipe()

        response = self.client.get(
            reverse(
                'recipes:index'
                )
            )
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['receitas']

        # checando se ela existe
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipes_index_template_do_not_loads_recipes_if_is_published_false(self):  # noqa: E501
        # criando a receita para o teste
        self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:index'
                )
            )

        # checando se ela existe
        self.assertIn(
            'No momento não tem-se receitas',
            response.content.decode('utf-8'))
