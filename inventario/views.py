from django.shortcuts import render, redirect
from core.models import TipodeMaterial
from .models import Inventario, ItemIventario, Material
from core.models import TipodeMaterial
from django.contrib.auth.decorators import login_required
from .forms import InventarioForm, ItemInventario_1Form, ItemInventario_2Form, ItemInventario_3Form


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
    materials = ItemIventario.objects.filter(inventario=inventario, material__tipo_de_material__descricao=escolha)
    # materials_2 = ItemIventario.objects.filter(inventario=inventario, material__tipo_de_material__descricao=escolha,
    #                                            contagem=2)
    # materials_3 = ItemIventario.objects.filter(inventario=inventario, material__tipo_de_material__descricao=escolha,
    #                                            contagem=3)
    if len(materials) == 0:
        materiais = Material.objects.filter(tipo_de_material__descricao=escolha)
        for mat in materiais:
            itens_inventario = ItemIventario.objects.create(inventario=inventario, material=mat)

        materials = ItemIventario.objects.filter(inventario=inventario,
                                                   material__tipo_de_material__descricao=escolha)

    # if len(materials_2) == 0:
    #     materiais = Material.objects.filter(tipo_de_material__descricao=escolha)
    #     for mat in materiais:
    #         itens_inventario = ItemIventario.objects.create(inventario=inventario, material=mat, contagem=2)
    #
    #     materials_2 = ItemIventario.objects.filter(inventario=inventario,
    #                                                material__tipo_de_material__descricao=escolha, contagem=2)
    #
    # if len(materials_3) == 0:
    #     materiais = Material.objects.filter(tipo_de_material__descricao=escolha)
    #     for mat in materiais:
    #         itens_inventario = ItemIventario.objects.create(inventario=inventario, material=mat, contagem=3)
    #
    #     materials_3 = ItemIventario.objects.filter(inventario=inventario,
    #                                                material__tipo_de_material__descricao=escolha, contagem=3)


    return render(request, 'inventario_2.html', {'inventario':inventario, 'escolha':escolha, 'materials':materials})


@login_required
def lanca_contagem(request, inventario, material):

    mat = ItemIventario.objects.get(id=material)
    form1 = ItemInventario_1Form(request.POST or None, instance=mat)
    form2 = ItemInventario_2Form(request.POST or None, instance=mat)
    form3 = ItemInventario_3Form(request.POST or None, instance=mat)
    print(mat)
    c1 = False
    c2 = False
    c3 = False

    if mat.contagem_1 is None:
        c1 = True
    elif mat.contagem_2 is None:
        c1 = False
        c2 = True
    elif mat.contagem_3 is None:
        c1 = False
        c2 = False
        c3 = True
    if request.method == 'POST':
        if c1:

            if form1.is_valid():
                    form1.save()
                    return redirect('inventario_2', mat.inventario.id, 'Descartável')

        if c2:
            if form2.is_valid():
                form2.save()
                return redirect('inventario_2', mat.inventario.id, 'Descartável')

        if c3:
            if form3.is_valid():
                form3.save()
                return redirect('inventario_2', mat.inventario.id, 'Descartável')

    return render(request, 'lanca_contagem.html', {'form1': form1, 'form2': form2, 'form3': form3, 'mat':mat,
                                                   'c1':c1, 'c2':c2, 'c3': c3})


@login_required
def inventario_delete(request, id):
    inventario = Inventario.objects.get(id=id)

    inventario.delete()

    return redirect('inventario')


@login_required
def lista_inventario(request):
    inventarios = Inventario.objects.all().order_by('-data')

    return render(request, 'lista_inventarios.html', {'inventarios': inventarios})
