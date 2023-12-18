# i have created this file - vikas
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'vikas', 'place': 'USA'}
    return render(request, 'index.html',params)

def removePunc(request):
    return HttpResponse('removePunc')

def charCount(request):
    return HttpResponse('charCount')

def spaceRemove(request):
    return HttpResponse('spaceRemove')

