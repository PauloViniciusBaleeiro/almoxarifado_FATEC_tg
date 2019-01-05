from django.urls import path
from .views import list_posicoes, cadastra_posicao, vincula_material, remover_posicao, remove_vinculo

urlpatterns = [
    path('posicao/', list_posicoes, name='list_posicoes'),
    path('posicao/cadastra/', cadastra_posicao, name='nova_posicao'),
    path('posicao/remover/<int:id>', remover_posicao, name='remover_posicao'),
    path('posicao/vincula/<int:id>', vincula_material, name='vincula_material'),
    path('posicao/vincula/remove/<int:id>', remove_vinculo, name='remove_vinculo')
]