from django.db import models
from core.models import Material
from django.utils.six import with_metaclass


class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)


class PosiçãodeEstocagem(models.Model):
    TIPOS = (('1', 'INDIFERENTE'),
             ('2', 'VENCIMENTO'),
             ('3', 'PEPS'),
             ('4', 'UEPS')
               )
    endereco_setor = UpperCaseCharField(max_length=8, unique=True, verbose_name="endereço do setor",
                                      help_text="Atenção, valor deve ser único")
    nome_posicao = models.CharField(max_length=20, verbose_name='nome/descrição do endereço')
    tipo_saida= models.CharField(max_length=2, choices=TIPOS, default=1, verbose_name='tipo de saída do material')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Posição de estocagem'
        verbose_name_plural = 'Posições de estocagem'
        unique_together = ['endereco_setor', 'material']

    def __str__(self):
        return self.nome_posicao


