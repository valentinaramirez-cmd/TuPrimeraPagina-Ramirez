from django.db import models

# Create your models here.
class Album (models.Model): 
    titulo = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    duracion = models.DurationField()
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    discografia = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()