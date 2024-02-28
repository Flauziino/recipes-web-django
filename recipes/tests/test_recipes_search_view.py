from django.urls import reverse, resolve
from recipes import views
from .test_recipes_base import RecipeTestBase


class RecipeSearchTest(RecipeTestBase):

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

    def test_recipes_search_term_in_on_page_title_and_escaped(self):
        response = self.client.get(
            reverse(
                'recipes:search',
            ) + '?q=<script>test</script>'
        )

        self.assertIn(
            'Search for &lt;script&gt;test&lt;/script&gt;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title = 'This is recipe one'
        a_title = 'This is recipe two'

        recipe = self.make_recipe(
            slug='one',
            title=title,
            author_data={'username': 'one'}
        )

        a_recipe = self.make_recipe(
            slug='two',
            title=a_title,
            author_data={'username': 'two'}
        )
        response = self.client.get(
            reverse('recipes:search') + f'?q={title}'
            )
        a_response = self.client.get(
            reverse('recipes:search') + f'?q={a_title}'
            )
        response_both = self.client.get(
            reverse('recipes:search',) + '?q=This'
            )

        self.assertIn(recipe, response.context['receitas'])
        self.assertNotIn(a_recipe, response.context['receitas'])

        self.assertIn(a_recipe, a_response.context['receitas'])
        self.assertNotIn(recipe, a_response.context['receitas'])

        self.assertIn(recipe, response_both.context['receitas'])
        self.assertIn(a_recipe, response_both.context['receitas'])
