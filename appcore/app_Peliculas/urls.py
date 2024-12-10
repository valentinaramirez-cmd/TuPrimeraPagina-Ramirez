from django.urls import path 
from .views import listar_peliculas, crear_pelicula

app_name = 'app_Peliculas'

urlpatterns = {
    path('listar_peliculas/', listar_peliculas, name='listar_peliculas'),
    path('crear_pelicula/', crear_pelicula, name='crear_pelicula')
}