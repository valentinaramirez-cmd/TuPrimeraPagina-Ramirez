
from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm): 
    class Meta: 
        model = Pelicula 
        fields = "__all__"
        widgets = {
            'estreno' : forms.DateInput(attrs={'type' : 'date'})
        }