from django.db import models

class Sugestao(models.Model):
    estabelecimento = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=100,null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    site = models.CharField(max_length=50,null=True, blank=True)
    data_insercao = models.DateField( auto_now_add=True,)
    def __str__(self):
        return self.estabelecimento
