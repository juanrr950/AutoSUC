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

from main.configuracion import configuracion_views
from django.urls.conf import re_path, include
from main.central import central_views
from main.registro import registro_views
from main.configuracion.carga_masiva import carga_masiva_views

urlpatterns = [
    #path('',views.home, name='home'),
    path('admin/', adminsite.urls), 
    path('',login_required(views.example,'next','/accounts/login'), name='example'),
    path('accounts/login/',views.login.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('tinymce/', include('tinymce.urls')),
    
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
    re_path(r'^suc/new_email_sucs/(?P<ids>(\d+\,?)+)/$',  login_required(suc_views.new_email_sucs, 'next','/accounts/login'),name='new_email_sucs'),
    
    #Registros
    path('registro/comprobar_poste/<id_poste>',
           login_required(registro_views.comprobar_id_poste,
                           'next','/accounts/login'),name='comprobar_poste'),
    
    #Centrals
    path('central/list/<view>',  login_required(central_views.Central_BT.as_view(),'next','/accounts/login'),name='list_central'),
    path('central/new_central',  login_required(central_views.new_central,'next','/accounts/login'),name='new_central'),
    path('central/edit_central/<pk>',  login_required(central_views.edit_central,'next','/accounts/login'),name='edit_central'),
    path('central/delete_central/<pk>',  login_required(central_views.delete_central,'next','/accounts/login'),name='delete_central'),
    #Configuración

    path('configuracion/carga_masiva/list/<view>',  login_required(carga_masiva_views.Carga_masiva_BT.as_view(),'next','/accounts/login'),name='list_carga_masiva'),
    path('configuracion/carga_masiva/new_carga_masiva',  login_required(carga_masiva_views.new_carga_masiva,'next','/accounts/login'),name='new_carga_masiva'),
    path('configuracion/carga_masiva/edit_carga_masiva/<pk>',  login_required(carga_masiva_views.edit_carga_masiva,'next','/accounts/login'),name='edit_carga_masiva'),
    path('configuracion/carga_masiva/delete_carga_masiva/<pk>',  login_required(carga_masiva_views.delete_carga_masiva,'next','/accounts/login'),name='delete_carga_masiva'),

    #Registros
    path('registro/list/<view>',  login_required(registro_views.Registro_BT.as_view(),'next','/accounts/login'),name='list_registro'),
    path('registro/new_registro',  login_required(registro_views.new_registro,'next','/accounts/login'),name='new_registro'),
    path('registro/edit_registro/<pk>',  login_required(registro_views.edit_registro,'next','/accounts/login'),name='edit_registro'),
    path('registro/delete_registro/<pk>',  login_required(registro_views.delete_registro,'next','/accounts/login'),name='delete_registro'),
    
                           
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]