from django.urls import path
from .views import criar_inventario, escolha

urlpatterns = [
    path('inventario/', criar_inventario, name='inventario'),
    path('inventário/<int:id>', escolha, name='inventario_1'),
    path('inventario/lista/', escolha, name='inventario_2'),

]