from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from main.models import Central
from django.http.response import JsonResponse

# Create your views here.
class login(LoginView):
    def __init__(self,  *args, **kwargs):
        super(LoginView, self).__init__(*args, **kwargs)

def home(request):
    return redirect('/')

def example(request):
    
    return render(request,'main/example.html')

def obtener_central(request, codigo_miga):
    
    if Central.objects.filter(codigo_miga=codigo_miga).exists():
        central=Central.objects.get(codigo_miga=codigo_miga).nombre_central
        return JsonResponse({'codigo_miga':codigo_miga,
                             'encontrada':True,
                             'nombre_central':central})
    else:
        return JsonResponse({'codigo_miga':codigo_miga,
                             'encontrada':False})