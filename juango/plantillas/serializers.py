from rest_framework import serializers
'''
METODO DE SERIALIZER SIMPLE

'''
class [CLASS_NAME]_serializer(serializers.ModelSerializer):
    
    '''
    [DATE_FIELD]= serializers.DateTimeField(format="%d/%m/%Y")
    [RELATION/PROPERTY_FIELD]=serializers.ReadOnlyField(source='[OBJECT_._ACCESS]')
    [METHOD_FIELD]=serializers.SerializerMethodField()
    
    def get_[METHOD_FIELD](self, object):
        return object.[OBJECT_._ACCESS]   
    '''
    class Meta:
        model=[CLASS_NAME]
        fields=[campos]
        