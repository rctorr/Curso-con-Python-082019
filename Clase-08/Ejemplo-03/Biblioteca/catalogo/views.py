from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petción de la url / """
    return HttpResponse(
        "<h2>Soy la página de inicio! Soy el amor de tu vida!</h2>")
