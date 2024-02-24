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
