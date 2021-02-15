from main.models import Carga_masiva
from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''
class Carga_masiva_form(ModelForm):
    class Meta:
        model = Carga_masiva
        fields=('csv',)
        '''
        widgets={
                '[TIPO_DATE]':DateInput(),
                '[TIPO_DATETIME]':TimeInput(),
                '[TIPO_TEXTAREA]':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                '[TIPO_MANYTOMANY]':forms.SelectMultiple(attrs={'class':'js-example-basic-multiple',}),
            
            }
        '''