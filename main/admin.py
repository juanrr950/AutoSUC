from django.contrib import admin
from main.models import Usuario
from django.contrib.auth.models import User, Group
from django.contrib.admin.sites import AdminSite

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'Sistema AutoSUC'
adminsite = MyAdminSite(name='myadmin')

adminsite.register(Usuario)
adminsite.register(User)
adminsite.register(Group)