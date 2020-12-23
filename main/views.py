from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

# Create your views here.
class login(LoginView):
    def __init__(self,  *args, **kwargs):
        super(LoginView, self).__init__(*args, **kwargs)

def home(request):
    return redirect('/')

def example(request):
    
    return render(request,'main/example.html')