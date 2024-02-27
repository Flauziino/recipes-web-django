from django.urls import reverse, resolve
from recipes import views
from .test_recipes_base import RecipeTestBase


class RecipeCategoryTest(RecipeTestBase):
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
