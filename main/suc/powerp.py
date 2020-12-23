
from pptx import Presentation
from pptx.util import Pt
 # Create an instance of Presentation class

def find_shape(slide,name):
    
    for i in slide.shapes:
        if name==i.name:
            return i
    

pres = Presentation('PLANTILLA_HORIZONTAL.pptx')

# Get the first slide

sld = pres.slides[0]

p1=find_shape(sld, "p1")
p1.text_frame.paragraphs[0].runs[0].text="L 1 Nº 302 (8E) (ID 12345)"
#Cambiamos el tamaño, no se porque al cambiar el texto se cambia sola la fuente 
#p1.text_frame.paragraphs[0].font.size=Pt(8)


m1=find_shape(sld, "m1")
m1.text_frame.paragraphs[0].runs[0].text="23"
#m1.text_frame.paragraphs[0].font.bold=True

ct=find_shape(sld, "cartelct")
ct.text_frame.paragraphs[0].runs[0].text="C.T. SEVILLA"
print(ct)
pres.save('ERDAGUER22.pptx')

print("Archivo modificado")