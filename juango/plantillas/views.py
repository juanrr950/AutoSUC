from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.djangoBT.views import BTView


'''
METODO DE LISTADO SIMPLE
'''
class [CLASS_NAME]_BT(BTView):
    def get(self, request, *args, **kwargs):
        #Sobreescribo el get para poner algunos campos solo
        #si tiene permisos
        
        return super().get( request, *args, **kwargs)
    
    template_name = "main/[ruta]/[class_name]_list.html"
    url_json='list_[class_name]'
    serializer = [CLASS_NAME]_serializer
    field_list=[campos]
    verbose_list=[CAMPOS]
    sort_list=[campos]
    data_sort_name=field_list[0] 
    data_sort_order="desc" 
    search_list=[campos]
    show_checkbox_colunm= False
    
    link_list=(('Editar','/[ruta]/edit_[class_name]/'),)
    
    def get_queryset(self):
        return [CLASS_NAME].objects.all()
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
                return super([CLASS_NAME]_BT, self).sort()

    '''
   
'''
METODO DE VISTA CREACIÓN CON FORMULARIO SIMPLE
'''
def new_[class_name](request):
    
    
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=[CLASS_NAME]_form(request.POST)
        #Descomentar si el formulario tiene archivos
        #form=[CLASS_NAME]_form(request.POST,request.FILES)
        
        if form.is_valid():
            [class_name]=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            [class_name].save()
            messages.success(request, "[CLASS_NAME] modificada con éxito. ")
            
            return redirect('list_[class_name]',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=[CLASS_NAME]_form()
         
    return render(request,'main/[ruta]/[class_name]_form.html',
                  {'form':form,
                   })    

'''
METODO DE VISTA EDICICÓN CON FORMULARIO SIMPLE

'''
def edit_[class_name](request,pk):
    
    [class_name]=[CLASS_NAME].objects.get(pk=pk)
    #COMPROBAR AQUI SI TIENE LOS PERMISOS NECESARIOS
    
    if request.method == 'POST':
        form=[CLASS_NAME]_form(request.POST,instance=[class_name])
        #Descomentar si el formulario tiene archivos
        #form=[CLASS_NAME]_form(request.POST,request.FILES,instance=[class_name])
        
        if form.is_valid():
            [class_name]=form.save(commit=False)
            #ASIGNAR AQUI CLASE RELACIONADA SI ES NECESARIO
            [class_name].save()
            messages.success(request, "[CLASS_NAME] modificada con éxito. ")
            
            return redirect('list_[class_name]',view="list") 
        else:
            messages.error(request, "Corrija los campos en rojo.",extra_tags='danger')
            
    else:
        form=[CLASS_NAME]_form(instance=[class_name])
         
    return render(request,'main/[ruta]/[class_name]_form.html',
                  {'form':form,
                   'pk':[class_name].id
                   }) 
    
def delete_[class_name](request,pk):
    usuario = request.user.usuario
    
    #COMPROBAR PERMISOS DE USUARIO
    [class_name]=get_object_or_404([CLASS_NAME],pk=pk)
    [class_name].delete()
        
    messages.success(request, "[class_name] eliminado con éxito. " )
    return redirect('list_[class_name]',view="list") 
