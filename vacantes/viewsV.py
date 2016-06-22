from django.shortcuts import render

from . import modelsV
# Create your views here.

def renderVacantes(request):
    vacs = modelsV.Vacante.objects.filter(abierta = True)
    data = {"vacantes":vacs}

    return render(request, 'vacantes.html', data)
