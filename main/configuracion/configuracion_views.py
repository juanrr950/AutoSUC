from main.suc.carga_registro import cargar_registros_txt
from django.http.response import HttpResponse



def cargar_postes(request):
    cargar_registros_txt()
    return HttpResponse('<h1>Page was found</h1>')
    