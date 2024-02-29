from django.shortcuts import render
from .forms import RegisterForm
from django.http import Http404


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
        raise Http404

    form = RegisterForm(request.POST)

    contexto = {
        'form': form
    }

    return render(
        request,
        'author/register_view.html',
        contexto
    )
