from django.db import models
from categoria.models import Categoria

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    observacao = models.TextField()
    site = models.CharField(max_length=50)


    def __str__(self):
        return self.nome
