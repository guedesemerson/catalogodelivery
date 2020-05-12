from django.shortcuts import render, redirect
from .forms import SugestaoForm
from categoria.models import Categoria
from estabelecimento.models import Estabelecimento
def add(request):
    form = SugestaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')
def formsugestao(request):
    listaEstabelecimento = Estabelecimento.objects.all()
    listaCategoria = Categoria.objects.all()
    form = SugestaoForm()
    return render(request,'sugestao/form_sugestao.html',{'form':form,'categoria': listaCategoria, 'estabelecimento': listaEstabelecimento})
