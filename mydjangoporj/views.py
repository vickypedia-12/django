# i have created this file - vikas
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> Hellow from index section</h1>')

def about(request):
    return HttpResponse('Hellow from about section')