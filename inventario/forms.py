from django.forms import ModelForm
from .models import ItemIventario, Inventario


class InventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'


class ItemInventarioForm(ModelForm):
    class Meta:
        model = ItemIventario
        exclude = ['inventario', 'contagem']
