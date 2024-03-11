from django.urls import path
from recipes import views


app_name = 'recipes'

# urls do app recipes
urlpatterns = [
    path(
        '',
        views.RecipeListIndexView.as_view(),
        name='index'
    ),

    path(
        'recipes/search',
        views.RecipeListSearchView.as_view(),
        name='search'
    ),

    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListCategoryView.as_view(),
        name='category'
    ),

    path(
        'recipes/<int:pk>',
        views.RecipeDetailView.as_view(),
        name='recipe'
    ),

    # URL PARA ENTREGA DE API
    path(
        'recipes/api/v1/',
        views.RecipeListIndexViewApi.as_view(),
        name='recipes_api'
    ),

    # URL PARA ENTREGA DE API
    path(
        'recipes/api/v1/<int:pk>',
        views.RecipeDetailViewApi.as_view(),
        name='recipe_api_detail'
    ),
]
