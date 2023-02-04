from django.shortcuts import render
##from . import views

from django.http import HttpResponse

def index(request):
    return HttpResponse("AGORA EH O EXEMPLO 02.")