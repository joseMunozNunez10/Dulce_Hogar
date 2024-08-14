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

class MiFormulario(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
        required=True
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
        required=True
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        required=True
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmación de contraseña'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove any help_text from fields
        for field in self.fields.values():
            field.help_text = None