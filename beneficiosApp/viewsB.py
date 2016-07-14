from django.shortcuts import render

from . import modelsB
from contactoApp import modelsC
# Create your views here.

def renderBeneficios(request):
    bens = modelsB.BeneficiosyPrestacione.objects.all()
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')
    data = {'beneficios':bens, "contactoI":cIngenia}

    return render(request, 'beneficios.html', data)
