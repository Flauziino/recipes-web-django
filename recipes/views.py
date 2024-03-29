import os

from dotenv import load_dotenv

from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView, DetailView


from . import models
from tag.models import Tag
from utils.pagination import make_pagination


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
        qs = qs.select_related('author', 'category', 'author__profile')
        qs = qs.prefetch_related('tags')

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

    def get_queryset(self, *args, **kwargs):
        self.receitas = super().get_queryset(*args, **kwargs)
        self.receitas = self.receitas.filter(
            category__id=self.kwargs.get('category_id')
        )
        if not self.receitas:
            raise Http404

        return self.receitas

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        for receita in self.receitas:
            category_name = receita.category.name

        ctx.update({
            'title': f'{category_name}  - Category | ',
        })
        return ctx


class RecipeListTagView(RecipeListBaseListView):
    template_name = 'recipes/tag.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            tags__slug=self.kwargs.get('slug', '')
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        tag_name = Tag.objects.filter(
            slug=self.kwargs.get('slug', '')
        ).first()

        if not tag_name:
            tag_name = 'Tag não encontrada'

        ctx.update({
            'page_title': f'{tag_name}  - Tag | ',
        })
        return ctx


class RecipeDetailView(DetailView):
    model = models.Recipe
    context_object_name = 'receita'
    template_name = 'recipes/recipe-view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({
            'is_detail_page': True,
        })
        return ctx


class RecipeListSearchView(RecipeListBaseListView):
    template_name = 'recipes/search.html'

    def get_queryset(self, *args, **kwargs):
        self.search_term = self.request.GET.get('q', '').strip()

        self.receitas = super().get_queryset(*args, **kwargs)
        self.receitas = self.receitas.filter(
            Q(title__icontains=self.search_term) |
            Q(description__icontains=self.search_term),
        )

        if not self.search_term:
            raise Http404

        return self.receitas

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'page_title': f'Search for {self.search_term} | ',
            'search_term': self.search_term,
            'additional_url_query': f'&q={self.search_term}'
        })
        return ctx
