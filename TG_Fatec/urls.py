"""TG_Fatec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
from estocagem import urls as posicao_urls
from movimento import urls as movimento_urls
from inventario import urls as inventario_urls
from django.contrib.auth import urls as auth_urls
from relatorios import urls as relatorios_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('', include(movimento_urls)),
    path('', include(inventario_urls)),
    path('users/', include(auth_urls)),
    path('', include(posicao_urls)),
    path('', include(relatorios_urls)),

]
