from django.urls import path
from .views import login, logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
]