from django.shortcuts import redirect, render

from .forms import PeliculaForm
from .models import Pelicula

# Create your views here.
def listar_peliculas(request): 
    peliculas = Pelicula.objects.all()
    return render (request, 'listar_peliculas.html', {'peliculas' : peliculas}) 

def crear_pelicula(request): 
    if request.method == 'POST' : 
        form = PeliculaForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect ('app_Peliculas:listar_peliculas')
    else: 
        form = PeliculaForm()

    return render (request, 'crear_peliculas.html', {'form' : form})