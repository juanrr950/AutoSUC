from main.models import Central
from main.central.central_forms import Central_form
from main.central.central_serializers import Central_serializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.djangoBT.views import BTView


'''
METODO DE LISTADO SIMPLE
'''
class Central_BT(BTView):
    def get(self, request, *args, **kwargs):
        #Sobreescribo el get para poner algunos campos solo
        #si tiene permisos
        
        return super().get( request, *args, **kwargs)
    
    template_name = "main/central/central_list.html"
    url_json='list_central'
    serializer = Central_serializer
    field_list=('codigo_miga', 'nombre_central')
    verbose_list=('CODIGO_MIGA', 'NOMBRE_CENTRAL')
    sort_list=('codigo_miga', 'nombre_central')
    data_sort_name=field_list[0] 
    data_sort_order="desc" 
    search_list=('codigo_miga', 'nombre_central')
    show_checkbox_colunm= False
    
    link_list=(('Editar','/central/edit_central/'),)
    
    def get_queryset(self):
        return Central.objects.all()
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
                return super(Central_BT, self).sort()

    '''
   
'''
METODO DE VISTA CREACIÓN CON FORMULARIO SIMPLE
'''
def new_central(request):
    
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Central_form(request.POST)
        #Descomentar si el formulario tiene archivos
        #form=Central_form(request.POST,request.FILES)
        
        if form.is_valid():
            central=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            central.save()
            messages.success(request, "Central modificada con éxito. ")
            
            return redirect('list_central',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Central_form()
         
    return render(request,'main/central/central_form.html',
                  {'form':form,
                   })    

'''
METODO DE VISTA EDICICÓN CON FORMULARIO SIMPLE

'''
def edit_central(request,pk):
    
    central=Central.objects.get(pk=pk)
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=Central_form(request.POST,instance=central)
        #Descomentar si el formulario tiene archivos
        #form=Central_form(request.POST,request.FILES,instance=central)
        
        if form.is_valid():
            central=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            central.save()
            messages.success(request, "Central modificada con éxito. ")
            
            return redirect('list_central',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=Central_form(instance=central)
         
    return render(request,'main/central/central_form.html',
                  {'form':form,
                   'pk':central.id
                   }) 
    
def delete_central(request,pk):
    usuario = request.user.usuario
    
    #COMPROBAR PERMISOS DE USUARIO
    central=get_object_or_404(Central,pk=pk)
    central.delete()
        
    messages.success(request, "central eliminado con éxito. " )
    return redirect('list_central',view="list") 
