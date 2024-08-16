from django.shortcuts import render, redirect
from m7_python.models import *
from m7_python.forms import *
from .models import Inmuebles, Tipo_user, Tipo_inmueble, Region, Comuna
from .forms import FiltroInmuebleForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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

def registerView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user=' + form.cleaned_data['username'])
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})


def register_tipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            
            # Verifica si el usuario existe
            user = User.objects.filter(username=username).first()
            if not user:
                return render(request, 'registration/register_tipo.html', {'form': form, 'error': 'Usuario no encontrado'})
            
            # Verifica si el tipo de usuario existe
            tipo_user = Tipo_user.objects.filter(id=int(tipo)).first()
            if not tipo_user:
                return render(request, 'registration/register_tipo.html', {'form': form, 'error': 'Tipo de usuario no encontrado'})
            
            # Guarda los datos en el modelo Profile
            dato = Profile(user=user, id_tipo_user=tipo_user, rut=rut, direccion=direccion, telefono=telefono)
            dato.save()
            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()
    
    return render(request, 'registration/register_tipo.html', {'form': form})


@login_required
def dashboardView(request): 
    return render(request, 'dashboard.html', {})


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=profile)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard')
    else:
        u_form = UserUpdateForm(instance=profile)
    
    context = {'u_form': u_form}
    return render(request, 'registration/update_profile.html', context)




