from django.shortcuts import render

from . import modelsV
from contactoApp.modelsC import ContactoIngenia
# Create your views here.

def renderVacantes(request):
    vacs = modelsV.Vacante.objects.filter(abierta = True)
    cIngenia = ContactoIngenia.objects.latest('fecha')
    data = {"vacantes":vacs, "contactoI":cIngenia}

    return render(request, 'vacantes.html', data)
