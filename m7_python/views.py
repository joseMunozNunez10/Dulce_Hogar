from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'acerca.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})