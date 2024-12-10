from django.shortcuts import redirect, render
from .forms import LibroForm
from .models import Libro

# Create your views here.
def listar_libros(request): 
    libros = Libro.objects.all()
    context = {'libros' : libros}
    return render (request, 'applibros/listar_libros.html', context) 

def crear_libro(request): 
    if request.method == 'POST' : 
        form = LibroForm(request.POST)

        if form.is_valid(): 
            form.save()
            return redirect('applibros:listar_libros')
    else: 
        form = LibroForm()

    return render(request, 'applibros/crear_libro.html', {'form' : form})


