from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from core.models import Material
from .models import RequisicaoMaterial, Requisicao, Devolucao, ItemDevolucao
from .forms import RequisiçãoItensForm, RequisiçãoInfoForm, DevolucaoForm, DevolucaoItemForm


@login_required
def requisita_material(request, **kwargs):
    form_item = RequisiçãoItensForm(request.POST or None)
    form_info = RequisiçãoInfoForm(request.POST or None)
    info = False
    item = False
    requisição = form_info.save(commit=False)

    if kwargs:
        id = kwargs['id']
        if id:
            instancia = Requisicao.objects.get(id=int(id))
            form_info = RequisiçãoInfoForm(request.POST or None, instance=instancia)
            requisição = form_info.save(commit=False)

            if form_info.is_valid():
                info = True
                if form_item.is_valid():
                    material = form_item.save(commit=False)
                    requisição.save()
                    try:
                        material.requisicao = requisição
                        material.save()
                        item = True
                        return redirect('requisicao', requisição.id)
                    except:
                        return HttpResponse('Item já adicionado, não é permitido adicionar outro')

                # if item:
                #     requisição.save()
                #     return redirect('requisicao')
                # else:
                #     return HttpResponse('Requisição não contém materiais')
                # return redirect('home')
    else:
        if form_info.is_valid():
            info = True
            if form_item.is_valid():
                material = form_item.save(commit=False)
                requisição.save()
                material.requisicao = requisição
                material.save()
                item = True
                return redirect('requisicao', requisição.id)
    if kwargs:
        material_list = RequisicaoMaterial.objects.filter(requisicao=id)
        info = True
        return render(request, 'requisita_material.html', {'form_info': form_info, 'form_item': form_item,
                                                           'material_list': material_list, 'info': info})
    return render(request, 'requisita_material.html', {'form_info': form_info, 'form_item': form_item,
                                                       'info': info})


@login_required
def lista_requisicoes_nao_atendidas(request):
    requisicoes = Requisicao.objects.exclude(situação__startswith='F')

    return render(request, 'list_nao_atendidos.html', {'requisicoes': requisicoes})


@login_required
def devolve_material(request, **kwargs):
    form_item = DevolucaoItemForm(request.POST or None)
    form_devolucao = DevolucaoForm(request.POST or None)
    dev = False
    item = False
    devolucao = form_devolucao.save(commit=False)

    if kwargs:
        id = kwargs['id']
        if id:
            instancia = Devolucao.objects.get(id=id)
            form_devolucao = DevolucaoForm(request.POST or None, instance=instancia)
            devolucao = form_devolucao.save(commit=False)

            if form_devolucao.is_valid():
                dev = True
                if form_item.is_valid():
                    material = form_item.save(commit=False)
                    devolucao.save()
                    try:
                        material.devolução = devolucao
                        print(material.devolução)
                        print(devolucao)
                        material.save()
                        item = True
                        return redirect('devolucao', devolucao.id)
                    except:
                        return HttpResponse('Item já adicionado, não é permitido adicionar outro')

                # if item:
                #     requisição.save()
                #     return redirect('requisicao')
                # else:
                #     return HttpResponse('Requisição não contém materiais')
                # return redirect('home')
    else:
        if form_devolucao.is_valid():
            dev = True
            if form_item.is_valid():
                material = form_item.save(commit=False)
                devolucao.save()
                material.devolução = devolucao
                material.save()
                item = True
                return redirect('devolucao', devolucao.id)
    if kwargs:
        material_list = ItemDevolucao.objects.filter(devolução=id)
        dev = True
        return render(request, 'devolve_material.html', {'form_devolucao': form_devolucao, 'form_item': form_item,
                                                         'material_list': material_list, 'dev': dev})
    return render(request, 'devolve_material.html', {'form_devolucao': form_devolucao, 'form_item': form_item,
                                                     'dev': dev})


@login_required
def descarte(request):
    pass