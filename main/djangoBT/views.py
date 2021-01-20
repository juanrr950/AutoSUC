# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic.base import View
from django.http.response import JsonResponse
from _functools import reduce
import operator
from django.db.models import Q
from rest_framework import serializers
from django.template.loader import render_to_string

class Serializer(serializers.ModelSerializer):
    class Meta:
        pass
    def __init__(self,  *args, **kwargs):
        self.Meta.model = kwargs.pop('model')
        self.Meta.fields= kwargs.pop('field_list')
        self.Meta.fields=self.Meta.fields+('id',)
        super().__init__()

class BTView(View):
    '''
    Para definar una clase que herede BTJsonView
    defina un atributo model con el modelo y de 
    forma opcional field_list donde se seleccionan
    los campos del modelo a serializer, sino esta se cogen todos.
    Otra opción es definir un serializer que debe contenera una
    clase de tipo ModelSerializer de rest_framework.
    
    Obligatoriamente defina sort_list una lista de campos por los que 
    ordenar por el parametro sort.
    '''

    def __init__(self):
        self.context={}
        super().__init__()
      
    def get(self, request, *args, **kwargs):
        if kwargs.pop('view')=='Json':
            self.request=request
            self.queryset=self.get_queryset()
            self.queryset=self.search()
            self.queryset=self.sort()        
            self.add_pagination()
            return JsonResponse(self.data, safe=False)
        else:
            self.context['table']=self.generate_HTML()
            return render(request, self.template_name, 
                          self.context)
    def _define_serializer(self):
        if hasattr(self, 'serializer'):
            dataSerializer=self.serializer(self.queryset, many=True)
        elif hasattr(self, 'model') and hasattr(self, 'field_list'):
            dataSerializer=Serializer(self.queryset, many=True,
                              model=self.model,
                              field_list=self.field_list,
                              )
            

        elif hasattr(self, 'model'):
            self.model._meta.fields
            field_list=[f.name for f in self.model._meta.get_fields()]
            dataSerializer=Serializer(self.queryset, many=True,
                              model=self.model,
                              field_list=field_list,
                              )
        else:
            raise Exception('Atributos necesarios no definos, <model> or <serializer>')
                
        
        return dataSerializer
    
    def add_pagination(self):
        offset=int(self.request.GET['offset'])
        limit=int(self.request.GET['limit'])
    
        numRows=self.queryset.count()
        if not numRows < offset+limit-offset:
            self.queryset=self.queryset[offset:offset+limit]
        
        dataSerializer=self._define_serializer()
        
        json_final = {"total": numRows, "rows": []}
        for i in dataSerializer.data:
            json_final['rows'].append(i)
        self.data=json_final
    
    def sort(self):
        if('sort' in self.request.GET):
            if(self.request.GET['order']=='asc'):
                sort=self.request.GET['sort']
            else:
                sort='-'+self.request.GET['sort']
    
            return self.queryset.order_by(sort)
        else:
            return self.queryset
    
    def search(self):
        if 'search' in self.request.GET:
            if(self.request.GET['search']!=''):
                wds = self.request.GET['search'].split()
                '''
                tag_qs = reduce(operator.and_,
                     (Q(**{'nombre__icontains':x}) | \
                     Q(estado__icontains=x)  for x in wds))
                '''
                
                list_and=[]
                for word in wds:
                    list_or=[]
                    for campo in self.search_list:
                        list_or.append(Q(**{campo+'__icontains':word}))
                    list_and.append(reduce(operator.or_, list_or))
                tag_qs=reduce(operator.and_,list_and)
                return self.queryset.filter(tag_qs)
        
        return self.queryset
        

    def generate_HTML(self):
        
                
        def merge(list1, list2, list3): 
            merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))] 
            return merged_list
        
        if not hasattr(self, 'link_list'):
            self.link_list=""
        if not hasattr(self, 'cursor_row'):
            self.cursor_row=""
        return  render_to_string('djangoBT/table.html',
                                 {'url_json':self.url_json,
                                  'field_list':[(self.field_list[i], self.verbose_list[i], self.sort_list[i]) for i in range(0, len(self.field_list))], 
                                  'data_sort_name':self.data_sort_name,
                                  'data_sort_order':self.data_sort_order, 
                                  'link_list':self.link_list,
                                  'cursor_row':self.cursor_row,
                                  'show_checkbox_colunm':self.show_checkbox_colunm})



