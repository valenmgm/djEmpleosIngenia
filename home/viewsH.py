from django.shortcuts import render

# Create your views here.
from vacantes import modelsV

def renderHome(request):
    vacantes = modelsV.Vacante.objects.filter(abierta = True)
    return render(request, 'home.html', {'vacantes':vacantes})

def renderIngeniaInfo(request):
    return render(request, 'infoingenia.html')

def renderBeneficios(request):
    return render(request, 'beneficios.html')
