from django.db import models

from django.db import models


class Vivienda(models.Model):
    tipo = models.CharField(max_length=50)
    zona = models.CharField(max_length=50)
    ndormitorios = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tamano = models.IntegerField()
    extras = models.CharField(max_length=255)
    foto_url = models.URLField()

class LNPatron(models.Model):
    patron = models.CharField(max_length=255)
    consultasql = models.CharField(max_length=255)

class LNDiccionario(models.Model):
    patron = models.CharField(max_length=50)
    campo = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50, null=True, blank=True)

