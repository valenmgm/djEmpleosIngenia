from __future__ import unicode_literals

from django.db import models
from djEmpleosIngenia.settings import MEDIA_ROOT
# Create your models here.
class HomeIngenia(models.Model):
    HOME_CHOICES = (
        ("info_1","Info 1"),
        ("info_2","Info 2"),
        ("info_3","Info 3"),
    )
    titulo = models.CharField(max_length=40, choices=HOME_CHOICES)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


def path_and_rename(instance, filename):
    return '{0}/{1}/{2}'.format(MEDIA_ROOT,'imagenesHome', instance.seccion)

class ImagenesHome(models.Model):
    IMAGEN_CHOICES = (
        ("imagen_1","Imagen 1"),
        ("imagen_2","Imagen 2"),
        ("imagen_3","Imagen 3")
    )
    seccion = models.CharField(max_length=50, choices=IMAGEN_CHOICES)
    imagen = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.seccion


class BeneficiosyPrestacione(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
