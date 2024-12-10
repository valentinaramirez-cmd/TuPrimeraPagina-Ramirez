from django.db import models

# Create your models here.
class Pelicula (models.Model): 
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    genero = models.CharField(max_length=50)
    estreno = models.DateField()

    def __str__(self):
        return super().__str__()