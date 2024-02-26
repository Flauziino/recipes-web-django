from .test_recipes_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_fields_max_length(self):
        fields = [
            ('title', 65),
            ('description', 255),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]

        for field, max_length in fields:
            setattr(
                self.recipe, field, 'A' * (max_length + 5)
            )
            with self.assertRaises(ValidationError):
                self.recipe.full_clean()
