from django.db import models
from core.models import Material
from django.contrib.auth.models import User


class Inventario(models.Model):
    data = models.DateField(verbose_name='data de realização', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class ItemIventario(models.Model):
    registro_de_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=3)
