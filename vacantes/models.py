from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Vacante(models.Model):
    #Atributos
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    sueldo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Requisito(models.Model):
    #Atributos
    titulo = models.CharField(max_length=120)
    contendio = models.TextField()
    #Relations
    requisito_de = models.ForeignKey(Vacante)

    def __str__(self):
        return self.titulo
