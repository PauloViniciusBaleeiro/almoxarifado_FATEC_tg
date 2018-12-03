from django.db import models
from core.models import Material
from django.contrib.auth.models import User


class Movimento(models.Model):
    TIPOS = (
        ('E', 'entrada'),
        ('S', 'saída'),
        ('P', 'perda'),
        ('A', 'avaria')
    )
    data_do_movimento = models.DateField(auto_now=True, editable=False)
    usuário = models.ForeignKey(User, on_delete=models.PROTECT)
    tipo_de_movimento = models.CharField(choices=TIPOS, max_length=10)

    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentos'


class MovimentoMaterial(models.Model):
    movimento = models.ForeignKey(Movimento, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=20)
    quatidade = models.FloatField()

    class Meta:
        verbose_name = 'Movimento - material'
        verbose_name_plural = 'Movimento-material'
        unique_together = ['movimento', 'material']


class Devolucao(models.Model):
    data = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Devolução'
        verbose_name_plural = "Devoluções"


class ItemDevolucao(models.Model):
    devolução = models.ForeignKey(Devolucao, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=30)
    quantidade = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Item - Devoluçaõ'
        verbose_name_plural = 'Itens - devoluções'
        unique_together = ['devolução', 'material']


class Requisicao(models.Model):
    SITUAÇÃO = (
        ('A', 'ABERTO'),
        ('PA', 'PARCIALMENTE ATENDIDA'),
        ('F', 'FECHADA')
    )
    data = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    situação = models.CharField(choices=SITUAÇÃO, max_length=10)

    class Meta:
        verbose_name = 'requisição'
        verbose_name_plural = 'requisições'


class RequisicaoMaterial(models.Model):
    CHOICES = (
        ('1', 'Desjejum'),
        ('2', 'Almoço'),
        ('3', "Café da tarde"),
        ('4', 'Jantar'),
        ('5', 'Lanche noturno')
    )
    requisicao = models.ForeignKey(Requisicao, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    serviço = models.CharField(max_length=30, choices=CHOICES, help_text='almoço, jantar, desejum...')
    quantidade = models.FloatField(default=0, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'requisições - materiais'
        unique_together = ['requisicao', 'material']

