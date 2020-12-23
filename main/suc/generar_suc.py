from main.models import Suc
from django.core.files.base import File
import os
from AutoSUC.settings import BASE_DIR
from main.suc.excel import generar_excel


def generar_suc(nombre_suc):
    
    generar_excel(nombre_suc)
    '''
    f = open(os.path.join(BASE_DIR,'media/file_example.txt'))
    suc=Suc.objects.get(id=1)
    suc.word=File(f)
    suc.save()
    '''