import os
from AutoSUC.settings import BASE_DIR
import shutil
from pathlib import Path

'''
Genera archivos encesarios para un CRUD básico en Django

'''
def generar_CRUD(modelo, campos_list, campos_form):
    modelo=modelo.lower()
    Modelo=modelo.capitalize()
    
    path_actual=os.path.join(Path(__file__).resolve().parent,'plantillas')
    path_py=os.path.join(BASE_DIR,'main',modelo)
    path_html=os.path.join(BASE_DIR,'main','templates','main',modelo)
    
    #Creamos la carpeta de los archivos python si no existe
    if not os.path.isdir(path_py):
        os.mkdir(path_py)
    else:
        raise Exception("Carpeta de archivos ya existente para esa modelo")
    
    #GENERADNO VIEWS
    #copiamos el archivo
    with open(os.path.join(path_actual,'views.py'), "rt") as fin:   
        data=fin.read()
    
    #Primero añadimos los import
    data="from main.models import "+Modelo+"\n"+\
        "from main."+modelo+"."+modelo+"_forms import "+Modelo+"_form\n"+\
        "from main."+modelo+"."+modelo+"_serializers import "+Modelo+"_serializer\n"+data
    
    #Sustituimos el nombre del modelop y los campos
    data=data.replace('[CLASS_NAME]', Modelo)
    data=data.replace('[class_name]', modelo)
    data=data.replace('[campos]', str(campos_list))
    data=data.replace('[CAMPOS]', str(campos_list).upper())
        
    with open(os.path.join(path_py,modelo+'_views.py'), "wt") as fout:
        fout.write(data)
    
    #GENERAMOS SERIALIZER
    #copiamos el archivo
    with open(os.path.join(path_actual,'serializers.py'), "rt") as fin:   
        data=fin.read()
    
    #Primero añadimos los import
    data="from main.models import "+Modelo+"\n"+data
            
    #Sustituimos el nombre del modelop y los campos
    data=data.replace('[CLASS_NAME]', Modelo)
    data=data.replace('[campos]', str(('id',*campos_list)))
        
    with open(os.path.join(path_py,modelo+'_serializers.py'), "wt") as fout:
        fout.write(data)
    
    #GENERAMOS el EL FORM
    #copiamos el archivo
    with open(os.path.join(path_actual,'forms.py'), "rt") as fin:   
        data=fin.read()
    
    #Primero añadimos los import
    data="from main.models import "+Modelo+"\n"+data
    
    #Sustituimos el nombre del modelop y los campos
    data=data.replace('[CLASS_NAME]', Modelo)
    data=data.replace('[campos]', str(campos_list))
        
    with open(os.path.join(path_py,modelo+'_forms.py'), "wt") as fout:
        fout.write(data)
     
    #Creamos la carpeta de los archivos html si no existe
    if not os.path.isdir(path_html):
        os.mkdir(path_html)
    else:
        raise Exception("Carpeta de templates: "+path_html+", ya existente para esa modelo")
        
    #GENERAMOS el EL LISTADO EN HTML
    #copiamos el archivo
    with open(os.path.join(path_actual,'list.html'), "rt") as fin:   
        data=fin.read()
    
    #Sustituimos el nombre del modelop y los campos
    data=data.replace('[class_name]', modelo)
    data=data.replace('[CLASS_NAME]', Modelo)
    data=data.replace('[campos]', str(campos_list))
        
    with open(os.path.join(path_html,modelo+'_list.html'), "wt") as fout:
        fout.write(data)
        
    #GENERAMOS el EL FORMULARIO EN HTML
    #copiamos el archivo
    with open(os.path.join(path_actual,'form.html'), "rt") as fin:   
        data=fin.read()
    
    #Sustituimos el nombre del modelop y los campos
    data=data.replace('[class_name]', modelo)
    data=data.replace('[CLASS_NAME]', Modelo)
    campos_dt=""
    for i in campos_form:
        campos_dt=campos_dt+"{{ form."+i+"|as_crispy_field }}\n"
    data=data.replace('[campos_fom]', campos_dt)
        
    with open(os.path.join(path_html,modelo+'_form.html'), "wt") as fout:
        fout.write(data)
    
    #Pintamos lineas para el path
    print("#"+Modelo+"s")
    print("path('"+modelo+"/list/<view>',  login_required("+modelo+"_views."+Modelo+"_BT.as_view(),'next','/accounts/login'),name='list_"+modelo+"'),")
    print("path('"+modelo+"/new_"+modelo+"',  login_required("+modelo+"_views.new_"+modelo+",'next','/accounts/login'),name='new_"+modelo+"'),")
    print("path('"+modelo+"/edit_"+modelo+"/<pk>',  login_required("+modelo+"_views.edit_"+modelo+",'next','/accounts/login'),name='edit_"+modelo+"'),")
    print("path('"+modelo+"/delete_"+modelo+"/<pk>',  login_required("+modelo+"_views.delete_"+modelo+",'next','/accounts/login'),name='delete_"+modelo+"'),")
    
modelo='Registro'
campos=('codigo_suc','codigo_miga','id_poste')

generar_CRUD(modelo, campos, campos)

print("Archivos generados, lineas a añadir en urls.py")
