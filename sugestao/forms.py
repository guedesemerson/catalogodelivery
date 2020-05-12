from django.forms import ModelForm
from .models import Sugestao

class SugestaoForm(ModelForm):
    class Meta:
        model= Sugestao
        fields=['estabelecimento',
                'telefone',
                'endereco',
                'bairro',
                'site',
                'observacao',
                 ]