from django.shortcuts import render

from . import modelsB
from contactoApp.modelsC import ContactoIngenia
# Create your views here.

def renderBeneficios(request):
    benscortos = modelsB.BeneficiosyPrestacionesCorto.objects.all()
    benslargos = modelsB.BeneficiosyPrestacionesLargo.objects.all()
    cIngenia = ContactoIngenia.objects.latest('fecha')
    data = {'beneficiosCortos':benscortos,
            'beneficiosLargos':benslargos,
            'contactoI':cIngenia}

    return render(request, 'beneficios.html', data)
