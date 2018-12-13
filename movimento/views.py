from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from core.models import Material
from .models import RequisicaoMaterial, Requisicao, Devolucao, ItemDevolucao, Movimento, MovimentoMaterial
from .forms import RequisiçãoItensForm, RequisiçãoInfoForm, DevolucaoForm, DevolucaoItemForm, MovimentoItemForm


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
                    except Exception as e:
                        return HttpResponse(e)
                    return redirect('requisita_new', requisição.id)

                if item:
                    requisição.save()
                    return redirect('requisicao')
                else:
                    return HttpResponse('Requisição não contém materiais')
                return redirect('home')
    else:
        if form_info.is_valid():
            info = True
            if form_item.is_valid():
                material = form_item.save(commit=False)
                requisição.save()
                material.requisicao = requisição
                material.save()
                item = True
                return redirect('requisita_new', requisição.id )
    if kwargs:
        id = kwargs['id']
        material_list = RequisicaoMaterial.objects.filter(requisicao=id)
        info = True
        return render(request, 'requisita_material.html', {'form_info': form_info, 'form_item': form_item,
                                                           'material_list': material_list, 'info': info,
                                                           'requisicao':id})
    return render(request, 'requisita_material.html', {'form_info': form_info, 'form_item': form_item,
                                                       'info': info})


@login_required
def remove_item(request, id):
    item = RequisicaoMaterial.objects.get(id=id)
    requisicao = item.requisicao
    item.delete()

    return redirect('requisita_new', requisicao.id)


@login_required
def cancela_requisição(request, id):
    requisicao = Requisicao.objects.get(id=id)
    materiais = RequisicaoMaterial.objects.filter(requisicao=id)
    for m in materiais:
        m.delete()
    requisicao.delete()

    return redirect('home')


@login_required
def atende_requisição(request, id):
    try:
        requisicao = Requisicao.objects.get(id=id)
        requisicao_itens = RequisicaoMaterial.objects.filter(requisicao=id)
    except:
        resposta = "Não foram localizadas requisições ou itens, tente novamente."
        return render(request, '', {'resposta': resposta})
    if requisicao.situação != 'F':
        mov = Movimento.objects.create(usuário=request.user, tipo_de_movimento='S')
        for item in requisicao_itens:
            material = Material.objects.get(id=item.material.id)
            material.quantidade -= item.quantidade
            material.save()
            mov_mat = MovimentoMaterial.objects.create(movimento=mov, material=material, quatidade=item.quantidade,
                                                       motivo="requição")
            mov_mat.save()

        requisicao.situação = 'F'
        requisicao.save()
        return render(request, 'requisicao_atendida_success.html', {'requisicao': requisicao,
                                                                    'itens': requisicao_itens})
    else:
        return HttpResponse('Requisição já atendida!')



@login_required
def lista_requisicoes_nao_atendidas(request):
    requisicoes = Requisicao.objects.exclude(situação__startswith='F')
    itens = len(requisicoes)

    return render(request, 'list_nao_atendidos.html', {'requisicoes': requisicoes, 'itens':itens})


@login_required
def exibe_requisicao_atendimento(request, id):
    try:
        requisicao = Requisicao.objects.get(id=id)
        requisicao_itens = RequisicaoMaterial.objects.filter(requisicao=id)
    except:
        resposta = "Não foram localizadas requisições ou itens, tente novamente."
        return render(request, '', {'resposta': resposta})

    bad_item = False
    equal_item = False
    check_qtd = check_quantidade(id)
    itens_menor = check_qtd[0]
    bad_item = check_qtd[1]
    itens_iguais = check_qtd[2]
    equal_item = check_qtd[3]

    return render(request, 'atendimento_de_requisicao.html', {'requisicao': requisicao,
                                                              'requisicao_itens': requisicao_itens,
                                                              'itens_menor': itens_menor, 'bad_item': bad_item,
                                                              'itens_iguais': itens_iguais, 'equal_item': equal_item})


def check_quantidade(id):
    req_item = RequisicaoMaterial.objects.filter(requisicao=id)
    qtd_menor = []
    qtd_igual = []
    bad_item = False
    equal_item = False

    for item in req_item:
        mat = Material.objects.get(id=item.material.id)
        if item.quantidade > mat.quantidade:
            qtd_menor.append(item)
            bad_item = True

        if item.quantidade == mat.quantidade:
            qtd_igual.append(item)
            equal_item = True

    return qtd_menor, bad_item, qtd_igual, equal_item


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
                        material.save()
                        item = True
                        return redirect('devolucao', devolucao.id)
                    except:
                        return HttpResponse('Item já adicionado, não é permitido adicionar outro')

                if item:
                    devolucao.save()
                    return redirect('requisicao')
                else:
                    return HttpResponse('Requisição não contém materiais')
                return redirect('home')
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
        devolucao = kwargs['id']
        material_list = ItemDevolucao.objects.filter(devolução=id)
        dev = True
        movimento = registra_movimento_devolucao(material_list, request.user)
        return render(request, 'devolve_material.html', {'form_devolucao': form_devolucao, 'form_item': form_item,
                                                         'material_list': material_list,
                                                         'dev': dev, 'devolucao': devolucao})
    return render(request, 'devolve_material.html', {'form_devolucao': form_devolucao, 'form_item': form_item,
                                                     'dev': dev})


@login_required
def remove_item_dev(request, id):
    item = ItemDevolucao.objects.get(id=id)
    dev = item.devolução
    item.delete()

    return redirect('devolucao', dev.id)


@login_required
def cancela_dev(request, id):
    dev = Devolucao.objects.get(id=id)
    itens = ItemDevolucao.objects.filter(devolução=dev)
    for m in itens:
        m.delete()
    dev.delete()

    return redirect('home')


@login_required
def descarte(request):
    form = MovimentoItemForm(request.POST or None)

    if form.is_valid():
        movimento = Movimento.objects.create(usuário=request.user, tipo_de_movimento='P')
        quantidade = form.cleaned_data['quatidade']
        motivo = form.cleaned_data['motivo']
        item = form.save(commit=False)
        item.movimento = movimento
        item.material.quantidade -= quantidade
        item.material.save()
        mov = registra_movimento(movimento, item.material, quantidade, motivo)
        item.save()
        return redirect('descarte')

    return render(request, 'descarte.html', {'form':form})

@login_required
def decremento(request):
    form = MovimentoItemForm(request.POST or None)

    if form.is_valid():
        movimento = Movimento.objects.create(usuário=request.user, tipo_de_movimento='S')
        quantidade = form.cleaned_data['quatidade']
        motivo = form.cleaned_data['motivo']
        item = form.save(commit=False)
        item.movimento = movimento
        item.material.quantidade -= quantidade
        item.material.save()
        mov = registra_movimento(movimento, item.material, quantidade, motivo)
        item.save()
        return redirect('descarte')

    return render(request, 'decremento.html', {'form': form})


@login_required
def localiza_requisicao(request):
    id = request.GET.get('id', None)
    name = request.GET.get('user', None)
    date = request.GET.get('data', None)
    if id:
        try:
            requisicao = Requisicao.objects.get(id=id)
        except:
            resposta = 'Não há requisições para id nº ' + id
            return render(request, 'localiza_requisicao.html', {'resposta': resposta})

        return render(request, 'localiza_requisicao.html', {'requisicao_id': requisicao})

    if name:
        requisicao = Requisicao.objects.filter(usuario__first_name=name)
        if len(requisicao) == 0:
            resposta = 'Não há requisições para ' + name
            return render(request, 'localiza_requisicao.html', {'resposta': resposta})

        return render(request, 'localiza_requisicao.html', {'requisicao_name': requisicao})

    if date:
        requisicao = Requisicao.objects.filter(data=date)
        if len(requisicao) == 0:
            date = datetime.strptime(date, '%Y-%m-%d')
            resposta = 'Não há requisições em ' + date.strftime('%d/%m/%Y')
            return render(request, 'localiza_requisicao.html', {'resposta': resposta})
        return render(request, 'localiza_requisicao.html', {'requisicao_data': requisicao})

    return render(request, 'localiza_requisicao.html')


def registra_movimento_devolucao(material, user):
    mov = Movimento.objects.create(usuário=user, tipo_de_movimento='E')

    for m in material:
        item = MovimentoMaterial.objects.create(movimento=mov, material=m.material, quatidade=m.quantidade,
                                                motivo="Devolução")

    s = "Success"

    return s


def registra_movimento(mov, material, quantidade, motivo):
    item = MovimentoMaterial(movimento=mov, material=material, quatidade=quantidade, motivo=motivo)
    return item

