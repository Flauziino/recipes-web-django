from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.urls import reverse

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
            'recipes:index'
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
    return render(
        request,
        'author/login.html'
    )
