from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from core.models import Material
from .models import RequisicaoMaterial, Requisicao
from .forms import RequisiçãoItensForm, RequisiçãoInfoForm


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
                    except :
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
