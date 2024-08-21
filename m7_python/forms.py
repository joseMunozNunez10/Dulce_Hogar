from django import forms
from django.contrib.auth.models import User
from .models import Inmuebles, Tipo_user, Tipo_inmueble, Comuna, Region
from django.contrib.auth.forms import UserCreationForm

class FiltroInmuebleForm(forms.Form):
    tipo_user = forms.ModelChoiceField(queryset=Tipo_user.objects.all(), required=False)
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_inmueble.objects.all(), required=False)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres')
    last_name = forms.CharField(label='Apellidos')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','username', 'email', 'password1', 'password2')

class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'), (2, 'Arrendador'))
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='Rut', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=100)  
    telefono = forms.CharField(label='Teléfono', max_length=100)       

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
            
class InmuebleForm(forms.Form):
    tipos = ((1, 'Casa'), (2, 'Departamento'), (3, 'Parcela'), (4, 'Estacionamiento'),(5, 'Otro'))
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas = [(x.id,x.comuna) for x in list(Comuna.objects.all())]

    def nombre_comuna(e):
        return e[1]
    comunas.sort(key=nombre_comuna)

    id_comuna = forms.ChoiceField(choices=comunas)
    regiones = [(x.id,x.region) for x in list(Region.objects.all())]
    id_region = forms.ChoiceField(choices=regiones)
    nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(label='Descripción del Inmueble', max_length=100)
    m2_construido = forms.CharField(label='M2 Construidos', max_length=100)
    numero_banos = forms.CharField(label='Numero de Banos', max_length=100)
    numero_hab = forms.CharField(label='Numero de Habitaciones', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=100)
    m2_terreno = forms.CharField(label='M2 Terreno', max_length=100)
    numero_est = forms.CharField(label='Numero de Estacionamientos', max_length=100)
    imagen = forms.ImageField()

class InmuebleUpdateForm(forms.ModelForm):
    class Meta:
        model = Inmuebles
        fields = ('nombre_inmueble', 'descripcion', 'm2_construido', 'numero_banos', 'numero_hab', 'direccion', 'm2_terreno', 'numero_est', 'imagen')  

