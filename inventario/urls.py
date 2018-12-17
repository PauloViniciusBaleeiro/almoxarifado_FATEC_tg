from django.urls import path
from .views import (criar_inventario, inventario_lista, escolha, lanca_contagem, inventario_delete, lista_inventario,
                    rel_inventario)

urlpatterns = [
    path('inventario/', criar_inventario, name='inventario'),
    path('inventario/<int:id>', escolha, name='inventario_1'),
    path('inventario/<int:id>/<escolha>', inventario_lista, name='inventario_2'),
    path('contagem/<int:inventario>/<int:material>', lanca_contagem, name='lanca_contagem'),
    path('inventario/delete/<int:id>', inventario_delete, name='inventario_delete'),
    path('inventario/lista/', lista_inventario, name='lista_inventario'),
    path('inventario/relatorio/<int:id>', rel_inventario, name='relatorio_inventario'),

]