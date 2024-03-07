from django.urls import path
from recipes import views


app_name = 'recipes'

# urls do app recipes
urlpatterns = [
    path('', views.RecipeListIndexView.as_view(), name='index'),

    path(
        'recipes/search',
        views.RecipeListSearchView.as_view(),
        name='search'
    ),

    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListCategoryView.as_view(), name='category'
    ),

    path('recipes/<int:id>', views.recipe, name='recipe'),
]
