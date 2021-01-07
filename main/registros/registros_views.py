from main.models import Registro
from django.http.response import JsonResponse

def comprobar_id_poste(request, id_poste):
    id_poste=id_poste.split('(ID ')[1].split(')')[0]
    if Registro.objects.filter(id_poste=id_poste).exists():
        poste=Registro.objects.get(id_poste=id_poste)
        return JsonResponse({'id_poste':id_poste,
                             'poste_registrado':True,
                             'codigo_suc':poste.codigo_suc})
    else:
        return JsonResponse({'id_poste':id_poste,
                             'poste_registrado':False})