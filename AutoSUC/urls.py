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

urlpatterns = [
    #path('',views.home, name='home'),
    path('admin/', adminsite.urls), 
    path('',login_required(views.example,'next','/accounts/login'), name='example'),
    path('accounts/login/',views.login.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    #SUCs
    path('suc/list/<view>',  login_required(suc_views.Suc_BT.as_view(),'next','/accounts/login'),name='list_suc'),
    path('suc/new_suc',  login_required(suc_views.new_suc,'next','/accounts/login'),name='new_suc'),
    path('suc/edit_suc/<pk>',  login_required(suc_views.edit_suc,'next','/accounts/login'),name='edit_suc'),
    path('suc/delete_suc/<pk>',  login_required(suc_views.delete_suc,'next','/accounts/login'),name='delete_suc'),
    
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]