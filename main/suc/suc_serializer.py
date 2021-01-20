from rest_framework import serializers
from main.models import Suc


class SucSerializer(serializers.ModelSerializer):
    
    created_date= serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    estado =serializers.SerializerMethodField()
    
    def get_estado(self, object):
        if object.enviado is not None:
            return "<span class='badge badge-info'>Enviado</span> "+object.enviado.strftime("%H:%M:%S %d/%m/%Y")
        else:
            return "<span class='badge badge-warning'>Realizado</span> "+object.created_date.strftime("%H:%M:%S %d/%m/%Y")
        
    class Meta:
        model=Suc
        fields=('id','nombre','created_date','provincia',
                'estado')
        