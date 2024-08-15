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

