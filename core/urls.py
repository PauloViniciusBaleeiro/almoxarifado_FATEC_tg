from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (landing, home, logout, listagem_fabricante as list, novo_fabricante as novo, deletar_fabricante as delete,
                    cadastra_cidade, cadastra_estado, cadastra_contato, atualiza_fabricante, remove_contato,
                    lista_material as list_m, lista_material_a as list_a, cadastra_material,
                    cadastra_tipo_de_material as cad_tipo_mat, altera_material, entrada_de_material,
                    deleta_material)

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
    path('fabricantes/', list, name='list_fabricantes'),
    path('fabricantes/novo/', novo, name='novo_fabricante'),
    path('fabricantes/remover/<int:id>', delete, name='delete'),
    path('fabricantes/atualizar/<int:id>', atualiza_fabricante, name='atualiza_fabricante'),
    path('fabricantes/contatos/<int:id>', cadastra_contato, name='contato'),
    path('fabricantes/contatos/deletar/<int:id>', remove_contato, name='remover_contato'),
    path('cidades/nova/', cadastra_cidade, name='nova_cidade'),
    path('estados/novo/', cadastra_estado, name='novo_estado'),
    path('materiais/', list_m, name='lista_material'),
    path('materiais/ordenada/', list_a, name='lista_m_alfa'),
    path('materiais/novo', cadastra_material, name='novo_material'),
    path('materiais/alterar/<int:id>', altera_material, name='altera_material'),
    path('material/deletar/<int:id>', deleta_material, name='deleta_material'),
    path('materiais/tipo/novo', cad_tipo_mat, name='novo_tipo_material'),
    path('materiais/entrada/', entrada_de_material, name='entrada_de_material'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)