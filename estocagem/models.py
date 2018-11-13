from django.db import models
from core.models import Material


class PosiçãodeEstocagem(models.Model):
    TIPOS = (('1', 'INDIFERENTE'),
             ('2', 'VENCIMENTO'),
             ('3', 'PEPS'),
             ('4', 'UEPS')
               )
    endereço_setor = models.CharField(max_length=8, primary_key=True, verbose_name="endereço do setor",
                                      help_text="Atenção, valor deve ser único")
    nome_posição = models.CharField(max_length=20, verbose_name='nome/descrição do endereço')
    tipo_saida= models.CharField(max_length=2, choices=TIPOS, default=1, verbose_name='tipo de saída do material')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Posição de estocagem'
        verbose_name_plural = 'Posições de estocagem'
        unique_together = ['endereço_setor', 'material']

    def __str__(self):
        return self.nome_posição


