from django.urls import path
from .views import (home, logout, listagem_fabricante as list, novo_fabricante as novo, cadastra_cidade,
                    cadastra_estado, cadastra_contato, atualiza_fabricante, deleta_contato)

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('fabricantes/', list, name='list_fabricantes'),
    path('fabricantes/novo/', novo, name='novo_fabricante'),
    path('fabricantes/atualizar/<int:id>', atualiza_fabricante, name='atualiza_fabricante'),
    path('fabricantes/contatos/<int:id>', cadastra_contato, name='contato'),
    path('fabricantes/contatos/deletar/<int:id>', deleta_contato, name='remover_contato'),
    path('cidades/nova/', cadastra_cidade, name='nova_cidade'),
    path('estados/novo/', cadastra_estado, name='novo_estado')
]