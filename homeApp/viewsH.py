 # -*- coding : utf-8 -*-
from django.shortcuts import render
from djEmpleosIngenia.settings import MEDIA_ROOT

# Create your views here.
from vacantesApp import modelsV
from contactoApp import modelsC
from . import modelsH

def renderHome(request):
    info_1 = modelsH.InfoIngenia.objects.get(seccion="info_1")
    info_2 = modelsH.InfoIngenia.objects.get(seccion="info_2")
    info_3 = modelsH.InfoIngenia.objects.get(seccion="info_3")
    info_intro = modelsH.InfoIngenia.objects.get(seccion="info_intro")

    imagen_1 = modelsH.ImagenesHome.objects.get(seccion='imagen_1')
    imagen_2 = modelsH.ImagenesHome.objects.get(seccion='imagen_2')
    imagen_3 = modelsH.ImagenesHome.objects.get(seccion='imagen_3')

    vacantes = modelsV.Vacante.objects.filter(abierta = True)
    beneficios = modelsH.BeneficiosyPrestacione.objects.all()
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')

    data = {"info_1":info_1,
            "info_2":info_2,
            "info_3":info_3,
            "info_intro":info_intro,
            "imagen_1":imagen_1.imagen,
            "imagen_2":imagen_2.imagen,
            "imagen_3":imagen_3.imagen,
            "Vacantes":vacantes,
            "contactoI":cIngenia,
            }

    return render(request, 'home.html', data)
