from django.db import models
from django.db.models.fields.files import FileField
from builtins import property
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import os
import shutil
from codecs import ignore_errors
from AutoSUC.settings import BASE_DIR
from django.utils.deconstruct import deconstructible
from django.core.files.storage import FileSystemStorage
from collections import Counter


    
def suc_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/{1}.jpg'.format(instance.usuario.username, instance.nombre)
    #return '{0}/{1}/{2}'.format(instance.usuario.username, instance.nombre, filename)

def only_int(value):
        if value.isdigit()==False:
            raise ValidationError('Codigo Miga contains characters, only digits')


class tModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Usuario(User,tModel):
    edad=models.IntegerField(blank=True, null=True)

class Suc(tModel):
    nombre = models.CharField(max_length=150,unique=True)
    via = models.CharField(max_length=150, null=True, blank=True)
    tipo_via = models.CharField(max_length=150, null=True, blank=True)
    provincia = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    numero_via = models.CharField(max_length=50, null=True, blank=True)
    codigo_miga = models.CharField(max_length=50)
    nombre_central = models.CharField(max_length=150)
    cto = models.IntegerField(null=True, blank=True)
    car_ftth_iua = models.BigIntegerField()
    fecha_ar = models.DateTimeField()
    plantilla = models.CharField(max_length=1,
        choices=(('V','Vertical'),('H','Horizonal')), default="V")
    nombre_tecnico = models.CharField(max_length=150)
    apellido_tecnico = models.CharField(max_length=150)
    segundo_apellido_tecnico = models.CharField(max_length=150, null=True, blank=True)
    dni_tecnico = models.CharField(max_length=150)
    poste_central = models.CharField(max_length=150, null=True, blank=True)
    comentarios = models.CharField(max_length=650, null=True, blank=True)
    poste_1 = models.CharField(max_length=150)
    poste_2 = models.CharField(max_length=150)
    poste_3 = models.CharField(max_length=150, blank=True,null=True)
    poste_4 = models.CharField(max_length=150, blank=True,null=True)
    poste_5 = models.CharField(max_length=150, blank=True,null=True)
    poste_6 = models.CharField(max_length=150, blank=True,null=True)
    poste_7 = models.CharField(max_length=150, blank=True,null=True)
    poste_8 = models.CharField(max_length=150, blank=True,null=True)
    poste_9 = models.CharField(max_length=150, blank=True,null=True)
    poste_10 = models.CharField(max_length=150, blank=True,null=True)
    medida_1_2 = models.CharField(max_length=150)
    medida_2_3 = models.CharField(max_length=150, blank=True,null=True)
    medida_3_4 = models.CharField(max_length=150, blank=True,null=True)
    medida_4_5 = models.CharField(max_length=150, blank=True,null=True)


    medida_5_6 = models.CharField(max_length=150, blank=True,null=True)
    medida_6_7 = models.CharField(max_length=150, blank=True,null=True)
    medida_7_8 = models.CharField(max_length=150, blank=True,null=True)
    medida_8_9 = models.CharField(max_length=150, blank=True,null=True)
    medida_9_10 = models.CharField(max_length=150, blank=True,null=True)
    word=FileField(blank=True,null=True, max_length=500)
    excel=FileField(blank=True,null=True, max_length=500)
    powerpoint=FileField(blank=True,null=True, max_length=500)
    imagen=FileField(upload_to=suc_directory_path, max_length=500)
    tiempo=models.IntegerField(blank=True,null=True)
    
    pagado = models.DateTimeField(blank=True,null=True)
    facturado = models.DateTimeField(blank=True,null=True)
    enviado = models.DateTimeField(blank=True,null=True)
    estado= models.CharField(max_length=1,
        choices=(('R','Realizado'),('E','Enviado'),
                 ('F','Facturado'),('P','Pagado'),
                 ('A','Anulada'),), 
        default="R")
    #Usuario que lo realiza
    usuario=models.ForeignKey(Usuario,related_name='sucs', on_delete=CASCADE)
    asignado=models.ForeignKey(Usuario,related_name='sucs_asignados', on_delete=CASCADE)
    
    @property
    def poste_1_id(self):
        if self.poste_1!=None:
            return self.poste_1.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def poste_2_id(self):
        if self.poste_2!=None:
            return self.poste_2.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def poste_3_id(self):
        if self.poste_3!=None:
            return self.poste_3.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def poste_4_id(self):
        if self.poste_4!=None:
            return self.poste_4.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def poste_5_id(self):
        if self.poste_5!=None:
            return self.poste_5.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def poste_6_id(self):
        if self.poste_6!=None:
            return self.poste_6.split('(ID ')[1].split(')')[0]
        else:
            return None
        
    @property
    def poste_7_id(self):
        if self.poste_7!=None:
            return self.poste_7.split('(ID ')[1].split(')')[0]
        else:
            return None
        
    @property
    def poste_8_id(self):
        if self.poste_8!=None:
            return self.poste_8.split('(ID ')[1].split(')')[0]
        else:
            return None
        
    @property
    def poste_9_id(self):
        if self.poste_9!=None:
            return self.poste_9.split('(ID ')[1].split(')')[0]
        else:
            return None
        
    @property
    def poste_10_id(self):
        if self.poste_10!=None:
            return self.poste_10.split('(ID ')[1].split(')')[0]
        else:
            return None
    @property
    def num_postes(self):
        res=2
        if self.poste_3!=None:
            res=res+1
        if self.poste_4!=None:    
            res=res+1
        if self.poste_5!=None:
            res=res+1
        if self.poste_6!=None:
            res=res+1
        if self.poste_7!=None:
            res=res+1
        if self.poste_8!=None:
            res=res+1
        if self.poste_9!=None:
            res=res+1
        if self.poste_10!=None:
            res=res+1
        return res

    def delete(self, using=None, keep_parents=False):
        #Borramos los archivos si existen
        shutil.rmtree(os.path.join(BASE_DIR,'media',self.usuario.username,self.nombre),ignore_errors=True)
        
        return tModel.delete(self, using=using, keep_parents=keep_parents)
    
    def clean(self, *args, **kwargs):
        
        super(Suc, self).clean(*args, **kwargs)
        if self.poste_1 is not None and self.poste_1!="" and self.poste_2 is not None and self.poste_2!="":
            
            #Validamos que no haya postes repetido en el form
            list=[self.poste_1_id,
                 self.poste_2_id,
                 self.poste_3_id,
                 self.poste_4_id,
                 self.poste_5_id,
                 self.poste_6_id,
                 self.poste_7_id,
                 self.poste_8_id,
                 self.poste_9_id,
                 self.poste_10_id
                 
                ]
           
            print(list)
           
            if self.poste_1_id is not None:
                if list.count(self.poste_1_id)>1:
                    raise ValidationError({'poste_1': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_2_id is not None:
                if list.count(self.poste_2_id)>1:
                    raise ValidationError({'poste_2': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_3_id is not None:
                if list.count(self.poste_3_id)>1:
                    raise ValidationError({'poste_3': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_4_id is not None:
                if list.count(self.poste_4_id)>1:
                    raise ValidationError({'poste_4': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_5_id is not None:
                if list.count(self.poste_5_id)>1:
                    raise ValidationError({'poste_5': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_6_id is not None:
                if list.count(self.poste_6_id)>1:
                    raise ValidationError({'poste_6': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_7_id is not None:
                if list.count(self.poste_7_id)>1:
                    raise ValidationError({'poste_7': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_8_id is not None:
                if list.count(self.poste_8_id)>1:
                    raise ValidationError({'poste_8': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_9_id is not None:
                if list.count(self.poste_9_id)>1:
                    raise ValidationError({'poste_9': ('Ha introducido dos postes con la misma ID'),})
                
            if self.poste_10_id is not None:
                if list.count(self.poste_10_id)>1:
                    raise ValidationError({'poste_10': ('Ha introducido dos postes con la misma ID'),})
                
           
               
                
            '''       
            
            
             
            def check_poste_repetido(id_poste,campo):
                if Registro.objects.filter(id_poste=id_poste).exists():
                    poste=Registro.objects.get(id_poste=id_poste)
                    return {campo: 'Poste repetido con '+poste.codigo_suc,}
                else:
                    return {}
           
            errores=dict(**check_poste_repetido(self.poste_1_id,"poste_1"),
            **check_poste_repetido(self.poste_2_id,"poste_2"), 
            **check_poste_repetido(self.poste_3_id,"poste_3"), 
            **check_poste_repetido(self.poste_4_id,"poste_4"), 
            **check_poste_repetido(self.poste_5_id,"poste_5") )
            
            if bool(errores):
                raise ValidationError(errores)  
            '''
            
        
        
        
class Registro(models.Model):
    codigo_suc=models.CharField(max_length=40,null=True,blank=True)
    codigo_miga=models.IntegerField(null=True,blank=True)
    id_poste=models.IntegerField(unique=True)
    def __str__(self):
        return str(self.id_poste)
    
class Central(models.Model):
    codigo_miga = models.CharField(max_length=50,unique=True)
    nombre_central = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.codigo_miga+" "+self.nombre_central
class Ajuste(tModel):
    nombre=models.CharField(unique=True, max_length=150)
    valor=models.CharField(max_length=250)
    def __str__(self):
        return self.nombre+" -> "+self.valor
    
class Carga_masiva(tModel):
    csv=FileField(upload_to='cargas_masivas')
    inicio=models.DateTimeField(blank=True,null=True)
    fin=models.DateTimeField(blank=True,null=True)
    lineas_total=models.IntegerField(blank=True,null=True)
    registros_nuevos=models.IntegerField(blank=True,null=True)
    porcentaje_completado=models.IntegerField(blank=True,null=True)
    estado= models.CharField(max_length=1,
        choices=(('P','PROCESANDO'),('T','TERMINADO'),('E','ERROR')), default="P")
    