from django.forms import ModelForm
from .models import Sugestao
from django import forms

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
        widgets = {'estabelecimento':forms.TextInput(attrs={'class':'form-control','placeholder':'this field is required'}),
                   'telefone': forms.TextInput(attrs={'class':'form-control','placeholder':'this field is required'}),
                  }