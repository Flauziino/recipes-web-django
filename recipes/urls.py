from django.urls import path
from recipes import views


app_name = 'recipes'

# urls do app recipes
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:id>', views.recipe, name='receita')
]
