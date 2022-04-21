
from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render
from AppOne.models import Integrantes

# Create your views here.

def integrantes(request):
    return render(request, 'AppOne/integrantes.html')

def empleo (request):
    return render(request,'AppOne/empleo.html')
    
def entretenimiento(request):
    return render(request, 'AppOne/entretenimiento.html')

def inicio(request):
    return render(request,'AppOne/inicio.html')