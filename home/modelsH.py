from __future__ import unicode_literals

from django.db import models

# Create your models here.
class infoIngenia(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
