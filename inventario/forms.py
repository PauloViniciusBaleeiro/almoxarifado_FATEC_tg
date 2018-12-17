from django.forms import ModelForm, DateInput
from .models import ItemIventario, Inventario, Material


class InventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields = ['data', 'user']
        widgets = {
            'data': DateInput(),
        }

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['tipo_de_material']

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

