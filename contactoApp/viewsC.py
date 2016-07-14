from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import modelsC
from . import formsC
# Create your views here.
def renderContactoIngenia(request):
    cRp = modelsC.ContactoRecursosHumanos.objects.latest('fecha')

    formI = formsC.formInteresado()
    data = {
        'contactoRp':cRp,
        'formInteresado':formI,
        'contactoI':cIngenia
    }
    
    return render(request, 'contacto.html', data)

def renderAplicaYa(request):
    if request.method == 'POST':
        formsetAplicante = formsC.formAplicante(request.POST)
        if formsetAplicante.is_valid():
            formsetAplicante.save()
            return redirect('urlHome')

    else:
        formA = formsC.formAplicante()
        cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')

        data = {
        'form':formA,
        'contactoI':cIngenia,
        }

        return render(request, 'aplicaya.html', data)
