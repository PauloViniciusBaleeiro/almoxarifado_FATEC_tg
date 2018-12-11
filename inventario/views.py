from django.shortcuts import render, redirect
from core.models import TipodeMaterial
from .models import Inventario, ItemIventario, Material
from core.models import TipodeMaterial
from django.contrib.auth.decorators import login_required
from .forms import InventarioForm, ItemInventarioForm


def lista_material(tipo):
    materiais = Material.objects.filter(tipo_de_material=tipo)

    return materiais

@login_required
def criar_inventario(request):
    form = InventarioForm(request.POST or None)

    if form.is_valid():
        inventario = form.save()
        inventario.save()
        return redirect('inventario_1', inventario.id)

    return render(request, 'inventario.html', {'form':form})


@login_required
def escolha(request, id):
    inventario = Inventario.objects.get(id=id)
    tipos = TipodeMaterial.objects.all()

    # escolha = request.GET.get('escolha', None)
    #
    # if escolha:
    #     print('passou aqui')
    #     materiais = Material.objects.filter(tipo_de_material__descricao=escolha)
    #     for mat in materiais:
    #         item_inventario = ItemIventario.objects.create(inventario=inventario, material=mat)
    #     materials = ItemIventario.objects.filter(inventario=inventario)
    #     return render(request, 'inventario_2.html', {'inventario': inventario, 'escolha':escolha,
    #                                                  'materials': materials})
    return render(request, 'inventario_1.html', {'inventario': inventario, 'tipos':tipos})


@login_required
def inventario_lista(request, id, escolha):
    inventario = Inventario.objects.get(id=id)

    materiais = Material.objects.filter(tipo_de_material__descricao=escolha)

    for mat in materiais:
        itens_inventario = ItemIventario.objects.create(inventario=inventario, material=mat)

    materials = ItemIventario.objects.filter(inventario=inventario, material__tipo_de_material__descricao=escolha)
    print(materials)

    return render(request, 'inventario_2.html', {'inventario':inventario, 'escolha':escolha, 'materials':materials})



