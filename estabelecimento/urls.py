from .views import list
from django.urls import path

urlpatterns = [
    path('list/', list, name='listestabelecimento'),

]