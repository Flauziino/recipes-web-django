from django.urls import path

from recipes import views


# urls do app recipes
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:id>', views.recipe, name='receita')
]
