from django.shortcuts import render
from djEmpleosIngenia.settings import MEDIA_ROOT

# Create your views here.
from vacantes import modelsV
from . import modelsH

def renderHome(request):
    homeIntro = modelsH.HomeIngenia.objects.get(titulo="info_1")
    homeQuienesSomos = modelsH.HomeIngenia.objects.get(titulo="info_2")
    homePorQueIngenia = modelsH.HomeIngenia.objects.get(titulo="info_3")

    imagenIntro = modelsH.ImagenesHome.objects.get(seccion='imagen_1')
    imagenAlgunosP = modelsH.ImagenesHome.objects.get(seccion='imagen_2')
    imagenSketch = modelsH.ImagenesHome.objects.get(seccion='imagen_3')

    vacantes = modelsV.Vacante.objects.filter(abierta = True)
    beneficios = modelsH.BeneficiosyPrestacione.objects.all()

    data = {"homeIntro":homeIntro.contenido,
            "homeQuienesSomos":homeQuienesSomos.contenido,
            "homePorQueIngenia":homePorQueIngenia.contenido,
            "homeImagenIntro":imagenIntro.imagen,
            "homeImagenAlgunosProyetos":imagenAlgunosP.imagen,
            "homeImagenSketch":imagenSketch.imagen,
            "homeVacantes":vacantes,
            #"homeBeneficios":beneficios,
            "MEDIA_ROOT":MEDIA_ROOT,
            }

    return render(request, 'home.html', data)
