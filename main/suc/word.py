from docx import Document
import os
from AutoSUC.settings import BASE_DIR

def generar_word(suc):
    
    def replace_string(doc, old_text, new_text):
        
        for p in doc.paragraphs:
            
            if old_text in p.text:
                inline = p.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if old_text in inline[i].text:
                        text = inline[i].text.replace(old_text, new_text)
                        inline[i].text = text
                #print(p.text)
    
        
        return 1
    
    doc = Document(os.path.join(BASE_DIR,
                            'media/plantillas/PLANTILLA.docx'))
  
    replace_string(doc, "_CIUDADDELSUC_", suc.ciudad.upper())
    replace_string(doc, "_FECHA_", suc.fecha_ar.strftime("%d/%m/%Y"))
    replace_string(doc, "_CENTRALYMIGA_", suc.nombre_central.upper()+" "+suc.codigo_miga)
    replace_string(doc, "_NOMBRET_", suc.nombre_tecnico.upper())
    replace_string(doc, "_APELLIDO1_", suc.apellido_tecnico.upper())
    replace_string(doc, "_APELLIDO2_ ", suc.segundo_apellido_tecnico.upper())
    replace_string(doc, "_DNIT_", suc.dni_tecnico.upper())
    replace_string(doc, "_CODIGOFIBRAFTTH_", str(suc.car_ftth_iua))
    replace_string(doc, "_NPOSTES_", str(suc.num_postes))
    replace_string(doc, "_NOMBRECOMPLETOT_", suc.nombre_tecnico.upper()+
                   " "+suc.apellido_tecnico.upper()+
                   " "+suc.segundo_apellido_tecnico.upper())
    postes=suc.poste_1_id+"\n"+suc.poste_2_id
    if suc.num_postes>=3:
        postes=postes+"\n"+suc.poste_3_id
    if suc.num_postes>=4:
        postes=postes+"\n"+suc.poste_4_id
    if suc.num_postes>=5:
        postes=postes+"\n"+suc.poste_5_id
    
    replace_string(doc, "_IDDEPOSTES_", postes)
    
    doc.save(os.path.join(BASE_DIR,
                        'media/'+suc.usuario.username+'/'+
                        suc.nombre+'/'+suc.nombre+'.docx'))
    
    suc.word=suc.usuario.username+'/'+suc.nombre+'/'+suc.nombre+'.docx'
    suc.save()