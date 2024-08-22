"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django import views
from django.contrib import admin 
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from m7_python.views import *
from django.contrib.auth.views import LoginView, LogoutView
from m7_python.views import dashboardView, registerView, register_tipoView, profile, new_inmuebleView
from m7_python import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='indice'),
    path('bienvenido/',bienvenido,name='bienvenido'),
    path('acerca/',acerca,name='acerca'),
    path('servicios/',servicios,name='servicios'),
    path('contactos/',contactos,name='contactos'),
    path('arriendos/',arriendos,name='arriendos'),
    path('ventas/',ventas,name='ventas'),
    path('login/', LoginView.as_view(next_page='dashboard'), name='login'),
    path('logout/', LogoutView.as_view(next_page='indice'), name='logout'),
    path('dashboard/', dashboardView, name='dashboard'),
    path('register/', registerView, name='register'),
    path('register_tipo/', register_tipoView, name='registerTipo'), 
    path('update_profile/', profile, name='update_profile'),
    path('new_inmueble/', views.new_inmuebleView, name='new_inmueble_url'),
    path('update_inmueble', views.inmueble_update, name='update_inmueble_url'),
    path('eliminar_inmueble', views.inmuebles_delete, name='delete_inmueble_url'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


