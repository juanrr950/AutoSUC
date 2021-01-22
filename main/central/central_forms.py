from main.models import Central
from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''
class Central_form(ModelForm):
    class Meta:
        model = Central
        fields=('codigo_miga', 'nombre_central')
        '''
        widgets={
                '[TIPO_DATE]':DateInput(),
                '[TIPO_DATETIME]':TimeInput(),
                '[TIPO_TEXTAREA]':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                
            }
        '''