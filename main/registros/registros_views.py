from main.models import Registro
from django.http.response import JsonResponse

def comprobar_id_poste(request, id_poste):
    id_poste=id_poste.split('(ID ')[1].split(')')[0]
    if Registro.objects.filter(id_poste=id_poste).exists():
        return JsonResponse({id_poste:'POSTE_REGISTRIADO'})
    else:
        return JsonResponse({id_poste:'NO_EXISTE'})