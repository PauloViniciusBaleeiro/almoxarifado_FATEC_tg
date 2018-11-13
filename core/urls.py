from django.urls import path
from .views import (home, logout, listagem_fabricante as list, novo_fabricante as novo, cadastra_cidade,
                    cadastra_estado, cadastra_contato, atualiza_fabricante, deleta_contato, lista_material as list_m,
                    cadastra_material, cadastra_tipo_de_material as cad_tipo_mat, altera_material)

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('fabricantes/', list, name='list_fabricantes'),
    path('fabricantes/novo/', novo, name='novo_fabricante'),
    path('fabricantes/atualizar/<int:id>', atualiza_fabricante, name='atualiza_fabricante'),
    path('fabricantes/contatos/<int:id>', cadastra_contato, name='contato'),
    path('fabricantes/contatos/deletar/<int:id>', deleta_contato, name='remover_contato'),
    path('cidades/nova/', cadastra_cidade, name='nova_cidade'),
    path('estados/novo/', cadastra_estado, name='novo_estado'),
    path('materiais/', list_m, name='lista_material'),
    path('materiais/novo', cadastra_material, name='novo_material'),
    path('material/alterar/<int:id>', altera_material, name='altera_material'),
    # path('material/deletar/<int:id>', ),
    path('materiais/tipo/novo', cad_tipo_mat, name='novo_tipo_material')
]