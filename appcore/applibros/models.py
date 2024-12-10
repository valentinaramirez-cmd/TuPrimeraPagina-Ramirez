from django.db import models

# Create your models here.

class Libro(models.Model): 
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=500)
    fecha_publicacion = models.DateField()

