from django.shortcuts import render
from .models import Sliders, Categoria, Servicio, Marca, Sucursal, Ejecutivo

# Create your views here.

def home(request):
    sliders = Sliders.objects.all()
    categories = Categoria.objects.all()
    services = Servicio.objects.all()
    marcas = Marca.objects.all()
    #Filtrar las ultimas 4 sucursales
    sucursales = Sucursal.objects.filter(estado=True).order_by('id')[:4]
    
    return render(request, 'page/home.html', {
        'sliders': sliders, 
        'categories': categories, 
        'services': services, 
        'marcas': marcas, 
        'sucursales': sucursales,
        })

def about(request):
    ejecutivos = Ejecutivo.objects.filter(estado=True)
    return render(request, 'page/about.html', {'ejecutivos': ejecutivos})
    