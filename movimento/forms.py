from django import forms
from django.forms import ModelForm
from .models import Movimento, MovimentoMaterial, RequisicaoMaterial, Requisicao
from core.models import Material


class RequisiçãoInfoForm(ModelForm):
    class Meta:
        model = Requisicao
        fields = ['usuario']


class RequisiçãoItensForm(ModelForm):
    class Meta:
        model = RequisicaoMaterial
        exclude = ['requisicao']

