from django.urls import path
from .views import movimentacoes_rel, estoque, perdas_avarias


urlpatterns = [
    path('relatorio/movimentacoes/', movimentacoes_rel, name='rel_movimentacoes'),
    path('relatorio/estoque/', estoque, name='estoque'),
    path('relatorio/perdas-avarias/', perdas_avarias, name='perdas_avarias'),
]