from django.shortcuts import render

from . import modelsI

from contactoApp import modelsC
# Create your views here.

def renderIngenia(request):

    ii = modelsI.IngeniaInfo.objects.get(seccion = "info_intro")
    ia1 = modelsI.IngeniaInfo.objects.get(seccion = "info_a1")
    ip1 = modelsI.IngeniaInfo.objects.get(seccion = "info_p1")
    ip2 = modelsI.IngeniaInfo.objects.get(seccion = "info_p2")
    ip3 = modelsI.IngeniaInfo.objects.get(seccion = "info_p3")
    ia2 = modelsI.IngeniaInfo.objects.get(seccion = "info_a2")

    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')

    data = {
        "info_intro":ii,
        "info_p1":ip1,
        "info_p2":ip2,
        "info_p3":ip3,
        "info_a1":ia1,
        "info_a2":ia2,
        "contactoI":cIngenia,
    }
    return render(request, 'ingenia.html', data)
