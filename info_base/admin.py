from django.contrib import admin

# Register your models here.
from . import modelsIB

admin.site.register(modelsIB.HomeIngenia)
admin.site.register(modelsIB.ImagenesHome)
admin.site.register(modelsIB.BeneficiosyPrestacione)
