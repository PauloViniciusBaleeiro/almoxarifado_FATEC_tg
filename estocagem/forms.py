from django.forms import ModelForm
from .models import PosiçãodeEstocagem


class PosicaoForm(ModelForm):
    class Meta:
        model = PosiçãodeEstocagem
        fields = ['material', 'endereço_setor', 'nome_posição', 'tipo_saida']
