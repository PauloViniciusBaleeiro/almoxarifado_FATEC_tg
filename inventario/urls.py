from django.urls import path
from .views import criar_inventario, inventario_lista, escolha, lanca_contagem

urlpatterns = [
    path('inventario/', criar_inventario, name='inventario'),
    path('inventario/<int:id>', escolha, name='inventario_1'),
    path('inventario/<int:id>/<escolha>', inventario_lista, name='inventario_2'),
    path('contagem/<int:inventario>/<int:material>', lanca_contagem, name='lanca_contagem')

]