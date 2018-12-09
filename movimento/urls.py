from django.urls import path
from .views import (requisita_material, lista_requisicoes_nao_atendidas as nao_atendidas, devolve_material,
                    descarte, decremento, localiza_requisicao, exibe_requisicao_atendimento, atende_requisição)

urlpatterns = [
    path('requisita/', requisita_material, name='requisicao'),
    path('requisita/<int:id>', requisita_material, name='requisita_new'),
    path('requisita/lista-nao', nao_atendidas, name='nao_atendidas'),
    path('requisita/detalhe/<int:id>', exibe_requisicao_atendimento, name='requisicao_detalhe'),
    path('requisita/atende-integral/<int:id>', atende_requisição, name='atende_integralmente'),
    path('devolucao/', devolve_material, name='devolucao'),
    path('devolucao/<int:id>', devolve_material, name='devolucao'),
    path('descarte/', descarte, name='descarte'),
    path('decremento/', decremento, name='decremento'),
    path('localiza/', localiza_requisicao, name='localiza_requisicao'),
]