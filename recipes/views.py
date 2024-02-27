from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models
from django.http.response import Http404


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

    receitas = get_list_or_404(
        models.Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    for receita in receitas:
        category_name = receita.category.name

    contexto = {
        'receitas': receitas,
        'title': f'{category_name}  - Category | '
    }

    return render(
        request,
        'recipes/category.html',
        contexto
    )


def recipe(request, id):

    receita = get_object_or_404(
        models.Recipe,
        id=id,
        is_published=True
    )

    contexto = {
        'receita': receita,
        'is_detail_page': True,
    }

    return render(
        request,
        'recipes/recipe-view.html',
        contexto
    )


def search(request):
    search_term = request.GET.get('q')

    if not search_term:
        raise Http404()

    return render(
        request,
        'recipes/search.html'
    )
