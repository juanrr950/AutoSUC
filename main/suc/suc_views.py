'''
METODO DE LISTADO SIMPLE
'''
from main.djangoBT.views import BTView
from main.models import Suc
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from main.suc.suc_form import Suc_form
from main.suc.generar_suc import generar_suc
from main.suc.carga_registro import cargar_registros_txt
import os, io
from django.http import HttpResponse
from AutoSUC.settings import BASE_DIR
from _io import StringIO
from zipfile import ZipFile
from main.suc.suc_serializer import SucSerializer
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from datetime import datetime

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
    field_list=('nombre','estado','provincia',
                )
    verbose_list=('NOMBRE','ESTADO','PROVINCIA',
                 )
    sort_list=('nombre','created_date','provincia')
    data_sort_name="created_date" 
    data_sort_order="desc" 
    search_list=('nombre','created_date','provincia')
    
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
    
    suc=Suc.objects.get(pk=pk)
    
    in_memory = io.BytesIO()
    zip = ZipFile(in_memory, "a")
        
    zip.write(os.path.join(BASE_DIR,
              suc.excel.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.excel.name))
    zip.write(os.path.join(BASE_DIR,
              suc.word.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.word.name))
    zip.write(os.path.join(BASE_DIR,
              suc.powerpoint.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.powerpoint.name))
    zip.write(os.path.join(BASE_DIR,
              suc.imagen.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.imagen.name))
   
   
    zip.close()

    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename="+suc.nombre+".zip"
    
    in_memory.seek(0)    
    response.write(in_memory.read())
    
    return response

def zips_memory_suc(ids):
    
    in_memory = io.BytesIO()
    zip = ZipFile(in_memory, "a")
        
    for i in ids:
        if i.isdigit():
            suc=Suc.objects.get(pk=i)
            zip.write(os.path.join(BASE_DIR,
                      suc.excel.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.excel.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.word.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.word.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.powerpoint.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.powerpoint.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.imagen.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.imagen.name))
        
   
    zip.close()
    in_memory.seek(0)    
    return in_memory.read()

def donwload_zip_sucs(request,ids):
    ids=ids.split(',')
    
    

    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename=BLOQUE_SUCS.zip"
    
    zip_suc=zips_memory_suc(ids)
    response.write(zip_suc)
    
    return response

def email_sucs(request,ids):
    ids=ids.split(',')
       
    zip_suc=zips_memory_suc(ids)
    body=""
    #nombres para el body
    for i in ids:
        if i.isdigit():
            suc=Suc.objects.get(pk=i)
            if suc.num_postes<5:
                body=body+"<b>"+suc.nombre+" -> "+str(suc.num_postes)+" Postes</b><br>"
            else:
                body=body+suc.nombre+"<br>"
    
    #try:
    email=EmailMessage(
        subject='SUCs '+request.user.usuario.first_name,
        body=body,
        from_email='sucs@izaresoft.com',
        to=['juanrr950@gmail.com','dalagch@gmail.com'],
        bcc=['sucs@izaresoft.com'],
        )
    email.attach('Bloque SUCs.zip', zip_suc, "application/zip")
    email.content_subtype = "html" 
    email.send()
    messages.success(request, "SUCs seleccionados enviados por email con éxito.")
       
    #except:
          
        #messages.error(request, "Ha habido un error durante el envío.",extra_tags='danger')
    for i in ids:
        if i.isdigit():
            suc=Suc.objects.get(pk=i)
            suc.enviado=datetime.now()
            suc.save()
    return redirect('list_suc',view="list") 
        