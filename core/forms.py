from django.forms import ModelForm
from .models import Fabricante


class FabricanteForms(ModelForm):
    class Meta:
        model = Fabricante
        fields = ['CNPJ', 'razao_social', 'nome_fantasia', 'logradouro', 'nome_do_logradouro', 'numero',
                  'complemento', 'bairro', 'cep', 'cidade']
