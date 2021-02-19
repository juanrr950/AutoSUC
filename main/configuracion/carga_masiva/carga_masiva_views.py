from main.models import Carga_masiva
from main.configuracion.carga_masiva.carga_masiva_forms import Carga_masiva_form
from main.configuracion.carga_masiva.carga_masiva_serializers import Carga_masiva_serializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.djangoBT.views import BTView
from main.suc.carga_registro import cargar_registros_txt
import threading


'''
METODO DE LISTADO SIMPLE
'''
class Carga_masiva_BT(BTView):
    def get(self, request, *args, **kwargs):
        #Sobreescribo el get para poner algunos campos solo
        #si tiene permisos
        
        return super().get( request, *args, **kwargs)
    
    template_name = "main/configuracion/carga_masiva/carga_masiva_list.html"
    url_json='list_carga_masiva'
    serializer = Carga_masiva_serializer
    field_list=('inicio','porcentaje_completado','estado', 'fin', 'lineas_total', 'registros_nuevos')
    verbose_list=('INICIO','% COMPLETADO', 'ESTADO', 'FIN', 'LINEAS_TOTAL', 'REGISTROS_NUEVOS')
    sort_list=('inicio','porcentaje_completado', 'estado', 'fin', 'lineas_total', 'registros_nuevos')
    data_sort_name=field_list[0] 
    data_sort_order="desc" 
    search_list=('inicio', 'estado', 'fin', 'lineas_total', 'registros_nuevos')
    show_checkbox_colunm= False
    
    link_list=(('Editar','/configuracion/carga_masiva/edit_carga_masiva/'),)
    
    def get_queryset(self):
        return Carga_masiva.objects.all()
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
                return super(Carga_masiva_BT, self).sort()

    '''
   
'''
METODO DE VISTA CREACIÓN CON FORMULARIO SIMPLE
'''
def new_carga_masiva(request):
    
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Carga_masiva_form(request.POST,request.FILES)
        
        if form.is_valid():
            carga_masiva=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            carga_masiva.save()
            
            hilo = threading.Thread(target=cargar_registros_txt, 
                            args=(carga_masiva,))
            hilo.start()
            messages.success(request, "Carga_masiva procesandose. ",extra_tags='info')
            
            return redirect('list_carga_masiva',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Carga_masiva_form()
         
    return render(request,'main/configuracion/carga_masiva/carga_masiva_form.html',
                  {'form':form,
                   })    

'''
METODO DE VISTA EDICICÓN CON FORMULARIO SIMPLE

'''
def edit_carga_masiva(request,pk):
    
    carga_masiva=Carga_masiva.objects.get(pk=pk)
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Carga_masiva_form(request.POST,request.FILES,instance=carga_masiva)
        
        if form.is_valid():
            carga_masiva=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            carga_masiva.save()
            messages.success(request, "Carga_masiva modificada con éxito. ")
            
            return redirect('list_carga_masiva',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Carga_masiva_form(instance=carga_masiva)
         
    return render(request,'main/configuracion/carga_masiva/carga_masiva_form.html',
                  {'form':form,
                   'pk':carga_masiva.id
                   }) 
    
def delete_carga_masiva(request,pk):
    usuario = request.user.usuario
    
    #COMPROBAR PERMISOS DE USUARIO
    carga_masiva=get_object_or_404(Carga_masiva,pk=pk)
    carga_masiva.delete()
        
    messages.success(request, "carga_masiva eliminado con éxito. " )
    return redirect('list_carga_masiva',view="list") 
