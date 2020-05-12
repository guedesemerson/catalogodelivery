from .views import add,formsugestao
from django.urls import path

urlpatterns = [
    path('adicionar/', add, name='adicionar_sugestao'),
    path('', formsugestao, name='form_sugestao'),
]