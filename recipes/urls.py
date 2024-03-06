from django.urls import path
from recipes import views


app_name = 'recipes'

# urls do app recipes
urlpatterns = [
    path('', views.RecipeListIndexView.as_view(), name='index'),
    path('recipes/search', views.search, name='search'),

    path(
        'recipes/category/<int:category_id>/',
        views.category, name='category'
    ),

    path('recipes/<int:id>', views.recipe, name='recipe'),
]
