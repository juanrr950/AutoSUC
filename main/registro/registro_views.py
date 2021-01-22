from main.models import Registro
from main.registro.registro_forms import Registro_form
from main.registro.registro_serializers import Registro_serializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.djangoBT.views import BTView
from django.http.response import JsonResponse


'''
METODO DE LISTADO SIMPLE
'''
class Registro_BT(BTView):
    def get(self, request, *args, **kwargs):
        #Sobreescribo el get para poner algunos campos solo
        #si tiene permisos
        
        return super().get( request, *args, **kwargs)
    
    template_name = "main/registro/registro_list.html"
    url_json='list_registro'
    serializer = Registro_serializer
    field_list=('codigo_suc', 'codigo_miga', 'id_poste')
    verbose_list=('CODIGO_SUC', 'CODIGO_MIGA', 'ID_POSTE')
    sort_list=('codigo_suc', 'codigo_miga', 'id_poste')
    data_sort_name=field_list[0] 
    data_sort_order="desc" 
    search_list=('codigo_suc', 'codigo_miga', 'id_poste')
    show_checkbox_colunm= False
    
    link_list=(('Editar','/registro/edit_registro/'),)
    
    def get_queryset(self):
        return Registro.objects.all()
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
                return super(Registro_BT, self).sort()

    '''
   
'''
METODO DE VISTA CREACIÓN CON FORMULARIO SIMPLE
'''
def new_registro(request):
    
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Registro_form(request.POST)
        #Descomentar si el formulario tiene archivos
        #form=Registro_form(request.POST,request.FILES)
        
        if form.is_valid():
            registro=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            registro.save()
            messages.success(request, "Registro modificada con éxito. ")
            
            return redirect('list_registro',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Registro_form()
         
    return render(request,'main/registro/registro_form.html',
                  {'form':form,
                   })    

'''
METODO DE VISTA EDICICÓN CON FORMULARIO SIMPLE

'''
def edit_registro(request,pk):
    
    registro=Registro.objects.get(pk=pk)
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Registro_form(request.POST,instance=registro)
        #Descomentar si el formulario tiene archivos
        #form=Registro_form(request.POST,request.FILES,instance=registro)
        
        if form.is_valid():
            registro=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            registro.save()
            messages.success(request, "Registro modificada con éxito. ")
            
            return redirect('list_registro',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Registro_form(instance=registro)
         
    return render(request,'main/registro/registro_form.html',
                  {'form':form,
                   'pk':registro.id
                   }) 
    
def delete_registro(request,pk):
    usuario = request.user.usuario
    
    #COMPROBAR PERMISOS DE USUARIO
    registro=get_object_or_404(Registro,pk=pk)
    registro.delete()
        
    messages.success(request, "registro eliminado con éxito. " )
    return redirect('list_registro',view="list") 


def comprobar_id_poste(request, id_poste):
    id_poste=id_poste.split('(ID ')[1].split(')')[0]
    if Registro.objects.filter(id_poste=id_poste).exists():
        poste=Registro.objects.get(id_poste=id_poste)
        return JsonResponse({'id_poste':id_poste,
                             'poste_registrado':True,
                             'codigo_suc':poste.codigo_suc})
    else:
        return JsonResponse({'id_poste':id_poste,
                             'poste_registrado':False})