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
