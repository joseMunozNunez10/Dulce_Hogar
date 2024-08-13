from django import forms
from .models import Inmuebles, Tipo_user, Tipo_inmueble, Comuna, Region

class FiltroInmuebleForm(forms.Form):
    tipo_user = forms.ModelChoiceField(queryset=Tipo_user.objects.all(), required=False)
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_inmueble.objects.all(), required=False)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
