from django.forms import ModelForm
from . import modelsC

class formAplicante(ModelForm):
    class Meta:
        model = modelsC.ContactoAplicante
        fields = ['nombre_completo', 'email', 'telefono',
                  'sexo', 'aplica_a', 'cv']

class formInteresado(ModelForm):
    class Meta:
        model = modelsC.ContactoInteresado
        fields = ['nombre', 'correo_electronico', 'mensaje']
