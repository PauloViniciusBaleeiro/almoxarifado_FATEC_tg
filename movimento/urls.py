from django.urls import path
from .views import requisita_material

urlpatterns = [
    path('requisita/', requisita_material, name='requisicao'),
    path('requisita/<int:id>', requisita_material, name='requisicao'),
]