from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    Nombre = models.CharField( max_length=200, null=None)
    Costo_presupuestado = models.BigIntegerField()
    Costo_real = models.BigIntegerField()
    Tienda = models.CharField(max_length=200)
    Notas = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre

    def sumar (self):
        sum(Costo_presupuestado)
        return sumar