from django.urls import path
from .views import movimentacoes_rel, estoque, perdas_avarias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('relatorio/movimentacoes/', movimentacoes_rel, name='rel_movimentacoes'),
    path('relatorio/estoque/', estoque, name='estoque'),
    path('relatorio/perdas-avarias/', perdas_avarias, name='perdas_avarias'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)