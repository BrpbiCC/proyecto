from django.shortcuts import render

# Create your views here.



def inicio(request):
        return render(request, 'core/inicio.html')

def registro(request):
        return render (request, 'core/registro.html')

def login(request):
        return render (request, 'core/login.html')

def hospedaje(request):
        return render (request, 'core/hospedaje.html')

def actividad(request):
        return render (request, 'core/actividad.html')

def gastronomia(request):
        return render (request, 'core/gastronomia.html')

