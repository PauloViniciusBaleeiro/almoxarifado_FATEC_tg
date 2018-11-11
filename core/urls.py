from django.urls import path
from .views import home, logout, listagem_fabricante as list

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('fabricantes/', list, name='list_fabricantes')
]