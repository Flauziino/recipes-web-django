from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm


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

            return redirect('recipes:index')

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
