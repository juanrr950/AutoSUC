"""AutoSUC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from main.suc import suc_views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from main.admin import adminsite
from main.registros import registros_views
from main.configuracion import configuracion_views
from django.urls.conf import re_path

urlpatterns = [
    #path('',views.home, name='home'),
    path('admin/', adminsite.urls), 
    path('',login_required(views.example,'next','/accounts/login'), name='example'),
    path('accounts/login/',views.login.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    path('central/obtener_central/<codigo_miga>',
           login_required(views.obtener_central,
                           'next','/accounts/login'),name='obtener_central'),
    
    #SUCs
    path('suc/list/<view>',  login_required(suc_views.Suc_BT.as_view(),'next','/accounts/login'),name='list_suc'),
    path('suc/new_suc',  login_required(suc_views.new_suc,'next','/accounts/login'),name='new_suc'),
    path('suc/edit_suc/<pk>',  login_required(suc_views.edit_suc,'next','/accounts/login'),name='edit_suc'),
    path('suc/delete_suc/<pk>',  login_required(suc_views.delete_suc,'next','/accounts/login'),name='delete_suc'),
    path('suc/donwload_zip_suc/<pk>',  login_required(suc_views.donwload_zip_suc,'next','/accounts/login'),name='donwload_zip_suc'),
    re_path(r'^suc/donwload_zip_sucs/(?P<ids>(\d+\,?)+)/$',  login_required(suc_views.donwload_zip_sucs,'next','/accounts/login'),name='donwload_zip_sucs'),
    re_path(r'^suc/email_sucs/(?P<ids>(\d+\,?)+)/$',  login_required(suc_views.email_sucs, 'next','/accounts/login'),name='email_sucs'),
    
    #Registros
    path('registro/comprobar_poste/<id_poste>',
           login_required(registros_views.comprobar_id_poste,
                           'next','/accounts/login'),name='comprobar_poste'),
    
    #Configuración
    path('configuracion/cargar_postes',
           login_required(configuracion_views.cargar_postes,
                           'next','/accounts/login'),name='cargar_postes'),
    
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]