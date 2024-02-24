from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):

    # teste de VIEWS
    def test_recipes_index_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:index'
            )
        )
        self.assertIs(view.func, views.index)

    def test_recipes_category_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1}
            )
        )
        self.assertIs(view.func, views.category)

    def test_recipes_recipe_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:recipe',
                kwargs={'id': 1}
            )
        )
        self.assertIs(view.func, views.recipe)

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
