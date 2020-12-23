from django.template.defaulttags import register

@register.filter
def filter_id_factura(dictionary, key):
    
    return dictionary.filter(factura_id=key)

