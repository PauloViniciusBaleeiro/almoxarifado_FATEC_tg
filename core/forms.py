from django.forms import ModelForm
from .models import Fabricante, Cidade, Estado, Contato, Material, TipodeMaterial


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
        fields = ['nome', 'descricao', 'unidade', 'quantidade', 'tipo_de_material', 'fabricante']


class TipodeMaterialForm(ModelForm):
    class Meta:
        model = TipodeMaterial
        fields = ['descricao']