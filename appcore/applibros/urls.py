from django.urls import path 
from .views import crear_libro, listar_libros

app_name = 'applibros'

urlpatterns = [
    path('listar_libros/', listar_libros, name='listar_libros'),
    path('crear_libro/', crear_libro, name='crear_libro')
] 