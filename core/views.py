from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings


def home(request):
    return render(request, settings.BASE_DIR + '/templates/home.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('home')
