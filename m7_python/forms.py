
from django import forms
from .models import Tipo_inmueble, Comuna, Region

class FiltroInmuebleForm(forms.Form):
    tipo_inmueble = forms.ModelChoiceField(
        queryset=Tipo_inmueble.objects.all(),
        required=False,
        empty_label="Todos los tipos"
    )
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        required=False,
        empty_label="Todas las comunas"
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        empty_label="Todas las regiones"
    )
    min_precio = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Precio mínimo'})
    )
    max_precio = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Precio máximo'})
    )
