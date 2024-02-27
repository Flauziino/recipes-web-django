from django.urls import reverse, resolve
from recipes import views
from .test_recipes_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

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

    # test da view category
    def test_recipes_category_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1}
            )
        )
        self.assertIs(view.func, views.category)

    # teste do status code(category.view)
    def test_recipes_category_view_returns_statuscode_404_if_no_recipes(self):
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': 10000}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_recipes_category_template_loads_recipes(self):
        # criando a receita para o teste
        needed = 'Categorias (titulo)'
        self.make_recipe(title=needed)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1}
                )
            )
        content = response.content.decode('utf-8')

        # checando se ela existe
        self.assertIn(needed, content)

    def test_recipes_category_template_do_not_loads_recipes_if_is_published_false(self):  # noqa: E501
        # criando a receita para o teste
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': recipe.category.id}
                )
            )

        self.assertEqual(response.status_code, 404)

    # test da view recipe
    def test_recipes_recipe_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:recipe',
                kwargs={'id': 1}
            )
        )
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_detail_returns_statuscode_404_(self):  # noqa: E501
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': 10000}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_template_loads_correct_recipe(self):
        # criando a receita para o teste
        needed = 'Detalhes da receita (titulo)'
        self.make_recipe(title=needed)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': 1}
                )
            )
        content = response.content.decode('utf-8')

        # checando se ela existe
        self.assertIn(needed, content)

    def test_recipes_recipe_template_do_not_loads_recipe_if_is_published_false(self):  # noqa: E501
        # criando a receita para o teste
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': recipe.id}
                )
            )

        self.assertEqual(response.status_code, 404)

    def test_recipes_search_uses_correct_view_function(self):
        view = resolve(
            reverse(
                'recipes:search',
            )
        )
        self.assertIs(
            view.func, views.search
        )

    def test_recipes_search_loads_correct_template(self):
        response = self.client.get(
            reverse(
                'recipes:search',
            ) + '?q=test'
        )
        self.assertTemplateUsed(
            response, 'recipes/search.html'
        )

    def test_recipes_search_raises_404_if_no_search_termo(self):
        response = self.client.get(
            reverse(
                'recipes:search',
            )
        )
        self.assertEqual(response.status_code, 404)
