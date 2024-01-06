from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}

    if request.method=='POST':
        FDTO=TopicForm(request.POST)
        if FDTO.is_valid():
           FDTO.save()
           return HttpResponse('Topic is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
           
            WFDO.save()
            return HttpResponse('webpage is inserted')
        else:
            return HttpResponse('invalid data')

    
    return render(request,'insert_webpage.html',d)



def insert_access(request):

    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('accessrecord is inserted')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'insert_access.html',d)

