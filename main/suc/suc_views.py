'''
METODO DE LISTADO SIMPLE
'''
from main.djangoBT.views import BTView
from main.models import Suc, Ajuste
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from main.suc.suc_form import Suc_form, email_form
from main.suc.generar_suc import generar_suc
from main.suc.carga_registro import cargar_registros_txt
import os, io
from django.http import HttpResponse
from AutoSUC.settings import BASE_DIR, EMAIL_HOST_USER
from _io import StringIO
from zipfile import ZipFile
from main.suc.suc_serializer import SucSerializer
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from datetime import datetime
from main.utils import get_ajuste, list_integer_from_string,\
    list_string_from_string
from main.suc.zip import zips_memory_suc

class Suc_BT(BTView):
    def get(self, request, *args, **kwargs):
        #Sobreescribo el get para poner algunos campos solo
        #si tiene permisos
        
        return super().get( request, *args, **kwargs)
    
    template_name = "main/suc/suc_list.html"
    url_json='list_suc'
    #model=Suc
    #Serializer opcional para tratar los datos antes de enviarlos a BootStrapTable.
    serializer = SucSerializer
    field_list=('nombre','estado','created_date','provincia','tiempo',
                'asignado'
                )
    verbose_list=('NOMBRE','ESTADO','FECHA REALIZADO','PROVINCIA','TIEMPO'
                 ,'ASIGNADO')
    sort_list=('nombre','estado','created_date','provincia','tiempo','asignado__first_name')
    data_sort_name="created_date" 
    data_sort_order="desc" 
    search_list=('nombre','estado','created_date','provincia','asignado__first_name')
    
    link_list=(('Editar','/suc/edit_suc/'),)
    show_checkbox_colunm=True
    
    def get_queryset(self):
        return Suc.objects.all()
    '''
    #Metodo para ordenar por campos especiales o derivados que no son directos
    #o no están en la base de datos
    def sort(self):
        if('sort' in self.request.GET):
            if self.request.GET['sort'] == '[FIELD_NAME]:
                if(self.request.GET['order'] == 'asc'):
                    return self.queryset.order_by('[CRITERIO_ORDEN]', 'numero')
                else:
                    return self.queryset.order_by('-[CRITERIO_ORDEN]', '-numero')
            else:
                return super(Suc_BT, self).sort()

    '''
   
'''
METODO DE VISTA CREACIÓN CON FORMULARIO SIMPLE
'''
def new_suc(request):
    
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        
        #Descomentar si el formulario tiene archivos
        form=Suc_form(request.POST,request.FILES)
        
        if form.is_valid():
            suc=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            suc.usuario=request.user.usuario
            suc.save()
            messages.success(request, "Suc creado con éxito. ")
            generar_suc(suc)
            
            return redirect('list_suc',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Suc_form()
         
    return render(request,'main/suc/suc_form.html',
                  {'form':form,
                   })    

'''
METODO DE VISTA EDICICÓN CON FORMULARIO SIMPLE

'''
def edit_suc(request,pk):
    
    suc=Suc.objects.get(pk=pk)
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        
        #Descomentar si el formulario tiene archivos
        form=Suc_form(request.POST,request.FILES,instance=suc)
        
        if form.is_valid():
            
            suc=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            suc.save()
            messages.success(request, "Suc modificado con éxito. ")
            generar_suc(suc)
            return redirect('list_suc',view="list")
            '''
            if os.path.exists(str(BASE_DIR)+suc.imagen.url):
                messages.success(request, "Suc modificado con éxito. ")
                generar_suc(suc)
                return redirect('list_suc',view="list")
            else:    
                messages.error(request, "Imagen no encontrada en sistema, carguela de nuevo.",extra_tags='danger')
            '''
             
        
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Suc_form(instance=suc)
         
    return render(request,'main/suc/suc_form.html',
                  {'form':form,
                   'pk':suc.id
                   }) 
    
def delete_suc(request,pk):
    usuario = request.user.usuario
    
    #COMPROBAR PERMISOS DE USUARIO
    
    suc=get_object_or_404(Suc,pk=pk)
    suc.delete()
        
    messages.success(request, "suc eliminado con éxito. " )
    return redirect('list_suc',view="list") 


def donwload_zip_suc(request,pk):
    list=[]
    list.append(pk)
    zip_suc=zips_memory_suc(list)
    response = HttpResponse()
    suc=Suc.objects.get(pk=int(pk))
    response["Content-Disposition"] = "attachment; filename="+suc.nombre+".zip"
  
    response.write(zip_suc)
    
    return response



def donwload_zip_sucs(request,ids):
    ids=ids.split(',')
    
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename=BLOQUE_SUCS.zip"
    
    zip_suc=zips_memory_suc(ids)
    response.write(zip_suc)
    
    return response

def new_email_sucs(request,ids):
    #limpiamos ids
    lids=list_integer_from_string(ids)
    
    sucs=Suc.objects.filter(id__in=lids)
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    if request.method == 'POST':
        form=email_form(request.POST)
        if form.is_valid():
            if enviar_email(sucs,form):
                messages.success(request, "SUCs enviados con éxito.")
                return redirect('list_suc',view="list") 
            else:
                messages.error(request, "Ha habido un error durante el envío.",extra_tags='danger')
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
    else:
        sucs=Suc.objects.filter(id__in=lids)
        body=""
        for i in sucs:
            if i.num_postes<5:
                body=body+"<b>"+i.nombre+" -> "+str(i.num_postes)+" Postes</b><br>"
            else:
                body=body+i.nombre+"<br>"
                
        form=email_form(initial={'para':get_ajuste("destino_email_pordefecto"),
                                 'cco':get_ajuste("copia_email_pordefecto"),
                                 'asunto':"Bloque SUCs "+request.user.first_name,
                                 'cuerpo':body})
         
    return render(request,'main/suc/suc_mail_form.html',
                  {'form':form,
                   })    
def enviar_email(sucs,form):
    
    zip_suc=zips_memory_suc(sucs)
    
    try:
        email=EmailMessage(
            subject=form.cleaned_data['asunto'],
            body=form.cleaned_data['cuerpo'],
            from_email=EMAIL_HOST_USER,
            to=list_string_from_string(form.cleaned_data['para']),
            bcc=list_string_from_string(form.cleaned_data['cco']),
            )
        email.attach('Bloque SUCs.zip', zip_suc, "application/zip")
        email.content_subtype = "html" 
        email.send()
        
       
        for suc in sucs:
            suc.enviado=datetime.now()
            suc.estado='E'
            suc.save()
        return True
    except:
        return False
    