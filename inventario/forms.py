from django.forms import ModelForm
from .models import ItemIventario, Inventario


class InventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'


class ItemInventario_1Form(ModelForm):
    class Meta:
        model = ItemIventario
        fields = ['contagem_1']


class ItemInventario_2Form(ModelForm):
    class Meta:
        model = ItemIventario
        fields = ['contagem_2']


class ItemInventario_3Form(ModelForm):
    class Meta:
        model = ItemIventario
        fields = ['contagem_3']

