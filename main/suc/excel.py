from xlrd import open_workbook
from xlutils.copy import copy
import os
from AutoSUC.settings import BASE_DIR


from openpyxl import load_workbook
import os
from AutoSUC.settings import BASE_DIR

def generar_excel(suc):
    workbook = load_workbook(filename=os.path.join(BASE_DIR,
                            'media/plantillas/PLANTILLA.xlsx'))
    
    sheet=workbook.active
    sheet["B13"]=suc.provincia.upper()
    sheet["F13"]=suc.nombre_central.upper()
    sheet["K13"]=suc.codigo_miga
        
    sheet["M18"]=suc.poste_1_id
    sheet["M19"]=suc.poste_2_id
    n=suc.num_postes
    if n>=3:
        sheet["M20"]=suc.poste_3_id
    if n>=4:
        sheet["M21"]=suc.poste_4_id
    if n>=5:
        sheet["M22"]=suc.poste_5_id
    if n>=6:
        sheet["M23"]=suc.poste_6_id
    if n>=7:
        sheet["M24"]=suc.poste_7_id
    if n>=8:
        sheet["M25"]=suc.poste_8_id
    if n>=9:
        sheet["M26"]=suc.poste_9_id
    if n>=10:
        sheet["M27"]=suc.poste_10_id
    
    
        
    if n<=9:    
        sheet["B27"]=""
        sheet["D27"]=""
        sheet["G27"]=""
        sheet["I27"]=""
        
    if n<=8:    
        sheet["B26"]=""
        sheet["D26"]=""
        sheet["G26"]=""
        sheet["I26"]=""
        
    if n<=7:    
        sheet["B25"]=""
        sheet["D25"]=""
        sheet["G25"]=""
        sheet["I25"]=""
        
    if n<=6:    
        sheet["B24"]=""
        sheet["D24"]=""
        sheet["G24"]=""
        sheet["I24"]=""
        
    if n<=5:    
        sheet["B23"]=""
        sheet["D23"]=""
        sheet["G23"]=""
        sheet["I23"]=""
    
    if n<=4:    
        sheet["B22"]=""
        sheet["D22"]=""
        sheet["G22"]=""
        sheet["I22"]=""
        
    if n<=3:    
        sheet["B21"]=""
        sheet["D21"]=""
        sheet["G21"]=""
        sheet["I21"]=""
        
    if n<=2:    
        sheet["B20"]=""
        sheet["D20"]=""
        sheet["G20"]=""
        sheet["I20"]=""
        
        
    workbook.save(filename=os.path.join(BASE_DIR,
                        'media/'+suc.usuario.username+'/'+suc.nombre+'/'+suc.nombre+'.xlsx'))
   
    #Guardamos el path en la base de datos
    suc.excel=suc.usuario.username+'/'+suc.nombre+'/'+suc.nombre+'.xlsx'
    suc.save()
