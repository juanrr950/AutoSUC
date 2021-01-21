from rest_framework import serializers
from main.models import Suc
from math import trunc


class SucSerializer(serializers.ModelSerializer):
    
    created_date= serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    estado =serializers.SerializerMethodField()
    tiempo=serializers.SerializerMethodField()
    asignado=serializers.ReadOnlyField(source='asignado.first_name')
    def get_estado(self, object):
        if object.estado=='E':
            return "<span class='badge badge-info'>Enviado</span> "
        elif object.estado=='F': 
            return "<span class='badge badge-primary'>Facturado</span> "
        elif object.estado=='P': 
            return "<span class='badge badge-success'>Pagado</span> "
        elif object.estado=='A': 
            return "<span class='badge badge-danger'>Anulado</span> "
        else:
            return "<span class='badge badge-warning'>Realizado</span> "
        
    def get_tiempo(self, suc):
        if suc.tiempo:
            return str(trunc(suc.tiempo/60))+":"+str(suc.tiempo%60)+" min."
        else:
            return "" 
    class Meta:
        model=Suc
        fields=('id','nombre','created_date','provincia',
                'estado','tiempo','asignado')
        