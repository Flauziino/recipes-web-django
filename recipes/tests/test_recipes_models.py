from .test_recipes_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_description_raises_error_if_title_has_more_than_65_chars(self):  # noqa: E501
        self.recipe.description = 'A' * 300

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_time_unit_raises_error_if_title_has_more_than_65_chars(self):  # noqa: E501
        self.recipe.preparation_time_unit = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_servings_unit_raises_error_if_title_has_more_than_65_chars(self):  # noqa: E501
        self.recipe.servings_unit = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
