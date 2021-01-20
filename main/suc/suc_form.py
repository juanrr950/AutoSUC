from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''

from main.models import Suc
from main.utils import DateInput, TimeInput, DateTimeInput
from django.forms.widgets import TextInput
class Suc_form(ModelForm):
    class Meta:
        model = Suc
        fields=['nombre','via','tipo_via','numero_via',
                'provincia','ciudad','codigo_miga',
                'nombre_central','cto','car_ftth_iua',
                'fecha_ar','plantilla','nombre_tecnico',
                'apellido_tecnico','segundo_apellido_tecnico','dni_tecnico',
                'poste_central','poste_1','poste_2',
                'poste_3','poste_4','poste_5',
                'medida_1_2','medida_2_3','medida_3_4',
                'medida_4_5','comentarios','word',
                'excel','powerpoint','imagen',
                'pagado','enviado','facturado']
        widgets={
                'fecha_ar':DateInput(),
                'poste_1':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_2':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_3':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_4':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_5':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'codigo_miga':forms.TextInput(attrs={'onchange':'obtenerCentral()'}),
                'pagado':TextInput(),
                'enviado':TextInput(),
                'facturado':TextInput(),
                #'comentarios':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                
            }