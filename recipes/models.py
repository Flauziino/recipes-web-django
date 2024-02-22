from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(
        max_length=65
        )

    def __str__(self):
        return self.name


class Recipe(models.Model):

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    title = models.CharField(
        verbose_name='Título',
        max_length=65,
    )

    description = models.CharField(
        verbose_name='Descrição',
        max_length=255,
    )

    slug = models.SlugField()

    preparation_time = models.IntegerField(
        verbose_name='Tempo de preparação'
    )

    preparation_time_unit = models.CharField(
        verbose_name='Tempo de preparação unitário',
        max_length=65,
    )

    servings = models.IntegerField(
        verbose_name='Porções'
    )

    servings_unit = models.CharField(
        max_length=65,
        verbose_name='Tipo da porção'
    )

    preparation_steps = models.TextField(
        verbose_name='Passo a passo da preparação'
    )

    preparation_steps_is_html = models.BooleanField(
        default=False,
        verbose_name='O passo a passo é HTML?'
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='Está publicado?'
    )

    cover = models.ImageField(
        upload_to='recipes/cover/%Y/%m/%d/',
        verbose_name='Imagem da receita'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Categoria'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Autor'
    )

    def __str__(self):
        return self.title
