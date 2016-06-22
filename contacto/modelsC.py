from __future__ import unicode_literals

from django.db import models
from vacantes import modelsV
# Create your models here.
def path_and_rename(instance, filename):
    vac_relacionada = modelsV.Vacante.objects.get(id=aplica_a)
    straplica_a = vac_relacionada.nombre
    return '{0}/{1}'.format(straplica_a, nombre+"CV")

class ContactoIngenia(models.Model):
    nombre_compania = models.CharField(max_length=30, default="Ingenia")
    direccion = models.CharField(max_length=140, default=" Anatole France 311 - Polanco, Mexico D.F. ")
    telefono = models.CharField(max_length=50, default="+51 (55) 50 2209 0000")
    correo = models.EmailField(blank=True)
    fecha = models.DateField(auto_now=True)
    def __str__(self):
        return ("Info " + str(self.fecha))

class ContactoAplicante(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    SEXO_CHOICES= (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=14)
    straplica_a = ''
    aplica_a = models.ForeignKey(modelsV.Vacante, limit_choices_to={'abierta': True}, on_delete=models.PROTECT)
    cv = models.FileField(upload_to=path_and_rename, blank = True)

    def __str__(self):
        info = modelsV.Vacante.objects.get(id=aplica_a)
        return str(self.nombre) + straplica_a


class ContactoInteresado(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    mensaje = models.TextField()    
