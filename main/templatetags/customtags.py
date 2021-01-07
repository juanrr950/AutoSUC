from django.template.defaulttags import register
from django import template
import os


register = template.Library()

def path(value,arg):
    
    return value.path.split('/')[arg]
    
register.filter('path',path)

@register.filter
def filename(value):
    return os.path.basename(value.file.name)



@register.simple_tag(name='data_sortable')
def data_sortable(value):
    if value=='None':
        res= " data-sortable=false "
    else:
        res= " data-sortable=true data-sort-name="+value+" "
    
    
    return res
        #data-sortable="True" data-sort-name="{{i.2}}"
        


@register.simple_tag
def dict_din(dictionary, key, key2):      
    return dictionary[key][key2]

