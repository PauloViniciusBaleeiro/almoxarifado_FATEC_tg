from django.shortcuts import render
from core.models import TipodeMaterial
from .models import Inventario, ItemIventario, Material
from django.contrib.auth.decorators import login_required
from .forms import InventarioForm, ItemInventarioForm


def lista_material(tipo):
    materiais = Material.objects.filter(tipo_de_material=tipo)

    return materiais

@login_required
def inventario(request):

    inventario = Inventario.objects.create()

