from django.template.loader import render_to_string
from django import template

register = template.Library()

def lbd_form_checkbox(elem):
    
    return render_to_string('LBD_forms/checkbox.html',
                            {'elem':elem,})
    
register.filter('lbd_form_checkbox',lbd_form_checkbox)

def lbd_form_textautocomplete(elem):
    
    return render_to_string('LBD_forms/textautocomplete.html',
                            {'elem':elem,})
    
register.filter('lbd_form_textautocomplete',lbd_form_checkbox)