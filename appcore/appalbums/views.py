from django.shortcuts import redirect, render

from .forms import AlbumForm
from .models import Album

# Create your views here.
def listar_albums(request): 
    albums = Album.objects.all()
    return render (request, 'listar_albums.html', {'albums' : albums}) 


def crear_album (request): 
    if request.method == 'POST' : 
        form = AlbumForm(request.POST)

        if form.is_valid() : 
            form.save()
            return redirect('app_albums:listar_albums')
    else: 
        form = AlbumForm()

    return render(request, 'crear_album.html', {'form' : form})


def buscar_album (request): 
    titulo = request.GET.get('buscar')
    albums = Album.objects.filter(titulo = titulo).values()
    return render(request, 'buscar_album.html', {'albums' : albums})