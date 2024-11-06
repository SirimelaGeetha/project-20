from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get(Topic_name=tn)
    if TO[1]:
         return HttpResponse('object is created')
    else:
        return HttpResponse('the object is not available')

def insert_webpage(request):
    tn=input('enter topic_name')
    n=input('enter name')
    u=input('enter url')

    TO=Topic.objects.get(Topic_name=tn)[0]
    WO=webpage.objects.get(Topic_name=tn,name=n,url=u)
    if WO[1]:
        return HttpResponse('new object is created')
    else:
        return HttpResponse('the object is not available')

def insert_accessrecord(request):
    tn=input('enter topic_name')
    n=input('enter name')
    au=input('enter author')
    d=input('enter date')

    TO=Topic.objects.get(Topic_name=tn)[0]
    WO=Webpage.objects.get(name=n)[0]
    ARO=AccessRecord.objects.get(Topic_name=tn,author=au,date=d)
    if ARO[1]:
        return HttpResponse('new object is created')
    else:
        return HttpResponse('the object is not available')
    

