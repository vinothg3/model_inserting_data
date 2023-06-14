from django.shortcuts import render

from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(Topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Webpage data is inserted')
def insert_access(requst):
    t=input('enter the auther name:')
    d=input('enter the date:')
    n=input('enter the name')
    WO=Webpage.objects.get_or_create(name=n)[0]
    WO.save()
    AO=Access.get_or_create(name=n,Author=t,Date=d)[0]
    AO.save()
    return HttpResponse('access inserted successfully')
