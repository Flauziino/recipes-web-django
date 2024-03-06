from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, AuthorRecipeForm
from recipes.models import Recipe


def register_view(request):
    form = RegisterForm()

    contexto = {
        'form': form,
        'form_action': reverse('authors:create')
    }

    return render(
        request,
        'author/register_view.html',
        contexto
    )


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        messages.success(
            request,
            'Cadastro realizado com sucesso!'
        )

        del (request.session['register_form_data'])

        return redirect(
            reverse('authors:login')
        )

    contexto = {
        'form': form
    }

    messages.error(
        request,
        'Existem erros em seu formulário, favor conferir os dados.'
    )

    return render(
        request,
        'author/register_view.html',
        contexto
    )


def login_view(request):
    form = LoginForm

    contexto = {
        'form': form,
        'form_action': reverse('authors:login_create')
    }
    return render(
        request,
        'author/login.html',
        contexto
    )


def login_create(request):
    if not request.POST:
        raise Http404

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(
                request, 'Logado com sucesso!'
            )
            login(request, authenticated_user)

            return redirect('authors:dashboard')

        messages.error(
            request, 'Falha ao logar, usuário ou senha inválidos'
        )
        return redirect('authors:login')

    messages.error(
        request, 'Falha ao logar, usuário ou senha inválidos'
    )
    return redirect('authors:login')


@login_required(
    login_url='authors:login', redirect_field_name='next'
)
def logout_view(request):
    if not request.POST:

        messages.error(
            request, 'Você precisa estar logado para realizar esta ação'
        )

        return redirect(
            reverse('authors:login')
        )

    if request.POST.get('username') != request.user.username:
        messages.error(
            request, 'Este usuário não tem acesso a esta página'
        )

        return redirect(
            reverse('authors:login')
        )

    logout(request)
    messages.success(
        request, 'Deslogado com sucesso!'
    )

    return redirect(
        reverse('authors:login')
    )


@login_required(
    login_url='authors:login', redirect_field_name='next'
)
def dashboard(request):
    receitas = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )

    contexto = {
        'receitas': receitas
    }

    return render(
        request,
        'author/dashboard.html',
        contexto
    )


@login_required(
    login_url='authors:login', redirect_field_name='next'
)
def dashboard_recipe_edit(request, id):
    receita = get_object_or_404(
        Recipe,
        is_published=False,
        author=request.user,
        pk=id
    )

    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=receita
    )

    if form.is_valid():
        receita = form.save(commit=False)

        receita.author = request.user
        receita.preparation_steps_is_html = False
        receita.is_published = False

        receita.save()

        messages.success(
            request, 'Sua receita foi salva com sucesso!'
        )
        return redirect(
            reverse('authors:dashboard_edit', args=(id,))
        )

    contexto = {
        'form': form
    }

    return render(
        request,
        'author/dashboard_recipe.html',
        contexto
    )


@login_required(
    login_url='authors:login', redirect_field_name='next'
)
def dashboard_recipe_create(request):

    if request.method == 'POST':
        form = AuthorRecipeForm(
            data=request.POST,
            files=request.FILES
        )

        if form.is_valid():
            form.save(commit=False)

            nova_receita = Recipe.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                preparation_time=form.cleaned_data['preparation_time'],
                preparation_time_unit=form.cleaned_data['preparation_time_unit'],  # noqa: E501
                servings=form.cleaned_data['servings'],
                servings_unit=form.cleaned_data['servings_unit'],
                preparation_steps=form.cleaned_data['preparation_steps'],
                cover=form.cleaned_data['cover'],
            )

            nova_receita.author = request.user
            nova_receita.preparation_steps_is_html = False
            nova_receita.is_published = False

            nova_receita.save()

            messages.success(
                request, 'Sua receita foi salva com sucesso!'
            )

            return redirect('authors:dashboard')

    else:
        form = AuthorRecipeForm()

    contexto = {
        'form': form,
    }

    return render(
        request,
        'author/dashboard_new_recipe.html',
        contexto
    )
