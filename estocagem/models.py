from django.db import models
from core.models import Material


class Posição_de_Estocagem(models.Model):
    TIPOS = (('1', 'INDIFERENTE'),
             ('2', 'VENCIMENTO'),
             ('3', 'PEPS'),
             ('4', 'UEPS')
               )
    endereço_setor = models.CharField(max_length=8, primary_key=True)
    nome_posição = models.CharField(max_length=20)
    tipo_saida= models.CharField(max_length=2, choices=TIPOS, default=1)

    def __str__(self):
        return self.nome_posição


class Posição_de_Estocagem_Material(models.Model):
    endereço_setor = models.ForeignKey(Posição_de_Estocagem)
    material = models.ForeignKey(Material)

    def __str__(self):
        return self.endereço_setor + ' - ' + self.material
