## -*- coding: UTF-8 -*-
from django.db.models import get_model
from django.core import management
from django.http import HttpResponse
from my_site.myapp.models import get_list, get_tit_fields
from django.utils import simplejson
from django.shortcuts import render_to_response
import re, logging



def manager():
    #management.call_command('syncdb', interactive=False)
    management.call_command('migrate', interactive=False)
    #management.call_command('makemigrations', interactive=False)

def run(request):
    manager()
    lists = get_list()
    return render_to_response('test.html', {'list':lists})

def insert(request):
    results = {'success': False}
    if 'my' in request.GET:
        get = request.GET['my']
        get = re.findall('.[^_]+', get)
        values = []
        for i in get:
            values.append(i.replace('_', ''))
        j = 1
        print values
        itog = {}
        model = get_model('myapp', values[0])
        fild = [key.name for key in model._meta.fields]
        for i in fild:
            if i != 'id':
                itog[i] = values[j]
                j += 1
            results = {'success': True}
        qs = model(**itog)
        qs.save()
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

def update(request):
    results = {'success': False}
    if 'my' in request.GET:
        results = {'success': True}
        get = request.GET['my']
        get = re.findall('.[^_]+', get)
        values = []
        for i in get:
            values.append(i.replace('_', ''))
        name = values[0]
        model = get_model('myapp', name)
        fild = [key.name for key in model._meta.fields]
        value = int(values[2])
        key = fild[value]
        itog = {}
        itog[key] = values[3]
        model.objects.filter(id=values[1]).update(**itog)
    json2 = simplejson.dumps(results)
    return HttpResponse(json2, mimetype='application/json')

def get_type(fil, fild):
    result = []
    i=0
    for key in fil:
        key1 = unicode(key)
        temp = key1.replace(fild[i],'')
        i+=1
        if (temp == "<django.db.models.fields.IntegerField: >"):
            result.append("int")
        if (temp =="<django.db.models.fields.CharField: >" ):
            result.append("char")
        if (temp =="<django.db.models.fields.DateField: >" ):
            result.append("date")
    return result

def get(request):
   
    if ('my' in request.GET):
        model = get_model('myapp', request.GET['my'])
        fild = [key.name for key in model._meta.fields]
        query = model.objects.all().values_list(*fild)
        title_field = get_tit_fields()
        qs = []
        type = get_type([key for key in model._meta.fields],fild)
        qs.append(type)
        temp =[]
        temp.append("id")
        for i in title_field[request.GET['my']]:
            temp.append(i)
        qs.append(temp)
        for key in query:
            temp = []
            for i in key:
                temp.append(unicode(i))
            qs.append(temp)
        result = simplejson.dumps(qs)
        return HttpResponse(result, content_type='application/json')
