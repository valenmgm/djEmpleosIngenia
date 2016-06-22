from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from . import modelsC
from . import formsC
# Create your views here.
def renderContactoIngenia(request):
    cIngenia = modelsC.ContactoIngenia.objects.latest('fecha')
    data = {'contactoI':cIngenia}
    return render(request, 'contacto.html', data)

def renderAplicaYa(request):
    if request.method == 'POST':
        formsetAplicante = formsC.formAplicante(request.POST)
        if formsetAplicante.is_valid():
            formsetAplicante.save()
            return redirect('urlHome')

    else:
        formA = formsC.formAplicante()
        return render(request, 'aplicaya.html', {'form': formA})
