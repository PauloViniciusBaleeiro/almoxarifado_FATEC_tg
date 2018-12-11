from django.urls import path
from .views import criar_inventario, inventario_lista, escolha

urlpatterns = [
    path('inventario/', criar_inventario, name='inventario'),
    path('inventario/<int:id>', escolha, name='inventario_1'),
    path('inventario/<int:id>/<escolha>', inventario_lista, name='inventario_2'),

]