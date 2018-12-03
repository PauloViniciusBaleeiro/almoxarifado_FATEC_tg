from django import forms
from django.forms import ModelForm
from .models import Movimento, MovimentoMaterial, RequisicaoMaterial, Requisicao, Devolucao, ItemDevolucao
from core.models import Material


class RequisiçãoInfoForm(ModelForm):
    class Meta:
        model = Requisicao
        fields = ['usuario']


class RequisiçãoItensForm(ModelForm):
    class Meta:
        model = RequisicaoMaterial
        exclude = ['requisicao']


class DevolucaoForm(ModelForm):
    class Meta:
        model = Devolucao
        fields = ['usuario']


class DevolucaoItemForm(ModelForm):
    class Meta:
        model = ItemDevolucao
        exclude = ['devolução']


class MovimentoForm(ModelForm):
    class Meta:
        model = Movimento


class MovimentoItemForm(ModelForm):
    class Meta:
        model = MovimentoMaterial
        exclude = ['movimento']
