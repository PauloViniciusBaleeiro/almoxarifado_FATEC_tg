from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from movimento.models import Movimento, MovimentoMaterial, Material
from datetime import datetime


@login_required
def movimentacoes_rel(request):
    now = datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    data = str(dia)+ "/"+ str(mes) + '/' + str(ano)
    movimentos = MovimentoMaterial.objects.all().order_by('-movimento__data_do_movimento')
    resp = request.user
    return render(request, 'movimentacoes.html', {'movimentos': movimentos, 'resp': resp, 'data': data})

@login_required
def estoque(request):
    now = datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    data = str(dia) + "/" + str(mes) + '/' + str(ano)
    materiais = Material.objects.all().order_by('nome')
    resp = request.user
    return render(request, 'estoque.html', {'materiais': materiais, 'resp': resp, 'data': data})

@login_required
def perdas_avarias(request):
    now = datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    data = str(dia) + "/" + str(mes) + '/' + str(ano)
    resp = request.user
    movimentos = Movimento.objects.filter(tipo_de_movimento__startswith='A') | Movimento.objects.filter(tipo_de_movimento__contains='P')
    materiais = []
    for m in movimentos:
        mat = MovimentoMaterial.objects.get(movimento=m)
        materiais.append(mat)
    return render(request, 'perdas_avarias.html', {'materiais': materiais, 'resp': resp, 'data': data})

