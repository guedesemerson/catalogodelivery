from django.shortcuts import render
from estabelecimento.models import Estabelecimento
from categoria.models import Categoria

def listcategoria(request, id):

    listaEstabelecimento = Estabelecimento.objects.all()

    listaCategoria = Categoria.objects.all()

    listacategoriaId = Estabelecimento.objects.filter(
        categoria = id,
    )

    nomeCategoria = Categoria.objects.get(id=id)

    return render(request, 'categoria/listacategoria.html',{'categoria': listaCategoria, 'estabelecimento': listaEstabelecimento, 'categoria_id': listacategoriaId, 'nomeCategoria':nomeCategoria} )

def modal(request, id):

    dadosModal = Estabelecimento.objects.get(id=id)

    return render(request,'categoria/modal.html',{'dadosModal':dadosModal})

