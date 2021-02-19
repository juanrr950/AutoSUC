from main.models import Central
from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''
class Central_form(ModelForm):
    class Meta:
        model = Central
        fields=('codigo_miga', 'nombre_central',
            
            )
        
        