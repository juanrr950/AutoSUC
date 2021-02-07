import io
from zipfile import ZipFile
import os
from AutoSUC.settings import BASE_DIR
from main.models import Suc


def zips_memory_suc(sucs):
    
    in_memory = io.BytesIO()
    zip = ZipFile(in_memory, "a")
        
    for i in sucs:
        if i.isdigit():
            suc=Suc.objects.get(pk=int(i))
            zip.write(os.path.join(BASE_DIR,
                      suc.excel.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.excel.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.word.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.word.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.powerpoint.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.powerpoint.name))
            zip.write(os.path.join(BASE_DIR,
                      suc.imagen.path), suc.provincia+"/"+suc.ciudad+"/"+suc.nombre+"/"+os.path.basename(suc.imagen.name))
        
   
    zip.close()
    in_memory.seek(0)    
    return in_memory.read()