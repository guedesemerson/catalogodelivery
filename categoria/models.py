from django.db import models

class Categoria(models.Model):

    nome_categoria = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_categoria
