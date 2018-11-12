from django.forms import ModelForm
from .models import Fabricante, Cidade, Estado, Contato


class FabricanteForms(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['CNPJ', 'razao_social', 'nome_fantasia', 'logradouro', 'nome_do_logradouro', 'numero',
                  'complemento', 'bairro', 'cep', 'cidade']

class EstadoForms(ModelForm):
    class Meta:
        model = Estado
        fields = ['sigla', 'descrição']


class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['telefone', 'e_mail']