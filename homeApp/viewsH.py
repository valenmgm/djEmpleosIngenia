 # -*- coding : utf-8 -*-
from django.shortcuts import render
from djEmpleosIngenia.settings import MEDIA_ROOT

# Create your views here.
from vacantesApp import modelsV
from contactoApp import modelsC
from . import modelsH

def renderHome(request):

    vacantes = modelsV.Vacante.objects.filter(abierta = True)
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')

    data = {
            "Vacantes":vacantes,
            "contactoI":cIngenia,
            }

    return render(request, 'home.html', data)
