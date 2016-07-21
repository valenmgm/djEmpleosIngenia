from django.shortcuts import render

from . import modelsI

from contactoApp.modelsC import ContactoIngenia
# Create your views here.

def renderIngenia(request):

    data = {}

    for info in modelsI.IngeniaInfo.objects.all():
        referencia = info.seccion
        objeto = modelsI.IngeniaInfo.objects.get(seccion = referencia)
        data[referencia] = objeto

    for imagen in modelsI.IngeniaImagen.objects.all():
        referencia = imagen.seccion
        objeto = modelsI.IngeniaImagen.objects.get(seccion = referencia)
        data[referencia] = objeto

    data["contactoI"] = ContactoIngenia.objects.latest('fecha')

    return render(request, 'ingenia.html', data)
