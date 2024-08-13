from django.shortcuts import render
from .models import Inmuebles
from .forms import FiltroInmuebleForm


def inicio(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'acerca.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})

def servicios(request):
    return render(request, 'servicios.html', {})

def contactos(request):
    return render(request, 'contactos.html', {})

def arriendos(request):
    return render(request, 'arriendo.html', {})

def ventas(request):
    return render(request, 'venta.html', {})

