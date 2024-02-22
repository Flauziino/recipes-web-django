from django.shortcuts import render


def index(request):
    return render(
        request,
        'recipes/index.html'
    )


def recipe(request, id):
    return render(
        request,
        'recipes/recipe-view.html'
    )
