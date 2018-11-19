from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PosiçãodeEstocagem
from .forms import PosicaoForm, VinculaMaterialForm
from core.models import Material

@login_required
def list_posicoes(request):
    posicoes = PosiçãodeEstocagem.objects.all()
    return render(request, 'list_posicao.html', {'posicoes': posicoes})


@login_required
def cadastra_posicao(request):
    form = PosicaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        endereco = form.cleaned_data['endereco_setor']
        endereco = str(endereco).upper()
        form.save()
        posicao = PosiçãodeEstocagem.objects.get(endereco_setor=endereco)
        return redirect('vincula_material', posicao.id)
    return render(request, 'nova_posicao.html', {'form': form})

@login_required
def vincula_material(request, id):
    posicao = PosiçãodeEstocagem.objects.get(id=id)
    form = VinculaMaterialForm(request.POST or None, request.FILES or None)
    materiais = Material.objects.all()
    if form.is_valid():
        material = form.cleaned_data['material']
        mat_object = Material.objects.get(nome=material)
        posicao.material = mat_object
        posicao.save()
        form.save()
    list_material = []
    for material in materiais:
        try:
            item = PosiçãodeEstocagem.objects.get(id=id, material=material.id)
            list_material.append(item)
        except:
            pass
    return render(request, 'vincula.html', {'form': form, 'posicao': posicao, 'list_material': list_material})