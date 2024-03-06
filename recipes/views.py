import os
from dotenv import load_dotenv

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import Http404
from django.db.models import Q
from django.views.generic import ListView

from utils.pagination import make_pagination
from . import models


load_dotenv()

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


class RecipeListBaseListView(ListView):
    model = models.Recipe
    paginate_by = None
    context_object_name = 'receitas'
    ordering = ['-id']
    template_name = 'recipes/index.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('receitas'),
            PER_PAGE,
        )
        ctx.update({
            'receitas': page_obj,
            'pagination_range': pagination_range
        })

        return ctx


class RecipeListIndexView(RecipeListBaseListView):
    template_name = 'recipes/index.html'


class RecipeListCategoryView(RecipeListBaseListView):
    template_name = 'recipes/category.html'


def category(request, category_id):

    receitas = get_list_or_404(
        models.Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    for receita in receitas:
        category_name = receita.category.name

    page_obj, pagination_range = make_pagination(
        request,
        receitas,
        PER_PAGE,
    )

    contexto = {
        'receitas': page_obj,
        'title': f'{category_name}  - Category | ',
        'pagination_range': pagination_range,
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

    page_obj, pagination_range = make_pagination(
        request,
        receitas,
        PER_PAGE,
    )

    contexto = {
        'page_title': f'Search for {search_term} | ',
        'search_term': search_term,
        'receitas': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    }

    return render(
        request,
        'recipes/search.html',
        contexto
    )
