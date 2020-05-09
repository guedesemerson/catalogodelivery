from .views import listcategoria
from django.urls import path

urlpatterns = [
    path('list/<id>', listcategoria, name='listcategoria'),

]