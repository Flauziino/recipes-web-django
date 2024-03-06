# type: ignore
# flake8: noqa
# ARQUIVO DESTINADO A "GUARDAR" AS FUNCOES QUE FORAM REMOVIDAS PARA DAR
# ESPACO A CLASSES DENTRO DO CODIGO

# FUNCBASEVIEW DA LISTA DA INDEX PAGE
def index(request):

    receitas = (
        models.Recipe.objects.filter(is_published=True)
        .order_by('-id')
    )

    page_obj, pagination_range = make_pagination(
        request,
        receitas,
        PER_PAGE,
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
