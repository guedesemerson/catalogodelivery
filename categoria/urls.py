from .views import listcategoria, modal
from django.urls import path

urlpatterns = [
    path('list/<id>', listcategoria, name='listcategoria'),
    path('modal/<id>', modal, name='modal'),

]