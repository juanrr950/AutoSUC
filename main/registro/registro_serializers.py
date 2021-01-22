from main.models import Registro
from rest_framework import serializers
'''
METODO DE SERIALIZER SIMPLE

'''
class Registro_serializer(serializers.ModelSerializer):
    
    '''
    [DATE_FIELD]= serializers.DateTimeField(format="%d/%m/%Y")
    [RELATION/PROPERTY_FIELD]=serializers.ReadOnlyField(source='[OBJECT_._ACCESS]')
    [METHOD_FIELD]=serializers.SerializerMethodField()
    
    def get_[METHOD_FIELD](self, object):
        return object.[OBJECT_._ACCESS]   
    '''
    class Meta:
        model=Registro
        fields=('id', 'codigo_suc', 'codigo_miga', 'id_poste')
        