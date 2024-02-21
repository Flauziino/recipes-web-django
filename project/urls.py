from django.urls import path, include


urlpatterns = [
    path('', include('recipes.urls')),  # linkando urls do app recipes
]
