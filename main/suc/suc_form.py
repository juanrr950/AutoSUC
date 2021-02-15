from django.forms.models import ModelForm
from django import forms
'''
CLASE FORM PARA FORMULARIO SIMPLE
'''

from main.models import Suc
from main.utils import DateInput, TimeInput, DateTimeInput
from django.forms.widgets import TextInput
from django.forms.forms import Form
from reportlab.platypus.para import Para
from tinymce.widgets import TinyMCE

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
                'poste_6','poste_7','poste_8',
                'poste_9','poste_10',
                'medida_1_2','medida_2_3','medida_3_4',
                'medida_4_5','medida_5_6','medida_6_7',
                'medida_7_8','medida_8_9','medida_9_10',
                'comentarios','word',
                'excel','powerpoint','imagen',
                'pagado','enviado','facturado','estado',
                'tiempo','asignado']
        widgets={
                'fecha_ar':DateInput(),
                'poste_1':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_2':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_3':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_4':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_5':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_6':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_7':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_8':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_9':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'poste_10':forms.TextInput(attrs={'onchange':'comprobarPoste(event)'}),
                'codigo_miga':forms.TextInput(attrs={'onchange':'obtenerCentral()'}),
                'pagado':TextInput(),
                'enviado':TextInput(),
                'facturado':TextInput(),
                'tiempo':forms.HiddenInput()
                #'comentarios':forms.Textarea(attrs={'rows':8,'style':'height:unset !important;'}),
                
            }
        
class email_form(Form):
    
    para=forms.CharField(label="Destinatario")
    cco=forms.CharField(label="En copia oculta")
    asunto=forms.CharField(label="Asunto")
    cuerpo = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    