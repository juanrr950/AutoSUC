from openpyxl.reader.excel import load_workbook
import os
from AutoSUC.settings import BASE_DIR
from main.models import Registro
import time
import re
from django.utils.timezone import now
from datetime import datetime


def cargar_registros_excel():
    print("Comenzamos abriendo el archivo")
    inicio=time.time()
    workbook = load_workbook(filename=os.path.join(BASE_DIR,
                            'media/registros/Robot_Tesa_Union7.xlsx'))
    
    print("Archivo abierto en "+str((time.time()-inicio)/60)+" min")    
    total=571362
    #total=241
    sheet=workbook.active
    registros=[]
    for i in range(1,total):
        poste_ori=sheet['D'+str(i)].value
        poste=''.join(i for i in poste_ori if i.isdigit())
        
        if poste.isdigit():
            poste=int(poste)
            if poste>0 and poste< 4294967295 :
                
                registros.append(Registro(codigo_suc=sheet['A'+str(i)].value,
                        codigo_miga=sheet['B'+str(i)].value,
                        id_poste=poste))
                if i%1000==0:
                    Registro.objects.bulk_create(registros,
                                                  ignore_conflicts=False)
                    registros=[]
            else: 
                print("Excluido poste: "+sheet['D'+str(i)].value)    
        else:
            print("Excluido poste: "+sheet['D'+str(i)].value)    
        
        if i%1000==0:
            print("LLevamos "+str(i)+" de "+str(total)+
                  ", un "+str(round(i/total,2)*100)+" % en "+
                  str((time.time()-inicio)/60)+" min")
        
#ESTA ESTOY USANDO    
'''
EL FORMATO DE LINEAS DE SUR:
[CODIGO SUC];[CÓDIGO MIGA];[ID POSTE]
'''        
def cargar_registros_txt(carga_masiva):
    reg_inicio=Registro.objects.count()
    print("Comenzamos abriendo el archivo, "+str(reg_inicio)+" nº de registro actuales")
    inicio=time.time()
    carga_masiva.inicio=datetime.now() 
    
    f = open(carga_masiva.csv.file.name, "r")
    
    lineas_totales=len(f.readlines())
    f.seek(0)
    carga_masiva.lineas_total=lineas_totales
    carga_masiva.save()
    
    print("Archivo abierto en "+str((time.time()-inicio))+" s, total lineas:"+str(lineas_totales) )   
    
    
    registros=[]
    i=0
    
    for x in f:

        i=i+1
        linea=x.split(";")
        poste_ori=linea[2]
        poste=''.join(i for i in poste_ori if i.isdigit())
        
        if poste.isdigit():
            poste=int(poste)
            if poste>0 and poste< 4294967295 :
                miga=linea[1]
                if not miga.isdigit():
                    miga=0
                registros.append(Registro(id_poste=poste,
                                          codigo_miga=miga,
                                          codigo_suc=linea[0]))
                if i%2000==0:
                    devuelve=Registro.objects.bulk_create(registros,
                                                  ignore_conflicts=True)
                    registros=[]
                    
                    #print(len(devuelve))
        '''    
            else: 
                print("Excluido poste: "+x)    
        else:
            print("Excluido poste: "+x)    
        '''
        if i%50000==0:
            print("LLevamos "+str(i)+"  lineas, en "+
                  str((time.time()-inicio)/60)+" min")
            porc=round(i/lineas_totales*100)
            carga_masiva.porcentaje_completado=porc
            carga_masiva.save()
            
    Registro.objects.bulk_create(registros,
                            ignore_conflicts=True)
    print("LLevamos "+str(i)+"  lineas, en "+
                  str((time.time()-inicio)/60)+" min") 
    
    reg_fin=Registro.objects.count()
    
    print(str(reg_fin-reg_inicio)+" registros se han cargado nuevos")
    
    carga_masiva.registro_nuevos=reg_fin-reg_inicio
    carga_masiva.estado='T'
    carga_masiva.save()