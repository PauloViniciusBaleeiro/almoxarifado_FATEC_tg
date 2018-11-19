from django.urls import path
from .views import list_posicoes, cadastra_posicao, vincula_material

urlpatterns = [
    path('posicao/', list_posicoes, name='list_posicoes'),
    path('posicao/cadastra/', cadastra_posicao, name='nova_posicao'),
    path('posicao/vincula/<int:id>', vincula_material, name='vincula_material')
]