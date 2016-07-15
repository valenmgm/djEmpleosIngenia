from django.shortcuts import render

from . import modelsV
from contactoApp import modelsC
# Create your views here.

def renderVacantes(request):
    vacs = modelsV.Vacante.objects.filter(abierta = True)
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')
    data = {"vacantes":vacs, "contactoI":cIngenia}

    return render(request, 'vacantes.html', data)
