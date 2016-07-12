from django.shortcuts import render
from djEmpleosIngenia.settings import MEDIA_ROOT

# Create your views here.
from vacantes import modelsV
from . import modelsIB

def renderHome(request):
    homeIntro = modelsIB.HomeIngenia.objects.get(titulo="home_intro")
    homeQuienesSomos = modelsIB.HomeIngenia.objects.get(titulo="home_quienes_somos")
    homePorQueIngenia = modelsIB.HomeIngenia.objects.get(titulo="home_por_que_ingenia")

    imagenIntro = modelsIB.ImagenesHome.objects.get(seccion='imagen_intro')
    imagenAlgunosP = modelsIB.ImagenesHome.objects.get(seccion='imagen_nuestros_proyectos')
    imagenSketch = modelsIB.ImagenesHome.objects.get(seccion='imagen_sketch_servicio')

    vacantes = modelsV.Vacante.objects.filter(abierta = True)
    beneficios = modelsIB.BeneficiosyPrestacione.objects.all()

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
