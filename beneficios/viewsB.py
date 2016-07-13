from django.shortcuts import render

from . import modelsB
# Create your views here.

def renderBeneficios(request):
    bens = modelsB.BeneficiosyPrestacione.objects.all()
    data = {'beneficios':bens}

    return render(request, 'beneficios.html', data)
