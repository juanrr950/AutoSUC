from rest_framework import serializers
from main.models import Suc


class SucSerializer(serializers.ModelSerializer):
    
    created_date= serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
        
    class Meta:
        model=Suc
        fields=('nombre','created_date','provincia')
        