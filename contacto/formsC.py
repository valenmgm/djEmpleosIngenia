from django.forms import ModelForm
from . import modelsC

class formAplicante(ModelForm):
    class Meta:
        model = modelsC.ContactoAplicante
        fields = ['nombre', 'email', 'telefono',
                  'sexo', 'aplica_a', 'cv']
