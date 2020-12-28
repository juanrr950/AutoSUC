
from pptx import Presentation
from pptx.util import Pt
import os
from AutoSUC.settings import BASE_DIR
def generar_powerpoint(suc):
        
    # Create an instance of Presentation class
    def find_shape(slide,name):
        
        for i in slide.shapes:
            if name==i.name:
                return i
    def delete_shape(name_shape):  
        elem=find_shape(sld, name_shape)
        elem._element.getparent().remove(elem._element)
        
    if suc.plantilla=='H':
        pres = Presentation(os.path.join(BASE_DIR,
                            'media/plantillas/PLANTILLA_HORIZONTAL.pptx'))
    else:
        pres = Presentation(os.path.join(BASE_DIR,
                            'media/plantillas/PLANTILLA_VERTICAL.pptx'))
    
    # Get the first slide
    sld = pres.slides[0]
    
    #Cambiamos los postes 
    p1=find_shape(sld, "p1")
    p1.text_frame.paragraphs[0].runs[0].text=suc.poste_1
    
    p2=find_shape(sld, "p2")
    p2.text_frame.paragraphs[0].runs[0].text=suc.poste_2
        
    
    #Introducimos las medidas
    m1=find_shape(sld, "m1")
    m1.text_frame.paragraphs[0].runs[0].text=suc.medida_1_2 + " m."
       
    n=suc.num_postes
    if n>=3:
        p3=find_shape(sld, "p3")
        p3.text_frame.paragraphs[0].runs[0].text=suc.poste_3
        
        m2=find_shape(sld, "m2")
        m2.text_frame.paragraphs[0].runs[0].text=suc.medida_2_3 + " m."
    if n>=4:
        p4=find_shape(sld, "p4")
        p4.text_frame.paragraphs[0].runs[0].text=suc.poste_4
    
        m3=find_shape(sld, "m3")
        m3.text_frame.paragraphs[0].runs[0].text=suc.medida_3_4 + " m."
    if n>=5:
        p5=find_shape(sld, "p5")
        p5.text_frame.paragraphs[0].runs[0].text=suc.poste_5
        
        m4=find_shape(sld, "m4")
        m4.text_frame.paragraphs[0].runs[0].text=suc.medida_4_5 + " m."
         
    #Borramos en cada caso si son menos de 5 postes
    if n<=4:    
        delete_shape("p5")
        delete_shape("vortex5")
        delete_shape("conector4_5")
        delete_shape("m4")
        delete_shape("letter4_5")       
       
    if n<=3:    
        delete_shape("p4")
        delete_shape("vortex4")
        delete_shape("conector3_4")
        delete_shape("m3")
        delete_shape("letter3_4")       
    if n<=2:    
        delete_shape("p3")
        delete_shape("vortex3")
        delete_shape("conector2_3")
        delete_shape("m2")
        delete_shape("letter2_3")   
    
    ct=find_shape(sld, "cartelct")
    ct.text_frame.paragraphs[0].runs[0].text=suc.nombre_central
    ct.text_frame.paragraphs[1].runs[0].text="MIGA: "+str(suc.codigo_miga)

    
    nombreppt=suc.nombre.split('_')[1]+suc.nombre.split('_')[2]
    nombreppt=''.join(e for e in nombreppt if e.isalnum())
    nombreppt=nombreppt[-11:]
    pres.save(os.path.join(BASE_DIR,
                        'media/'+suc.usuario.username+'/'+
                        suc.nombre+'/'+nombreppt+'.pptx'))
    
    suc.powerpoint=suc.usuario.username+'/'+suc.nombre+'/'+nombreppt+'.pptx'
    suc.save()