from django import forms
from .models import Libro

class LibroForm(forms.ModelForm): 
    class Meta: 
        model = Libro 
        fields = "__all__"
        widgets = {
            'fecha_publicacion' : forms.DateInput(attrs={'type' : 'date'})
        }