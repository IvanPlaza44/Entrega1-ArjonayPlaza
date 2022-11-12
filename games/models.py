from django.db import models
from datetime import datetime
# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    plataformas = models.CharField(max_length=30)
    precio = models.IntegerField()
    jugadores = models.IntegerField()
    lanzamiento = models.DateField()
    resumen = models.CharField(max_length=30)
    autor =models.CharField(max_length=30, null=True)
    fecha_de_creacion= models.DateTimeField(auto_now_add=True, null= True)
    def __str__(self):
        return f'{self.nombre} de {self.desarrollador} '