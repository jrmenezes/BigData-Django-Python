from django.shortcuts import render
##from . import views
from django.http import HttpResponse

def index(request):
    return HttpResponse("EXEMPLO 01.")

# def teste(request):
#     return HttpResponse("EXEMPLO 01. -Teste")
