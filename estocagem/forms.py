from django.forms import ModelForm
from .models import PosiçãodeEstocagem, VinculaPosicao


class PosicaoForm(ModelForm):
    class Meta:
        model = PosiçãodeEstocagem
        fields = ['endereco_setor', 'nome_posicao', 'tipo_saida']


class VinculaMaterialForm(ModelForm):
    class Meta:
        model = VinculaPosicao
        fields = ['material']
