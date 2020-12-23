from docx import Document


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

doc = Document("PLANTILLA.docx")
replace_string(doc, "aaCENTRALAAAACODIGOaaaMIGAaaa", "SEVILLA 165166")
aaaNOMBREaaaCIUDADaaa
replace_string(doc, "aaaNOMBREaaaCIUDADaaa", "LA PUEBLA DEL RÍO")
doc.save('NOMBRE_SUC.docx')

print("Word modificado")