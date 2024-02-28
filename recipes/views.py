from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import Http404
from django.db.models import Q
from django.core.paginator import Paginator

from utils.pagination import make_pagination_range
from . import models


def index(request):

    receitas = (
        models.Recipe.objects.filter(is_published=True)
        .order_by('-id')
        )

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(receitas, 6)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        current_page
    )

    contexto = {
        'receitas': page_obj,
        'pagination_range': pagination_range,
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
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    receitas = models.Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ), is_published=True
    ).order_by('id')

    contexto = {
        'page_title': f'Search for {search_term} | ',
        'search_term': search_term,
        'receitas': receitas
    }

    return render(
        request,
        'recipes/search.html',
        contexto
    )
