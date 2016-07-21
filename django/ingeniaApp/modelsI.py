from __future__ import unicode_literals

from django.db import models

from djEmpleosIngenia.settings import MEDIA_ROOT
import datetime

def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    return '{0}/{1}/{2}{3}{4}'.format(MEDIA_ROOT,'imagenesIngenia', str(datetime.date.today()), instance.seccion,"." + ext)

# Create your models here.
class IngeniaInfo(models.Model):
    HOME_CHOICES = (
        ("info_intro","Intro"),
        ("info_a1","Adicional 1"),
        ("info_p1","Pilar 1"),
        ("info_p2","Pilar 2"),
        ("info_p3","Pilar 3"),
        ("info_a2","Adicional 2"),
    )
    seccion = models.CharField(max_length=40, choices=HOME_CHOICES)
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo + " " +self.seccion

class IngeniaImagen(models.Model):
    IMAGEN_CHOICES = (
        ("imagen_intro","Imagen Intro"),
        ("imagen_a1","Imagen Adicional 1"),
        ("imagen_a2","Imagen Adicional 2"),
    )
    seccion = models.CharField(max_length=50, choices=IMAGEN_CHOICES)
    imagen = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.seccion
