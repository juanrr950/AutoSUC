from main.models import Suc
from django.core.files.base import File
import os
from AutoSUC.settings import BASE_DIR
from main.suc.excel import generar_excel
from main.suc.powerp import generar_powerpoint
from main.suc.word import generar_word


def generar_suc(suc):
    
    generar_excel(suc)
    generar_powerpoint(suc)
    generar_word(suc)