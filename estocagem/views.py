from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import PosiçãodeEstocagem, VinculaPosicao
from .forms import PosicaoForm, VinculaMaterialForm

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
def remover_posicao(request, id):
    try:
        posicao = PosiçãodeEstocagem.objects.get(id=id)
    except:
        return HttpResponse('Posição não encontrada!')
    if request.method == 'POST':
        posicao.delete()
        return redirect('list_posicoes')
    return render(request, 'del_posicao_confirma.html', {'posicao': posicao})

@login_required
def vincula_material(request, id):
    try:
        posicao = PosiçãodeEstocagem.objects.get(id=id)
        materiais = VinculaPosicao.objects.filter(posicao__id=id)
    except:
        return HttpResponse('Posição não encontrada!')
    form = VinculaMaterialForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        formulario = form.save()
        formulario.posicao = posicao
        try:
            formulario.save()
        except:
            return HttpResponse('Item já alocado!')
        return redirect('vincula_material', posicao.id)
    return render(request, 'vincula.html', {'form': form, 'posicao': posicao, 'materiais': materiais})