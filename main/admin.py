from django.contrib import admin
from main.models import Usuario, Ajuste
from django.contrib.auth.models import User, Group
from django.contrib.admin.sites import AdminSite
from django import forms
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Sistema AutoSUC'
adminsite = MyAdminSite(name='myadmin')

adminsite.register(Usuario, UserAdmin)
#admin.site.register(User)
adminsite.register(Group)
adminsite.register(Ajuste)