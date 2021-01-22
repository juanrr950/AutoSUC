from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''
class [CLASS_NAME]_form(ModelForm):
    class Meta:
        model = [CLASS_NAME]
        fields=[campos]
        '''
        widgets={
                '[TIPO_DATE]':DateInput(),
                '[TIPO_DATETIME]':TimeInput(),
                '[TIPO_TEXTAREA]':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                
            }
        '''