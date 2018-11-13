from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import (FabricanteForms, CidadeForm, EstadoForms, ContatoForm, MaterialForm, TipodeMaterialForm)
from .models import Fabricante, Contato, Material


def home(request):
    return render(request, 'home.html')


def logout(request):
    logout(request)
    return redirect('home')


@login_required
def listagem_fabricante(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'list_fabricantes.html', {'fabricantes': fabricantes})

@login_required
def novo_fabricante(request):
    form = FabricanteForms(request.POST or None, request.FILES or None)

    if form.is_valid():
        cnpj = form.cleaned_data['CNPJ']
        form.save()
        fabricante = Fabricante.objects.get(CNPJ=cnpj)
        return redirect('contato', fabricante.id)
    return render(request, 'novo_fabricante.html', {'form': form})

@login_required
def atualiza_fabricante(request, id):
    fabricante = get_object_or_404(Fabricante, pk=id)
    form = FabricanteForms(request.POST or None, request.FILES or None, instance=fabricante)

    if form.is_valid():
        form.save()
        return redirect('list_fabricantes')
    return render(request, 'novo_fabricante.html', {'form': form})

@login_required
def deletar_fabricante(request, id):
    fabricante = get_object_or_404(Fabricante, pk=id)
    if request.method == 'POST':
        fabricante.delete()
        return redirect('list_fabricantes')
    return render(request, 'del_fab_confirma.html', {'fabricante': fabricante})


@login_required
def cadastra_contato(request, id):
    try:
        fabricante = Fabricante.objects.get(id=id)
        contatos = Contato.objects.filter(fabricante__id=id)
    except:
        return HttpResponse('Fabricante não encontrado!')
    form = ContatoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        formulario = form.save()
        formulario.fabricante = fabricante
        formulario.save()
        return redirect('contato', fabricante.id)
    return render(request, 'novo_contato.html', {'form': form, 'fabricante':fabricante, 'contatos':contatos})

@login_required
def deleta_contato(request, id):
    contato = Contato.objects.get(id=id)
    fabricante_id = contato.fabricante.id
    contato.delete()
    return redirect('contato', fabricante_id)

@login_required
def cadastra_cidade(request):
    form = CidadeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'nova_cidade.html', {'form': form})

@login_required
def cadastra_estado(request):
    form = EstadoForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('nova_cidade')
    return render(request, 'novo_estado.html', {'form': form})

@login_required
def lista_material(request):
    materiais = Material.objects.all()
    return render(request, 'list_material.html', {'materiais': materiais})

@login_required
def cadastra_material(request):
    form = MaterialForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_material')
    return render (request, 'novo_material.html', {'form' : form})


@login_required
def cadastra_tipo_de_material(request):
    form = TipodeMaterialForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('novo_material')
    return render(request, 'novo_tipo_de_material.html', {'form': form})

@login_required
def altera_material(request, id):
    material = get_object_or_404(Material, pk=id)
    form = MaterialForm(request.POST or None, request.FILES or None, instance=material)

    if form.is_valid():
        form.save()
        return redirect('lista_material')
    return render(request, 'novo_material.html', {'form': form})

