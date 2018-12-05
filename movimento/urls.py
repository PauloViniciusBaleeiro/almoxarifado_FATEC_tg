from django.urls import path
from .views import (requisita_material, lista_requisicoes_nao_atendidas as nao_atendidas, devolve_material,
                    descarte, decremento)

urlpatterns = [
    path('requisita/', requisita_material, name='requisicao'),
    path('requisita/<int:id>', requisita_material, name='requisita_new'),
    path('requisita/lista-nao', nao_atendidas, name='nao_atendidas'),
    path('devolucao/', devolve_material, name='devolucao'),
    path('devolucao/<int:id>', devolve_material, name='devolucao'),
    path('descarte/', descarte, name='descarte'),
    path('decremento/', decremento, name='decremento'),
]