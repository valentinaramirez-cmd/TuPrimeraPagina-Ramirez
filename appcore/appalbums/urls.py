from django.urls import path 
from .views import crear_album, listar_albums, buscar_album

app_name = 'appalbums'

urlpatterns = {
    path('listar_albums/', listar_albums, name='listar_albums'),
    path('crear_album/', crear_album, name='crear_album'), 
    path('buscar_album/', buscar_album, name='buscar_album')
}