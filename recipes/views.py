from django.shortcuts import render
from . import models


def index(request):

    receitas = (
        models.Recipe.objects.filter(is_published=True)
        .order_by('-id')
        )

    contexto = {
        'receitas': receitas,
    }

    return render(
        request,
        'recipes/index.html',
        contexto
    )


def category(request, category_id):

    receitas = (
        models.Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    contexto = {
        'receitas': receitas,
    }

    return render(
        request,
        'recipes/category.html',
        contexto
    )


def recipe(request, id):

    receita = (
        models.Recipe.objects.get(id=id)
    )

    contexto = {
        'receita': receita
    }

    return render(
        request,
        'recipes/recipe-view.html',
        contexto
    )
