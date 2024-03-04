from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404
from django.contrib import messages


def register_view(request):
    form = RegisterForm()

    contexto = {
        'form': form
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
