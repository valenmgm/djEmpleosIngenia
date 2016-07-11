from __future__ import unicode_literals

from django.db import models
from djEmpleosIngenia.settings import MEDIA_ROOT
# Create your models here.
class HomeIngenia(models.Model):
    HOME_CHOICES = (
        ("home_intro","Home Intro"),
        ("home_quienes_somos","Home Quienes Somos"),
        ("home_por_que_ingenia","Home Por Que Ingenia"),
    )
    titulo = models.CharField(max_length=40, choices=HOME_CHOICES)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


def path_and_rename(instance, filename):
    return '{0}/{1}/{2}'.format(MEDIA_ROOT,'imagenesHome', instance.seccion)

class ImagenesHome(models.Model):
    IMAGEN_CHOICES = (
        ("imagen_intro","Imagen Intro"),
        ("imagen_nuestros_proyectos","Imagen Algunos de Nuestros Projectos"),
        ("imagen_sketch_servicio","Imagen Sketch Servicio")
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
