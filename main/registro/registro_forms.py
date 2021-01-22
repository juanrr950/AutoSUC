from main.models import Registro
from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''
class Registro_form(ModelForm):
    class Meta:
        model = Registro
        fields=('codigo_suc', 'codigo_miga', 'id_poste')
        '''
        widgets={
                '[TIPO_DATE]':DateInput(),
                '[TIPO_DATETIME]':TimeInput(),
                '[TIPO_TEXTAREA]':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                
            }
        '''