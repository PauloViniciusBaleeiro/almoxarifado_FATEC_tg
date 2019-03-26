from django.db import models
from core.models import Material
from django.contrib.auth.models import User


class Inventario(models.Model):
    data = models.DateField(verbose_name='data de realização')
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'inventario'
        verbose_name_plural = 'inventarios'


class ItemIventario(models.Model):

    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    contagem_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Quantidade')
    contagem_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Quantidade')
    contagem_3 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Quantidade')


    class Meta:
        verbose_name = 'item de inventario'
        verbose_name_plural = 'itens de inventário'
        unique_together=['inventario', 'material']
