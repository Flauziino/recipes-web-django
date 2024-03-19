from django.urls import reverse, resolve

from recipes import views

from .test_recipes_base import RecipeTestBase

from tag.models import Tag
from unittest.mock import patch


class RecipesTagsTest(RecipeTestBase):

    def setUp(self):
        self.tag = Tag.objects.create(
            name='uma tag',
            slug='uma-tag'
        )

    def test_recipes_tag_views_function_is_correct(self):
        view = resolve(
            reverse(
                'recipes:tag',
                kwargs={'slug': self.tag.slug}
            )
        )
        self.assertIs(view.func.view_class, views.RecipeListTagView)

    def test_recipes_tag_view_returns_Tag_nao_encontrada_if_no_tags(self):
        response = self.client.get(
            reverse(
                'recipes:tag',
                kwargs={'slug': 'd1221d1d12d2'}
            )
        )

        self.assertContains(
            response,
            'Tag não encontrada'
        )
