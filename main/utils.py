from django import forms
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm
import locale


class CalculoException(Exception):
    pass
class DateInput(forms.DateInput):
    input_type = 'date'
    def __init__(self):
        forms.DateInput.__init__(self,format=('%Y-%m-%d'))
        
class TimeInput(forms.DateInput):
    input_type = 'time'
    def __init__(self):
        forms.DateInput.__init__(self,format=('%H:%M'))

        
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    def __init__(self):
        forms.DateTimeInput.__init__(self,format=('%Y-%m-%dT%H:%M:%S'))
                
def prodn( *args):
    res=1
    
    for i in args:
        if i is not None:
            res=res*i
        else:
            res=0;
            break;
    return res
def suman( *args):
    res=0
    for i in args:
        if i:
            res=res+i
        
    return res

def sumanS( *args):
    try:
        res=0
        for i in args:
            if i:
                res=res+i
            
    except:
        res=0
    return res

def nstr(obj):
    if obj is not None:
        return str(obj)
    else:
        return ""

def nbl(obj):
    if obj is not None:
        if obj:
            return "Sí"
        else:
            return "No"
    else:
        return ""
       
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 7)
        self.drawRightString(20*cm, 1*cm,
            "Página %d de %d" % (self._pageNumber, page_count))
        
def cortar_texto(texto, palabras):
    
    if texto is not None:
        words=texto.split()
        if len(words) > palabras:
            txt=""
            for i in range(0,palabras-1):
                txt=txt+" "+words[i]
            txt=txt+" ..."
            return txt
    
    return texto 

def formatES(value):
    locale.setlocale(locale.LC_ALL, 'es_ES')
    if value is not None:
        return locale.format_string('%.2f', value, grouping=True, monetary=False)
    else:
        return ""