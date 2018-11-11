from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FabricanteForms
from .models import Fabricante



def home(request):
    return render(request, 'home.html')


def logout(request):
    logout(request)
    return redirect('home')


@login_required
def listagem_fabricante(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'list_fabricantes.html', {'fabricantes': fabricantes})

@login_required
def novo_fabricante(request):
    form = FabricanteForms(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
