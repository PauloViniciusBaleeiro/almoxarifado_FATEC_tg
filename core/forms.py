from django import forms
from django.forms import ModelForm
from .models import Fabricante, Cidade, Estado, Contato, Material, TipodeMaterial, EntradaDeMaterial


class FabricanteForms(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['CNPJ', 'razao_social', 'nome_fantasia', 'logradouro', 'nome_do_logradouro', 'numero',
                  'complemento', 'bairro', 'cep', 'cidade']

class EstadoForms(ModelForm):
    class Meta:
        model = Estado
        fields = ['sigla', 'descricao']


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['telefone', 'e_mail']


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = ['quantidade']


class TipodeMaterialForm(ModelForm):
    class Meta:
        model = TipodeMaterial
        fields = ['descricao']


class EntradaMaterialForm(ModelForm):
    quantidade = forms.FloatField(label='quantidade')

    class Meta:
        model = EntradaDeMaterial
        fields = ['material', 'lote', 'nota_fiscal', 'data_de_fabricacao', 'data_de_validade', 'fabricante',
                  'quantidade']

