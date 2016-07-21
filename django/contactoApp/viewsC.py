from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from . import modelsC
from . import formsC
# Create your views here.
@csrf_exempt
def renderContactoIngenia(request):
    cRp = modelsC.ContactoRecursosHumanos.objects.latest('fecha')
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')
    formI = formsC.formInteresado()
    formA = formsC.formAplicante()

    data = {
        'contactoRp':cRp,
        'contactoI':cIngenia,
        'formInteresado':formI,
        'formAplicante':formA,
    }

    if request.method == "POST":
        formsetInteresado = formsC.formInteresado(request.POST)
        if formsetInteresado.is_valid():
            formsetInteresado.save()
            return render(request, 'urlExito')

        else:
            formsetAplicante = formsC.formAplicante(request.POST)
            if formsetAplicante.is_valid():
                formsetAplicante.save()
                return redirect('urlExito')

    else:
        return render(request, 'contacto.html', data)



def renderExito(request):
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')
    return render(request, 'exito.html', {'contactoI':cIngenia})
