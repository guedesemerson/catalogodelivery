from django.shortcuts import render
from estabelecimento.models import Estabelecimento
from categoria.models import Categoria

def list(request):
    listaEstabelecimento = Estabelecimento.objects.all()
    listaCategoria = Categoria.objects.all()
    return render(request, 'estabelecimento/listaEstabelecimento.html',{'categoria': listaCategoria, 'estabelecimento': listaEstabelecimento} )



