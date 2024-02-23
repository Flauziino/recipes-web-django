from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):

    def test_recipe_index_url_is_correct(self):
        index_url = reverse('recipes:index')
        self.assertEqual(index_url, '/')
