# -*- coding: UTF-8 -*-
from django.db import models
import yaml

list_names={}
list_fields={}

class dynamic_model(object):
    attrs = {}

    def __init__(self, name, filds):
        self.name = name
        self.filds = filds
        self.attrs = {}
        self.attrs = self.get_attrs()
        self.model = type(self.name, (models.Model,), self.attrs)

    def get_attrs(self):
       for key in self.filds:
            self.attrs[key['fild']] = self.choice_fild(key['type'])
       self.attrs['__module__']  =  'my_site.myapp.models'
       return  self.attrs

    def choice_fild(self, fild_type):
        self.type = fild_type
        if  self.type == 'int':
            return  models.IntegerField()
        if self.type == 'data':
            return models.DateField(blank=False)
        if self.type == 'char': 
            return models.CharField(max_length=32)

    def __unicode__(self):
	    for i, j in self.attrs.items():
		    return i

def run():
	temp = yaml.load(open('/home/my_site/my_site/conf.yaml'))
	for key, value in temp.items():
            title = value['title']
            list_names[key] = title
            del value['title']
            value = value['filds']
            list_fields[key] = get(value)
            models = dynamic_model(key, value)

def get(temp):
	result =[]
	for i in temp:
		result.append(i['title'])
	return result

def get_list():
    return list_names

def get_tit_fields():
        return list_fields

run()



