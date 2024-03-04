from .test_recipes_base import RecipeBaseFunctionalTest
from selenium.webdriver.common.by import By


class RecipeIndexFunctionalTest(RecipeBaseFunctionalTest):

    def test_recipe_index_page_without_recipes(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn(
            'No momento não tem-se receitas', body.text
        )
