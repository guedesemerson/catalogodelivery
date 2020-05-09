from django.shortcuts import render
from estabelecimento.models import Estabelecimento
from categoria.models import Categoria
def home(request):
    listaEstabelecimento = Estabelecimento.objects.all()
    listaCategoria = Categoria.objects.all()
    return render(request, 'core/index.html',  {'categoria': listaCategoria, 'estabelecimento': listaEstabelecimento})
