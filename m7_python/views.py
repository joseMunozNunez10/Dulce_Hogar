from django.shortcuts import render
from .models import Inmuebles, Tipo_user, Tipo_inmueble, Region, Comuna
from .forms import FiltroInmuebleForm


def inicio(request):
    tipos_usuario = Tipo_user.objects.all()
    tipos_inmueble = Tipo_inmueble.objects.all()
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    
    inmuebles = Inmuebles.objects.all()

    context = {
        'tipos_usuario': tipos_usuario,
        'tipos_inmueble': tipos_inmueble,
        'comunas': comunas,
        'regiones': regiones,
        'inmuebles': inmuebles,
    }
    
    return render(request, 'index.html', context)

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

