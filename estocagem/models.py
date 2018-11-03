from django.db import models
from core.models import Material


class PosiçãodeEstocagem(models.Model):
    TIPOS = (('1', 'INDIFERENTE'),
             ('2', 'VENCIMENTO'),
             ('3', 'PEPS'),
             ('4', 'UEPS')
               )
    endereço_setor = models.CharField(max_length=8, primary_key=True)
    nome_posição = models.CharField(max_length=20)
    tipo_saida= models.CharField(max_length=2, choices=TIPOS, default=1)

    class Meta:
        verbose_name = 'Posição de estocagem'
        verbose_name_plural = 'Posições de estocagem'

    def __str__(self):
        return self.nome_posição


class PosiçãodeEstocagemMaterial(models.Model):
    endereço_setor = models.ForeignKey(PosiçãodeEstocagem, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Posição de estocagem - Material'
        verbose_name_plural = 'Posições de estocagem - Materiais'

    def __str__(self):
        return self.endereço_setor + ' - ' + self.material
